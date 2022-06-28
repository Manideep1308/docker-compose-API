from flask import Flask, request
from flask_cors import CORS

# import fileinput

app =Flask(__name__)
CORS(app)


@app.route('/init')
def init():

 version = request.args.get('version')
   
 with open("docker-compose.yml", 'w') as f:
        f.write("version: '" +str(version)+ "'\n")
        f.write("volumes :\n")
        f.write("services:\n")     

 return "added version"


@app.route('/volumes')
def vol():
 addvolume =request.args.get('addvolume')   

 with open("docker-compose.yml", "r") as f:
    contents = f.readlines()

 contents.insert(2, " "+str(addvolume)+":\n")

 with open("docker-compose.yml", "w") as f:
    contents = "".join(contents)
    f.write(contents)       

 return "added volume"         



@app.route('/appendvolumes')
def appendvol():


 volumename =request.args.get('volumename')
 path =request.args.get('path')
    
 with open("docker-compose.yml", "a+") as f:

       f.write("      - "+(volumename) +":/"+path+"\n")       

 return "appended volumes"         


@app.route('/appendenv')
def appendenv():


 username =request.args.get('username')
 password =request.args.get('password')
 dbserver =request.args.get('dbserver')   


 with open("docker-compose.yml", "a+") as f:
       f.write("    environmnet:\n")
       f.write("      ADMINUSERNAME: "+str(username)+"\n")
       f.write("      ADMINPASSWORD: "+str(password)+"\n")
       f.write("      SERVER: "+str(dbserver)+"\n")           

 return "appended environment"  

@app.route('/services')
def service():

 servicename =request.args.get('servicename')           
 imagename = request.args.get('imagename')
 ports=request.args.get('ports')
 containername =request.args.get('containername')
 volume =request.args.get('volume')
 volumepath =request.args.get('volumepath')



 with open("docker-compose.yml", "a+") as f1:
         f1.write("  "+str(servicename)+":\n")
         f1.write("    image: " + str(imagename) + "\n")
         f1.write("    ports:\n")
         f1.write("     - '" +str(ports)+":"+str(ports)+"'\n")
         f1.write("    container_name: " + str(containername) + "\n")
         f1.write("    volumes:\n")
         f1.write("      - "+volume+":/"+volumepath+"\n")
      
      


 return "services are added to the compose file"        

# main()
# home() 
app.run(port=1564, host='0.0.0.0', debug=True)


