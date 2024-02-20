import pymongo
from config import  DEVICE_URL
from AndroidManagementObject import SharedObject
from config import ENTERPRISE_NAME , DEVICE_DB_NAME, DEVICE_COLLECTION_NAME , MONGODB_URL ,DEVICE_URL

def DeleteDevices(device) :

    print('dev',device)

    try :
        device_ids_to_delete = [device.get("deviceid")]

        shared_obj = SharedObject.shared_instance
        client = pymongo.MongoClient(MONGODB_URL)
        db=client[DEVICE_DB_NAME]
        collection = db[DEVICE_COLLECTION_NAME]

        for device_id in device_ids_to_delete:
            print("dc",device_id)
            shared_obj.value.enterprises().devices().delete(name=device_id, wipeReasonMessage="Testing deletion").execute()
            result =collection.delete_one({"name":device_id})
            print("result is" , result)
      
       

        client.close()    

    except Exception as e:
        print("An exception occurred in deleting List of Devices ",e)
        return "An exception occurred in deleting List of Devices"
    


    return "devices deleted successfully"