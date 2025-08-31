from django.shortcuts import render, redirect
from django.contrib import messages
import requests, re, json

# Create your views here.

def email_validation(request):
    api_key='XZI6PGI561YGVCODJIWO'
    pn = request.POST.get('email')
    url = requests.get('https://api.mailboxvalidator.com/v1/validation/single?key='+str(api_key)+'&format=json&email='+str(pn))
    resp=url.json()
    messages.info(request, 'Email_Address: '+resp['email_address']
    +'\n\nDomain: '+resp['domain']
    +'\n\nGreylisted (True/False): '+resp['is_greylisted']
    +'\n\nVerified (True/False): '+resp['is_verified'])
    return render(request, 'email_validation.html')

def phone_validation(request):
    api_key='f168a85a371ac82a558a7142d806db6a'
    pn = request.POST.get('phone_number')
    if (len(str(pn)) == 10):
        url = requests.get('http://apilayer.net/api/validate?access_key='+str(api_key)+'&number='+str(pn)+'&country_code=IN')
        resp = url.json()
        messages.info(request, json.dumps(resp, sort_keys=True, indent=4))
    else:
        messages.info(request, 'Please provide a valid 10-digit mobile number...')
    return render(request, 'phone_validation.html')
   
def ip_validation(request):
    api_key='4524747c5d92ad84d2caea256e0791b3'
    ip= request.POST.get('IP')
    url = requests.get('http://api.ipstack.com/'+str(ip)+'?access_key='+api_key+'&fields=longitude,latitude,zip,city,region_name,region_code,country_name,country_code,type,ip').json()
    messages.info(request, json.dumps(url, sort_keys=True, indent=4))
    return render(request, 'ip_validation.html')

def file_validation(request):
    hash = request.POST.get('hash')
    url = 'https://www.virustotal.com/api/v3/search?query='+str(hash)
    resp = requests.get(url, headers={"x-apikey":"0f613b2015ca58c5e380d03f61da6eaec001ca65682d868c53de2a38b65e6930"}).json()  
    messages.info(request, 'File_Type: '+list(resp.items())[0][1][0]['attributes']['type_description']
                +'\n\nExtension: '+list(resp.items())[0][1][0]['attributes']['type_extension']
                +'\n\nAnalysis Stats: '+str(list(resp.items())[0][1][0]['attributes']['last_analysis_stats'])
                +'\n\nMD5: '+list(resp.items())[0][1][0]['attributes']['md5']
                +'\n\nSHA1: '+list(resp.items())[0][1][0]['attributes']['sha1']
                +'\n\nSHA256: '+list(resp.items())[0][1][0]['attributes']['sha256']
                +'\n\nSSDEEP: '+list(resp.items())[0][1][0]['attributes']['ssdeep'])
    return render(request, 'file_validation.html')

def url_validation(request):
    site = request.POST.get('URL')
    url = 'https://www.virustotal.com/api/v3/search?query='+str(site)
    resp = requests.get(url, headers={"x-apikey":"0f613b2015ca58c5e380d03f61da6eaec001ca65682d868c53de2a38b65e6930"}).json()
    messages.info(request, 'URL: '+str(list(resp.items())[0][1][0]['attributes']['last_final_url'])
                +'\n\nAnalysis Stats: '+str(list(resp.items())[0][1][0]['attributes']['last_analysis_stats'])
                )
    return render(request, 'url_validation.html')

def file_behavioral(request):
    hash = request.POST.get('hash')
    url = 'https://www.virustotal.com/api/v3/files/'+str(hash)+'/behaviour_summary'
    resp = requests.get(url, headers={"x-apikey":"0f613b2015ca58c5e380d03f61da6eaec001ca65682d868c53de2a38b65e6930"}).json()
    messages.info(request, resp)
    return render(request, 'file_behavioral.html')


def index(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request, 'about_us.html')

def login(request):
    return render(request, 'login.html')

def service(request):
    return render(request, 'service.html')

def modules(request):
    return render(request, 'modules.html')

def contact_us(request):
    return render(request, 'contact_us.html')