import requests

def call_api(api_name, start_date, end_date, dir_name):
    api_key = '4b6d674c796a756e3538686b557551'
    url_format = 'http://openAPI.seoul.go.kr:8088/{api_key}}/json/{api_name}/1/{end_index}/{date}'
    headers = {'content-type': 'application/json;charset=utf-8'}

    for date in pd.date_range(start_date, end_date).strftime("%Y%m%d"):
        # 최초 1회 Call은 해당 일자의 데이터 수를 확인한다.
        url = url_format.format(api_name=api_name, api_key=api_key, end_index=1, date=date)
        response = requests.get(url, headers=headers)
        end_index = response.json()[api_name]["list_total_count"]
        print("Max Count(%s): %s" % (date, end_index))

        # 해당 일자의 모든 데이터를 불러온다.
        # url = url_format.format(api_name=api_name, api_key=api_key, end_index=end_index, date=date)
        # response = requests.get(url, headers=headers)
        # result = pd.DataFrame(response.json()[api_name]["row"])

        # 수집된 데이터를 CSV로 저장합니다.
        # result.to_csv("./raw_data/%s/dust_%s.csv" % (dir_name, date), index=False, encoding="utf-8")

        # API 부하 관리를 위해 0.5초 정도 쉬어 줍시다 (찡긋)
        # sleep(0.5)