# -*- coding: utf-8 -*-

import xlrd
import pg_tool


def save_remark(fileName):
    wb = xlrd.open_workbook(fileName)
    sheet = wb.sheet_by_index(0)
    sqlst=[]
    for i in range(1, sheet.nrows):
        if i%50==0:
            pg_tool.insert_update(sqlst=sqlst)
            sqlst=[]
        sqlst.append("insert into heds_remark(remark_content) values('%s');" % sheet.cell(i,3).value)
    return 'OK'

print(save_remark("d:/contract_remark.xlsx"))
