from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from scripts import helpers
from cloud_services import detect_faces

config = helpers.get_config()

# run application with: uvicorn main:app --reload
app = FastAPI()


@app.post('/predict')
def get_face_recognition():

    return HTTPException(status_code=501, detail='Not yet implemented')