#Import necessary libraries
from flask import Flask, render_template, request

import numpy as np
import os

from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

filepath = 'C:/Users/Anandh/AppData/Local/Programs/Python/Python38/Tomato_Leaf_Disease_Prediction/fruitdata.h5'
model = load_model(filepath)
print(model)

print("Model Loaded Successfully")

def pred_tomato_dieas(plant):
  test_image = load_img(plant, target_size = (128, 128)) # load image 
  print("@@ Got Image for prediction")
  
  test_image = img_to_array(test_image)/255 # convert image to np array and normalize
  test_image = np.expand_dims(test_image, axis = 0) # change dimention 3D to 4D
  
  result = model.predict(test_image) # predict diseased palnt or not
  print('@@ Raw result = ', result)
  
  pred = np.argmax(result, axis=1)
  print(pred)
  if plant=="fruit":
    if pred==0:
        return "Apple__Black_rot", 'Apple__Black_rot.html'
       
    elif pred==1:
        return "Apple__healthy", 'Apple__healthy.html'
        
    elif pred==2:
        return "Corn_(maize)__healthy", 'Corn_(maize)__healthy.html'
        
    elif pred==3:
        return "Corn_(maize)__Northern_Leaf_Blight", 'Corn_(maize)__Northern_Leaf_Blight.html'
       
    elif pred==4:
        return "Peach__Bacterial_spot", 'Peach__Bacterial_spot.html'
        
    elif pred==5:
        return "Peach__healthy", 'Peach__healthy.html'
  elif plant=="Vegetable":
    if pred==0:
        return "Pepper,_bell__Bacterial_spot", 'Pepper,_bell__Bacterial_spot.html'
       
    elif pred==1:
        return "Pepper,_bell__healthy", 'Pepper,_bell__healthy.html'
        
    elif pred==2:
        return "Potato__Early_blight", 'Potato__Early_blight.html'
        
    elif pred==3:
        return "Potato__healthy", 'Potato__healthy.html'
       
    elif pred==4:
        return "Potato__Late_blight", 'Potato__Late_blight.html'
        
    elif pred==5:
        return "Tomato__Bacterial_spot", 'Tomato__Bacterial_spot.html'
    
    elif pred==6:
        return "Tomato__Late_blight" , 'Tomato__Late_blight.html'
    
    elif pred==7:
        return "Tomato__Leaf_Mold" , 'Tomato__Leaf_Mold.html'
    
    elif pred==8:
        return "Tomato__Septoria_leaf_spot" , 'Tomato__Septoria_leaf_spot.html'
      
        

    

# Create flask instance
app = Flask(__name__)

# render index.html page
@app.route("/", methods=['GET', 'POST'])
def home():
        return render_template('index.html')
    
 
# get input image from client then predict class and render respective .html page for solution
@app.route("/predict", methods = ['GET','POST'])
def predict():
     if request.method == 'POST':
        file = request.files['image'] # fet input
        filename = file.filename        
        print("@@ Input posted = ", filename)
        
        file_path = os.path.join('C:/Users/Madhuri/AppData/Local/Programs/Python/Python38/Tomato_Leaf_Disease_Prediction/static/upload/', filename)
        file.save(file_path)

        print("@@ Predicting class......")
        pred, output_page = pred_tomato_dieas(tomato_plant=file_path)
              
        return render_template(output_page, pred_output = pred, user_image = file_path)
    
# For local system & cloud
if __name__ == "__main__":
    app.run(threaded=False,port=8080) 
    
    
