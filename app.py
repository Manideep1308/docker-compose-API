
from flask import Flask, request
from flask_cors import CORS


# import fileinput

app =Flask(__name__)
CORS(app)


@app.route('/init', methods=['POST'])

def init():

#  version = request.args.get('version')
#  composefilename=request.args.get('composefilename')


 version=request.json['version']
 composefilename=request.json['composefilename']                          #body params
   
#  with open("docker-compose.yml", 'w') as f:
 with open(str(composefilename), 'w') as f:
        f.write("version: '" +str(version)+ "'\n")
        f.write("volumes :\n")
        f.write("services:\n")

#  print(request.json['version']) 
#  print(request.json['composefilename'])                         

 return  (
     '{\n'
     '   "'+str(version)+'" : "added" \n'
     '}\n'
   )  


@app.route('/volumes', methods=['POST'])
def vol():
#  addvolume =request.args.get('addvolume')
#  composefilename=request.args.get('composefilename')


 addvolume =request.json['addvolume']
 composefilename=request.json['composefilename']                      #body params

#  with open("docker-compose.yml", "r") as f:
 with open(str(composefilename), 'r') as f:
    contents = f.readlines()

 contents.insert(2, " "+str(addvolume)+":\n")

 with open(str(composefilename), "w") as f:
    contents = "".join(contents)
    f.write(contents) 

 

 return (
     '{\n'
     '   "'+str(addvolume)+'" : "added" \n'
     '}\n'
   )        



@app.route('/appendvolumes', methods=['POST'])
def appendvol():

#  composefilename =request.args.get('composefilename') 
#  volumename =request.args.get('volumename')
#  path =request.args.get('path')


 composefilename=request.json['composefilename'] 
 volumename =request.json['volumename']                           #body params
 path =request.json['path']
    
 with open(str(composefilename), "a+") as f:

       f.write("      - "+(volumename) +":/"+path+"\n")       

 return  (
     '{\n'
     '   "'+str(volumename)+'" : "added" \n'
     '}\n'
   )          


@app.route('/appendenv', methods=['POST'])
def appendenv():

#  composefilename=request.args.get('composefilename')
#  username =request.args.get('username')
#  password =request.args.get('password')
#  dbserver =request.args.get('dbserver')


 composefilename=request.json['composefilename']
 username =request.json['username']                  #body params
 password =request.json['password']
 dbserver =request.json['dbserver']    


 with open(str(composefilename), "a+") as f:
       f.write("    environmnet:\n")
       f.write("      ADMINUSERNAME: "+str(username)+"\n")
       f.write("      ADMINPASSWORD: "+str(password)+"\n")
       f.write("      SERVER: "+str(dbserver)+"\n")           

 return  (
     '{\n'
     '   "'+str(dbserver)+'" : "added" \n'
     '}\n'
   )    

@app.route('/services', methods=['POST'])
def service():

#  composefilename=request.args.get('composefilename')
#  servicename =request.args.get('servicename')           
#  imagename = request.args.get('imagename')
#  ports=request.args.get('ports')
#  containername =request.args.get('containername')
#  volume =request.args.get('volume')
#  volumepath =request.args.get('volumepath')


 composefilename=request.json['composefilename']
 servicename =request.json['servicename']          
 imagename = request.json['imagename']
 ports=request.json['ports']                                 #body params
 containername =request.json['containername']
 volume =request.json['volume']
 volumepath =request.json['volumepath']



 with open(str(composefilename), "a+") as f1:
         f1.write("  "+str(servicename)+":\n")
         f1.write("    image: " + str(imagename) + "\n")
         f1.write("    ports:\n")
         f1.write("     - '" +str(ports)+":"+str(ports)+"'\n")
         f1.write("    container_name: " + str(containername) + "\n")
         f1.write("    volumes:\n")
         f1.write("      - "+volume+":/"+volumepath+"\n")
         f1.close()
      
      


 return  (
     '{\n'
     '   "'+str(servicename)+'" : "added" \n'
     '}\n'
   )  

@app.route('/changes', methods=['POST'])
def change():

    # composefilename=request.args.get('composefilename')    
    # stringtoreplace=request.args.get('stringtoreplace')
    # afterreplace=request.args.get('afterreplace')

    composefilename=request.json['composefilename']         #body params
    stringtoreplace=request.json['stringtoreplace']
    afterreplace=request.json['afterreplace']

    f1 = open(str(composefilename),'r')
    data = f1.read()
    data = data.replace(str(stringtoreplace), str(afterreplace))
    f1.close()
    f2 = open(str(composefilename),'w')
    f2.write(data)
    f2.close() 

    return  (
     '{\n'
     '   "changingfrom" : "'+str(stringtoreplace)+'"\n'
     '   "changingto" : "'+str(afterreplace)+'"\n'
     '}\n'
   ) 

@app.route('/repeatedstringchanges', methods=['POST'])
def repeat():

    # composefilename=request.args.get('composefilename')    
    # stringtoreplace=request.args.get('stringtoreplace')
    # afterreplace=request.args.get('afterreplace')

    composefilename=request.json['composefilename']
    nthoccurance =request.json['nthoccurance']                                                                  #body params
    stringtoreplace=request.json['stringtoreplace']
    afterreplace=request.json['afterreplace']

    f1 = open(str(composefilename),'r')
    data = f1.read()
    nth = int(nthoccurance)
    data = data.replace(str(stringtoreplace), str(afterreplace), nth)
    data = data.replace(str(afterreplace), str(stringtoreplace), nth-1)
    f1.close()
    f2 = open(str(composefilename),'w')
    f2.write(data)
    f2.close() 

    return  (
     '{\n'
     '   "changingfrom" : "'+str(stringtoreplace)+'"\n'
     '   "changingto" : "'+str(afterreplace)+'"\n'
     '}\n'
   ) 


# main()
# home() 
app.run(port=1564, host='0.0.0.0', debug=True)


