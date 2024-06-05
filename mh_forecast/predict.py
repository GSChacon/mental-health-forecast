import pandas as pd
import joblib
from tensorflow.keras import models

def predict(_SEX, _AGE80, _RFHLTH, _HLTHPLN, MEDCOST1, CHECKUP1, _TOTINDA, SLEPTIM1, _MICHD, _LTASTH1, MARITAL,
            EDUCA, RENTHOM1, EMPLOY1, CHILDREN, _BMI5CAT, DECIDE, DIFFALON, _SMOKER3, ALCDAY4, LSATISFY,
            EMTSUPRT, SDHISOLT, SDHEMPLY, SDHFOOD1, SDHBILLS, SDHUTILS, SDHTRNSP, SDHSTRE1, _RACEGR4):

    # Carrega o modelo previamente salvo
    preproc = joblib.load('models/preprocessor.pkl')
    model = models.load_model('models/nn_model.keras')

    # Cria um dicionário com as variáveis recebidas
    data = {
        '_SEX': [_SEX], '_AGE80': [_AGE80], '_RFHLTH': [_RFHLTH], '_HLTHPLN': [_HLTHPLN], 'MEDCOST1': [MEDCOST1],
        'CHECKUP1': [CHECKUP1], '_TOTINDA': [_TOTINDA], 'SLEPTIM1': [SLEPTIM1], '_MICHD': [_MICHD], '_LTASTH1': [_LTASTH1],
        'MARITAL': [MARITAL], 'EDUCA': [EDUCA], 'RENTHOM1': [RENTHOM1], 'EMPLOY1': [EMPLOY1], 'CHILDREN': [CHILDREN],
        '_BMI5CAT': [_BMI5CAT], 'DECIDE': [DECIDE], 'DIFFALON': [DIFFALON], '_SMOKER3': [_SMOKER3], 'ALCDAY4': [ALCDAY4],
        'LSATISFY': [LSATISFY], 'EMTSUPRT': [EMTSUPRT], 'SDHISOLT': [SDHISOLT], 'SDHEMPLY': [SDHEMPLY], 'SDHFOOD1': [SDHFOOD1],
        'SDHBILLS': [SDHBILLS], 'SDHUTILS': [SDHUTILS], 'SDHTRNSP': [SDHTRNSP], 'SDHSTRE1': [SDHSTRE1], '_RACEGR4': [_RACEGR4]
    }

    # Converte o dicionário em um DataFrame do pandas
    df = pd.DataFrame(data)

    # Faz o pré-processamento dos dados
    X_test = preproc.transform(df)

    # Faz a previsão usando o modelo carregado
    prediction = model.predict(X_test)

    # Retorna a previsão
    return prediction

if __name__ == "__main__":
    # Exemplo de dados de entrada
    resultado = predict(1, 65, 1, 1, 0, 1, 1, 7, 1, 0, 2, 4, 2, 1, 0, 2, 1, 0, 2, 3, 4, 3, 2, 2, 2, 3, 1, 1, 1, 4)
    print(f"A previsão é: {resultado}")
