#날씨 api데이터 정리 소스!! 지우면 안됨!!!!!!!!!!!*************

from urllib.parse import urlencode, unquote
import requests
import json
from datetime import datetime

#현재 날씨정보
#구글맵에서 위도 경도 확인한 후 https://fronteer.kr/service/kmaxy 에서 격자정보로 변환한뒤 사용해야함!!
now = datetime.today().strftime("%Y%m%d")            # 현재 날짜 가져오기
now_time = datetime.today().hour  # 현재시간 ex)14 int타입
now_min = datetime.today().minute  # 현재 분 ex)20 int타입
before_time = now_time-1  # 1시간 전 ex) 현재 14시 1시간전 13
zero = "00"
zero1 = "0"
if(before_time < 10):
    before_time1 = zero1 + str(before_time) + zero
else:
    before_time1 = str(before_time)+zero  # base_time에 넣을 데이터

if(now_time < 10):
    now_time1 = zero1 + str(now_time) + zero
else:
    now_time1 = str(now_time)+zero  # base_time에 넣을 데이터

#T1H: 기온 RN1:1시간 강수량 UUU:동서바람성분 VVV:남북바람성분
#REH: 습도 PTY: 강수형태 LGT:낙뢰 VEC: 풍향 WSD: 풍속
url = "http://apis.data.go.kr/1360000/VilageFcstInfoService/getUltraSrtNcst"
if now_min < 30:
    queryString = "?" + urlencode(  # 초단기 실황조회
        {
            "ServiceKey": unquote("ytObEXrMLIF%2FQljMeab%2BsGGHUM2%2B9xLwfxZKeaX2gQyBDuNR4h%2F2%2BbaOZIB6yuJrdFo7KYHPcBGIRq6C3s%2BRFA%3D%3D"),
            "base_date": now,
            "base_time": before_time1,
            "nx": 67,  # 대전광역시 서구 격자
            "ny": 101,
            "numOfRows": "10",
            "pageNo": 1,
            "dataType": "JSON"
        }
    )
else:
    queryString = "?" + urlencode(
        {
            "ServiceKey": unquote("ytObEXrMLIF%2FQljMeab%2BsGGHUM2%2B9xLwfxZKeaX2gQyBDuNR4h%2F2%2BbaOZIB6yuJrdFo7KYHPcBGIRq6C3s%2BRFA%3D%3D"),
            "base_date": now,
            "base_time": now_time1,
            "nx": 67,  # 대전광역시 서구 격자
            "ny": 101,
            "numOfRows": "10",
            "pageNo": 1,
            "dataType": "JSON"
        }
    )

queryURL = url + queryString
response = requests.get(queryURL)

r_dict = json.loads(response.text)
r_response = r_dict.get("response")  # 데이터 중 response찾기
r_body = r_response.get("body")  # 데이터 중 body찾기
r_items = r_body.get("items")  # 데이터 중 items찾기
r_item = r_items.get("item")  # 데이터 중 item찾기
result = {}
for item in r_item:
    if(item.get("category") == "T1H"):  # 기온
        result = item
        break
for item in r_item:
    if(item.get("category") == "RN1"):  # 1시간 강수량
        result2 = item
        break
for item in r_item:
    if(item.get("category") == "REH"):  # 습도
        result3 = item
        break
#&PTY 보고 없음(0), 비(1), 비+눈(2), 눈(3), 소나기(4) 1이면 비 2면 비+눈
for item in r_item:
    if(item.get("category") == "PTY"):  # 강수상태
        result4 = item
        break



rain = result4.get("obsrValue")  # 강수상태
now_rain = ""
if(rain == '0'):
    now_rain = "비가오지않음"
elif(rain == '1'):
    now_rain = "비"
elif(rain == '2'):
    now_rain = "비+눈"
elif(rain == '3'):
    now_rain = "눈"
elif(rain == '4'):
    now_rain = "소나기"

current_temp = result.get("obsrValue")  # 온도
precipitation = result2.get("obsrValue")  # 강수량
current_humi = result3.get("obsrValue")  # 습도
#now_rain #강수상태

url2 = "http://apis.data.go.kr/1360000/VilageFcstInfoService/getVilageFcst"  # 동네예보조회 URL!!!
queryString2 = "?" + urlencode(  # 동네예보조회
    {
        "ServiceKey": unquote("ytObEXrMLIF%2FQljMeab%2BsGGHUM2%2B9xLwfxZKeaX2gQyBDuNR4h%2F2%2BbaOZIB6yuJrdFo7KYHPcBGIRq6C3s%2BRFA%3D%3D"),
        "base_date": now,
        "base_time": "0500",  # 시간바꾸면 안됩니다!!!!
        "nx": 67,  # 대전광역시 서구 격자
        "ny": 101,
        "numOfRows": "10",
        "pageNo": 1,
        "dataType": "JSON"
    }
)
queryURL2 = url2 + queryString2
response2 = requests.get(queryURL2)
###########동네예보
r_dict2 = json.loads(response2.text)
r_response2 = r_dict2.get("response")
r_body2 = r_response2.get("body")
r_items2 = r_body2.get("items")
r_item2 = r_items2.get("item")
result_ = {}

for item in r_item2:
    if(item.get("category") == "SKY"):  # 하늘상태
        result_ = item
        break
for item in r_item2:
    if(item.get("category") =="POP"): #강수확률
        result_2 = item
        break

rain_pop= result_2.get("fcstValue")   
#print(rain_pop)
sky_result = result_.get("fcstValue")  # fcstValue값으로 확인!!
weather = ""
if (sky_result == '1'):
    weather = "맑음"
    #print("맑음")
elif (sky_result == '3'):
    weather = "구름많음"
    #print("구름많음")
elif (sky_result == '4'):
    weather = "흐림"
    #print("흐림")

#current_temp 온도, precipitation강수량 current_humi 습도 now_rain 강수상태 weather 날씨(구름상태) rain_pop 강수확률
#now_time1[:-2] 현재시간
print_wether = now_time1[:-2] + "시 " + "기온 : " + current_temp + "°C " +\
    "습도 : " + current_humi + "%" + "강수량 : " + precipitation + "mm" +\
    "강수상태 : " + now_rain +" "+"날씨 : "+ weather + "강수확률" + rain_pop + "%"

#print(print_wether)
#database에 입력할 값
db_current_temp=float(current_temp) #온도 
db_current_humi=float(current_humi) # 습도
db_precipitation =float(precipitation) #강수량
db_rainpop=float(rain_pop) #강수상태
# now_rain,weather은 str으로 그냥 넣어야함.
now_time_data =now+now_time1

#print(type(db_precipitation))
#print(type(current_temp),type(current_humi),type(precipitation),type(now_rain),type(weather))# 모두 str  

# aaa=[123,456]
# bbb=[123,456]
# #print(len(aaa))

# for i in range(len(aaa)):
#     if (aaa[i]==bbb[i]):
#         print("같음!!")

# import datetime 
# import threading 
# def aaa():
#     a=1
#     print("함수")

# def bbb():
#     print("aaa")
#     aaa()
#     threading.Timer(60, bbb).start()

# bbb()        