import pandas as pd
import time
import os
from xml.dom.minidom import Document

# 带有约束的文件路径
y_filePath = 'data/副本CN202M NS造车BOM 20190703-ECU筛选OK.xlsx'
# 所有品种代码文件
x_filePath = 'data/20190702.XLSX'
# 项目名称
carType = "CN202M"
# VIN码填充
vin = "LZW00000000000000"
# productionLineNo
productionLineNo = "BB"
serialNo = "BBG0004NS002"


# 结果存放目录
fileFolder = 'XML/'

# 带有约束的文件处理
y_dic_data = []
y_test_data = []
# 所有品种代码文件处理结果
x_test_data=[]
x_dic_data = []

# 删除文件
def del_file(path):
    for i in os.listdir(path):
        path_file = os.path.join(path, i)
        if os.path.isfile(path_file):
            os.remove(path_file)
        else:
            del_file(path_file)

# 带有约束的文件处理
def ExcelBoundOptions():
    df = pd.read_excel(y_filePath)
    for i in df.index.values:#获取行号的索引，并对其进行遍历：
        #根据i来获取每一行指定的数据 并利用to_dict转成字典
        if i >= 0:
            row_data=df.iloc[i,:].to_dict()
            y_test_data.append(row_data)

    # 遍历数组
    for dic in y_test_data:
        # 遍历字典
        # 去除首个字符&和末尾的.
        ops = str(dic["零部件用法约束代码 Options"])
        op = ops[:-1]
        # 设置约束条件
        # 如果是/只包含&的情况
        strss = str(dic["模块名称"]) + "=" + str(dic["零部件号PART NO."])
        if ops == "nan":
            json = {"partNo": dic["零部件号PART NO."], "ASM": dic["上级零部件号Next Up ASM."],"ChineseName": dic["零部件功能地址描述 FNA Description"],"StandardChineseName": dic["中文名称库标准名称 Standard Chinese Name"], "Options": "","lvs":dic["车型中文描述 Series in Chinese"], "module": strss,"oyu": [],"flag":0}
            y_dic_data.append(json)
        elif "&" in op and "/" not in op and "-" not in op:
            o_splits = op.split("&")
            json = {"partNo":dic["零部件号PART NO."],"ASM":dic["上级零部件号Next Up ASM."],"ChineseName":dic["零部件功能地址描述 FNA Description"],"StandardChineseName":dic["中文名称库标准名称 Standard Chinese Name"],"Options":op,"lvs":dic["车型中文描述 Series in Chinese"],"module":strss,"oyu":o_splits,"flag":0}
            y_dic_data.append(json)
        # elif "&" in op and "/" in op and "-" not in op:
        elif "&" in op and "/" in op and "-" not in op:
            op = ops[1:-1]
            arrh = op.split("&")
            yu = []
            huos = []
            for v in arrh:
                if len(v) > 3:
                    huos = v.split("/")
                else:
                    yu.append(v)
            json = {"partNo":dic["零部件号PART NO."],"ASM":dic["上级零部件号Next Up ASM."],"ChineseName":dic["零部件功能地址描述 FNA Description"],"StandardChineseName":dic["中文名称库标准名称 Standard Chinese Name"],"Options":op,"lvs":dic["车型中文描述 Series in Chinese"],"module":strss,"oyu":yu,"huo":huos,"flag":1}
            y_dic_data.append(json)
            # print(yu,huos)
        # 有与或非
        elif "&" in op and "/" in op and "-"  in op:
            huo_1 = []
            yu_1 = []
            fei_1 = []
            op = ops[1:-1]
            arr = op.split("&")
            for v in arr:
                if len(v) > 3:
                    arr1 = v.split("/")
                    for vk in arr1:
                        if len(vk) > 3:
                            arr2 = vk.split("-")
                            fei_1 = arr2[1:]
                            huo_1.append(arr2[0])
                        else:
                            huo_1.append(vk)
                else:
                    yu_1.append(v)
            json = {"partNo":dic["零部件号PART NO."],"ASM":dic["上级零部件号Next Up ASM."],"ChineseName":dic["零部件功能地址描述 FNA Description"],"StandardChineseName":dic["中文名称库标准名称 Standard Chinese Name"],"Options":op,"lvs":dic["车型中文描述 Series in Chinese"],"module":strss,"oyu":yu_1,"huo":huo_1,"fei":fei_1,"flag":2}
            y_dic_data.append(json)

# // excel处理
def ExcelHandleOp():
    df = pd.read_excel(x_filePath)
    for i in df.index.values:#获取行号的索引，并对其进行遍历：
        #根据i来获取每一行指定的数据 并利用to_dict转成字典
        if i >= 0:
            row_data=df.iloc[i,:].to_dict()
            x_test_data.append(row_data)
    # 遍历数组
    print(len(x_test_data))
    for dic in x_test_data:
        # 遍历字典
        temp = []
        for key in dic:
            if dic[key] == "X":
                temp.append(key)
        temps = []
        for keys in temp :
            if "." not in keys:
                temps.append(keys)

        astr = ','.join(temps)
        json = {"car":dic["Car"],"VSN":dic["VSN"],"data":astr,"datarr":temp,"vehiclePartNo":"","lv0":dic["Level"]}
        x_dic_data.append(json)

