import pprint
import requests
from decouple import config

# 1. 토큰 및 기본 url 설정
token = config('TELEGRAM_TOKEN') # .env 설정값 가져오기
base_url = f'https://api.telegram.org/bot{token}/'

# 2. getUpdates 정보 가져오기
response = requests.get(base_url+'getUpdates').json()
# print(response)
pprint.pprint(response)
# 3. 나의 chat_id 가져오기
chat_id = response.get('result')[0].get('message').get('from').get('id')

# 4. chat_id에 메시지
# 4-1. 요청 보낼 URL 만들기
text = 'ㅂㅈㄷㄱㅁㄴㅇㄹㅋㅌㅊㅍ'
api_url = f'{base_url}sendMessage?chat_id={chat_id}&text={text}'

# 4-2. 
requests.get(api_url)