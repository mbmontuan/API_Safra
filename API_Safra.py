from datetime import datetime
import requests
import json
class apiSafra():
    token = ''
    tonekDara = ''

    def setToken(self):
        url = 'https://idcs-902a944ff6854c5fbe94750e48d66be5.identity.oraclecloud.com/oauth2/v1/token'
        payload = 'grant_type=client_credentials&scope=urn:opc:resource:consumer::all'
        headers = {'authorization':'Basic ZTMzYjYxMWE4MTIwNGYzMThhMTVkNTcyOGI5OTg2NjE6MzE1OTFhZDItMWNiZC00NGU5LWEwMWMtMWJiY2MwOTg1NTQ0','cache-control':'no-cache', 'postman-token':'280d6ac2-0e1c-d7ed-fc20-85de145f3d1c','content-type': 'application/x-www-form-urlencoded'}
        r = requests.post(url, data=payload, headers=headers)
        self.token = r.json()["access_token"]
        self.tokenData = datetime.timestamp(datetime.now())

    def getMorningCall(self):
        if self.token != '':
            tempo = (self.tokenData-datetime.timestamp(datetime.now()))*1000
            if tempo < 3600:
                url = 'https://af3tqle6wgdocsdirzlfrq7w5m.apigateway.sa-saopaulo-1.oci.customer-oci.com/fiap-sandbox/media/v1/youtube?fromData=2020-07-09&toData=2020-07-14&playlist=morningCalls&channel=safra'
                headers = {'authorization': 'Bearer ' + self.token}
                r = requests.get(url, headers=headers)
                return r.json()["data"][0]["links"][0]["href"]
            else: 
                self.setToken()
                return self.getMorningCall()
        else: 
            self.setToken()
            return self.getMorningCall()
    
print(apiSafra().getMorningCall())