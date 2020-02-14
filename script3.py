from openpyxl import load_workbook
import random


wb = load_workbook('./DATA.xlsx')
lst = (wb.sheetnames)

sheet = wb[lst[1]]
sheet.title
# random.randint(A, B) - случайное целое число N, A ≤ N ≤ B.

barnaul_adr = []
volgograd_adr = []
voronej_adr = []
ekaterenburg_adr = []
izevsk_adr = []
irkuts_adr = []
kazan_adr = []
kaliningrad_adr = []
kemerovo_adr = []
krasnodar_adr = []
krasnoyars_adr = []
moskow_adr = []
naber_cheln_adr = []
nizniy_novgorod_adr = []
novosib_adr = []
omsk_adr = []
orenburg_adr = []
perm_adr = []
rostov_na_dony_adr = []
ryazan_adr = []
samara_adr = []
sankt_peter_adr = []
saratov_adr = []
sochi_and_adler = []
toliatty_adr = []
tomsk_adr = []
tyla_adr = []
tumen_adr = []
ufa_adr = []
chelabinsk_adr = []
yaroslavl_adr = []
musor_exela = []
goroda_arr = [musor_exela, barnaul_adr, volgograd_adr, voronej_adr, ekaterenburg_adr, izevsk_adr, irkuts_adr, kazan_adr, kaliningrad_adr, kemerovo_adr, krasnodar_adr, krasnoyars_adr, moskow_adr, naber_cheln_adr, nizniy_novgorod_adr, novosib_adr, omsk_adr, orenburg_adr, perm_adr, rostov_na_dony_adr, ryazan_adr, samara_adr, sankt_peter_adr, saratov_adr, sochi_and_adler, toliatty_adr, tomsk_adr, tyla_adr, tumen_adr, ufa_adr, chelabinsk_adr, yaroslavl_adr]
number_gorod = 0
#for cell in sheet[goroda_arr[number_gorod]]:
#    if cell.value == None:
#        break
kolichestvo_gorodov = 32
for number_gorod in range(kolichestvo_gorodov):
    for cell in list(sheet.rows)[number_gorod]:
        if cell.value == None:
            number_gorod = number_gorod +1
            break
        else:
            goroda_arr[number_gorod].append(cell.value)
        # goroda_arr[number_adr].pop(0)

    #print(str(cell.value))
#print(element)
goroda_arr.pop(0)
#print(goroda_arr)

print(goroda_arr[1][0])

vca = 'Программист'
slovar = {
    'Программист': 'txi'}
result = slovar.get(vca)
print(result)
#browser.find_elements_by_xpath(result)[0]

