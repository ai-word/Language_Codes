---
--- Generated by EmmyLua(https://github.com/EmmyLua)
--- Created by apple.
--- DateTime: 2019-03-26 20:57
---
--Lua不直接支持命名参数的语法，但是可以借助表来实现：将所有参数打包到一个表中，然后以这个表为函数的唯一参数
--修改文件名
function rname(arg)
    return os.rename(arg.old,arg.new)
end
s = rname({old="old.lua",new="new.lua"})
print(s)