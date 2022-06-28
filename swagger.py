from flask import Flask, request
from flasgger import Swagger
from flask_cors import CORS
app = Flask(__name__)
CORS(app) 
swagger = Swagger(app)


@app.route('/init')
def init():
 """Example endpoint returning a devops data
    This is using docstrings for specifications.
    ---
    parameters:
      - name: version
        in: query
        type: string
        required: true
      
    definitions:
      Palette:
        type: object
        properties:
          palette_name:
            type: array
            items:
              $ref: '#/definitions/Color'
      Color:
        type: string
    responses:
      200:
        description: A list of colors (may be filtered by palette)
        schema:
          $ref: '#/definitions/Palette'
        examples:
          rgb: ['red', 'green', 'blue']
    """

 version = request.args.get('version')
   
 with open("docker-compose.yml", 'w') as f:
        f.write("version: '" +str(version)+ "'\n")
        f.write("volumes :\n")
        f.write("services:\n")     

 return (
     '{\n'
     '   "status" : 200 \n'
     '}\n'
   )


@app.route('/volumes')
def vol():
 """Example endpoint returning a devops data
    This is using docstrings for specifications.
    ---
    parameters:
      - name: addvolume
        in: query
        type: string
        required: true
      
    definitions:
      Palette:
        type: object
        properties:
          palette_name:
            type: array
            items:
              $ref: '#/definitions/Color'
      Color:
        type: string
    responses:
      200:
        description: A list of colors (may be filtered by palette)
        schema:
          $ref: '#/definitions/Palette'
        examples:
          rgb: ['red', 'green', 'blue']
    """

 addvolume =request.args.get('addvolume')   

 with open("docker-compose.yml", "r") as f:
    contents = f.readlines()

 contents.insert(2, " "+str(addvolume)+":\n")

 with open("docker-compose.yml", "w") as f:
    contents = "".join(contents)
    f.write(contents)       

 return (
     '{\n'
     '   "status" : 200 \n'
     '}\n'
   )         



@app.route('/appendvolumes')
def appendvol():
 """Example endpoint returning a devops data
    This is using docstrings for specifications.
    ---
    parameters:
      - name: volumename
        in: query
        type: string
        required: true
      - name: path
        in: query
        type: string
        required: true 
      
    definitions:
      Palette:
        type: object
        properties:
          palette_name:
            type: array
            items:
              $ref: '#/definitions/Color'
      Color:
        type: string
    responses:
      200:
        description: A list of colors (may be filtered by palette)
        schema:
          $ref: '#/definitions/Palette'
        examples:
          rgb: ['red', 'green', 'blue']
    """  

 volumename =request.args.get('volumename')
 path =request.args.get('path')
    
 with open("docker-compose.yml", "a+") as f:

       f.write("      - "+(volumename) +":/"+path+"\n")       

 return (
     '{\n'
     '   "status" : 200 \n'
     '}\n'
   )         


@app.route('/appendenv')
def appendenv():
 """Example endpoint returning a devops data
    This is using docstrings for specifications.
    ---
    parameters:
      - name: username
        in: query
        type: string
        required: true
      - name: password
        in: query
        type: string
        required: true 
      - name: dbserver
        in: query
        type: string
        required: true   
      
    definitions:
      Palette:
        type: object
        properties:
          palette_name:
            type: array
            items:
              $ref: '#/definitions/Color'
      Color:
        type: string
    responses:
      200:
        description: A list of colors (may be filtered by palette)
        schema:
          $ref: '#/definitions/Palette'
        examples:
          rgb: ['red', 'green', 'blue']
    """  

 username =request.args.get('username')
 password =request.args.get('password')
 dbserver =request.args.get('dbserver')   


 with open("docker-compose.yml", "a+") as f:
       f.write("    environmnet:\n")
       f.write("      ADMINUSERNAME: "+str(username)+"\n")
       f.write("      ADMINPASSWORD: "+str(password)+"\n")
       f.write("      SERVER: "+str(dbserver)+"\n")           

 return (
     '{\n'
     '   "status" : 200 \n'
     '}\n'
   )  

@app.route('/services')
def service():
 """Example endpoint returning a devops data
    This is using docstrings for specifications.
    ---
    parameters:
      - name: servicename
        in: query
        type: string
        required: false
      - name: imagename
        in: query
        type: string
        required: false        
      - name: ports
        in: query
        type: string
        required: true    
      - name: containername
        in: query
        type: string
        required: false
      - name: volume
        in: query
        type: string
        required: true       
      - name: volumepath
        in: query
        type: string
        required: false     
     
    definitions:
      Palette:
        type: object
        properties:
          palette_name:
            type: array
            items:
              $ref: '#/definitions/Color'
      Color:
        type: string
    responses:
      200:
        description: A list of colors (may be filtered by palette)
        schema:
          $ref: '#/definitions/Palette'
        examples:
          rgb: ['red', 'green', 'blue']
    """ 
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
      
      


 return (
     '{\n'
     '   "status" : 200 \n'
     '}\n'
   )        

# main()
# home() 
app.run(port=1111, host='0.0.0.0', debug=True)


