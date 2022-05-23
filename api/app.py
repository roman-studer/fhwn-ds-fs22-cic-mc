from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from cloud_services import detect_faces
import sys

sys.path.insert(0, '../scripts')
from helpers import get_config

config = get_config()

# run application with: uvicorn app:app --reload
app = FastAPI()


@app.post('/predict')
def get_face_recognition():

    return HTTPException(status_code=501, detail='Not yet implemented')