from AndroidManagementObject import SharedObject
from config import ENTERPRISE_NAME ,PASSWORD


def SetPasswordOnDevice() :

    try :
        
        shared_obj = SharedObject.shared_instance

        shared_obj.value.enterprises().devices().issueCommand( name=ENTERPRISE_NAME + '/devices/376f03d570d8eabd',
        body={ "type": "RESET_PASSWORD","newPassword": "passwo"} ).execute()

        print("Set new password is called")


    except Exception as e:
      print("An exception occurred in setting the password on device ",e)
      return "An exception occurred in setting the password on device "
    
    return "ckjbv"


def LOSTMODE() :

    try :
        
        shared_obj = SharedObject.shared_instance

        shared_obj.value.enterprises().devices().issueCommand( name=ENTERPRISE_NAME + '/devices/376f03d570d8eabd',
        body={   "type": "LOCK"} ).execute()

        SetPasswordOnDevice()

        print("LOST MODE")

    except Exception as e:
      print("An exception occurred in appying policies ",e)
      return "An exception occurred in appying policies"
    

    return "ckjbv"