#Рубрики
xpath_rubriks = {
    'IT / Интернет / Телеком': '//*[@id="jqmContent"]/div/div[1]/ul/li[1]/ul[1]/li/a',
    'Топ-менеджмент': '//*[@id="jqmContent"]/div/div[1]/ul/li[1]/ul[2]/li/a',

    'Банки / Инвестиции / Ценные бумаги': '//*[@id="jqmContent"]/div/div[1]/ul/li[1]/ul[3]/li/ul/li[1]/a',
    'Бухгалтерия / Аудит / Экономика предприятия':'//*[@id="jqmContent"]/div/div[1]/ul/li[1]/ul[3]/li/ul/li[2]/a',
    'Страхование':'//*[@id="jqmContent"]/div/div[1]/ul/li[1]/ul[3]/li/ul/li[3]/a',

    'HR / Кадры / Подбор персонала':'//*[@id="jqmContent"]/div/div[1]/ul/li[1]/ul[4]/li/ul/li[1]/a',
    'Административный персонал':'//*[@id="jqmContent"]/div/div[1]/ul/li[1]/ul[4]/li/ul/li[2]/a',
    'Консалтинг / Тренинги':'//*[@id="jqmContent"]/div/div[1]/ul/li[1]/ul[4]/li/ul/li[3]/a',
    'Охрана / Безопасность':'//*[@id="jqmContent"]/div/div[1]/ul/li[1]/ul[4]/li/ul/li[4]/a',
    'Юриспруденция':'//*[@id="jqmContent"]/div/div[1]/ul/li[1]/ul[4]/li/ul/li[5]/a',
    'Дизайн / Полиграфия':'//*[@id="jqmContent"]/div/div[1]/ul/li[1]/ul[4]/li/ul/li[6]/a',
    'Маркетинг / Реклама / PR':'//*[@id="jqmContent"]/div/div[1]/ul/li[1]/ul[4]/li/ul/li[7]/a',
    'СМИ / Издательства':'//*[@id="jqmContent"]/div/div[1]/ul/li[1]/ul[4]/li/ul/li[8]/a',

    'Госслужба / Некоммерческие организации':'//*[@id="jqmContent"]/div/div[1]/ul/li[1]/ul[6]/li/ul/li[1]/a',
    'Культура / Искусство / Развлечения':'//*[@id="jqmContent"]/div/div[1]/ul/li[1]/ul[6]/li/ul/li[2]/a',
    'Образование / Наука':'//*[@id="jqmContent"]/div/div[1]/ul/li[1]/ul[6]/li/ul/li[3]/a',

    'Торговля':'//*[@id="jqmContent"]/div/div[1]/ul/li[2]/ul[1]/li/a',
    'Производство / Агропром':'//*[@id="jqmContent"]/div/div[1]/ul/li[2]/ul[2]/li/a',

    'Недвижимость / Риелторские услуги':'//*[@id="jqmContent"]/div/div[1]/ul/li[2]/ul[3]/li/ul/li[1]/a',
    'Строительство / ЖКХ / Эксплуатация':'//*[@id="jqmContent"]/div/div[1]/ul/li[2]/ul[3]/li/ul/li[2]/a',

    'Логистика / Склад / ВЭД':'//*[@id="jqmContent"]/div/div[1]/ul/li[2]/ul[4]/li/ul/li[1]/a',
    'Транспорт / Автобизнес / Автосервис':'//*[@id="jqmContent"]/div/div[1]/ul/li[2]/ul[4]/li/ul/li[2]/a',

    'Красота / Фитнес / Спорт':'//*[@id="jqmContent"]/div/div[1]/ul/li[2]/ul[5]/li/ul/li[1]/a',
    'Медицина / Фармация / Ветеринария':'//*[@id="jqmContent"]/div/div[1]/ul/li[2]/ul[5]/li/ul/li[2]/a',

    'Бытовые услуги / Обслуживание оборудования':'//*[@id="jqmContent"]/div/div[1]/ul/li[2]/ul[6]/li/ul/li[1]/a',
    'Домашний персонал':'//*[@id="jqmContent"]/div/div[1]/ul/li[2]/ul[6]/li/ul/li[2]/a',
    'Рестораны / Питание':'//*[@id="jqmContent"]/div/div[1]/ul/li[2]/ul[6]/li/ul/li[3]/a',
    'Туризм / Гостиницы':'//*[@id="jqmContent"]/div/div[1]/ul/li[2]/ul[6]/li/ul/li[4]/a',
    'Работа без специальной подготовки / Без опыта':'//*[@id="jqmContent"]/div/div[1]/ul/li[2]/ul[6]/li/ul/li[5]/a',
    'Работа для студентов / Стажировки':'//*[@id="jqmContent"]/div/div[1]/ul/li[2]/ul[8]/li/a',
}
#Словари для рубрик
#IT / Интернет / Телеком
xpath_it_ithernet = {
    #Программирование, разработка
    'Ведущий разработчик' : '/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[1]/label/input',
    'Программист' : '/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[2]/label/input',
    'Проектировщик': '/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[3]/label/input',
    'Тестировщик': '/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[4]/label/input',
    #
    #Виды ПО
    #
    '1С': '/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[1]/label/input',
    'ERP-системы': '//*[@id="jqmContent"]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[2]/label/input',
    'Банковское ПО': '/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[3]/label/input',
    'Игровое ПО': '//*[@id="jqmContent"]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[4]/label/input',
    #
    #Аналитика
    #
    'Бизнес-аналитик': '/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[3]/li/ul/li[1]/label/input',
    'Системный аналитик': '/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[3]/li/ul/li[2]/label/input',
    'Технический писатель': '/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[3]/li/ul/li[3]/label/input',
    #
    #Сети, защита информации
    #
    'Компьютерная, информационная безопасность': '/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[4]/li/ul/li[1]/label/input',
    'Системное администрирование, DBA': '/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[4]/li/ul/li[2]/label/input',
    #
    #Монтаж, техобслуживание
    #
    'Беспроводные технологии, сотовая связь': '/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[5]/li/ul/li[1]/label/input',
    'Монтаж оборудования и сетей': '/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[5]/li/ul/li[2]/label/input',
    'Обслуживание банкоматов и платежных терминалов': '/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[5]/li/ul/li[3]/label/input',
    'Сборка ПК': '/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[5]/li/ul/li[4]/label/input',
    'Техподдержка, сервисное обслуживание': '/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[5]/li/ul/li[5]/label/input',
    #
    #Продажи, работа с клиентами
    #
    'Продажи, работа с клиентами': '/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[1]/label/input',
    'Тендеры': '/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[2]/label/input',
    'Электронная коммерция': '/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[3]/label/input',
    #
    #Маркетинг, консалтинг
    #
    'IT-консалтинг': '/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[1]/label/input',
    'Интернет-маркетинг, SMO, SMM': '/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[2]/label/input',
    'Поисковая оптимизация, SEO': '/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[3]/label/input',
    #
    #Дизайн, верстка, контент
    #
    'Веб-дизайн': '/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[3]/li/ul/li[1]/label/input',
    'Верстка':  '/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[3]/li/ul/li[2]/label/input',
    'Контент, модерация': '/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[3]/li/ul/li[3]/label/input',
    'Мультимедиа': '/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[3]/li/ul/li[4]/label/input',
    #
    # Операторы
    #
    'Call-центр': '/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[4]/li/ul/li[1]/label/input',
    'ПК, БД': '/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[4]/li/ul/li[2]/label/input',
    #
    #Руководство
    #
    'IT-директор, технический директор': '/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[5]/li/ul/li[1]/label/input',
    'Директор, управляющий': '/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[5]/li/ul/li[2]/label/input',
    'Руководитель отдела, заместитель руководителя': '/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[5]/li/ul/li[2]/label/input',
    'Руководитель проекта': '/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[5]/li/ul/li[4]/label/input',
    'Небольшой опыт, нет опыта': '/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[6]/li/label/input',
    'Другое': '/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[7]/li/label/input'

}
#Топ-менеджмент
xpath_top_menegment = {
    #Административное управление
    #
    'HR-директор, директор по персоналу': '/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[1]/label/input',
    'Директор, управляющий': '/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[2]/label/input',
    'Директор филиала, офиса': '/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[3]/label/input',
    'Исполнительный директор, административный директор': '/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[4]/label/input',
    #
    #Функциональное управление
    #
    'IT-директор, технический директор': '/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[1]/label/input',
    'Арт-директор, креативный директор': '/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[2]/label/input',
    #
    #Финансы, коммерция, развитие
    #
    'Директор по маркетингу': '/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[1]/label/input',
    'Директор по развитию': '/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[2]/label/input',
    'Коммерческий директор, директор по продажам': '/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[3]/label/input',
    'Финансовый директор': '/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[4]/label/input',
    'Другое': '/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/label/input',
}

