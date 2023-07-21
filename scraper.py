import requests
from bs4 import BeautifulSoup


class Scraper:
    '''Scraper abstract class for extension in future...'''

    def __init__(self, url):
        self.url = url
        self.parse()

    def parse(self):
        response = requests.get(self.url)
        self.soup = BeautifulSoup(response.text, 'lxml')

    @staticmethod
    def extract_text_from_element(ele, tag, attrs):
        try:
            return ele.find(tag, attrs).text.replace('\xa0', '')
        except Exception as e:
            print(e)
            return 'N/A'

    def get_details(self):
        raise NotImplementedError
