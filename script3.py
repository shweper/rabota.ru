from openpyxl import load_workbook
import random


wb = load_workbook('./DATA.xlsx')
lst = (wb.sheetnames)

# print(random.choice(lst))
# Берём рандомный лист
# sheet = wb[random.choice(lst)]
sheet = wb[lst[1]]
sheet.title
#print(sheet.cell(row=1, column=1).value)
# random.randint(A, B) - случайное целое число N, A ≤ N ≤ B.

a=0
for cell in sheet['A']:
    if cell.value == None:
        break
    else:
         a = a + 1
         #print(cell.value)
a=a-1
element = 2

for element in range(a):
    element = element + 1
    for cell in list(sheet.rows)[element]:
     print(str(cell.value))
print(element)
#random_gor = random.randint(2, gor-2)
#random_adr = random.randint(2, adr-2)
#print(gor, adr)
#gorod = (sheet.cell(row=random_gor, column=1).value)
#addres = (sheet.cell(row=random_gor, column=random_adr).value)

#print(gorod)
#print(addres)
