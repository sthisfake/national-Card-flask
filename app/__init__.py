from flask import Flask, redirect, url_for, request , render_template
from flask import jsonify,render_template


app = Flask(__name__)

# templates = Jinja2Templates(directory="templates")

class NationalCard():
    def __ini__(self , nationalCode , firtName , lastName , birthDate
     , fathersName , expirationDate , faceImage , cardImage ) :

     self.nationalCode = nationalCode 
     self.firtName = firtName 
     self.lastName = lastName
     self.birthDate = birthDate
     self.fathersName = fathersName
     self.expirationDate = expirationDate
     self.faceImage = faceImage
     self.cardImage = cardImage



@app.route("/")
def index():
    return render_template('home.html')