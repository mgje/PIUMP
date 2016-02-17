"uses openpyxl lib / does not work wit TP"
import openpyxl
wb = openpyxl.Workbook()
print wb.get_sheet_names()
sheet = wb.get_active_sheet()
print sheet.title
sheet.title = 'Spam Bacon Eggs Sheet'
print wb.get_sheet_names()
wb.save('example_copy.xlsx')