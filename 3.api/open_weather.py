import requests

import dotenv
import os
dotenv.load_dotenv()  # .env 환경변수 파일을 로드함 

# 발급받은 REST API 키 입력
OPEN_WEATHER_MAP_KEY = os.getenv("OPEN_WEATHER_MAP_KEY")

url = "https://api.openweathermap.org/data/2.5/weather"
params= {
    'q': 'Seoul',
    'appid': OPEN_WEATHER_MAP_KEY,
    'units': 'metric'
}

response = requests.get(url, params=params)

if response.status_code == 200:
    import json
    data = response.json()
    print(json.dumps(data, indent=3, ensure_ascii=False))
else:
    print("Error:", response.status_code)        