import pymongo 
from flask import Flask , jsonify 
from AndroidManagementObject import SharedObject
from config import ENTERPRISE_NAME , DEVICE_DB_NAME, DEVICE_COLLECTION_NAME , MONGODB_URL ,DEVICE_URL
from bson import json_util, ObjectId
import json



def GetListOfDevices() :

    try :

        shared_obj = SharedObject.shared_instance



        json_data = shared_obj.value.enterprises().devices().list(
        parent=ENTERPRISE_NAME,
        pageSize=10
        ).execute()


        if len(json_data) != 0 :

        #    print("List of device is",json_data)

        # EnrollDeviceData()
            client = pymongo.MongoClient(MONGODB_URL)
            db=client[DEVICE_DB_NAME]
            collection = db[DEVICE_COLLECTION_NAME]
    
            for device in json_data["devices"] :
    
                print("fhhkjg",device)
                device_data = device.get("name")
                print("fdj",device_data)
    
    
      
    
                document =collection.find_one({"name":device_data})
                if document :
                    print("document found")
                else :
                    print("document not found",device)
                #result = collection.update_one(filter_criteria,{"$set" :device_data },upsert=True)
                    device_json= json.loads(json_util.dumps(device))
                    result = collection.insert_one(device_json)
                    print("result is",result)
        
        
            client.close()

    except Exception as e:
        print("An exception occurred in Getting List of Devices ",e)
        return "An exception occurred in Getting List of Devices"




   
    return json_data