import os
import re
import time
import xlwt
import string


<<<<<<< HEAD
file = open("D:\\Documents\Desktop\test\test1.txt","r",encoding='UTF-8-sig')
=======
file = open("D:\\Documents\Desktop\hest2\lzj\\yinduhe.csv","r",encoding='UTF-8-sig')
>>>>>>> finally commit
rows = []
urbans = []
# 列出txt中每一行
for r in file:
    r = r.strip('\n')
    rows.append(r)
    print(r)
print(rows) # 输出的是 txt表中 行数据。


# 生成 Glaciers 列表,并删除重复项。
for i in rows:
    i = i.strip('\n')
    ii = i.split(',')
    # print(ii[1])
    if not ii[1] in urbans:
        urbans.append(ii[1])
print(urbans)
print(len(urbans))

# 形成了我想要的字典嵌套
zidian1 ={}
zidian0 = {}
for i in urbans:
    zidian2 = {}
    for j in rows:
        jj=j.split(',')
        if jj[1] == i:
            zidian2[jj[3]] = jj[2]
    print(zidian2)

    # 对字典按键（key）进行排序（默认由小到大）
    rank1_zidian2 = sorted(zidian2.keys())
    rank2_zidian2 = sorted(zidian2.items(), key=lambda x: x[0])
    rank3_zidian2 = dict(rank2_zidian2)
    print(rank3_zidian2)

    zidian1 = {i:rank3_zidian2}

    print(zidian1)
    zidian0.update(zidian1)

print(zidian0)

# 哈哈哈计算了
down = {}
for k,v in zidian0.items():
    print('名字:'+k)
    zu = v # zu是一个字典，也就是嵌套字典的子字典。
    print(zu)
    n = len(zu)
    print(n)  # 表示有几个等高线

<<<<<<< HEAD
    # python 计算字典里所有值的总和
    zulist = zu.values() # 把zu字典里的vules变成了列表。
=======
    #python计算字典里所有值的总和 *8
    zulist = zu.values() #把zu字典里的vules变成了列表。
>>>>>>> finally commit
    sum1 = 0
    for x in zulist:
        sum1 = float(x)+sum1
    allsum = sum1/2
    print(allsum) # 求得 总面积/2。

    sum0 = 0
    for i,j in zu.items():
        sum0 = sum0 + float(zu[i])
        if sum0 >= allsum:
            print('zhongzhi'+i)
            break
    down[k] =i
print("aaaaa:")
print(down)
print(len(down))


# 字典数据写入excel
def write_to_excel(down, filename):
    # 一个Workbook对象，这就相当于创建了一个Excel文件
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('0', cell_overwrite_ok=True)
    # 第一行(列标题)
    sheet.write(0, 0, 'name')
    sheet.write(0, 1, 'contour')

    w = 1
    for x,y in down.items():
        sheet.write(w,0,x)
        sheet.write(w,1,y)
        w = w + 1

    #for i in range(len(down)):
        #sheet.write(i + 1, 0, down[i])
        #sheet.write(i + 1, 1, down[i][1])


    book.save(filename)

<<<<<<< HEAD
aha = "D:\\Documents\Desktop\test\test1.xls"
=======
aha = "D:\\Documents\Desktop\hest2\lzj\out1_ydh.xls"
>>>>>>> finally commit
write_to_excel(down, aha)






