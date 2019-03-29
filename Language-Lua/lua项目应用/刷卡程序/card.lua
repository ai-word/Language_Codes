local cjson = require "cjson"
local lorm = require "lorm.sqlite"
local logging = require "log4l.db"
local socket = require"socket"
local utilib = require "utilib"
require 'alien'

function println(...)
	io.write(string.format(...))
end

function printall(tb)
	local function printtable(tb, sp)
		println("%s{\n", (' '):rep(sp))
		for k, v in pairs(tb) do
			if type(v) == "table" then
				println("%s\"%s\": [\n", (' '):rep(4+sp), tostring(k))
				printtable(v, sp+8)
				println("%s]\n", (' '):rep(4+sp))
			else
				println("%s\"%s\": \"%s\",\n", (' '):rep(4+sp), tostring(k), tostring(v))
			end
		end
		println("%s}\n", (' '):rep(sp))
	end
	printtable(tb, 0)
end

utilib.ChangeDirToDCMHOME()
logger = logging.new("ERROR", "data/syslog.db")

local meterstack = require "protocol.meterstack"
local protoservice = require "protocol.service"

local udp = assert(socket.udp())
assert(udp:setpeername("127.0.0.1", 4999))

local icdev

local rf = alien.load("librf.so")

rf.dc_init:types("int", "int", "long")
rf.dc_request:types("int", "int", "byte", "ref uint")
rf.dc_config_card:types("int", "int", "byte")
rf.dc_card:types("int", "int", "byte", "ref uint")
rf.dc_pro_resethex:types("int", "int", "ref char", "string")
rf.dc_pro_commandlink_hex:types("int", "int", "byte", "string", "ref char", "string", "byte", "byte")
rf.dc_beep:types("int", "int", "uint")
rf.dc_halt:types("int", "int")
rf.dc_exit:types("int", "int")
--rf.dc_des_hex:types("int", "string", "string", "string", "int")
rf.dc_getver:types("int", "int", "string")
rf.dc_anticoll:types("int", "int", "byte", "ref uint")
rf.dc_select:types("int", "int", "ulong", "ref char")
rf.a_hex:types("int", "string", "string", "int")


local Sleep = utilib.Sleep

function InitCardReader()
    icdev = rf.dc_init(100, 9600)
    if icdev < 0 then
        println("dc_init error. %d\n", icdev)
        return
    end
    println("icdev=0x%x\n", icdev)

    local rbuff = alien.array("byte", 4)
    rf.dc_getver(icdev, rbuff.buffer)
    println("verson=%s\n", tostring(rbuff.buffer))
end

--验证口令
function Verify(Password)
	local rbuff = alien.array("byte", 8)
	local cmd = "0020000103" .. Password
	println("Send %d bytes:%s(verify)\n", cmd:len() /2 , cmd)
	local _, rlen = rf.dc_pro_commandlink_hex(icdev, cmd:len()/2, cmd, 0, rbuff.buffer, 7, 56)
	println("recv %d bytes:%s\n\n", rlen, tostring(rbuff.buffer))
	if rlen < 2 or tostring(rbuff.buffer):sub(-4) ~= "9000" then
		print("error 1")
	end
end

--读取数据
function ReadData()
	local rbuff = alien.array("byte", 48)
	local cmd = "00A40000023F01"
	println("Send %d bytes:%s(select DF 0x3F01)\n", cmd:len() /2 , cmd)
	local res, rlen = rf.dc_pro_commandlink_hex(icdev, cmd:len()/2, cmd, 0, rbuff.buffer, 7, 56)
	println("Recv %d bytes:%s\n\n", rlen, tostring(rbuff.buffer))
	if rlen < 2 or tostring(rbuff.buffer):sub(-4) ~= "9000" then
		print("error 0")
		return false, ""
	end
	Verify("123456")
