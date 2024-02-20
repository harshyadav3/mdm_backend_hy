import json
import pymongo
from config import POLICY_NAME ,POLICY_COLLECTION_NAME,POLICY_DB_NAME,MONGODB_URL
from datetime import datetime

from AndroidManagementObject import SharedObject



def applyPolicies(policy_jsn) :
   
   try :
     
     policy_json=json.dumps(policy_jsn)
     shared_obj = SharedObject.shared_instance
   
    
     #androidmanagement.enterprises().policies().patch(
     shared_obj.value.enterprises().policies().patch(name=POLICY_NAME, body=json.loads(policy_json)).execute()
     print("QIJNFD") 

  
     new_key = "name"
     new_value = POLICY_NAME 
     pol =json.loads(policy_json)
     pol[new_key]=new_value

     new_key1 = "last_updatedAt"
     new_value1= datetime.now()
     pol[new_key1]=new_value1
    
     filter_criteria = {"name":pol["name"]}
     client = pymongo.MongoClient(MONGODB_URL)
     db=client[POLICY_DB_NAME]
     collection = db[POLICY_COLLECTION_NAME]
    
    # result = collection.insert_one(pol)
     result = collection.update_one(filter_criteria,{"$set" : pol},upsert=True)
     print("result is",result)
     client.close()

   except Exception as e:
     print("An exception occurred in appying policies ",e)
     return "An exception occurred in appying policies"
  

   return "dcvjx"

