import sys

import urllib2
from bs4 import BeautifulSoup

class Scraping:
    def __init__(self, keyword, page=1):
        self.keyword = keyword
        self.page = page

    def get_page_source(self):
        """
        Function to get the page source
        :return: soup: Page Source
        """
        try:
            url = "http://www.shopping.com/products?KW=%s" % (self.keyword)
            page = urllib2.urlopen(url)
            soup = BeautifulSoup(page, "html.parser")
            return soup
        except:
            import traceback
            print traceback.format_exc()

    def get_total_count(self, soup):
        """
        :param soup: Source of Page
        :return: total count of objects returned
        """
        try:
            content = soup.find('span', class_='numTotalResults').string
            total = content.split(' ')[5]
            return total.strip()
        except:
            import traceback
            print traceback.format_exc()

    def get_page_source_per_page(self):
        """
        Func to get page source for a particular page
        :return: soup : Page source
        """
        try:
            url = "http://www.shopping.com/products~PG-%s?KW=%s" % (self.page, self.keyword)
            print url
            page = urllib2.urlopen(url)
            soup = BeautifulSoup(page, "html.parser")
            return soup
        except:
            import traceback
            print traceback.format_exc()

    def get_details_per_page(self, soup):
        """
        Function to get all details of products
        :param soup: source code
        :return:
        """
        try:
            form = soup.find('form',{"name":"compareprd"})
            products = form.findAll('div', {'class':'gridBox'})
            count = 1
            for product in products:
                product_name = get_product_name(product)
                product_price = get_product_price(product)
                print "%4s %140s %10s" % (count, product_name, product_price)
                count += 1
        except:
            import traceback
            print traceback.format_exc()


def get_product_price(product):
    """
    Helper function to get all the products
    :param product: product source
    :return:
    """
    try:
        product_price_tags = product.findAll('span', {'class': ['productPrice', 'productPrice ']})
        for price_tag in product_price_tags:
            if price_tag['class'][0] == "productPrice":
                price = price_tag.find('a')
                if price:
                    product_price = price.string
                else:
                    product_price = price_tag.string
            else:
                product_price = price_tag.string
        product_price = product_price.strip()
        return product_price
    except:
        import traceback
        print traceback.format_exc()


def get_product_name(product):
    """
    helper function to get the product price
    :param product:
    :return:
    """
    try:
        product_info = product.find('a', {'class': 'productName '})
        if product_info.has_attr('title'):
            product_name = product_info['title']
        else:
            title = product_info.find('span')
            if title:
                product_name = title['title']
        return product_name
    except:
        import traceback
        print traceback.format_exc()


def take_input():
    no_of_arguments = len(sys.argv)
    if no_of_arguments == 2:
        keyword = sys.argv[1]
        url = Scraping(keyword)
        source = url.get_page_source()
        print url.get_total_count(source)
    elif no_of_arguments == 3:
        keyword = sys.argv[1]
        page = sys.argv[2]
        url = Scraping(keyword, page)
        source = url.get_page_source_per_page()
        url.get_details_per_page(source)


take_input()
