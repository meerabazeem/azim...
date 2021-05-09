from flask import Flask,render_template,request

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
	
	return render_template("index.html")
	
@app.route("/index.html", methods=['GET'])
def index1():

        return render_template("index.html")
        
@app.route("/gettingface.html", methods=['GET'])
def gettingface():
	
	return render_template("gettingface.html")  
	
@app.route("/featuresextraction.html", methods=['GET'])
def featuresextraction():
	
	return render_template("featuresextraction.html")    
    
@app.route("/facerecognition.html", methods=['GET'])
def facerecognition():
	
	return render_template("facerecognition.html") 

          	  
if __name__ == "__main__":
    app.run(debug=True, host="192.168.10.14", port="5000") 
    
    
     
    
   

