import bs4
import requests
import threading

NEW_URL = ''


def scraping_site():
    # type: () -> object
    re = requests.get(NEW_URL)
    if re.status_code == 200:
        soup = BeautifulSoup(re.text, 'html.parser')

        if soup is not None:
            articles = soup.find_all('div', {'class': 'product-container'})

            for article in articles:
                title = article.find('h5', {'class': 'product-name-container'})
                price = article.find('span', {'class': 'price product-price'})
                old_price = article.find('span', {'class': 'old-price product-price'})
                if title is not None and price is not None and old_price is not None:
                    texto = title.getText()
                    texto1 = price.getText()
                    texto2 = old_price.getText()

                    print (texto)
                    print (texto1)
                    print (texto2)


scraping_site()