#ФИНАНСЫ / СТРАХОВАНИЕ
#Банки / Инвестиции / Ценные бумаги
xpath_banki_invest = {
    #Операции, направления
    #
    'Валютные операции': '/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[1]/label/input',
    'Лизинг': '/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[2]/label/input',
    'Межбанковские операции': '/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[3]/label/input',
    'Налогообложение':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[4]/label/input',
    'Обслуживание банкоматов': '/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[5]/label/input',
    'Пластиковые карты': '/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[6]/label/input',
    'Финансовая аналитика': '/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[7]/label/input',
    'Ценные бумаги': '/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[8]/label/input',
    #
    #Работа с клиентами
    #
    'Консультирование, работа с клиентами': '/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[1]/label/input',
    'Кредитование': '/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[2]/label/input',
    'Продажи финансовых услуг': '/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[3]/label/input',
    'Расчетно-кассовое обслуживание': '/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[4]/label/input',
    #
    #Руководство
    #
    'Руководитель департамента, высшее руководство': '/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[1]/label/input',
    'Руководитель отдела, заместитель руководителя': '/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[2]/label/input',
    'Небольшой опыт, нет опыта': '/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[3]/li/label/input',
    'Другое': '/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[4]/li/label/input'

}
#Бухгалтерия / Аудит / Экономика предприятия
xparh_buhgalteria = {
    #Бухгалтерия
    #
    '1C': '//*[@id="jqmContent"]/div/div[1]/ul/li[1]/ul/li/ul/li[1]/label/input',
    'Бухгалтер': '/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[2]/label/input',
    'Казначейство': '/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[3]/label/input',
    'Касса': '/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[4]/label/input',
    'МСФО, GAAP':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[5]/label/input',
    'Налоговый учет': '/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[6]/label/input',
    'Первичная документация': '/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[7]/label/input',
    'Расчет заработной платы': '/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[8]/label/input',
    'Расчет себестоимости': '/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[9]/label/input',
    'Расчеты с покупателями': '/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[10]/label/input',
    'Составление отчетности': '/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[11]/label/input',
    'Учет основных средств и материальных активов': '/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[12]/label/input',
    #
    #Аудит, экономика предприятия
    #
    'Аудит, внутренний контроль': '/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[1]/label/input',
    'Планово-экономическое управление': '/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[2]/label/input',
    'Финансовый консалтинг': '/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[3]/label/input',
    #
    #Руководство
    #
    'Главный бухгалтер': '/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[1]/label/input',
    'Заместитель главного бухгалтера': '/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[2]/label/input',
    'Руководитель отдела, заместитель руководителя': '/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[3]/label/input',
    'Финансовый директор': '/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[4]/label/input',
    'Небольшой опыт, нет опыта': '/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[3]/li/label/input',
    'Другое': '/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[4]/li/label/input'
}

#Страхование
xpath_strahovanie= {
    #Имущественное страхование
    #
    'Автострахование':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[1]/label/input',
    'Страхование недвижимости, имущества':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[2]/label/input',
    #
    #Личное страхование
    #
    'Медицинское страхование':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[1]/label/input',
    'Страхование жизни':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[2]/label/input',

#Страхование бизнеса

    'Корпоративное страхование':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[3]/li/ul/li/label/input',

    #Оценка, урегулирование убытков

    'Оценка, экспертиза':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[1]/label/input',
    'Урегулирование убытков':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[2]/label/input',

    #Руководство

    'Директор, управляющий':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[1]/label/input',
    'Директор филиала':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[2]/label/input',
    'Руководитель отдела, заместитель руководителя':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[3]/label/input',
    'Небольшой опыт, нет опыта':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[3]/li/label/input',
    'Другое':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[4]/li/label/input'
}


#ОФИСНЫЕ СЛУЖБЫ / БИЗНЕС-УСЛУГИ
#HR / Кадры / Подбор персонала
xpath_hr_kadri = {
    #Кадровое дело

    'Кадровое делопроизводство':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[1]/label/input',
    'Охрана труда':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[2]/label/input',

#Развитие персонала

    'Льготы и компенсации':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[1]/label/input',
    'Обучение и развитие персонала':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[2]/label/input',
    'Тренинги':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[3]/label/input',

    #Консультирование

    'Кадровый консалтинг':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[3]/li/ul/li[1]/label/input',
    'Психологические консультации':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[3]/li/ul/li[2]/label/input',

#Подбор персонала

    'Аутстаффинг, лизинг персонала':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[1]/label/input',
    'Подбор домашнего персонала':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[2]/label/input',
    'Подбор сотрудников, рекрутмент':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[3]/label/input',
    'Региональный подбор':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[4]/label/input',
    'Хедхантинг, executive search':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[5]/label/input',

#Руководство

    'HR-директор, директор по персоналу':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[1]/label/input',
    'Директор, управляющий':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[2]/label/input',
    'Руководитель отдела, заместитель руководителя':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[3]/label/input',
    'Небольшой опыт, нет опыта':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[4]/label/input',
    'Другое':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[5]/label/input'
}

#Административный персонал
xpath_adm_personal= {
    #Секретариат, делопроизводство

    'Архив':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[1]/label/input',
    'Делопроизводство':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[2]/label/input',
    'Офис-менеджер':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[3]/label/input',
    'Переводчик':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[4]/label/input',
    'Помощник руководителя':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[5]/label/input',
    'Ресепшн, приемная':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[6]/label/input',
    'Секретарь':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[7]/label/input',

    #Операторы

    'Оператор call-центра, на телефоне':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[1]/label/input',
    'Оператор ПК, БД':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[2]/label/input',

    #АХО

    'Администратор':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[1]/label/input',
    'Водитель':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[2]/label/input',
    'Диспетчер':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[3]/label/input',
    'Курьер':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[4]/label/input',
    'Специалист АХО':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[5]/label/input',
    'Уборщик':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[6]/label/input',

    #Руководство

    'Исполнительный директор, административный директор':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[1]/label/input',
    'Руководитель отдела, заместитель руководителя':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[2]/label/input',
    'Небольшой опыт, нет опыта':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[3]/label/input',
    'Другое':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[4]/label/input'

}
#Консалтинг / Тренинги
xpath_konsalting = {
    #Консалтинг
    'IT-консалтинг':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[1]/label/input',
    'Кадровый консалтинг':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[2]/label/input',
    'Консалтинг в области налогов и бухучета':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[3]/label/input',
    'Управленческий консалтинг, организационное развитие':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[4]/label/input',
    'Юридический консалтинг':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[5]/label/input',

    #Исследования
    'Аналитика, исследования рынка':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li/label/input',

    #Продажи
    'Продажа услуг, работа с клиентами':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[3]/li/ul/li/label/input',

    #Тренинги
    'Психологическое консультирование':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[1]/label/input',
    'Тренинги, коучинг':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[2]/label/input',
    #Руководство
    'Директор по развитию':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[1]/label/input',
    'Директор, управляющий':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[2]/label/input',
    'Руководитель отдела, заместитель руководителя':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[3]/label/input',
    'Небольшой опыт, нет опыта':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[4]/label/input',
    'Другое':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[5]/label/input'
    }

#Охрана / Безопасность
xpath_ohrana= {
    'Инкассация':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[1]/label/input',
    'Личная охрана, охрана мероприятий':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[2]/label/input',
    'Охрана объектов, сопровождение грузов':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[3]/label/input',
    'Сторож / Вахтер / Консьерж':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[4]/label/input',

    'Коллекторская деятельность':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[1]/label/input',
    'Экономическая безопасность':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[2]/label/input',

    'Сотрудники полиции, МВД, МЧС':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li/label/input',

    'Системы безопасности и видеонаблюдения':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li/label/input',

    'Директор, управляющий':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[3]/li/ul/li[1]/label/input',
    'Начальник охраны, руководитель СБ':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[3]/li/ul/li[2]/label/input',

    'Небольшой опыт, нет опыта':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[3]/li/ul/li[3]/label/input',
    'Другое':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[3]/li/ul/li[4]/label/input'
}

