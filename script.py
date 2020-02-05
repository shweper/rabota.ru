from openpyxl import load_workbook
import random

wb = load_workbook('./DATA.xlsx')
lst = (wb.sheetnames)

# print(random.choice(lst))
# Берём рандомный лист
# sheet = wb[random.choice(lst)]
sheet = wb[lst[0]]
sheet.title

# random.randint(A, B) - случайное целое число N, A ≤ N ≤ B.
a = 3
b = [a]
for row in sheet.iter_cols(max_col=1):
    for value in row:
        a = a+1

# альтернативный рандом
#        b.append(a)
# b.pop()
# b.pop()
# b.pop()
# print(b)
# i = random.choice(b)

i = random.randint(3, a-3)
################### заводим содержимое в переменные ################################
# print(a)
vacancy = (sheet.cell(row=i, column=1).value)
zp_ot = (sheet.cell(row=i, column=2).value)
zp_do = (sheet.cell(row=i, column=3).value)
opyt = (sheet.cell(row=i, column=4).value)
obraz = (sheet.cell(row=i, column=5).value)
pol = (sheet.cell(row=i, column=6).value)
vozr_ot = (sheet.cell(row=i, column=7).value)
vozr_do = (sheet.cell(row=i, column=8).value)
opisanie = (sheet.cell(row=i, column=9).value)
name_hr = (sheet.cell(row=i, column=10).value)
mail = (sheet.cell(row=i, column=11).value)
phone = (sheet.cell(row=i, column=12).value)
priem_zv_c = (sheet.cell(row=i, column=13).value)
priem_zv_do = (sheet.cell(row=i, column=14).value)
dni_priem = (sheet.cell(row=i, column=15).value)
company = (sheet.cell(row=i, column=16).value)
opis_company = (sheet.cell(row=i, column=17).value)
# gorod = (sheet.cell(row=i, column=18).value)
# print(vacancy)


