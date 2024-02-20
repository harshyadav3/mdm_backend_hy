import json
from config import ENTERPRISE_NAME,POLICY_NAME,QR_CODE_URL
from AndroidManagementObject import SharedObject
from urllib.parse import urlencode


def GenerateQRCode() : 


   try :

      shared_obj = SharedObject.shared_instance
      enrollment_token = shared_obj.value.enterprises().enrollmentTokens().create(
         parent=ENTERPRISE_NAME,
         body={"policyName": POLICY_NAME,  "allowPersonalUsage": "PERSONAL_USAGE_DISALLOWED","user": {
         "accountIdentifier" : "6001"
      }},).execute()



      image = {
         'cht': 'qr',
         'chs': '500x500',
         'chl': enrollment_token['qrCode']
      }

      qrcode_url = QR_CODE_URL+ urlencode(image)

      print('Please visit this URL to scan the QR code:', qrcode_url)

   except Exception as e:
      print("An exception occurred in Generating QR code ",e)
      return "An exception occurred in Generating QR code "
    
   
   return "xzckivhx"