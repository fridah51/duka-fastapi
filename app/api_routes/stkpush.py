import base64
from datetime import datetime
from fastapi import APIRouter,Depends, HTTPException
from typing import List,Dict,Generator
import requests
from requests.auth import HTTPBasicAuth
import json

from  ..schemas import StkResponse,StkRequestBody



stkpush_router = APIRouter()


now = datetime.now()
timestamp = now.strftime("%Y%m%d%H%M%S")
shortcode = "174379"
passkey ="bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
password = shortcode + passkey + timestamp 
encode_password = base64.b64encode(password.encode())
decoded_password = encode_password.decode('utf-8')
initiatorPass = "Safaricom999!*!"
print(decoded_password, timestamp)



def getAccessToken():
    Consumer_Key = "vAtF2qnWAXFIMR15yFoI4VaTkG3hjCLG"
    Consumer_Secret = "NYiGPialXh3u656l"
    url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    r = requests.get(url, auth=HTTPBasicAuth(Consumer_Key, Consumer_Secret))
    print(r.json())
    return r.json()['access_token']



@stkpush_router.post("", 
summary="make an stkpush",
status_code=201
)
async def post_stk( payloads:StkRequestBody):
    token = getAccessToken()

    headers = {
    'Authorization': "Bearer %s" % token
    }
    payload = {
        "BusinessShortCode": 174379,
        "Password": decoded_password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": payloads.amount,
        "PartyA": payloads.mobile,
        "PartyB": 174379,
        "PhoneNumber": payloads.mobile,
        "CallBackURL": "https://mydomain.com/path",
        "AccountReference": "CompanyXLTD",
        "TransactionDesc": "Payment of X" 
    }

    if not payload:
        raise HTTPException(status_code=401, detail=f"{payload} :request body not correct ")

    pj = json.dumps(payload)
    response = requests.post("https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest", headers = headers, data = pj)
    print(response.json())
    r = response.json()
    
    return r