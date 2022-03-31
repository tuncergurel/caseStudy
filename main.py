from bs4 import BeautifulSoup
import requests
from datetime import date
import pandas as pd
import openpyxl

class CreateUrl():
    def __init__(self):
        pass

    def getUrlsFromExcel(filename, sheet):
        filename = filename
        sheet = sheet
        datas = pd.read_excel(io=filename, sheet_name=sheet,header=None)

        urls = []

        for i in datas:
            urls.append(datas[i])

        print("urls extensions received")
        return(urls[0])

    def makeUrl(url):
        urls = []
        for i in url:
            urls.append("https://www.markastok.com" + str(i))

        print("urls prepared")
        return urls


    def writeToExcel(urls_list):
        excel = openpyxl.load_workbook("example.xlsx")
        sheet = excel['URL']

        for i in range(len(urls_list)):
            sheet['B' + str(i+1)].value = urls_list[i]

        excel.save('example.xlsx')
        print("urls added excel")


    def getInfos(address):
        # print(address[:1])
        url = address[:100]

        vals = []
        for urls in url:
            page = requests.get(urls)
            soup = BeautifulSoup(page.content,'html.parser')

            product_name = soup.title.text if soup.title is not None else ""         #Name
            product_price =  soup.find('span', attrs={'class': 'discountPrice'}).text if soup.find('span', attrs={'class': 'discountPrice'}) is not None else "-"  # Price

            productStock = ""
            for i in soup.find_all('a', attrs={'class': 'col box-border'}):  # In stock
                productStock += str(i.find("p").text) + ","



            productNoneStock = ""
            for i in soup.find_all('a', attrs={'class': 'col box-border passive'}): # out of stock
                productNoneStock += str(i.find("p").text) + ","

            p_code = soup.find('div', attrs={'class': 'fl col-12 product-feature'}).text if soup.find('div', attrs={'class': 'fl col-12 product-feature'}) is not None else "-"   # code
            product_code = p_code[-16:] #  assumed 16 characters


            val = [urls, product_name, product_price, productStock, productNoneStock, product_code]
            vals.append(val)
        # print(vals)
        return(vals)


def main():
    urls = CreateUrl.getUrlsFromExcel(filename="URL's.xlsx",sheet='URL')

    urls_list = CreateUrl.makeUrl(urls)

    # CreateUrl.writeToExcel(urls_list)

    return CreateUrl.getInfos(urls_list)

if __name__ == '__main__':
    main()