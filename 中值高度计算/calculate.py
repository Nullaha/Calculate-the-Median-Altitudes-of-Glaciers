import os
import re
import time
import xlwt
import string


file = open("D:\\Documents\Desktop\ceshihight\wanglu\Output.txt","r",encoding='UTF-8-sig') # RE
rows = []
urbans = []
# �г�txt��ÿһ��
for r in file:
    r = r.strip('\n')
    rows.append(r)
    print(r)
print(rows) #������� txt���� �����ݡ�



# ���� ������ �б�,��ɾ���ظ��
for i in rows:
    i = i.strip('\n')
    ii = i.split(',')
    # print(ii[1])
    if not ii[1] in urbans:
        urbans.append(ii[1])
print(urbans)
print(len(urbans))

#�γ�������Ҫ���ֵ�Ƕ��
zidian1 ={}
zidian0 = {}
for i in urbans:
    zidian2 = {}
    for j in rows:
        jj=j.split(',')
        if jj[1] == i:
            zidian2[jj[3]] = jj[2]
    print(zidian2)

    # ���ֵ䰴����key����������Ĭ����С����
    rank1_zidian2 = sorted(zidian2.keys())
    rank2_zidian2 = sorted(zidian2.items(), key=lambda x: x[0])
    rank3_zidian2 = dict(rank2_zidian2)
    print(rank3_zidian2)

    zidian1 = {i:rank3_zidian2}

    print(zidian1)
    zidian0.update(zidian1)

print(zidian0)

#������������
down = {}
for k,v in zidian0.items():
    print('����:'+k)
    zu = v #Ƕ���ֵ�����ֵ䡣
    print(zu)
    n = len(zu)
    print(n)  #��ʾ�м����ȸ���

    #python�����ֵ�������ֵ���ܺ�
    zulist = zu.values() #��zu�ֵ����vules������б�
    sum1 = 0
    for x in zulist:
        sum1 = float(x)+sum1
    allsum = sum1/2
    print(allsum) #��� �����/2��

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


# �ֵ�����д��excel
def write_to_excel(down, filename):
    # һ��Workbook��������൱�ڴ�����һ��Excel�ļ�
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('0', cell_overwrite_ok=True)
    # (�б���)
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

aha = "D:\\Documents\Desktop\ceshihight\wanglu\Output.xls"  #RE
write_to_excel(down, aha)






