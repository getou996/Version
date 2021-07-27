import openpyxl
excel = openpyxl.load_workbook('hello.xlsx')
sheets = excel.sheetnames
for sheet in sheets:
    excel_sheet = excel[sheet]
    for value in excel_sheet.values:
        if type(value[0]) == int:
            connent={}
            connent['url'] = value[1]
            connent['type'] = value[2]
            connent['data'] = value[3]
            for key in list(connent.keys()):
                if connent[key] is None:
                    del connent[key]
            print(connent)
    # print('sheet:{} end'.format(sheet))
excel.close()