from page import *
from selen import Selen
from Суп import Req
import csv
import os
import datetime

now = datetime.datetime.now()
CSV = 'Currency.csv'

Selen('https://alfabank.ru/currency/', 'Альфа банк').bank_sel(
    '//*[@id="page-inner"]/div[3]/div[2]/div[2]/div/div/div[2]/div[5]/table/tbody/tr[3]/td[2]',
    '//*[@id="page-inner"]/div[3]/div[2]/div[2]/div/div/div[2]/div[5]/table/tbody/tr[3]/td[5]',
    '//*[@id="page-inner"]/div[3]/div[2]/div[2]/div/div/div[2]/div[5]/table/tbody/tr[4]/td[2]',
    '//*[@id="page-inner"]/div[3]/div[2]/div[2]/div/div/div[2]/div[5]/table/tbody/tr[4]/td[5]')
sber = Selen('https://www.sberbank.ru/ru/quotes/currencies', 'Сбербанк')
sber.click()
sber.bank_sel(
    '//*[@id="main"]/div/table/tbody/tr/td/div/div/div/div/div/div[2]/div/div/div/div/div[3]/div[1]/div/div/div[1]/div/div[1]/table/tbody/tr[3]/td[3]/span/span[1]',
    '//*[@id="main"]/div/table/tbody/tr/td/div/div/div/div/div/div[2]/div/div/div/div/div[3]/div[1]/div/div/div[1]/div/div[1]/table/tbody/tr[3]/td[2]/span/span[1]',
    '//*[@id="main"]/div/table/tbody/tr/td/div/div/div/div/div/div[2]/div/div/div/div/div[3]/div[1]/div/div/div[1]/div/div[1]/table/tbody/tr[2]/td[3]/span/span[1]',
    '//*[@id="main"]/div/table/tbody/tr/td/div/div/div/div/div/div[2]/div/div/div/div/div[3]/div[1]/div/div/div[1]/div/div[1]/table/tbody/tr[2]/td[2]/span/span[1]')
Selen('https://www.vtb.ru/', 'ВТБ').bank_sel(
    '/html/body/footer/div[2]/div[2]/noindex/section/div[1]/div[2]/div[2]',
    '/html/body/footer/div[2]/div[2]/noindex/section/div[1]/div[2]/div[3]',
    '/html/body/footer/div[2]/div[2]/noindex/section/div[1]/div[3]/div[2]',
    '/html/body/footer/div[2]/div[2]/noindex/section/div[1]/div[3]/div[3]')
Selen('https://www.gazprombank.ru/', 'Газпромбанк').bank_sel(
    '//*[@id="__next"]/div[1]/div[1]/div[2]/div[2]/div[6]/div/div[1]/div/div[1]/div[2]/div[3]',
    '//*[@id="__next"]/div[1]/div[1]/div[2]/div[2]/div[6]/div/div[1]/div/div[1]/div[2]/div[2]',
    '//*[@id="__next"]/div[1]/div[1]/div[2]/div[2]/div[6]/div/div[1]/div/div[1]/div[3]/div[3]',
    '//*[@id="__next"]/div[1]/div[1]/div[2]/div[2]/div[6]/div/div[1]/div/div[1]/div[3]/div[2]')

Req('АТБ', 'https://www.atb.su/', 'BITRIX_SM_CITY=58').bank_soup('div', 'currency_block-table-td', 6, 7, 11, 12)
Req('Открытие', 'https://www.open.ru/', 'tmr_reqNum=46').bank_soup('td', 'main-page-exchange__td', 4, 6, 8, 10)
with open(CSV, 'a', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Дата', 'Банк', 'USD продажа ', 'USD покупка', 'EUR продажа', 'EUR покупка'])
    T = datetime.datetime.today().strftime("%Y.%m.%d—%H:%M")
    for bank in banks:
        writer.writerow([T, bank['Название'], bank['Покупка доллара'], bank['Продажа доллара'], bank['Покупка евро'],
                         bank['Продажа евро']])
        T = ''
    writer.writerow([' '])
print('Успешно!')


def key(p, string):
    return p.find_element_by_class_name(string)
