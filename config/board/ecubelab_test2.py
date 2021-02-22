#Ecubelab api키 테스트코드
import requests
from bs4 import BeautifulSoup
import json
url = 'https://api.cleancitynetworks.com/v2/products/details/'
headers = {'authorization': 'c81f8c5650b220f9e12490a8fc4bfbdb'}

resp = requests.get(url, headers=headers)
data= resp.text
#print(data)
r_dict = json.loads(data)
r_response = r_dict.get("products")

result = {} #products
result2 = {}
result3 = {}
result4 = {}

#print(r_response)
# 시리얼 기준으로 데이터 가져오기
# 데이터 보내는 간격 알아야함!!
# FB1000001911AF00
# FB1000001911AF04
# FB1000001909AG91
# FB1000001909AE65

for item in r_response:
    if(item.get('serial') == 'FB1000001911AF00'): 
        result = item
        break

#print(result)
#print(type(result.get('address')))
address = result.get('address') #주소
latitude = result.get('latitude') #위도
longitude = result.get('longitude') #경도

###테스트!!
#print(result)
#print("주소 : " + result.get('address')) #str
#print("위도 : " + str(latitude) + "도") #float
#print("경도 : " + str(longitude) + "도") #float

#status 
# current_fill_level': 0, 'battery_health': 100, 'temperature': 12

status_data=result.get('status')
current_fill_level=status_data.get('current_fill_level') #int 현재 수위(%) #int
battery_health =status_data.get('battery_health') #배터리 상태(%) #int
equ_temp=status_data.get('temperature') #온도 #int
#
#print(type(battery_health))
#print(battery_health)
##dates 
#last_gps_detected_date': '2020-01-29T06:15:21', 'last_booted_date': '2020-05-28T05:02:10', 'registered_date': '2019-07-09T09:30:08', 'last_report_date': '2021-02-16T22:07:11', 'last_collection_date': '2020-09-07T00:46:07'

dates_data=result.get('dates')
last_gps_detected_date= dates_data.get('last_gps_detected_date') #마지막 GPS 탐지 날짜(UTC+0) #str
last_booted_date=dates_data.get('last_booted_date') #마지막 부팅 날짜(UTC+0) #str
registered_date=dates_data.get('registered_date') #등록일자(UTC+0) #str
last_report_date=dates_data.get('last_report_date') #마지막 데이터 전송 날짜(UTC+0) #str
last_collection_date=dates_data.get('last_collection_date') #마지막 수집 날짜(UTC+0) #str
#print(dates_data)

#테스트!!
#print(type(last_collection_date))
#print("fill_level")
#print(registered_date)
#print("last_gps_detected_date")
#print(last_gps_detected_date)

print_ecube_test = "주소 : "+ address +" 위도 : "+str(latitude) +" 경도 : "+ str(longitude) +"수위 : " +str(current_fill_level) +"배터리상태 : " +str(battery_health)\
+ "온도 :" +str(equ_temp)

serial='FB1000001909AG91'    #시리얼값
#print(print_ecube_test)

#def FB1000001911AF04():
for item in r_response:
    if(item.get('serial') == 'FB1000001911AF04'): 
        result2 = item
        break
#print(result2)
address2 = result2.get('address') #주소
latitude2 = result2.get('latitude') #위도
longitude2 = result2.get('longitude') #경도
#status 
# current_fill_level': 0, 'battery_health': 100, 'temperature': 12

status_data2=result2.get('status')
current_fill_level2=status_data2.get('current_fill_level') #int 현재 수위(%) #int
battery_health2 =status_data2.get('battery_health') #배터리 상태(%) #int
equ_temp2=status_data2.get('temperature') #온도 #int

##dates 
#last_gps_detected_date': '2020-01-29T06:15:21', 'last_booted_date': '2020-05-28T05:02:10', 'registered_date': '2019-07-09T09:30:08', 'last_report_date': '2021-02-16T22:07:11', 'last_collection_date': '2020-09-07T00:46:07'

