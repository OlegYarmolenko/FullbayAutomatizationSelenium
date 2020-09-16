
import xlwt
import xlsxwriter

# i=0
#
# row_wt: int=0
# col_wt: int=1
# text_wt=100
# partstame=1
#
# workbook_wt = xlwt.Workbook()
# ws = workbook_wt.add_sheet("Partslist")
#
# while i<3:
#
#     ws.write(row_wt, 0, partstame)
#     ws.write(row_wt, 1, text_wt)
#
#     partstame+=partstame
#     text_wt+=text_wt
#     row_wt+=row_wt
#     i+=i
#     workbook_wt.save("writed.xls")

# import xlsxwriter module
import xlsxwriter

workbook_wt = xlsxwriter.Workbook('Newparts_list.xlsx')
worksheet_wt = workbook_wt.add_worksheet()

i=0
parttest="sdfsdf"
row_wt=0
col_wt=0
text_wt=55
partstame=1

while i<10:
    worksheet_wt.write(row_wt, col_wt, text_wt)
    row_wt= row_wt+1
    text_wt= text_wt+1
    i= i+1













workbook_wt.close()




