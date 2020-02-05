from splinter import Browser
import pandas as pd

browser = Browser('chrome')
# browser.driver.set_window_size(640, 480)
browser.visit('https://nn.rabota.ru/v3_myVacancy.html?action=create&company_registered=true&employer_registered=true')
# Логинимся
login_bar_xpath = '//*[@id="mail"]'
login_bar = browser.find_by_xpath(login_bar_xpath)[0]
login_bar.fill('shweper@ya.ru')

pass_bar_xpath = '//*[@id="password"]'
pass_bar = browser.find_by_xpath(pass_bar_xpath)[0]
pass_bar.fill('Fqtawe98')
# кликкаем войти
browser.find_by_xpath('//*[@id="authForm"]/input[5]').click()

a = 100
vak_bar_xpath = '//*[@id="custom_position"]'
vak_bar = browser.find_by_xpath(vak_bar_xpath)[0]
vak_bar.fill(a)




# browser.quit()