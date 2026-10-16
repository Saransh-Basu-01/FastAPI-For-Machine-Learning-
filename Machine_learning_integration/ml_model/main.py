from fastapi import FastAPI
from schemas import InputSchema,OutputSchema
from predict import make_predictions,make_batch_predictions
from typing import List

app=FastAPI()


@app.get('/')
def index():
    return {'message': 'Welcome to the ML Model Prediction API'}

@app.post('/prediction',response_model=OutputSchema)
def predict(user_input:InputSchema):
    predictions=make_predictions(user_input.model_dump())
    return OutputSchema(predicted_price=round(predictions,2))


@app.post('/batch_predictions',response_model=List[OutputSchema])
def make_batch_prediction(user_inputs:List[InputSchema]):
    predictions=make_batch_predictions(x.model_dump() for x in user_inputs)
    return [OutputSchema(predicted_price=round(prediction, 2)) for prediction in predictions]