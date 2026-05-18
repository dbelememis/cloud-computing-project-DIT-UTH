from fastapi import FastAPI, UploadFile, File
from fastapi.responses import Response

from processing import grayscale

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Image Processing API"}

@app.post("/grayscale")
async def convert_to_grayscale(file: UploadFile = File(...)):

    image_bytes = await file.read()

    processed_image = grayscale(image_bytes)

    return Response(
        content=processed_image,
        media_type="image/png"
    )