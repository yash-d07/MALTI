import requests
import time
import json

indicators=[]
n=int(input("Enter number of URLs:- "))
for i in range(n):
    print("Enter URL:- ")
    item=input()
    indicators.append(item)

api_key='0f613b2015ca58c5e380d03f61da6eaec001ca65682d868c53de2a38b65e6930'

url='https://www.virustotal.com/vtapi/v2/url/report'

for site in indicators:
    params={'apikey':api_key, 'resource':site}
    response = requests.get(url, params=params)
    response_json = json.loads(response.content)
    print(response_json)
    if response_json['positives'] <=0:
        with open('vt_results.txt', 'a') as vt:
            vt.write(site) and vt.write('-\t NOT MALICIOUS\n')
            
    elif 1 >= response_json['positives'] >= 3:
        with open('vt_results.txt', 'a') as vt:
            vt.write(site) and vt.write('-\t MAYBE MALICIOUS\n')
        
    elif response_json['positives'] >= 4:
        with open('vt_results.txt', 'a') as vt:
            vt.write(site) and vt.write('-\t MALICIOUS!!!\n')
            
    else:
        print('url not found')
        
    time.sleep(15)
    
#"https://webzel.net/koko/wechat1.zip",
#   "https://bitly.com/2P6T5rM"