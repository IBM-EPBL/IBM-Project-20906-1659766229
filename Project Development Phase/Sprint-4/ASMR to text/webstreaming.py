from flask import Flask,render_template,request
import cv
from keras.models import load_model
import numpy as np
from gtts import gTTS
import os
from keras.preprocessing import image
from playsound import playsound
app = Flask(__name__)

model=load_model("aslpng1.h5")

vals = ['A', 'B','C','D','E','F','G','H','I']

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')
@app.route('/index', methods=['GET'])
def home():
	return render_template('index.html')
@app.route('/predict', methods=['GET', 'POST'])
def predict():
		print("[INFO] starting video stream...")
		vs = cv.VideoCapture(0)

		(W, H) = (None, None)

		while True:
			(grabbed, frame) = vs.read()

			if not grabbed:
				break

			if W is None or H is None:
				(H, W) = frame.shape[:2]
			output = frame.copy()
			# r = cv.selectROI("Slect", output)
			# print(r)
			cv.rectangle(output, (81, 79), (276,274), (0,255,0), 2)
			frame = frame[81:276, 79:274]
			frame = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
			_, frame = cv.threshold(frame, 95, 255, cv.THRESH_BINARY_INV)
			frame = cv.cvtColor(frame, cv.COLOR_GRAY2RGB)


			
			img = np.expand_dims(img,axis=0)
			if(np.max(img)>1):
				img = img/255.0
			
			
			result = np.argmax(model.predict(img))
			index=['A', 'B','C','D','E','F','G','H','I']
			result=str(index[result])

			
			cv.putText(output, "The Predicted Letter : {}".format(result), (10, 50), cv.FONT_HERSHEY_PLAIN,
						2, (150,0,150), 2)
			cv.putText(output, "Press q to exit", (10,450), cv.FONT_HERSHEY_PLAIN, 2, (0,0,255), 2)
			

			speech = gTTS(text = result, lang = 'en', slow = False)
			
			cv.imshow("Output", output)
			key = cv.waitKey(1) & 0xFF

			if key == ord("q"):
				break
		 

		print("[INFO] cleaning up...")
		vs.release()
		cv.destroyAllWindows()
		return render_template("index.html")

	
if __name__ == '_main_':
	  app.run(debug=True)