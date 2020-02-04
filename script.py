from openpyxl import load_workbook
import random

wb = load_workbook('./DATA.xlsx')
lst = (wb.sheetnames)

# print(random.choice(lst))
# Берём рандомный лист
sheet = wb[random.choice(lst)]
sheet.title
# заводим содержимое в переменные
vacancy = (sheet.cell(row=3, column=1).value)
zp_ot = (sheet.cell(row=3, column=2).value)
zp_do = (sheet.cell(row=3, column=3).value)
opyt = (sheet.cell(row=3, column=4).value)
obraz = (sheet.cell(row=3, column=5).value)
pol = (sheet.cell(row=3, column=6).value)
vozr_ot = (sheet.cell(row=3, column=7).value)
vozr_do = (sheet.cell(row=3, column=8).value)
opisanie = (sheet.cell(row=3, column=9).value)
name_hr = (sheet.cell(row=3, column=10).value)
mail = (sheet.cell(row=3, column=11).value)
phone = (sheet.cell(row=3, column=12).value)
priem_zv_c = (sheet.cell(row=3, column=13).value)
priem_zv_do = (sheet.cell(row=3, column=14).value)
dni_priem = (sheet.cell(row=3, column=15).value)
company = (sheet.cell(row=3, column=16).value)
opis_company = (sheet.cell(row=3, column=17).value)
gorod = (sheet.cell(row=3, column=18).value)
print(vacancy)