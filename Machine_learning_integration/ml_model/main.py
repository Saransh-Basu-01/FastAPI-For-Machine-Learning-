from fastapi import FastAPI
from schemas import InputSchema,OutputSchema
from predict import make_predictions
from typing import List

app=FastAPI()


@app.get('/')
def index():
    return {'message': 'Welcome to the ML Model Prediction API'}

@app.post('/prediction',response_model=OutputSchema)
def predict(user_input:InputSchema):
    predictions=make_predictions(user_input.model_dump())
    return OutputSchema(predicted_price=round(predictions,2))