--[[
	--选择标示为0002的二进制文件
	cmd = "00A40000020002"
	println("Send %d bytes:%s(select EF 0x0002)\n", cmd:len() /2 , cmd)
	res, rlen = rf.dc_pro_commandlink_hex(icdev, cmd:len()/2, cmd, 0, rbuff.buffer, 7, 56)
	println("Recv %d bytes:%s\n\n", rlen, tostring(rbuff.buffer))
		if rlen < 2 or tostring(rbuff.buffer):sub(-4) ~= "9000" then
		print("error 2")
		return false
	end
--]]
	--读取20个字节
	--cmd = "00B0000006"
	cmd = "00B0820014"
	println("Send %d bytes:%s(read binary file)\n", cmd:len() /2 , cmd)
	res, rlen = rf.dc_pro_commandlink_hex(icdev, cmd:len()/2, cmd, 0, rbuff.buffer, 7, 56)
	println("Recv %d bytes:%s\n\n", rlen, tostring(rbuff.buffer))
	if rlen < 2 or tostring(rbuff.buffer):sub(-4) ~= "9000" then
		print("error 3")
		return false, ""
	end
	local UserID = tostring(rbuff.buffer):sub(1, 40)
	local dest = alien.array("byte", 20)
	rf.a_hex(UserID, dest.buffer, 38)
	UserID = tostring(dest.buffer)
	return true, UserID
end


function GetUserID()

    while true do
        local res, TagType = rf.dc_request(icdev, 0, 0)

        if res == 0 then
            print("TagType:" .. TagType)

            if TagType == 8 then
                print("CPU card")
            elseif TagType == 4 then
                print("M1 card")
            end

            local res, CardNo = rf.dc_anticoll(icdev, 0, 0)
            if res == 0 then
                print("CardNo:" .. CardNo)
            else
                print("dc_card() error:" .. res)
            end
 
            local res, Size = rf.dc_select(icdev, CardNo, 0)
            if res == 0 then
                print("Size:" .. Size)
            else
                print("dc_select() error:" .. res)
            end
            if TagType == 8 then
                local rbuff = alien.array("byte", 48)
                local _, rlen = rf.dc_pro_resethex(icdev, 0, rbuff.buffer)
                println("recv %d bytes:%s\n", rlen, tostring(rbuff.buffer))

                local res, UserID = ReadData()
                rf.dc_halt(icdev)
                if res then
                    print(UserID)
                    --print("UserID:"..UserID)
                    rf.dc_beep(icdev, 40)
                    return true, UserID
                end
            end

        end

        Sleep(1000)
    end

    return false
end

local function OpenValve(UserID)
    local baseCon = lorm.new('data/base.db')
    local meterinfos = baseCon:queryObjects([[
            select *
            from base_MeterInfo
            where UserID = ?
        ]], {UserID})
    if #meterinfos ~= 1 then
        print("Could not find this UserID:" .. UserID)
        return 
    end
       
    local metercode = meterinfos[1].MeterCode
    local db_data = protoservice.fetch_db_data(metercode)
    local Meter = meterstack.get_meter(db_data.MeterModelCode)
    print(metercode)
 
    local st, err = pcall(function()
        local singlecmd
        for _, v in ipairs(Meter.singleCmds) do
            if v.cmdName == "允许开阀" then
                singlecmd = v
                break 
            end
        end
        print(singlecmd.id)
        --printall(singlecmd)
        replydata = protoservice.handl_single_cmd(db_data, singlecmd.id, nil, 100)
        --printall(replydata)
        --dataitems = singlecmd.dataItems
        replydata = protoservice.handl_single_cmd(db_data, 1, nil, 100)
        --printall(replydata)
        print("end")
    end)
    if not st then
        print(err)
    end
    --local log = table.concat(logger:getlog(), "\n")
end

InitCardReader()

while true do
    local Status, UserID = false, ''
    Status, UserID = GetUserID()
    if Status then
        udp:send(UserID)
        OpenValve(UserID)
    end
end

rf.dc_exit(icdev)
udp:close()

--update base_MeterInfo set UserID = '4400020101000296002' where MeterAddr1 = '131830';    