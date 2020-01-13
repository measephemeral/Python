import requests
import pandas as pd
from _datetime import date

def call_api(api_name, start_date, end_date, dir_name):
    api_key = '4b6d674c796a756e3538686b557551'
    url_format = 'http://openAPI.seoul.go.kr:8088/{api_key}}/json/DailyAverageAirQuality/1/{end_index}/{date}'
    headers = {'content-type': 'application/json;charset=utf-8'}

    for date in pd.date_range(start_date, end_date).strftime("%Y%m%d"):
        url = url_format.format(api_key=api_key, end_index=1, date=date)
        response = requests.get(url, headers=headers)
        end_index = response.json()['DailyAverageAirQuality']["list_total_count"]
        
    print("Max Count(%s): %s" % (date, end_index))