#Юриспруденция
xpath_urisprud= {
    'Авторское право, интеллектуальная собственность':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[1]/label/input',
    'Административное право':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[2]/label/input',
    'Гражданское право':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[3]/label/input',
    'Трудовое право':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[4]/label/input',
    'Уголовное право':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[5]/label/input',
    'Финансовое, налоговое право':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[6]/label/input',

    'Адвокатура, судебная деятельность':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[1]/label/input',
    'Арбитраж':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[2]/label/input',
    'Лицензирование':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[3]/label/input',
    'Нотариат':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[4]/label/input',
    'Регистрация, ликвидация предприятий':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[5]/label/input',
    'Юридическое консультирование':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[6]/label/input',
    'Юридическое сопровождение бизнеса':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[7]/label/input',

    'Директор, управляющий':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[1]/label/input',
    'Руководитель отдела, заместитель руководителя:':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[2]/label/input',
    'Небольшой опыт, нет опыта':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[3]/label/input',
    'Другое':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[4]/label/input'
}


#МАРКЕТИНГ / РЕКЛАМА / СМИ
#Дизайн / Полиграфия
xpath_design= {
    '3D-дизайн, промышленный дизайн':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[1]/label/input',
    'Веб-дизайн, мультимедиа':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[2]/label/input',
    'Дизайнер':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[3]/label/input',
    'Дизайн интерьера':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[4]/label/input',
    'Дизайн одежды, аксессуаров':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[5]/label/input',
    'Дизайн печатных изданий':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[6]/label/input',
    'Дизайн упаковки, рекламной и сувенирной продукции':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[7]/label/input',
    'Ландшафтный дизайн':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[8]/label/input',
    'Флористика':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[9]/label/input',

    'Продажа полиграфических услуг':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li/label/input',

    'Препресс, верстка':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[1]/label/input',
    'Технолог печати, инженер':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[2]/label/input',
    'Типографские мастера и рабочие':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[3]/label/input',

    'Арт-директор, креативный директор':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[3]/li/ul/li[1]/label/input',
    'Директор, управляющий':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[3]/li/ul/li[2]/label/input',
    'Руководитель отдела, заместитель руководителя':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[3]/li/ul/li[3]/label/input',
    'Небольшой опыт, нет опыта':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[3]/li/ul/li[4]/label/input',
    'Другое':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[3]/li/ul/li[5]/label/input'
}
#Маркетинг / Реклама / PR
xpath_marketing= {
    'BTL-услуги':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[1]/label/input',
    'Аналитика, исследования рынка':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[2]/label/input',
    'Бренд-менеджмент':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[3]/label/input',
    'Интернет-маркетинг, SMO, SMM':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[4]/label/input',
    'Консультирование':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[5]/label/input',
    'Мерчандайзинг':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[6]/label/input',
    'Рекламно-сувенирная продукция':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[7]/label/input',
    'Трейд-маркетинг':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[8]/label/input',

    'Event-услуги':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[1]/label/input',
    'Выставочная деятельность':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[2]/label/input',
    'Копирайтер, редактор, журналист':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[3]/label/input',
    'Маркетинговые коммуникации, PR':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[4]/label/input',
    'Промоутер, модель':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[5]/label/input',

    'Медиапланирование':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[1]/label/input',
    'Продажа рекламных услуг':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[2]/label/input',
    'Производство рекламы':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[3]/label/input',

    'Директор по маркетингу, развитию':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[1]/label/input',
    'Директор по продажам':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[2]/label/input',
    'Директор, управляющий':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[3]/label/input',
    'Креативный директор, арт-директор':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[4]/label/input',
    'Руководитель проекта, направления':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[5]/label/input',
    'Небольшой опыт, нет опыта':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[6]/label/input',
    'Другое':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[7]/label/input'

}

#СМИ / Издательства
xpath_smi= {
    'Журналистика':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[1]/label/input',
    'Корректура':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[2]/label/input',
    'Перевод':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[3]/label/input',
    'Редакторское дело':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[4]/label/input',

    'Дизайн, верстка, препресс':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[1]/label/input',
    'Дистрибуция, распространение печатной продукции':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[2]/label/input',
    'Издательская деятельность':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[3]/label/input',
    'Фотосъемка, фотодело':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[4]/label/input',

    'Продажа рекламных услуг':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[1]/label/input',

    'Производство телепрограмм и кинофильмов':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[1]/label/input',
    'Радио':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[2]/label/input',
    'Телевидение':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[3]/label/input',

    'Арт-директор, креативный директор':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[1]/label/input',
    'Главный редактор, шеф-редактор':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[2]/label/input',
    'Директор, управляющий':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[3]/label/input',
    'Коммерческий директор, директор по продажам':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[4]/label/input',
    'Руководитель отдела, заместитель руководителя':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[5]/label/input',
    'Небольшой опыт, нет опыта':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[6]/label/input',
    'Другое':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[7]/label/input',
}


#КУЛЬТУРА / ОБРАЗОВАНИЕ / ГОССЛУЖБА
#Госслужба / Некоммерческие организации
xpath_gossluzba = {
    'Лицензирование, экспертиза':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[1]/label/input',
    'Социальная защита':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[2]/label/input',
    'Управление, контроль':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[3]/label/input',

    'Благотворительность':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[1]/label/input',
    'Волонтерство':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[2]/label/input',
    'Общественная деятельность':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[3]/label/input',

    'Директор':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[1]/label/input',
    'Руководитель отдела, заместитель руководителя':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[2]/label/input',
    'Небольшой опыт, нет опыта':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[3]/label/input',
    'Другое':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[4]/label/input'

}

