from flask import Flask, redirect, url_for, request , render_template
from flask import jsonify,render_template ,request
from werkzeug.utils import secure_filename
import os
import json


UPLOAD_FOLDER = 'app/static/images/'

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

class NationalCard():
    def __init__(self , nationalCode , firtName , lastName , birthDate
     , fathersName , expirationDate , faceImage , cardImage ) :

     self.nationalCode = nationalCode 
     self.firtName = firtName 
     self.lastName = lastName
     self.birthDate = birthDate
     self.fathersName = fathersName
     self.expirationDate = expirationDate
     self.faceImage = faceImage
     self.cardImage = cardImage

        


cards = {
'1' : {
    "nationalCode" : 1,
    "firtName" : "pouya",
    "lastName" : "teimoury",
    "birthDate" : "13970829",
    "fathersName" : "khodabakhsh",
    "expirationDate" : "14011125" ,
    "faceImage" : "face.JPG",
    "cardImage" : "card.jpg"} , 
'2':{
    "nationalCode" : 2,
    "firtName" : "reza",
    "lastName" : "farjam",
    "birthDate" : "13970829",
    "fathersName" : "ali",
    "expirationDate" : "14011125" ,
    "faceImage" : "face.JPG",
    "cardImage" : "card.jpg"} ,

'3':{
    "nationalCode" : 3,
    "firtName" : "ahmad",
    "lastName" : "yazdan",
    "birthDate" : "13970829",
    "fathersName" : "sohrab",
    "expirationDate" :"14011125" ,
    "faceImage" : "face.JPG",
    "cardImage" : "card.jpg"} , 
'4':{
    "nationalCode" : 4,
    "firtName" : "ali",
    "lastName" : "hassani",
    "birthDate" : "13970829",
    "fathersName" : "mohammad",
    "expirationDate" : "14011125" ,
    "faceImage" : "face.JPG",
    "cardImage" : "card.jpg"} ,
'5':{
    "nationalCode" : 5,
    "firtName" : "shadmehr",
    "lastName" : "gholipor",
    "birthDate" : "13970829",
    "fathersName" : "panjali",
    "expirationDate" : "14011125" ,
    "faceImage" : "face.JPG",
    "cardImage" : "card.jpg"
}
}

for data in cards:
    cards.get(data)["birthDate"] = cards.get(data)["birthDate"][:4] + '/' +  cards.get(data)["birthDate"][4:6] + '/' +  cards.get(data)["birthDate"][6:]
    cards.get(data)["expirationDate"] = cards.get(data)["expirationDate"][:4] + '/' + cards.get(data)["expirationDate"][4:6] + '/' + cards.get(data)["expirationDate"][6:]


@app.route("/")
def index():
    return render_template('home.html')


@app.route('/test',methods = ['POST'])
def recive_image():
    content = request.files['file']  
    content.save(os.path.join(app.config['UPLOAD_FOLDER'] , content.filename))

    newCard = NationalCard(len(cards) + 1 , "newUser" + str(len(cards) + 1) 
    ,"newUser" + str(len(cards) + 1) ,  "13970829" , "newUser" + str(len(cards) + 1) , "13970829" ,
    "face.JPG" , content.filename ) 

    recevied = newCard.__dict__
    recevied = PutSlash(recevied)
    cards[str(newCard.nationalCode)] = recevied
    return recevied
    #return redirect(f'/{str(newCard.nationalCode)}')


@app.route('/<number>' , methods = ['GET'])    
def show_info(number):
        if number not in cards:     
            return render_template('nofound.html')
        else: 
            result   = cards.get(number)   
            return render_template('index.html', data = result)




def PutSlash(data : dict):
    data["birthDate"] = data["birthDate"][:4] + '/' +  data["birthDate"][4:6] + '/' +  data["birthDate"][6:]
    data["expirationDate"] = data["expirationDate"][:4] + '/' + data["expirationDate"][4:6] + '/' + data["expirationDate"][6:]
    return data
