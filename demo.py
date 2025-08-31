import json, requests
site = 'google.com'
url = 'https://www.virustotal.com/api/v3/search?query='+str(site)
resp = requests.get(url, headers={"x-apikey":"0f613b2015ca58c5e380d03f61da6eaec001ca65682d868c53de2a38b65e6930"}).json()

print(list(resp.items())[0][1][0]['id'])