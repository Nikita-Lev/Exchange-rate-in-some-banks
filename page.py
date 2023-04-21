import requests


def get_page(URL, town):
    HEADERS = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Cookie': town}
    page = requests.get(URL, headers=HEADERS)
    page.encoding = 'utf-8'
    return page


banks = []


def fill(name, USDbuy, USDsel, EURbuy, EURsel):
    banks.append(
        {
            'Название': name, 'Покупка доллара': USDbuy, 'Продажа доллара': USDsel, 'Покупка евро': EURbuy,
            'Продажа евро': EURsel
        }
    )
