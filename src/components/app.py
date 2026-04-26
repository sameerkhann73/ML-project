import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from src.pipelines.predict_pipeline import PredictPipeline, CustomData

application = Flask(__name__)
app=application


@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST','GET'])

def predict_datapoint():
    if request.method=='GET':
        return render_template('index.html')
    else:
        data=CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('race_ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=request.form.get('reading_score'),
            writing_score=request.form.get('writing_score')
        )
        pred_df=data.get_data_as_dataframe()
        print(pred_df)
        predict_pipeline=PredictPipeline()
        result=predict_pipeline.predict(pred_df)
        return render_template('home.html',result=result[0])

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8000,debug=True)