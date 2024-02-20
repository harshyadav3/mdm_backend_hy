from flask import Flask , jsonify , request ,Response
from Authenticate import auth
from DeleteListOfDevices import DeleteDevices
from ListOfDevices import GetListOfDevices
from LostMode import EnableLostMode
from Policies import applyPolicies
from SetPassword import LOSTMODE, SetPasswordOnDevice
from TokenGeneration import GenerateQRCode




app = Flask(__name__)


auth()

@app.route('/api/policies' , methods=['POST'])
def policies():
    
     data =request.json
    
     
     print(data)
     applyPolicies(data)
     return jsonify(message='Hello , enforce policies')


@app.route('/api/GenerateQRCode' , methods=['GET'])
def getQRCode():
     GenerateQRCode()
     return jsonify(message='Hello , welcome your QR Code is generated successfully')



@app.route('/api/GetListOfDevices' , methods=['GET'])
def getListofdevices():
     result=GetListOfDevices()
     return jsonify(message=result)



@app.route('/api/DeleteListOfDevices' , methods=['POST'])
def DeleteMultipleDevices():
     data = request.json
     DeleteDevices(data)
     return jsonify(message='Hello , List of all deleted device')




@app.route('/api/changePassword' , methods=['GET'])
def changePassword():
     SetPasswordOnDevice()
     return jsonify(message='Hello , your password has been changed')



@app.route('/api/EnableLostMode' , methods=['GET'])
def LostMode():
     #EnableLostMode()
     LOSTMODE()
     return jsonify(message='Hello , Lost Mode has been enabled')
   

@app.route('/')
def index():
   
    return jsonify(message='Hello , welcome you are authorised successfully')



if __name__ == "__main__" :
    
     app.run(host='0.0.0.0')