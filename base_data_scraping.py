import pandas as pd
import numpy as np
import quandl, math, datetime, pickle
import matplotlib.pyplot as plt
from matplotlib import style
import bs4 as bs
import requests

style.use('ggplot')

def Get_Company_List():
    resp = requests.get('https://en.wikipedia.org/wiki/Semiconductor_industry')
    soup = bs.BeautifulSoup(resp.text)
    table = soup.find_all('table', {'class': "wikitable sortable"})[5]
    companies = []
    for item in table.findAll('tr')[1:]:
        company = item.findAll('td')[0].text
        company = company[:-1]
        if company[len(company) -1 ] == ']':
            company = company[:-3]
        companies.append(company)
    return companies

if __name__ == "__main__":
    print(Get_Company_List())
    