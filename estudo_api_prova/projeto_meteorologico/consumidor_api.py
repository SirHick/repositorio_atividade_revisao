import requests

def obter_dados_meteorologicos():
    endereco = "https://api.open-meteo.com/v1/forecast"

    parametros = {
        "latitude": -26.48,
        "longitude": -49.07,
        "current": ["temperature_2m", "relative_humidity_2m", "apparent_temperature", "wind_speed_10m", "precipitation"],
        "timezone": "America/Sao_Paulo" 
    }

    resposta = requests.get(endereco, params = parametros, timeout=15)
    resposta.raise_for_status()

    dados = resposta.json()
    condicoes_atuais = dados["current"]

    return{
        "temperatura": condicoes_atuais["temperature_2m"],
        "umidade_relativa": condicoes_atuais["relative_humidity_2m"],
        "sensacao_termica": condicoes_atuais["apparent_temperature"],
        "velocidade_vento": condicoes_atuais["wind_speed_10m"],
        "precipitacao": condicoes_atuais["precipitation"]
    }