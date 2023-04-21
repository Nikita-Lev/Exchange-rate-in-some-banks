from bs4 import BeautifulSoup
from page import *


class Req():

    def __init__(self, url):
        self.url = url
        self.html = get_page(url)

    def soup(self, type_of_class, name_of_class, a1, a2, a3, a4):
        if self.html.status_code == 200:
            soup = BeautifulSoup(self.html.text, 'html.parser')
            items = soup.find_all(type_of_class, class_=name_of_class)
            fill(self.name, Req.rep(items[a1]), Req.rep(items[a2]), Req.rep(items[a3]), Req.rep(items[a4]))
        else:
            print('Ошибка!')