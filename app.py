
from flask import Flask, request, Response, json, render_template
from flask_cors import CORS
import os

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
     '   "'+str(composefilename)+'" : "created" \n'
     '   "version:'+str(version)+'" : "added" \n'
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
       f.write("    environment:\n")
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




@app.route('/index', methods=['POST', 'GET'])
def fun1():

 composefilename=request.json['composefilename']

 f= open(str(composefilename), 'r')
 list=f.readlines() 
 return render_template("table.html", len =len(list), list=list)    



@app.route('/appendvolumeusingindex', methods=['POST'])
def volappen():

 composefilename=request.json['composefilename']
 volumename =request.json['volumename']                           #body params
 path =request.json['path']
 index = request.json['index']  

 data2 =("      - "+(volumename) +":/"+path+"\n") 

 with open(str(composefilename), 'r') as f:
    contents = f.readlines()
 contents.insert(int(index), data2)
 with open(str(composefilename), "w") as f:
    contents = "".join(contents)
    f.write(contents) 
 return  (
     '{\n'
     '   "'+str(volumename)+'" : "appended" \n'
     '}\n'
   ) 



@app.route('/appendenvusingindex', methods=['POST'])
def env():

 composefilename=request.json['composefilename']
 username =request.json['username']                  #body params
 password =request.json['password']
 dbserver =request.json['dbserver'] 
 index = request.json['index'] 


 data1=("    environment:\n"
        "      ADMINUSERNAME: "+(username)+"\n"
        "      ADMINPASSWORD: "+(password)+"\n"
        "      SERVER: "+(dbserver)+"\n") 



     

 with open(str(composefilename), 'r') as f:
     contents = f.readlines()
 contents.insert(int(index), data1)
 with open(str(composefilename), "w") as f:
    contents = "".join(contents)
    f.write(contents) 
 return  (
     '{\n'
     '   "'+str(dbserver)+'" : "appended" \n'
     '}\n'
   ) 





@app.route('/delete', methods =['POST']) 
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
    

@app.route('/deletemultiple', methods=['POST'])
def delete_multiple_lines():
    
    filename=request.json['filename']
    index=request.json['index']

    is_skipped = False
    counter = 0
    original_file=filename
    line_numbers=index
        
    dummy_file = original_file + '.bak'
    with open(original_file, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
     
        for line in read_obj:
           
            if counter not in line_numbers:
                write_obj.write(line)
            else:
                is_skipped = True
            counter += 1
   
    if is_skipped:
        os.remove(original_file)
        os.rename(dummy_file, original_file)
    else:
        os.remove(dummy_file)


    return  (
     '{\n'
     '   "'+str(index)+' lines" : "deleted" \n'
     '}\n'
   ) 



@app.errorhandler(Exception)
def all_exception_handler(error):
    res = {"error": str(error)}
    return Response(status=500, mimetype="application/json", response=json.dumps(res))



def error_401_handler(error):
    res = {"error": "Unauthorized"}
    return Response(status=401, mimetype="application/json", response=json.dumps(res))

# main()
# home() 
app.run(port=1564, host='0.0.0.0', debug=True)


