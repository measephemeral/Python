import bs4
import requests

html = requests.get('https://finance.naver.com/marketindex/exchangeDetail.nhn?marketindexCd=FX_USDKRW')

soup = bs4.BeautifulSoup(html.text,'html.parser')
dollar = soup.select_one('#content > div.spot > div.today > p.no_today')

print(dollar.text)