#Культура / Искусство / Развлечения
xpath_kultura= {
    'Изобразительное искусство':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[1]/label/input',
    'Искусствоведение , реставрация, антиквариат':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[2]/label/input',
    'Мода':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[3]/label/input',
    'Фотография':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[4]/label/input',

    'Актер , артист эстрады':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[1]/label/input',
    'Кино, мультипликация':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[2]/label/input',
    'Музыка, вокальное искусство:':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[3]/label/input',
    'Театр':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[4]/label/input',
    'Хореография, балет':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[5]/label/input',

    'Библиотечное дело, архивное дело':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[1]/label/input',
    'Литература, переводы':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[2]/label/input',

    'Организация мероприятий':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[1]/label/input',
    'Технический, административный персонал':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[2]/label/input',

    'Директор, управляющий':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[3]/li/ul/li[1]/label/input',
    'Руководитель отдела, коллектива':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[3]/li/ul/li[2]/label/input',
    'Небольшой опыт, нет опыта':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[3]/li/ul/li[3]/label/input',
    'Другое':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[3]/li/ul/li[4]/label/input',
}

#Образование / Наука
xpath_obrazovanie= {
    'Воспитатель':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[1]/label/input',
    'Преподаватель вуза, учебного центра':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[2]/label/input',
    'Преподаватель иностранного языка':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[3]/label/input',
    'Репетитор':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[4]/label/input',
    'Учитель начальных классов':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[5]/label/input',
    'Учитель среднего и старшего звена':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[6]/label/input',

    'Консалтинг':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[1]/label/input',
    'Логопедия, дефектология':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[2]/label/input',
    'Психология':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[3]/label/input',
    'Тренинги':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[4]/label/input',

    'Научная деятельность, лабораторные работы':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li/label/input',

    'Методист':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li/label/input',

    'Директор':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[3]/li/ul/li[1]/label/input',
    'Руководитель отдела, направления':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[3]/li/ul/li[2]/label/input',
    'Небольшой опыт, нет опыта':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[3]/li/ul/li[3]/label/input',
    'Другое':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[3]/li/ul/li[4]/label/input'

}

#Торговля
xpath_torgovla= {
    'Администратор магазина, торгового зала':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[1]/label/input',
    'Менеджер по продажам':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[2]/label/input',
    'Мерчандайзер':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[3]/label/input',
    'Продавец / Кассир':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[4]/label/input',
    'Продавец-консультант':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[5]/label/input',
    'Продажи по телефону / Телемаркетинг':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[6]/label/input',
    'Товаровед / Учет товаров':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[7]/label/input',
    'Торговый представитель':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[8]/label/input',

    'Менеджер по закупкам':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[1]/label/input',
    'Снабжение':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[2]/label/input',

    'Продажи по каталогам / MLM':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li/label/input',

    'Продажи по телефону / Телемаркетинг':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[1]/label/input',
    'Продажи / Работа с клиентами':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[2]/label/input',
    'Работа с регионами':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[3]/label/input',
    'Торговый представитель':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[4]/label/input',

    'Директор по развитию':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[3]/li/ul/li[1]/label/input',
    'Директор / Управляющий':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[3]/li/ul/li[2]/label/input',
    'Коммерческий директор / Директор по продажам':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[3]/li/ul/li[3]/label/input',
    'Руководитель отдела / Заместитель руководителя':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[3]/li/ul/li[4]/label/input',
    'Небольшой опыт / Нет опыта':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[3]/li/ul/li[5]/label/input',
    'Другое':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[3]/li/ul/li[6]/label/input'
}

#Производство / Агропром
xpath_proizvodstvo= {
    'Инженер / Технолог / Конструктор':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[1]/label/input',
    'КИПиА / Метрология':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[2]/label/input',
    'Контроль качества':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[3]/label/input',
    'Охрана труда / Экология':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[4]/label/input',
    'Проектирование':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[5]/label/input',
    'Сертификация':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[6]/label/input',

    'Монтажник':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[1]/label/input',
    'Оператор станков / Автоматических линий':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[2]/label/input',
    'Сборщик':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[3]/label/input',
    'Сварщик':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[4]/label/input',
    'Столяр':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[5]/label/input',
    'Техник':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[6]/label/input',
    'Токарь':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[7]/label/input',
    'Фрезеровщик':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[8]/label/input',
    'Швея':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[9]/label/input',
    'Электрик':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[10]/label/input',
    'Электромонтажник':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[11]/label/input',
    'Ювелир':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[12]/label/input',

    'Продажи / Работа с клиентами':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[3]/li/ul/li[1]/label/input',
    'Снабжение / Закупки / Тендеры':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[3]/li/ul/li[2]/label/input',

    'Автомобилестроение, производство автозапчастей':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[1]/label/input',
    'Атомная и другие виды энергетики':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[2]/label/input',
    'Деревообработка, производство мебели':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[3]/label/input',
    'Добывающая промышленность':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[4]/label/input',
    'Животноводство / Мясопереработка':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[5]/label/input',
    'Легкая промышленность, производство ТНП':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[6]/label/input',
    'Металлургия, металлообработка':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[7]/label/input',
    'Нефтегазовая отрасль':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[8]/label/input',
    'Оборонное производство, авиакосмическая отрасль':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[9]/label/input',
    'Пищевое производство':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[10]/label/input',
    'Приборостроение, радиотехника, электроника':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[11]/label/input',
    'Производство пищевого и торгового оборудования':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[12]/label/input',
    'Производство стройматериалов и конструкций':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[13]/label/input',
    'Растениеводство / Сельхозпроизводство':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[14]/label/input',
    'Станкостроение, производство техники и оборудования':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[15]/label/input',
    'Судостроение, судоремонт':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[16]/label/input',
    'Фармацевтическое производство':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[17]/label/input',
    'Химия, нефтехимия':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[18]/label/input',
    'Другие виды производства':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[19]/label/input',

    'Главный инженер / Главный специалист':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[1]/label/input',
    'Директор по развитию':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[2]/label/input',
    'Директор / Управляющий':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[3]/label/input',
    'Коммерческий директор / Директор по продажам':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[4]/label/input',
    'Мастер участка / смены / Бригадир':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[5]/label/input',
    'Начальник производства / цеха / отдела':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[6]/label/input',
    'Небольшой опыт / Нет опыта':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[7]/label/input',
    'Другое':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[8]/label/input'
}


#СТРОИТЕЛЬСТВО / НЕДВИЖИМОСТЬ
#Недвижимость / Риелторские услуги
xpath_nedvizimost= {
    #Жилая недвижимость
    'Аренда':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[1]/label/input',
    'Продажа':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[2]/label/input',
    #Коммерческая недвижимость (временно поставлю 1, чтоб не дублировать ключи
    'Аренда1':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[1]/label/input',
    'Продажа1':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[2]/label/input',

    'Консалтинг / Оценка':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li/label/input',

    'Директор / Управляющий':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[1]/label/input',
    'Директор филиала':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[2]/label/input',
    'Руководитель отдела / направления':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[3]/label/input',
    'Небольшой опыт / Нет опыта':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[4]/label/input',
    'Другое':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[5]/label/input'

}

