from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mh_forecast import predict

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def index():
    return {"greeting": "Mental Health Forecast API ok!"}

@app.get("/predict")
def predict_query(_SEX, _AGE80, _RFHLTH, _HLTHPLN, MEDCOST1, CHECKUP1, _TOTINDA, SLEPTIM1, _MICHD, _LTASTH1, MARITAL,
            EDUCA, RENTHOM1, EMPLOY1, CHILDREN, _BMI5CAT, DECIDE, DIFFALON, _SMOKER3, ALCDAY4, LSATISFY,
            EMTSUPRT, SDHISOLT, SDHEMPLY, SDHFOOD1, SDHBILLS, SDHUTILS, SDHTRNSP, SDHSTRE1, _RACEGR4):

    prediction=predict.predict_health(_SEX, _AGE80, _RFHLTH, _HLTHPLN, MEDCOST1, CHECKUP1, _TOTINDA, SLEPTIM1, _MICHD, _LTASTH1, MARITAL,
            EDUCA, RENTHOM1, EMPLOY1, CHILDREN, _BMI5CAT, DECIDE, DIFFALON, _SMOKER3, ALCDAY4, LSATISFY,
            EMTSUPRT, SDHISOLT, SDHEMPLY, SDHFOOD1, SDHBILLS, SDHUTILS, SDHTRNSP, SDHSTRE1, _RACEGR4)

    return prediction
