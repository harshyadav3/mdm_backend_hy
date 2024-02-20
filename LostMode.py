import json
from AndroidManagementObject import SharedObject
from config import ENTERPRISE_NAME


def EnableLostMode() :


  command_body = '''
    {
    "type": "START_LOST_MODE",
    "startLostModeParams": {
    "lostOrganization": {
     "defaultMessage": "Example Organisation",
     "localizedMessages":{
       "en-US": "Example Organisation"
     }
    },
    "lostStreetAddress": {
     "defaultMessage": "1800 Amphibious Blvd. Mountain View, CA 94045",
     "localizedMessages":{
       "en-US": "1800 Amphibious Blvd. Mountain View, CA 94045"
     }
    }
   }
   }
   '''

  try:
 


    shared_obj = SharedObject.shared_instance

    shared_obj.value.enterprises().devices().issueCommand(
        name=ENTERPRISE_NAME + '/devices/376f03d570d8eabd',
        body=json.loads(command_body)
    ).execute()
    
    print("Lost mode is set")
  
  except Exception as e:
     print("An exception occurred in setting lost mode ",e)
     return "An exception occurred in setting lost mode"

  return "lost mode applied successfully"
    