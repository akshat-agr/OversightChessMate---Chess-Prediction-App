import numpy as np
from flask import Flask, request, render_template
import pickle

flask_app = Flask(__name__, static_url_path='/static')
model = pickle.load(open("model.pkl", "rb"))

@flask_app.route("/")
def Home():
    return render_template("home.html")

@flask_app.route("/predict", methods=["POST"])
def predict():
    Y = int(request.form['Y'])
    O = int(request.form['O'])
    I = int(request.form['inc'])  
    M = int(request.form['mis'])
    Bl = int(request.form['blu'])
    C = request.form['dropdown']
    data1 = np.array([[O, Y, -1*I, -1*M, -1*Bl]])
    data2 = np.array([[Y, O, I, M, Bl]])
    if(C=="option1"):
            prediction = model.predict(data1)
    elif(C=="option2"):
         prediction = model.predict(data2)
    else:
        prediction = "ERROR"

    if(C=="option1"):
         if(prediction[0]== 'Black'):
               result_text="YOU ARE MOST LIKELY TO WIN!" 
               background_image = "win.jpeg"

         elif(prediction[0]== 'White'):
              result_text="YOU HAVE TOUGH CHANCES OF WINING!" 
              background_image = "loss.jpeg"

         else:
              result_text="GAME RESULT IS MOST LIKELY TO BE DRAW!" 
              background_image = "draw.jpeg"

    else:
         if(prediction[0]== 'White'):
               result_text="YOU ARE MOST LIKELY TO WIN!" 
               background_image = "win.jpeg"
       
         elif(prediction[0]== 'Black'):
              result_text="YOU HAVE TOUGH CHANCES OF WINING!"
              background_image = "loss.jpeg"
 
         else:
              result_text="GAME RESULT IS MOST LIKELY TO BE DRAW!"  
              background_image = "draw.jpeg"
                    

    return render_template("result.html", prediction_text=result_text, background_image=background_image)
if __name__ == "__main__":
    flask_app.run(debug=True)