#Строительство / ЖКХ / Эксплуатация
xpath_stroitelstvo_zkh= {
    'Архитектура':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[1]/label/input',
    'Геодезия / Землеустройство':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[2]/label/input',
    'Замерщик':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[3]/label/input',
    'Инженер ПТО':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[4]/label/input',
    'Проектирование':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[5]/label/input',
    'Сметное дело':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[6]/label/input',
    'Снабжение / Закупки / Тендеры':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[7]/label/input',

    'Вентиляция / Климатическое оборудование':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[1]/label/input',
    'Водоснабжение / Водоотведение / Отопление':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[2]/label/input',
    'Газоснабжение':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[3]/label/input',
    'Инженер по сервису':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[4]/label/input',
    'Инженер по сетям':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[5]/label/input',
    'Инженер-строитель':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[6]/label/input',
    'КИПиА / Метрология':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[7]/label/input',
    'Наружные трубопроводы и коммуникации':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[8]/label/input',
    'Электроснабжение / Слаботочные системы':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[9]/label/input',
    'Энергетик / Теплотехник':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[10]/label/input',

    'Благоустройство территорий':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[3]/li/ul/li[1]/label/input',
    'Лифты':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[3]/li/ul/li[2]/label/input',
    'Машинист/водитель спецтехники':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[3]/li/ul/li[3]/label/input',
    'Эксплуатация зданий / Коммунальные службы':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[3]/li/ul/li[4]/label/input',

    'Охрана труда / Техника безопасности':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[4]/li/ul/li[1]/label/input',
    'Технадзор':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[4]/li/ul/li[2]/label/input',

    'Бетонщик / Арматурщик':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[1]/label/input',
    'Дорожный рабочий':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[2]/label/input',
    'Каменщик':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[3]/label/input',
    'Кровельщик / Жестянщик':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[4]/label/input',
    'Маляр':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[5]/label/input',
    'Машинист стройтехники':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[6]/label/input',
    'Монтажник / Сборщик':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[7]/label/input',
    'Монтажник-слаботочник':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[8]/label/input',
    'Отделочник':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[9]/label/input',
    'Плотник / Столяр':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[10]/label/input',
    'Промышленный альпинист':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[11]/label/input',
    'Сантехник / Слесарь-сантехник':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[12]/label/input',
    'Сварщик':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[13]/label/input',
    'Слесарь / Сборщик':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[14]/label/input',
    'Штукатур / Плиточник':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[15]/label/input',
    'Электрик / Электромонтер':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[16]/label/input',
    'Электромонтажник':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[17]/label/input',

    'Главный инженер / Ведущий специалист':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[1]/label/input',
    'Директор / Управляющий':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[2]/label/input',
    'Коммерческий директор / Директор по продажам':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[3]/label/input',
    'Прораб':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[4]/label/input',
    'Руководитель отдела / участка / Бригадир':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[5]/label/input',
    'Небольшой опыт / Нет опыта':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[6]/label/input',
    'Другое':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[7]/label/input'
}

#ТРАНСПОРТ / ЛОГИСТИКА
#Логистика / Склад / ВЭД
xpath_logistika = {
    'Водитель':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[1]/label/input',
    'Логистика':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[2]/label/input',
    'Экспедирование':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[3]/label/input',

    'Менеджер по ВЭД':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[1]/label/input',
    'Таможенное оформление':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[2]/label/input',

    'Закупки / Снабжение':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[3]/li/ul/li[1]/label/input',
    'Продажа логистических услуг':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[3]/li/ul/li[2]/label/input',

    'Грузчик / Комплектовщик':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[1]/label/input',
    'Кладовщик / Товаровед':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[2]/label/input',
    'Оператор':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[3]/label/input',
    'Упаковщик / Фасовщик':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[4]/label/input',

    'Административный персонал':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[1]/label/input',
    'Диспетчер':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[2]/label/input',

    'Директор / Управляющий':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[3]/li/ul/li[1]/label/input',
    'Заведующий / начальник склада':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[3]/li/ul/li[2]/label/input',
    'Руководитель отдела / Заместитель руководителя':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[3]/li/ul/li[3]/label/input',
    'Небольшой опыт / Нет опыта':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[3]/li/ul/li[4]/label/input',
    'Другое':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[3]/li/ul/li[5]/label/input'
}

#Транспорт / Автобизнес / Автосервис
xpath_transport= {
    'Автобус / маршрутное такси':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[1]/label/input',
    'Газель (малый коммерческий а/т)':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[2]/label/input',
    'На служебном грузовом а/м':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[3]/label/input',
    'На служебном легковом а/м':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[4]/label/input',
    'С личным грузовым а/м':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[5]/label/input',
    'С личным легковым а/м':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[6]/label/input',
    'Спецтехника':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[7]/label/input',
    'Такси':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[8]/label/input',
    'Троллейбус / трамвай':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[9]/label/input',
    'Экспедирование':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[10]/label/input',

    'Лизинг / прокат автотранспорта':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[1]/label/input',
    'Продажа автозапчастей и автохимии':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[2]/label/input',
    'Продажа коммерческого транспорта / спецтехники':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[3]/label/input',
    'Продажа легковых автомобилей':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[4]/label/input',
    'Продажа мототехники и запчастей':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[5]/label/input',

    'Авиация':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[3]/li/ul/li[1]/label/input',
    'Водный транспорт':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[3]/li/ul/li[2]/label/input',
    'Железнодорожный транспорт':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[3]/li/ul/li[3]/label/input',
    'Метрополитен':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[3]/li/ul/li[4]/label/input',

    'Автомойщик':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[1]/label/input',
    'Администратор':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[2]/label/input',
    'Диспетчер':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[3]/label/input',
    'Заправщик':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[4]/label/input',

    'Жестянщик':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[1]/label/input',
    'Маляр / Колорист':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[2]/label/input',
    'Слесарь / Механик':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[3]/label/input',
    'Электрик':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[4]/label/input',
    'Арматурщик':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[5]/label/input',
    'Инженер':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[6]/label/input',
    'Установщик дополнительного оборудования':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[7]/label/input',
    'Шиномонтажник':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[8]/label/input',

    'Директор / Управляющий':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[3]/li/ul/li[1]/label/input',
    'Руководитель отдела / Заместитель руководителя':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[3]/li/ul/li[2]/label/input',
    'Небольшой опыт / Нет опыта':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[3]/li/ul/li[3]/label/input',
    'Другое':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[3]/li/ul/li[4]/label/input'
}

