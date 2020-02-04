from splinter import Browser
import pandas as pd

browser = Browser('chrome')
# browser.driver.set_window_size(640, 480)
browser.visit('https://yandex.ru')
search_bar_xpath = '//*[@id="text"]'
search_bar = browser.find_by_xpath(search_bar_xpath)[0]
search_bar.fill('splinter - python acceptance testing for web applications')

search_button_xpath = '/html/body/div[1]/div[2]/div[3]/div/div[2]/div/fwap/dhtaq/aqwf/div/div[2]/div/div[2]/div/form'
search_button = browser.find_by_xpath(search_button_xpath)[0]
search_button.click()





browser.quit()