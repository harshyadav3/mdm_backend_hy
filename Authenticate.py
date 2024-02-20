from googleapiclient.discovery import build
from google_auth_oauthlib.flow import Flow
from google.oauth2 import service_account
from config import SCOPE ,SERVICE_FILE
from AndroidManagementObject import SharedObject
import json





def auth() :
    
    #SCOPES = ['https://www.googleapis.com/auth/androidmanagement']
    SCOPES = [SCOPE]
    #SERVICE_ACCOUNT_FILE =  'mdm-app-412111-c37e53d3ec57.json'
    SERVICE_ACCOUNT_FILE =  SERVICE_FILE 

    credentials = service_account.Credentials.from_service_account_file( SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    androidmanagement = build('androidmanagement', 'v1', credentials=credentials)
   
    global_object =SharedObject(androidmanagement)

    print('\nAuthentication succeeded.',androidmanagement)
    print('\nglobal object is',global_object.value)
       
    return 'cfbkujv'