#КРАСОТА / ЗДОРОВЬЕ
#Красота / Фитнес / Спорт
xpath_krasota= {
    'Визажист':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[1]/label/input',
    'Косметология':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[2]/label/input',
    'Маникюр / Педикюр':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[3]/label/input',
    'Массаж':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[4]/label/input',
    'Парикмахер / Стилист':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[5]/label/input',
    'Тренер / Инструктор':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[6]/label/input',

    'Продажи услуг / Работа с клиентами':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li/label/input',

    'Администратор':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[1]/label/input',
    'Директор / Управляющий':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[2]/label/input',
    'Небольшой опыт / Нет опыта':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[3]/label/input',
    'Другое':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[4]/label/input'
}

#Медицина / Фармация / Ветеринария
xpath_medicina= {
    'Аллерголог-иммунолог':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[1]/label/input',
    'Анестезиолог':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[2]/label/input',
    'Гастроэнтеролог':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[3]/label/input',
    'Гинеколог / Акушер':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[4]/label/input',
    'Кардиолог':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[5]/label/input',
    'Косметолог / Дерматовенеролог':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[6]/label/input',
    'Медицинская диагностика / УЗИ / Рентген':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[7]/label/input',
    'Невролог / Мануальный терапевт':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[8]/label/input',
    'Онколог / Маммолог':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[9]/label/input',
    'Отоларинголог':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[10]/label/input',
    'Офтальмолог':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[11]/label/input',
    'Педиатр':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[12]/label/input',
    'Психиатр / Нарколог':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[13]/label/input',
    'Стоматолог':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[14]/label/input',
    'Терапевт':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[15]/label/input',
    'Травматолог / Ортопед':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[16]/label/input',
    'Уролог':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[17]/label/input',
    'Физиотерапевт / ЛФК':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[18]/label/input',
    'Хирург':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[19]/label/input',
    'Эндокринолог':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[20]/label/input',
    'Другие специалисты':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[21]/label/input',

    'Ассистент':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[1]/label/input',
    'Лаборант':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[2]/label/input',
    'Массажист':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[3]/label/input',
    'Медсестра':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[4]/label/input',
    'Санитар':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[5]/label/input',
    'Сиделка / Няня':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[6]/label/input',
    'Фельдшер':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[7]/label/input',

    'Обслуживание медтехники и оборудования':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[1]/label/input',
    'Оптика':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[2]/label/input',
    'Продажа медицинских товаров / услуг':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[3]/label/input',
    'Фармацевт / Провизор':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[4]/label/input',

    'Клинические испытания / Лабораторные исследования':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[3]/li/ul/li[1]/label/input',
    'Консультирование / Экспертиза':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[3]/li/ul/li[2]/label/input',
    'Медицинский представитель':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[3]/li/ul/li[3]/label/input',

    'Ветеринария':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[4]/li/ul/li/label/input',

    'Регистратура / Административный персонал':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[5]/li/ul/li/label/input',

    'Главврач / Заведующий отделением':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[6]/li/ul/li[1]/label/input',
    'Директор / Управляющий':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[6]/li/ul/li[2]/label/input',
    'Руководитель отдела / Заместитель руководителя':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[6]/li/ul/li[3]/label/input',
    'Небольшой опыт / Нет опыта':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[6]/li/ul/li[4]/label/input',
    'Другое':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[6]/li/ul/li[5]/label/input'

}

#СФЕРА УСЛУГ
#Бытовые услуги / Обслуживание оборудования
xpath_bitovie_yslugy= {
    'Металлоремонт':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[1]/label/input',
    'Пошив и ремонт одежды':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[2]/label/input',
    'Ремонт часов, ювелирных изделий':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[3]/label/input',
    'Ремонт электроники, ПК, телефонов':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[4]/label/input',
    'Уборка помещений / Клининговые услуги':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[5]/label/input',
    'Фото / видеосъемка':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[6]/label/input',
    'Химчистка / Прачечная':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[7]/label/input',

    'Прием заказов / Диспетчер':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[1]/label/input',
    'Продажа услуг / Работа с клиентами':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[2]/label/input',

    'Пищевое и холодильное оборудование':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[1]/label/input',
    'Промышленное оборудование':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[2]/label/input',
    'Системы вентиляции и климатическая техника':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[3]/label/input',
    'Строительная и спецтехника':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[4]/label/input',
    'Торговое и складское оборудование':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[5]/label/input',

    'Директор / Управляющий':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[1]/label/input',
    'Руководитель отдела / службы':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[2]/label/input',
    'Небольшой опыт / Нет опыта':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[3]/label/input',
    'Другое':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[4]/label/input'
}

#Домашний персонал
xpath_home_personal= {
    'Водитель':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[1]/label/input',
    'Горничная':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[2]/label/input',
    'Домработница':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[3]/label/input',
    'Повар':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[4]/label/input',
    'Помощник по хозяйству':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[5]/label/input',
    'Разнорабочий':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[6]/label/input',
    'Садовник':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[7]/label/input',
    'Семейная пара':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[8]/label/input',
    'Управляющий':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[9]/label/input',
    'Экономка':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[10]/label/input',

    'Воспитатель / Гувернантка':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[1]/label/input',
    'Няня':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[2]/label/input',
    'Сиделка':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[3]/label/input',
    'Небольшой опыт / Нет опыта':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[4]/label/input',
    'Другое':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[5]/label/input'

}

#Рестораны / Питание
xpath_restorani= {
    'Кондитер':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[1]/label/input',
    'Пекарь':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[2]/label/input',
    'Пиццамейкер':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[3]/label/input',
    'Повар':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[4]/label/input',
    'Посудомойщик':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[5]/label/input',
    'Сушист':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[6]/label/input',

    'Бармен / Бариста':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[1]/label/input',
    'Буфетчик':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[2]/label/input',
    'Кассир':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[3]/label/input',
    'Официант':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[4]/label/input',
    'Сомелье':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[5]/label/input',
    'Хостес / Администратор зала':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[6]/label/input',
    'Кальянщик':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[7]/label/input',

    'Директор / Управляющий':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[1]/label/input',
    'Су-шеф':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[2]/label/input',
    'Шеф-повар / Заведующий производством':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[3]/label/input',
    'Небольшой опыт / Нет опыта':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[4]/label/input',
    'Другое':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[5]/label/input'
}

