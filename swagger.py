from crypt import methods
from flask import Flask, request
from flasgger import Swagger
from flask_cors import CORS
app = Flask(__name__)
CORS(app) 
swagger = Swagger(app)


@app.route('/init', methods=['POST'])
def init():
 """API for initializing the docker-compose file name with version
    This API is used to initialize the docker compose file with version number.
    ---
    parameters:
      - name: composefilename
        in: query
        type: string
        required: false
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
 composefilename=request.args.get('composefilename') 
   
 with open(str(composefilename), 'w') as f:
        f.write("version: '" +str(version)+ "'\n")
        f.write("volumes :\n")
        f.write("services:\n")     

 return (
     '{\n'
     '   "'+str(composefilename)+'" : "created" \n'
     '   "version:'+str(version)+'" : "added" \n'
     '}\n'
   )


@app.route('/volumes', methods=['POST'])
def vol():
 """Initialize volumes
    This API is used to initialize the volumes used for services.
    ---
    parameters:
      - name: composefilename
        in: query
        type: string
        required: false
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
 composefilename=request.args.get('composefilename') 
   

 with open(str(composefilename), "r") as f:
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
 """Appending volumes to the services
    This API is used to append the particular volume to particular service.
    ---
    parameters:
      - name: composefilename
        in: query
        type: string
        required: false
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
 composefilename=request.args.get('composefilename') 

 volumename =request.args.get('volumename')
 path =request.args.get('path')
    
 with open(str(composefilename), "a+") as f:

       f.write("      - "+(volumename) +":/"+path+"\n")       

 return (
     '{\n'
     '   "'+str(volumename)+'" : "added" \n'
     '}\n'
   )         


@app.route('/appendenv', methods=['POST'])
def appendenv():
 """Appending environemnt to the service
    This API is used to add environment parameters like username, password , database server to the service.
    ---
    parameters:
      - name: composefilename
        in: query
        type: string
        required: false
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
 composefilename=request.args.get('composefilename') 


 with open(str(composefilename), "a+") as f:
       f.write("    environmnet:\n")
       f.write("      ADMINUSERNAME: "+str(username)+"\n")
       f.write("      ADMINPASSWORD: "+str(password)+"\n")
       f.write("      SERVER: "+str(dbserver)+"\n")           

 return (
     '{\n'
     '   "'+str(dbserver)+'" : "added" \n'
     '}\n'
   )  

@app.route('/services', methods=['POST'])
def service():
 """Describe the services
    This API is used to add services to the compose file.
    ---
    parameters:
      - name: composefilename
        in: query
        type: string
        required: false
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
 composefilename=request.args.get('composefilename') 



 with open(str(composefilename), "a+") as f1:
         f1.write("  "+str(servicename)+":\n")
         f1.write("    image: " + str(imagename) + "\n")
         f1.write("    ports:\n")
         f1.write("     - '" +str(ports)+":"+str(ports)+"'\n")
         f1.write("    container_name: " + str(containername) + "\n")
         f1.write("    volumes:\n")
         f1.write("      - "+volume+":/"+volumepath+"\n")
      
      


 return (
     '{\n'
     '   "'+str(servicename)+'" : "added" \n'
     '}\n'
   )

@app.route('/changes', methods=['POST'])
def change():
    """Any changes can be made in compose file
    This API is used to make or replace some changes in compose file.
    ---
    parameters:
      - name: composefilename
        in: query
        type: string
        required: false
      - name: stringtoreplace
        in: query
        type: string
        required: false        
      - name: afterreplace
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

    composefilename=request.args.get('composefilename')    
    stringtoreplace=request.args.get('stringtoreplace')
    afterreplace=request.args.get('afterreplace')

    # composefilename=request.json['composefilename']         #body params
    # strintoreplace=request.json['stringtoreplace']
    # afterreplace=request.json['afterreplace']

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
    """Changes can be made for repeated strings
    This API is used to make changes for the repeated strings in the compose file.
    ---
    parameters:
      - name: composefilename
        in: query
        type: string
        required: false
      - name: nthoccurance
        in: query
        type: string
        required: false
      - name: stringtoreplace
        in: query
        type: string
        required: false        
      - name: afterreplace
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
app.run(port=1111, host='0.0.0.0', debug=True)


