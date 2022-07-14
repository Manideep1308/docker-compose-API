import os
from flask import Flask, jsonify, request

from flask_cors import CORS
 
 
app = Flask(__name__)
CORS(app)

@app.route('/copyfiles', methods=['POST'])
def method1():
    keyname=request.args.get('keyname')
    filename=request.args.get('filename')
    ipaddress=request.args.get('ipaddress')
    path=request.args.get('path')  

    os.system('/bin/bash --rcfile sh shell1.sh '+ str(keyname) + ' ' + str(filename) + ' ' + ipaddress + ' ' + str(path))
    return (
     '{\n'
     '   "status" : 200 \n'
     '}\n'
   )

@app.route('/installdocker', methods=['POST'])
def method2():
    keyname=request.args.get('keyname')
    ipaddress=request.args.get('ipaddress')

    os.system('/bin/bash --rcfile sh shell2.sh '+ str(keyname) + ' ' + str(ipaddress))
    return (
     '{\n'
     '   "status" : 200 \n'
     '}\n'
   )

@app.route('/composeup', methods=['POST'])
def method3():
    keyname=request.args.get('keyname')
    ipaddress=request.args.get('ipaddress')

    os.system('/bin/bash --rcfile sh shell3.sh '+ str(keyname) + ' ' + str(ipaddress))
    return (
     '{\n'
     '   "status" : 200 \n'
     '}\n'
   )   

@app.route('/composedown', methods=['POST'])
def method4():
    keyname=request.args.get('keyname')
    ipaddress=request.args.get('ipaddress')

    os.system('/bin/bash --rcfile sh shell4.sh '+ str(keyname) + ' ' + str(ipaddress))
    return (
     '{\n'
     '   "status" : 200 \n'
     '}\n'
   )            

app.run(port=1234, host='0.0.0.0')   