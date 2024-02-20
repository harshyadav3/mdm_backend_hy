import json
from config import POLICY_NAME

from AndroidManagementObject import SharedObject



def  applyPo() :
   

   policy_json = '''
{ 
  "locationMode":"LOCATION_DISABLED",
  "applications": [
    {
        "packageName": "com.google.android.apps.docs",
      "installType": "FORCE_INSTALLED"
    },
  {
  "installType": "AVAILABLE",
  "packageName": "com.cdotindia.capsachet",
   "permissionGrants":[
    {
       "permission":"android.permission.ACCESS_COARSE_LOCATION",
        "policy": "GRANT"
    }
  ]

},
{
   "installType": "FORCE_INSTALLED",
  "packageName": "com.google.android.apps.docs.editors.docs"
},
{
   "installType": "FORCE_INSTALLED",
  "packageName":"com.android.chrome"
},
{
  "packageName":"com.google.android.apps.work.clouddpc",
  "autoUpdateMode":"AUTO_UPDATE_HIGH_PRIORITY"
}],
  "keyguardDisabledFeatures": ["BIOMETRICS","DISABLE_FINGERPRINT","IRIS","FACE"],
  "usageLog": {
    "enabledLogTypes": [
      "SECURITY_LOGS",
      "NETWORK_ACTIVITY_LOGS"
    ]},
   
"cameraAccess":"CAMERA_ACCESS_UNSPECIFIED",
  "advancedSecurityOverrides": {
     "developerSettings": "DEVELOPER_SETTINGS_DISABLED"
  },

      "passwordPolicies": [
    {
        "passwordQuality":"ALPHABETIC",
        "passwordMinimumLength": 8,
        "passwordScope": "SCOPE_PROFILE"
    }
  ],
    "permissionGrants":[
    {
       "permission":"android.permission.ACCESS_COARSE_LOCATION",
        "policy": "DENY"
    }
  ],

    "playStoreMode": "WHITELIST",
    "bluetoothDisabled": true,
    "cameraDisabled": true,
    "usbFileTransferDisabled": false, 
    "screenCaptureDisabled" : true



}
'''

