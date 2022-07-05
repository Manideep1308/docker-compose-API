from __future__ import print_function
from flask import Flask, request, render_template, jsonify, json, Response
from flask_cors import CORS
import sys

app =Flask(__name__)
CORS(app)

@app.route('/show', methods=['POST', 'GET'])
def home():

 composefilename=request.json['composefilename']

 f= open(str(composefilename), 'r')
 list=f.readlines() 
 return render_template("table.html", len =len(list), list=list) 
    


@app.route('/append', methods=['POST'])
def appendenv():

 composefilename=request.json['composefilename']
 append=request.json['append']
 volumename =request.json['volumename']                           #body params
 path =request.json['path']
 username =request.json['username']                  #body params
 password =request.json['password']
 dbserver =request.json['dbserver'] 
 index = request.json['index']   


 data1=("    environmnet:\n"
        "      ADMINUSERNAME: "+str(username)+"\n"
        "      ADMINPASSWORD: "+str(password)+"\n"
        "      SERVER: "+str(dbserver)+"\n") 

 data2 =("      - "+(volumename) +":/"+path+"\n") 



 if(str(append)=='volume'):       

   with open(str(composefilename), 'r') as f:
    contents = f.readlines()
   contents.insert(int(index), data2)
   with open(str(composefilename), "w") as f:
    contents = "".join(contents)
    f.write(contents) 
   return  (
     '{\n'
     '   "'+str(dbserver)+'" : "added" \n'
     '}\n'
   ) 



 if(str(append) =='environment'):       

   with open(str(composefilename), 'r') as f:
     contents = f.readlines()
   contents.insert(int(index), data1)
   with open(str(composefilename), "w") as f:
    contents = "".join(contents)
    f.write(contents) 
   return  (
     '{\n'
     '   "'+str(volumename)+'" : "added" \n'
     '}\n'
   ) 

 else:
        return 'not matched'





@app.route('/delete', methods =['POST', "GET"]) 
def test():
  
 composefilename=request.json['composefilename']
 index=request.json['index']
 with open(str(composefilename), "r+") as f:
    lines = f.readlines()
    del lines[int(index)]  # use linenum - 1 if linenum starts from 1
    f.seek(0)
    f.truncate()
    f.writelines(lines)

 return(
    '{\n'
     '   "'+str(index)+'" : "deleted" \n'
    '}\n'
   ) 
    
 

@app.errorhandler(Exception)
def all_exception_handler(error):
    res = {"error": str(error)}
    return Response(status=500, mimetype="application/json", response=json.dumps(res))



def error_401_handler(error):
    res = {"error": "Unauthorized"}
    return Response(status=401, mimetype="application/json", response=json.dumps(res))


app.run(port=7568, host='0.0.0.0', debug=True)  

