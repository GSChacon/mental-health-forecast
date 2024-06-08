import streamlit as st
import requests

# Título do projeto
st.title('Mental Health Forecast')

# Início do formulário
with st.form("health_survey"):
    _SEX = st.selectbox('Sexo', ['Masculino', 'Feminino'])
    _SEX = 1 if _SEX == 'Masculino' else 2

    _AGE80 = st.number_input('Idade', min_value=18, max_value=120, value=18)

    _RFHLTH = st.selectbox('Percepção sobre sua própria saúde', ['Boa', 'Razoável ou Ruim', 'Não sei'])
    _RFHLTH_dict = {'Boa': 1, 'Razoável ou Ruim': 2, 'Não sei': 9}
    _RFHLTH = _RFHLTH_dict[_RFHLTH]

    _HLTHPLN = st.selectbox('Possui plano de saúde', ['Sim', 'Não', 'Não sei'])
    _HLTHPLN_dict = {'Sim': 1, 'Não': 2, 'Não sei': 9}
    _HLTHPLN = _HLTHPLN_dict[_HLTHPLN]

    MEDCOST1 = st.selectbox('Enfrentou alguma barreira financeira para consultas médicas nos últimos 12 meses', ['Sim', 'Não', 'Não sei', 'Recusar a responder'])
    MEDCOST1_dict = {'Sim': 1, 'Não': 2, 'Não sei': 7, 'Recusar a responder': 9}
    MEDCOST1 = MEDCOST1_dict[MEDCOST1]

    CHECKUP1 = st.selectbox('Quanto tempo faz que realizou check-ups médicos de rotina', ['Menos de 1 ano', '1-2 anos', '2-5 anos', 'Mais de 5 anos', 'Não sei', 'Nunca', 'Recusar a responder'])
    CHECKUP1_dict = {'Menos de 1 ano': 1, '1-2 anos': 2, '2-5 anos': 3, 'Mais de 5 anos': 4, 'Não sei': 7, 'Nunca': 8, 'Recusar a responder': 9}
    CHECKUP1 = CHECKUP1_dict[CHECKUP1]

    _TOTINDA = st.selectbox('Realizou atividades físicas nos últimos 30 dias', ['Sim', 'Não', 'Não sei'])
    _TOTINDA_dict = {'Sim': 1, 'Não': 2, 'Não sei': 9}
    _TOTINDA = _TOTINDA_dict[_TOTINDA]

    SLEPTIM1 = st.slider('Duração média do sono (em horas)', 0, 24, 8)

    _MICHD = st.selectbox('Diagnosticado com infarto ou doença arterial coronariana', ['Sim', 'Não'])
    _MICHD_dict = {'Sim': 1, 'Não': 2}
    _MICHD = _MICHD_dict[_MICHD]

    _LTASTH1 = st.selectbox('Diagnosticado com asma', ['Sim', 'Não'])
    _LTASTH1_dict = {'Sim': 2, 'Não': 1}
    _LTASTH1 = _LTASTH1_dict[_LTASTH1]

    MARITAL = st.selectbox('Estado civil', ['Casado', 'Divorciado', 'Viúvo', 'Separado', 'Nunca casou', 'Mora com parceiro', 'Recusar a responder'])
    MARIAL_dict = {'Casado': 1, 'Divorciado': 2, 'Viúvo': 3, 'Separado': 4, 'Nunca casou': 5, 'Mora com parceiro': 6, 'Recusar a responder': 9}
    MARITAL = MARIAL_dict[MARITAL]


    EDUCA = st.selectbox('Nível de escolaridade', ['Não completou Ensino Fundamental', 'Ensino Fundamental Completo', 'Ensino Médio Incompleto', 'Ensino Médio Completo', 'Ensino Superior Incompleto', 'Ensino Superior Completo', 'Recusar a responder'])
    EDUCA_dict = {'Não completou Ensino Fundamental': 1, 'Ensino Fundamental Completo': 2, 'Ensino Médio Incompleto': 3, 'Ensino Médio Completo': 4, 'Ensino Superior Incompleto': 5, 'Ensino Superior Completo': 6, 'Recusar a responder': 9}
    EDUCA = EDUCA_dict[EDUCA]

    RENTHOM1 = st.selectbox('Proprietário ou inquilino da residência', ['Proprietário', 'Inquilino', 'Outro', 'Não sei', 'Recusar a responder'])
    RENTHOM1_dict = {'Proprietário': 1, 'Inquilino': 2, 'Outro': 3, 'Não sei': 7, 'Recusar a responder': 9}
    RENTHOM1 = RENTHOM1_dict[RENTHOM1]

    EMPLOY1 = st.selectbox('Situação de emprego', ['Empregado', 'Autônomo', 'Desempregado por 1 ano ou mais', 'Desempregado por menos de 1 ano', 'Dono/a de casa', 'Estudante', 'Aposentado', 'Incapaz de trabalhar', 'Recusar a responder'])
    EMPLOY1_dict = {'Empregado': 1, 'Autônomo': 2, 'Desempregado por 1 ano ou mais': 3, 'Desempregado por menos de 1 ano': 4, 'Dono/a de casa': 5, 'Estudante': 6, 'Aposentado': 7, 'Incapaz de trabalhar': 8, 'Recusar a responder': 9}
    EMPLOY1 = EMPLOY1_dict[EMPLOY1]

    CHILDREN = st.number_input('Número de crianças na residência', min_value=0, max_value=87, value=0)
    if CHILDREN == 0:
        CHILDREN = 88

    _BMI5CAT = st.selectbox('Categoria de índice de massa corporal (IMC)', ['Abaixo do peso', 'Peso normal', 'Sobrepeso', 'Obesidade'])
    _BMI5CAT_dict = {'Abaixo do peso': 1, 'Peso normal': 2, 'Sobrepeso': 3, 'Obesidade': 4}
    _BMI5CAT = _BMI5CAT_dict[_BMI5CAT]

    DECIDE = st.selectbox('Dificuldade em se concentrar, memorizar coisas ou tomar decisões devido a problemas de saúde mental ou física', ['Sim', 'Não', 'Não sei', 'Recusar a responder'])
    DECIDE_dict = {'Sim': 1, 'Não': 2, 'Não sei': 7, 'Recusar a responder': 9}
    DECIDE = DECIDE_dict[DECIDE]

    DIFFALON = st.selectbox('Dificuldade em realizar atividades devido a problemas de saúde mental ou física', ['Sim', 'Não', 'Não sei', 'Recusar a responder'])
    DIFFALON_dict = {'Sim': 1, 'Não': 2, 'Não sei': 7, 'Recusar a responder': 9}
    DIFFALON = DIFFALON_dict[DIFFALON]

    _SMOKER3 = st.selectbox('Status de tabagismo', ['Fuma todos os dias', 'Fuma alguns dias', 'Ex-fumante', 'Nunca fumou', 'Recusar a responder'])
    _SMOKER3_dict = {'Fuma todos os dias': 1, 'Fuma alguns dias': 2, 'Ex-fumante': 3, 'Nunca fumou': 4, 'Recusar a responder': 9}
    _SMOKER3 = _SMOKER3_dict[_SMOKER3]

    ALCDAY4 = st.number_input('Frequência de consumo de álcool nos últimos 30 dias (dias de consumo)', min_value=0, max_value=30, value=0)
    if ALCDAY4 == 0:
        ALCDAY4 = 888
    else:
        ALCDAY4 = ALCDAY4 + 200

    LSATISFY = st.selectbox('Grau de satisfação com a vida em geral', ['Muito satisfeito', 'Satisfeito', 'Insatisfeito', 'Muito insatisfeito', 'Não sei', 'Recusar a responder'])
    LSATISFY_dict = {'Muito satisfeito': 1, 'Satisfeito': 2, 'Insatisfeito': 3, 'Muito insatisfeito': 4, 'Não sei': 7, 'Recusar a responder': 9}
    LSATISFY = LSATISFY_dict[LSATISFY]

    EMTSUPRT = st.selectbox('Frequência de apoio emocional de amigos ou familiares recebida', ['Sempre', 'Frequentemente', 'Às vezes', 'Raramente', 'Nunca', 'Não sei', 'Recusar a responder'])
    EMTSUPRT_dict = {'Sempre': 1, 'Frequentemente': 2, 'Às vezes': 3, 'Raramente': 4, 'Nunca': 5, 'Não sei': 7, 'Recusar a responder': 9}
    EMTSUPRT = EMTSUPRT_dict[EMTSUPRT]

    SDHISOLT = st.selectbox('Frequência da sensação de isolamento social', ['Sempre', 'Frequentemente', 'Às vezes', 'Raramente', 'Nunca', 'Não sei', 'Recusar a responder'])
    SDHISOLT_dict = {'Sempre': 1, 'Frequentemente': 2, 'Às vezes': 3, 'Raramente': 4, 'Nunca': 5, 'Não sei': 7, 'Recusar a responder': 9}
    SDHISOLT = SDHISOLT_dict[SDHISOLT]

    SDHEMPLY = st.selectbox('Perdeu o emprego ou teve redução de horas nos últimos 12 meses', ['Sim', 'Não', 'Não sei', 'Recusar a responder'])
    SDHEMPLY_dict = {'Sim': 1, 'Não': 2, 'Não sei': 7, 'Recusar a responder': 9}
    SDHEMPLY = SDHEMPLY_dict[SDHEMPLY]

    SDHFOOD1 = st.selectbox('Durante os últimos 12 meses, com que frequência a comida que você comprou não durou e você não teve dinheiro para comprar mais', ['Sempre', 'Frequentemente', 'Às vezes', 'Raramente', 'Nunca', 'Não sei', 'Recusar a responder'])
    SDHFOOD1_dict = {'Sempre': 1, 'Frequentemente': 2, 'Às vezes': 3, 'Raramente': 4, 'Nunca': 5, 'Não sei': 7, 'Recusar a responder': 9}
    SDHFOOD1 = SDHFOOD1_dict[SDHFOOD1]

    SDHBILLS = st.selectbox('Enfrentou insegurança financeira nos últimos 12 meses (não conseguir pagar as contas)', ['Sim', 'Não', 'Não sei', 'Recusar a responder'])
    SDHBILLS_dict = {'Sim': 1, 'Não': 2, 'Não sei': 7, 'Recusar a responder': 9}
    SDHBILLS = SDHBILLS_dict[SDHBILLS]

    SDHUTILS = st.selectbox('Teve dificuldade em pagar contas de serviços públicos nos últimos 12 meses', ['Sim', 'Não', 'Não sei', 'Recusar a responder'])
    SDHUTILS_dict = {'Sim': 1, 'Não': 2, 'Não sei': 7, 'Recusar a responder': 9}
    SDHUTILS = SDHUTILS_dict[SDHUTILS]

    SDHTRNSP = st.selectbox('Teve dificuldade de se transportar para lugares do dia a dia nos últimos 12 meses', ['Sim', 'Não', 'Não sei', 'Recusar a responder'])
    SDHTRNSP_dict = {'Sim': 1, 'Não': 2, 'Não sei': 7, 'Recusar a responder': 9}
    SDHTRNSP = SDHTRNSP_dict[SDHTRNSP]

    SDHSTRE1 = st.selectbox('Sentiu estresse nos últimos 12 meses', ['Sempre', 'Frequentemente', 'Às vezes', 'Raramente', 'Nunca', 'Não sei', 'Recusar a responder'])
    SDHSTRE1_dict = {'Sempre': 1, 'Frequentemente': 2, 'Às vezes': 3, 'Raramente': 4, 'Nunca': 5, 'Não sei': 7, 'Recusar a responder': 9}
    SDHSTRE1 = SDHSTRE1_dict[SDHSTRE1]

    _RACEGR4 = st.selectbox('Raça/etnia', ['Branco', 'Negro', 'Outro', 'Multirracial', 'Hispânico', 'Recusar a responder'])
    _RACEGR4_dict = {'Branco': 1, 'Negro': 2, 'Outro': 3, 'Multirracial': 4, 'Hispânico': 5, 'Recusar a responder': 9}
    _RACEGR4 = _RACEGR4_dict[_RACEGR4]


    # Botão de submissão
    submit_button = st.form_submit_button(label='Submeter')

