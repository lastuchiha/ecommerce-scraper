from scraper import Scraper


class Flipkart(Scraper):
    def get_details(self, additional=False):
        product_details = self.soup.find('div', {'class': 'aMaAEs'})

        self.title = self.extract_text_from_element(
            product_details, 'h1', {'class': 'yhB1nd'})

        self.price = self.extract_text_from_element(
            product_details, 'div', {'class': '_30jeq3 _16Jk6d'}
        )

        self.mrp = self.extract_text_from_element(
            product_details, 'div', {'class': '_3I9_wc _2p6lqe'}
        )

        result = {
            'id': self.url.split('?')[0].split('/')[-1],
            'title': self.title,
            "price": self.price,
            "mrp": self.mrp
        }

        if additional:
            self.rating = self.extract_text_from_element(
                self.soup, 'div', {'class': '_2d4LTz'}
            )

            result['rating'] = self.rating

        return result
