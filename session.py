#session.py

import requests


header ={    
  "Content-Type": "application/json",
    "X-Android-Package": "com.coinday.app",
    "X-Android-Cert": "D224B0C3D056BEFF68A6007B5965FF8F926CD780",
    "Accept-Language": "en-GB, en-US",
    "X-Client-Version": "Android/Fallback/X20000003/FirebaseCore-Android",
    "Content-Length": "486",
    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 13; RMX3461 Build/TP1A.220905.001)",
    "Host": "securetoken.googleapis.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip"
}

data = {"grantType":"refresh_token","refreshToken":""}

url = "https://securetoken.googleapis.com/v1/token?key=AIzaSyAor2pDtvb7UN0WYRR9wotPoZ0i2vxd_Z8"

urlLogin = "https://api.thecoinday.app/api/v1/auth/login"

loginHeader = { "Host": "api.thecoinday.app",
    "cookie": "",
    "content-type": "application/json; charset\u003dutf-8",
    "content-length": "1137",
    "accept-encoding": "gzip",
    "user-agent": "okhttp/4.8.0"
}

loginData = {"idToken":""}

sessionDataMeta = "session\u003d"


def findSessionId(idtoken):
  data["refreshToken"]=idtoken
  r = requests.post(url,headers=header,json=data).json()
  return r['access_token'],r['id_token']
	
	
def login(idtoken):
	sessionId = findSessionId(idtoken)
	
	loginHeader['cookie'] = sessionDataMeta+sessionId[0]
	
	loginData['idToken'] = sessionId[1]
	resLogin = requests.post(urlLogin,headers=loginHeader,json=loginData)
#	print(resLogin.json())
	return resLogin.json()['session']
