from openpyxl import Workbook

wb = Workbook()
excel = wb.active
for x in range(1, 10):
    for y in range(1, 3):
        excel.cell(row=x, column=y, value=y)
wb.save('text.xlsx')
