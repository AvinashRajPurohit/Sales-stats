import urllib.request
import pandas as pd
from html_table_parser.parser import HTMLTableParser

DATA_LINK = 'http://www.citymayors.com/features/euro_cities1.html'


def url_get_contents(url: str):
    """
    This function will Opens a website and read
    its binary contents (HTTP Response Body) and
    making request to the website

    url = country contant that we want to extract...
    """
    req = urllib.request.Request(url=url)
    f = urllib.request.urlopen(req)
    return f.read()


def save_country_data_in_csv():
    """
    This function will save the country data in csv format
    """
    xhtml = url_get_contents(DATA_LINK).decode('utf-8')
    parser = HTMLTableParser()
    parser.feed(xhtml)
    table_header = ["Rank"]
    table_header += parser.tables[0][0][3:]
    table = parser.tables[0][0:]
    table = table[1:]
    dataframe = pd.DataFrame(table, columns=table_header)
    dataframe.to_csv("100_country.csv", index=False)
    print('data is stored in csv file')


save_country_data_in_csv()
