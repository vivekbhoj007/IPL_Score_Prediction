# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 12:50:50 2020

@author: vbhoj
"""

#pip install flask
from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('first-innings-score-lr-model.pkl','rb'))


@app.route('/')

def home():
    return render_template('ipl.html')
        # return "<h1>Welcome to homepage</h1>"


@app.route('/predict', methods=['POST','GET'])

def predict():
    temp_array = list()
    
    if request.method == 'POST':
     
      
        bat_team = request.form['bat_team']
        
        print(bat_team,'batting team.....................')
        if bat_team == 'sbat':
            return render_template('ipl.html',prediction_text="Please select the batting team")
        
        elif bat_team == 'csk':
             temp_array = temp_array + [1,0,0,0,0,0,0,0]
             
        elif bat_team == 'dd':
             temp_array = temp_array + [0,1,0,0,0,0,0,0]
             
        elif bat_team == 'kxp':
            temp_array = temp_array + [0,0,1,0,0,0,0,0]
        
        elif bat_team == 'kkr':
            temp_array = temp_array + [0,0,0,1,0,0,0,0]
        
        elif bat_team == 'mi':
            temp_array = temp_array + [0,0,0,0,1,0,0,0]
        
        elif bat_team == 'rr':
            temp_array = temp_array + [0,0,0,0,0,1,0,0]
        
        elif bat_team == 'rcb':
            temp_array = temp_array + [0,0,0,0,0,0,1,0]
            
        elif bat_team == 'srh':
             temp_array = temp_array + [0,0,0,0,0,0,0,1]
             
             
             
        bowl_team = request.form['bowl_team']
        print(bowl_team,'bowling team.................')
        
        if bowl_team == 'sbowl':
            return render_template('ipl.html',prediction_text="Please select the bowling team")
            
        elif bowl_team == 'csk':
             temp_array = temp_array + [1,0,0,0,0,0,0,0]
             
        elif bowl_team == 'dd':
             temp_array = temp_array + [0,1,0,0,0,0,0,0]
             
        elif bowl_team == 'kxp':
            temp_array = temp_array + [0,0,1,0,0,0,0,0]
        
        elif bowl_team == 'kkr':
            temp_array = temp_array + [0,0,0,1,0,0,0,0]
        
        elif bowl_team == 'mi':
            temp_array = temp_array + [0,0,0,0,1,0,0,0]
        
        elif bowl_team == 'rr':
            temp_array = temp_array + [0,0,0,0,0,1,0,0]
        
        elif bowl_team == 'rcb':
            temp_array = temp_array + [0,0,0,0,0,0,1,0]
            
        elif bowl_team == 'srh':
             temp_array = temp_array + [0,0,0,0,0,0,0,1]
             
             
        venue = request.form['venue']
        print(venue,'venueeeeeeeeeeeeeeeeeeeeeeeeeee')
        
        if venue =='sv':
            return render_template('ipl.html',prediction_text="Please select the venue") 
        
        elif venue =='eg':
             temp_array = temp_array + [1,0,0,0,0,0,0,0,0,0]
             
        elif venue =='mcs':
             temp_array = temp_array + [0,1,0,0,0,0,0,0,0,0]
             
        elif venue =='fsk':
            temp_array = temp_array + [0,0,1,0,0,0,0,0,0,0]
        
        elif venue =='ws':
            temp_array = temp_array + [0,0,0,1,0,0,0,0,0,0]
        
        elif venue =='mcsc':
            temp_array = temp_array + [0,0,0,0,1,0,0,0,0,0]
        
        elif venue =='pcas':
            temp_array = temp_array + [0,0,0,0,0,1,0,0,0,0]
        
        elif venue =='sms':
            temp_array = temp_array + [0,0,0,0,0,0,1,0,0,0]

        elif venue =='rgisu':
            temp_array = temp_array + [0,0,0,0,0,0,0,1,0,0]

        elif venue =='spsm':
            temp_array = temp_array + [0,0,0,0,0,0,0,0,1,0]

        elif venue =='km':
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,1]
    
        
        runs = int(request.form['runs'])   
        print(runs,'runsssssssssssssssssss')
        
        wickets = int(request.form['wickets'])   
        print(wickets,'wktsssssssssssssss')
        
        overs = int(request.form['overs']) 
        print(overs,'ooooooooooooooooooooo')
        
        runs_last_5 = int(request.form['runs_last_5'])
        print(runs_last_5,'run-last-5...............')
        
        wickets_last_5 = int(request.form['wickets_last_5'])  
        print(wickets_last_5,'wkts last-5..............')           
        
        temp_array = temp_array + [overs, runs, wickets, runs_last_5, wickets_last_5]
        print(temp_array,'temp-array......................')
        data = np.array([temp_array])
        
        # prediction=model.predict([[venue,bat_team,bowl_team,runs,wickets,overs,runs_last_5,wickets_last_5]])
        prediction = model.predict(data)
        # output = prediction
        output=round(prediction[0],2)
        
        
        if output<0:
            return render_template('ipl.html',prediction_text="Wrong Score {} ".format(output))
        else:
            return render_template('ipl.html',prediction_text="Expected Target of {} team is {}".format(bat_team,output))
    
    else:
        return render_template('ipl.html')



if __name__ == "__main__":
    # app.run(debug=True)
    app.run()
       
    
    