# Ação após a submissão do formulário
if submit_button:
    url = 'https://mental-health-forecast-isn3eqtz4q-rj.a.run.app/predict'

    data = {
            '_SEX': _SEX,
            '_AGE80': _AGE80,
            '_RFHLTH': _RFHLTH,
            '_HLTHPLN': _HLTHPLN,
            'MEDCOST1': MEDCOST1,
            'CHECKUP1': CHECKUP1,
            '_TOTINDA': _TOTINDA,
            'SLEPTIM1': SLEPTIM1,
            '_MICHD': _MICHD,
            '_LTASTH1': _LTASTH1,
            'MARITAL': MARITAL,
            'EDUCA': EDUCA,
            'RENTHOM1': RENTHOM1,
            'EMPLOY1': EMPLOY1,
            'CHILDREN': CHILDREN,
            '_BMI5CAT': _BMI5CAT,
            'DECIDE': DECIDE,
            'DIFFALON': DIFFALON,
            '_SMOKER3': _SMOKER3,
            'ALCDAY4': ALCDAY4,
            'LSATISFY': LSATISFY,
            'EMTSUPRT': EMTSUPRT,
            'SDHISOLT': SDHISOLT,
            'SDHEMPLY': SDHEMPLY,
            'SDHFOOD1': SDHFOOD1,
            'SDHBILLS': SDHBILLS,
            'SDHUTILS': SDHUTILS,
            'SDHTRNSP': SDHTRNSP,
            'SDHSTRE1': SDHSTRE1,
            '_RACEGR4': _RACEGR4}

    response = requests.get(url=url, params=data)

    if response.status_code == 200:
            data = response.json()
            if data[0] == 1:
                st.error("Segundo o modelo, o paciente tem risco de estar em depressão.")
            if data[0] == 0:
                st.success("Segundo o modelo, o paciente não tem risco de estar com depressão.")
    else:
            st.error("Erro na requisição: " + str(response.status_code))
