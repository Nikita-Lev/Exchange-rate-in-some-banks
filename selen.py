from selenium import webdriver
from page import fill
from time import sleep


class Selen():
    def __init__(self, url, name):
        chromedriver = 'D:\Projects\Курс доллара и евро\chromedriver_win32.\chromedriver.exe'
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        self.browser = webdriver.Chrome(executable_path=chromedriver, options=options)
        self.browser.get(url)
        self.name = name
        print(f'Получение данных банка "{name}"...')

    def find(self, s):
        return float(self.browser.find_element_by_xpath(s).text.replace(',', '.'))

    def click(self):
        sleep(2.5)
        city = self.browser.find_element_by_xpath(
            '//*[@id="main"]/div/table/tbody/tr/td/div/div/div/div/div/div[2]/div/div/div/div/div[3]/div[1]/div/div/aside/div/div[1]/div[2]/div/label[1]/div[2]')
        self.browser.execute_script("arguments[0].click();", city)
        sleep(0.5)

    def bank_sel(self, x1, x2, x3, x4):
        try:
            fill(self.name, self.find(x1), self.find(x2), self.find(x3), self.find(x4))
        finally:
            self.browser.close()
            self.browser.quit()
