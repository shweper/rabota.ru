from openpyxl import load_workbook
import random

wb = load_workbook('./DATA.xlsx')
lst = (wb.sheetnames)

# print(random.choice(lst))
# Берём рандомный лист
# sheet = wb[random.choice(lst)]
sheet = wb[lst[1]]
sheet.title

# random.randint(A, B) - случайное целое число N, A ≤ N ≤ B.
gor = 2
adr = 2
for row in sheet.iter_cols(max_col=1):
    for value in row:
        gor = gor+1

for col in sheet.iter_rows(max_row=1):
    for value in col:
        adr = adr+1

random_gor = random.randint(2, gor-2)
random_adr = random.randint(2, adr-2)
print(gor, adr)
gorod = (sheet.cell(row=random_gor, column=1).value)
addres = (sheet.cell(row=random_gor, column=random_adr).value)

print(gorod)
print(addres)