#Туризм / Гостиницы
xpath_turizm= {
    'Авиа / железнодорожные билеты':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[1]/label/input',
    'Бронирование гостиниц':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[2]/label/input',
    'Визовая поддержка':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[3]/label/input',
    'Продажи / Работа с клиентами':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[4]/label/input',
    'Экскурсионное обслуживание':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[5]/label/input',

    'Администратор / Портье':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[1]/label/input',
    'Обслуживающий персонал':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[2]/label/input',
    'Организация и проведение мероприятий':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[3]/label/input',
    'Продажи / Работа с клиентами':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[4]/label/input',

    'Директор / Управляющий':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[1]/label/input',
    'Руководитель отдела / направления':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[2]/label/input',
    'Небольшой опыт / Нет опыта':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[3]/label/input',
    'Другое':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[4]/label/input'

}

#Работа без специальной подготовки / Без опыта
xpath_job_no_opit= {
    'Агент':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[1]/label/input',
    'Мерчандайзинг / Выкладка товара':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[2]/label/input',
    'Продажи / Работа с клиентами':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[3]/label/input',
    'Тайный покупатель / Тайный клиент':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[4]/label/input',
    'Торговый представитель':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[1]/li/ul/li[5]/label/input',

    'Грузчик':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[1]/label/input',
    'Разнорабочий':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[2]/label/input',
    'Складские работы1':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[2]/li/ul/li[3]/label/input',

    'Гардеробщик':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[3]/li/ul/li[1]/label/input',
    'Дворник':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[3]/li/ul/li[2]/label/input',
    'Заправщик / Парковщик':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[3]/li/ul/li[3]/label/input',
    'Персонал гостиниц и ресторанов':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[3]/li/ul/li[4]/label/input',
    'Прием заказов':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[3]/li/ul/li[5]/label/input',
    'Сторож / Вахтер / Консьерж':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[3]/li/ul/li[6]/label/input',
    'Уборщик':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul[3]/li/ul/li[7]/label/input',

    'Оператор call-центра / на телефоне':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[1]/label/input',
    'Оператор ПК':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[2]/label/input',

    'Администратор':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[1]/label/input',
    'Диспетчер':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[2]/label/input',
    'Курьер':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[2]/li/ul/li[3]/label/input',

    'Промоутер / Проведение опросов':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[3]/li/ul/li[1]/label/input',
    'Расклейщик / Раздатчик':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[3]/li/ul/li[2]/label/input',

    'Домашний персонал':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[4]/li/ul/li/label/input',
    'Другое':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[5]/li/label/input'

}
#Работа для студентов / Стажировки
xpath_job_for_student= {
    'IT / Интернет / Телеком':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[1]/label/input',
    'Маркетинг / Реклама / СМИ':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[1]/label/input',
    'Продажи':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[1]/label/input',
    'Производство':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[1]/label/input',
    'Рестораны / Гостиницы / Туризм':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[1]/label/input',
    'Строительство':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[1]/label/input',
    'Финансы / Банки':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[1]/label/input',
    'Юриспруденция':'/html/body/div[6]/div[1]/div/div[1]/ul/li[1]/ul/li/ul/li[1]/label/input',

    'Call-центр':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[1]/label/input',
    'Делопроизводство':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[1]/label/input',
    'Курьер':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[3]/label/input',
    'Оператор ПК':'/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[1]/li/ul/li[1]/label/input',
    'Стажировка': '/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[3]/li/label/input',
    'Другое': '/html/body/div[6]/div[1]/div/div[1]/ul/li[2]/ul[3]/li/label/input',

}

#Соотношение рубрик и подрубрик

vibor_podrubrik = {
'IT / Интернет / Телеком': xpath_it_ithernet,
'Топ-менеджмент': xpath_top_menegment,

#'ФИНАНСЫ / СТРАХОВАНИЕ':

'Банки / Инвестиции / Ценные бумаги': xpath_banki_invest,
'Бухгалтерия / Аудит / Экономика предприятия': xparh_buhgalteria,
'Страхование':xpath_strahovanie,

#'ОФИСНЫЕ СЛУЖБЫ / БИЗНЕС-УСЛУГИ'

'HR / Кадры / Подбор персонала': xpath_hr_kadri,
'Административный персонал': xpath_adm_personal,
'Консалтинг / Тренинги':xpath_konsalting,
'Охрана / Безопасность':xpath_ohrana,
'Юриспруденция':xpath_urisprud,

#'МАРКЕТИНГ / РЕКЛАМА / СМИ'

'Дизайн / Полиграфия':xpath_design,
'Маркетинг / Реклама / PR':xpath_marketing,
'СМИ / Издательства':xpath_smi,

#'КУЛЬТУРА / ОБРАЗОВАНИЕ / ГОССЛУЖБА'

'Госслужба / Некоммерческие организации':xpath_gossluzba,
'Культура / Искусство / Развлечения':xpath_kultura,
'Образование / Наука':xpath_obrazovanie,
'Торговля':xpath_torgovla,
'Производство / Агропром':xpath_proizvodstvo,

#'СТРОИТЕЛЬСТВО / НЕДВИЖИМОСТЬ'

'Недвижимость / Риелторские услуги':xpath_nedvizimost,
'Строительство / ЖКХ / Эксплуатация':xpath_stroitelstvo_zkh,

#'ТРАНСПОРТ / ЛОГИСТИКА'

'Логистика / Склад / ВЭД':xpath_logistika,
'Транспорт / Автобизнес / Автосервис':xpath_transport,

#'КРАСОТА / ЗДОРОВЬЕ'

'Красота / Фитнес / Спорт':xpath_krasota,
'Медицина / Фармация / Ветеринария':xpath_medicina,

#'СФЕРА УСЛУГ'

'Бытовые услуги / Обслуживание оборудования':xpath_bitovie_yslugy,
'Домашний персонал':xpath_home_personal,
'Рестораны / Питание':xpath_restorani,
'Туризм / Гостиницы':xpath_turizm,
'Работа без специальной подготовки / Без опыта':xpath_job_no_opit,
'Работа для студентов / Стажировки':xpath_job_for_student

}
pod_rubriks = vibor_podrubrik.get('IT / Интернет / Телеком', 0)