dates_data2=result2.get('dates')
last_gps_detected_date2= dates_data2.get('last_gps_detected_date') #마지막 GPS 탐지 날짜(UTC+0) #str
last_booted_date2=dates_data2.get('last_booted_date') #마지막 부팅 날짜(UTC+0) #str
registered_date2=dates_data2.get('registered_date') #등록일자(UTC+0) #str
last_report_date2=dates_data2.get('last_report_date') #마지막 데이터 전송 날짜(UTC+0) #str
last_collection_date2=dates_data2.get('last_collection_date') #마지막 수집 날짜(UTC+0) #str
'''
print_ecube_test2 = "주소 : "+ address2 +" 위도 : "+str(latitude2) +" 경도 : "+ str(longitude2) +"수위 : " +str(current_fill_level2) +"배터리상태 : " +str(battery_health2)\
+ "온도 :" +str(equ_temp2) +"gps탐지날짜 " + last_gps_detected_date2 +"마지막 부팅날짜 " + last_booted_date2 + "등록일자 : " + registered_date2 + "마지막 데이터 전송 날짜 "\
    + last_report_date2 + "마지막 수집 날짜: " + last_collection_date2
'''
serial2='FB1000001911AF04'    #시리얼값
#print(print_ecube_test2)

for item in r_response:
    if(item.get('serial') == 'FB1000001909AG91'): 
        result3 = item
        break

address3 = result3.get('address') #주소
latitude3 = result3.get('latitude') #위도
longitude3 = result3.get('longitude') #경도
#status 
# current_fill_level': 0, 'battery_health': 100, 'temperature': 12

status_data3=result3.get('status')
current_fill_level3=status_data3.get('current_fill_level') #int 현재 수위(%) #int
battery_health3 =status_data3.get('battery_health') #배터리 상태(%) #int
equ_temp3=status_data3.get('temperature') #온도 #int

##dates 
#last_gps_detected_date': '2020-01-29T06:15:21', 'last_booted_date': '2020-05-28T05:02:10', 'registered_date': '2019-07-09T09:30:08', 'last_report_date': '2021-02-16T22:07:11', 'last_collection_date': '2020-09-07T00:46:07'

dates_data3=result3.get('dates')
last_gps_detected_date3= dates_data3.get('last_gps_detected_date') #마지막 GPS 탐지 날짜(UTC+0) #str
last_booted_date3=dates_data3.get('last_booted_date') #마지막 부팅 날짜(UTC+0) #str
registered_date3=dates_data3.get('registered_date') #등록일자(UTC+0) #str
last_report_date3=dates_data3.get('last_report_date') #마지막 데이터 전송 날짜(UTC+0) #str
last_collection_date3=dates_data3.get('last_collection_date') #마지막 수집 날짜(UTC+0) #str

print_ecube_test3 = "주소 : "+ address3 +" 위도 : "+str(latitude3) +" 경도 : "+ str(longitude3) +"수위 : " +str(current_fill_level3) +"배터리상태 : " +str(battery_health3)\
+ "온도 :" +str(equ_temp3)

serial3='FB1000001909AG91'    #시리얼값
print(print_ecube_test3)

for item in r_response:
    if(item.get('serial') == 'FB1000001909AE65'): 
        result4 = item
        break

address4 = result4.get('address') #주소
latitude4 = result4.get('latitude') #위도
longitude4 = result4.get('longitude') #경도
#status 
# current_fill_level': 0, 'battery_health': 100, 'temperature': 12

status_data4=result4.get('status')
current_fill_level4=status_data4.get('current_fill_level') #int 현재 수위(%) #int
battery_health4 =status_data4.get('battery_health') #배터리 상태(%) #int
equ_temp4=status_data4.get('temperature') #온도 #int

##dates 
#last_gps_detected_date': '2020-01-29T06:15:21', 'last_booted_date': '2020-05-28T05:02:10', 'registered_date': '2019-07-09T09:30:08', 'last_report_date': '2021-02-16T22:07:11', 'last_collection_date': '2020-09-07T00:46:07'

dates_data4=result4.get('dates')
last_gps_detected_date4= dates_data4.get('last_gps_detected_date') #마지막 GPS 탐지 날짜(UTC+0) #str
last_booted_date4=dates_data4.get('last_booted_date') #마지막 부팅 날짜(UTC+0) #str
registered_date4=dates_data4.get('registered_date') #등록일자(UTC+0) #str
last_report_date4=dates_data4.get('last_report_date') #마지막 데이터 전송 날짜(UTC+0) #str
last_collection_date4=dates_data4.get('last_collection_date') #마지막 수집 날짜(UTC+0) #str

print_ecube_test4 = "주소 : "+ address4 +" 위도 : "+str(latitude4) +" 경도 : "+ str(longitude4) +"수위 : " +str(current_fill_level4) +"배터리상태 : " +str(battery_health4)\
+ "온도 :" +str(equ_temp4)

serial3='FB1000001909AE65'    #시리얼값
print(print_ecube_test4)



#FB1000001911AF04()  
#FB1000001909AG91()
#FB1000001909AE65()