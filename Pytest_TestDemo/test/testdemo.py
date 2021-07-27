import os
# from openpyxl import load_workbook,styles
# content=['突然','lose','dnmd']
# excel =load_workbook(os.getcwd()+'/hello.xlsx')
# sheet = excel['Sheet1']
# style =styles.Font(color='#25BB60')
# for value in sheet.values:
#     if value[3] == 'result':
#         sheet.cell(2 , 4, value='pass').font = style
# sheet.append(content)
# sheet['B2'] = 'sex'
# sheet.cell(2,3,value='WDNMD')
# excel.save('hello.xlsx')
# excel.close()
# str='$loginname.data[0].from$'
# str1 = str.split('$')[1]
# f = str[str.find("$")+1:]
# s = f[:f.find('.')]
# print(os.getcwd())
# print(s)
# # print(f)
# # depend[s]
# print(str1[str1.find('.')+1:])
# import json
# x = {'姓名': '丢辣', '性别': '女', '年龄': '10'}
# j = json.dumps(x)
# print(j)
# print(json.loads(j))
import yaml
import pytest
file = open('D:\TestScrip\Version\Pytest_TestDemo\InterfaceTest\data\\test001.yaml','rb')
l = yaml.load(file, Loader=yaml.FullLoader)
# print(type(l))
@pytest.mark.parametrize('u',l)
def test01(u):
    print(u)
    print(type(u))


if __name__ == '__main__':
    pytest.main(['-s',"testdemo.py"])
# print(os.getcwd())