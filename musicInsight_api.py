from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware

import numpy as np
import os

from predict import Predictor
from chromaprint import ChromaprintExtractor

from labels import labels

app = FastAPI()

# Dev Environment
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # O ["*"] para permitir todos los orígenes
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

chromaprint_extractor = ChromaprintExtractor()
predictor = Predictor()

@app.post("/extract-chromaprint/")
async def extract_chromaprint(audio_file: UploadFile):
    if audio_file.filename.endswith((".mp3", ".wav")):
        # Save the uploaded file temporarily
        audio_path = "temp_audio.wav"
        with open(audio_path, "wb") as audio_data:
            audio_data.write(audio_file.file.read())

    try:
        fingerprint, response = chromaprint_extractor.query_acoustid(audio_file.filename)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        # Clean up temporary audio file
        os.remove(audio_path)

    return {
        "Fingerprint": fingerprint,
        "AcoustID Response": response
    }

@app.post("/predict/")
async def predict_genre(audio_file: UploadFile):
    if audio_file.filename.endswith((".mp3", ".wav")):
        # Save the uploaded file temporarily
        audio_path = "temp_audio.wav"
        with open(audio_path, "wb") as audio_data:
            audio_data.write(audio_file.file.read())

    try:
        genre_primary, genre_full, genre_secondary = predictor.predict(audio_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        # Clean up temporary audio file
        os.remove(audio_path)

    return {
        "Primary Genre": genre_primary,
        "Full Genre": genre_full,
        "Secondary Genre": genre_secondary,
    }