# 生成vehiclePartNo dic_data y_dic_data
def productvehiclePartNo():
    len0 = len(x_dic_data)
    for i in range(len0) :
        for dic in y_dic_data:
            if dic["flag"] == 0:
                flag = False
                y_arr = dic["oyu"]
                if len(y_arr)<1:
                    flag = True
                else:
                    for v in y_arr:
                        if v in x_dic_data[i]["data"] and x_dic_data[i]["lv0"] in dic["lvs"]:
                            flag = True
                        else:
                            flag = False
                            break
                if flag:
                    x_dic_data[i]["vehiclePartNo"] += dic["module"] + ","
            elif dic["flag"] == 1:
                global yflag,hflag
                yflag = False
                hflag = False
                y_arr = dic["oyu"]
                h_arr = dic["huo"]
                for v in y_arr:
                    if v in x_dic_data[i]["data"] and x_dic_data[i]["lv0"] in dic["lvs"]:
                        yflag = True
                    else:
                        yflag = False
                        break
                for v in h_arr:
                    if v in x_dic_data[i]["data"] and x_dic_data[i]["lv0"] in dic["lvs"]:
                        hflag = True
                        break
                    else:
                        hflag = False

                if hflag and yflag:
                    x_dic_data[i]["vehiclePartNo"] += dic["module"] + ","
            elif dic["flag"] == 2:
                yflag_1 = False
                hflag_1 = False
                fflag_1 = False
                y_arr = dic["oyu"]
                h_arr = dic["huo"]
                f_arr = dic["fei"]
                for v in y_arr:
                    if v in x_dic_data[i]["data"] and x_dic_data[i]["lv0"] in dic["lvs"]:
                        yflag_1 = True
                    else:
                        yflag_1 = False
                        break

                for v in h_arr:
                    if v in x_dic_data[i]["data"] and x_dic_data[i]["lv0"] in dic["lvs"]:
                        hflag_1 = True
                        break
                    else:
                        hflag_1 = False

                for v in f_arr:
                    if v in x_dic_data[i]["data"] and x_dic_data[i]["lv0"] in dic["lvs"]:
                        fflag_1 = False
                        break
                    else:
                        fflag_1 = True
                if hflag_1 and yflag_1 and fflag_1:
                    x_dic_data[i]["vehiclePartNo"] += dic["module"] + ","

# 生成xml文件
def productXML(arr):
    counts = 0
    print(len(arr))
    for dic in arr:
        vehicleVsn = dic["VSN"]
        vehicleRpo = dic["data"]
        vehiclePartNo = dic["vehiclePartNo"]
        DefineXML(vin, vehicleVsn, carType, serialNo, productionLineNo, vehicleRpo, vehiclePartNo,counts)
# 定义XML
def DefineXML(vin,vehicleVsn,carType,serialNo,productionLineNo,vehicleRpo,vehiclePartNo,counts):
    doc = Document()
    vehicleDatas = doc.createElement('vehicleDatas')
    doc.appendChild(vehicleDatas)
    vehicle = doc.createElement('vehicle')
    vehicleDatas.appendChild(vehicle)
    vehicle.setAttribute("config","vehicleDataConfig")
    data_vin = doc.createElement('data')
    data_vin_text = doc.createTextNode(vin)
    data_vin.appendChild(data_vin_text)
    data_vin.setAttribute("name","vin")
    vehicle.appendChild(data_vin)

    data_vsn = doc.createElement('data')
    data_vsn_text = doc.createTextNode(vehicleVsn)
    data_vsn.appendChild(data_vsn_text)
    data_vsn.setAttribute("name","vehicleVsn")
    vehicle.appendChild(data_vsn)

    data_carType = doc.createElement('data')
    data_carType_text = doc.createTextNode(carType)
    data_carType.appendChild(data_carType_text)
    data_carType.setAttribute("name","carType")
    vehicle.appendChild(data_carType)

    data_serialNo = doc.createElement('data')
    data_serialNo_text = doc.createTextNode(serialNo)
    data_serialNo.appendChild(data_serialNo_text)
    data_serialNo.setAttribute("name","serialNo")
    vehicle.appendChild(data_serialNo)

    data_lno = doc.createElement('data')
    data_lno_text = doc.createTextNode(productionLineNo)
    data_lno.appendChild(data_lno_text)
    data_lno.setAttribute("name","productionLineNo")
    vehicle.appendChild(data_lno)

    data_Rpo = doc.createElement('data')
    data_Rpo_text = doc.createTextNode(vehicleRpo)
    data_Rpo.appendChild(data_Rpo_text)
    data_Rpo.setAttribute("name","vehicleRpo")
    vehicle.appendChild(data_Rpo)

    data_vpno = doc.createElement('data')
    data_vpno_text = doc.createTextNode(vehiclePartNo[:-1])
    data_vpno.appendChild(data_vpno_text)
    data_vpno.setAttribute("name","vehiclePartNo")
    vehicle.appendChild(data_vpno)
    ticks = time.time()
    f = open("XML/"+vehicleVsn[0:4]+"-"+str(ticks).split(".")[0]+'.vdf', 'w')
    doc.writexml(f, indent='\t', newl='\n', addindent='\t', encoding='utf-8')
    f.close()
# excel数据处理
def ExcelHandle():
    ExcelBoundOptions()
    ExcelHandleOp()
    productvehiclePartNo()
    productXML(x_dic_data)

if __name__ == '__main__':
    del_file(fileFolder)
    ExcelHandle()
