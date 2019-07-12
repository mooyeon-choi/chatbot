import pprint
import requests
from decouple import config

file_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQpr5I2O-mRoRgmdioLyW5dKEJ25HJetvy69UMTCKJlmLQXZXPS'
response = requests.get(file_url, stream=True)
image = response.raw.read()
# 1. 네이버 API 설정
naver_client_id = config('NAVER_CLIENT_ID')
naver_client_secret = config('NAVER_CLIENT_SECRET')
# 2. URL 설정
naver_url = 'https://openapi.naver.com/v1/vision/celebrity'
# 3. 요청보내기! POST
headers = {
    'X-Naver-Client-Id' : naver_client_id,
    'X-Naver-Client-Secret' :naver_client_secret
    }
response = requests.post(naver_url, 
                        headers=headers, 
                        files={'image': image}).json()
best = response.get('faces')[0].get('celebrity')
text = f"{best.get('confidence')*100}만큼 {best.get('value')}를 닮으셨네요~"
print(text)