''''''
"""
========================================================
MÓDULO 10 - INTRODUÇÃO ÀS APIs
PROJETO PRÁTICO - PREVISÃO DO TEMPO
========================================================

Autor: Pedro Henrique

Este programa utiliza a API do OpenWeatherMap para
consultar informações meteorológicas de uma cidade.

Conceitos utilizados:
- API
- HTTP
- requests
- JSON
- try / except
- Tratamento de erros
- Funções
- Dicionários
========================================================
"""

import requests


# ========================================================
# CONFIGURAÇÃO
# ========================================================

API_KEY = "COLOQUE_SUA_CHAVE_AQUI"

URL_API = "https://api.openweathermap.org/data/2.5/weather"


# ========================================================
# FUNÇÃO PARA BUSCAR O CLIMA
# ========================================================

def consultar_clima(cidade):
    """
    Consulta a API do OpenWeatherMap e retorna
    os dados do clima da cidade.
    """

    parametros = {
        "q": cidade,
        "appid": API_KEY,
        "units": "metric",
        "lang": "pt_br"
    }

    try:
        print("\n🔎 Consultando informações do clima...")

        resposta = requests.get(
            URL_API,
            params=parametros,
            timeout=10
        )

        # Verifica se a API retornou erro HTTP
        resposta.raise_for_status()

        # Converte a resposta para JSON
        dados = resposta.json()

        return dados

    except requests.exceptions.Timeout:
        print("\n⏰ Erro: a conexão demorou muito para responder.")

    except requests.exceptions.ConnectionError:
        print("\n🌐 Erro: não foi possível conectar à internet.")

    except requests.exceptions.HTTPError:
        print("\n❌ Erro: não foi possível encontrar a cidade ou acessar a API.")

    except requests.exceptions.RequestException as erro:
        print(f"\n⚠️ Erro na requisição: {erro}")

    except ValueError:
        print("\n⚠️ Erro: a resposta recebida não está em formato JSON.")

    return None


# ========================================================
# FUNÇÃO PARA EXIBIR O CLIMA
# ========================================================

def mostrar_clima(dados):
    """
    Exibe os dados recebidos da API.
    """

    if dados is None:
        return

    try:
        cidade = dados["name"]
        pais = dados["sys"]["country"]

        temperatura = dados["main"]["temp"]
        sensacao = dados["main"]["feels_like"]
        temperatura_min = dados["main"]["temp_min"]
        temperatura_max = dados["main"]["temp_max"]

        umidade = dados["main"]["humidity"]

        descricao = dados["weather"][0]["description"]

        vento = dados["wind"]["speed"]

        print("\n" + "=" * 50)
        print("🌤️        PREVISÃO DO TEMPO")
        print("=" * 50)

        print(f"📍 Localização: {cidade} - {pais}")
        print(f"☁️ Condição: {descricao}")
        print(f"🌡️ Temperatura: {temperatura:.1f} °C")
        print(f"🌡️ Sensação térmica: {sensacao:.1f} °C")
        print(f"🔽 Temperatura mínima: {temperatura_min:.1f} °C")
        print(f"🔼 Temperatura máxima: {temperatura_max:.1f} °C")
        print(f"💧 Umidade: {umidade}%")
        print(f"💨 Vento: {vento} m/s")

        print("=" * 50)

    except KeyError:
        print("\n⚠️ Erro: alguns dados esperados não foram encontrados.")


# ========================================================
# MENU PRINCIPAL
# ========================================================

def menu():
    while True:

        print("\n" + "=" * 50)
        print("🌦️  SISTEMA DE PREVISÃO DO TEMPO")
        print("=" * 50)

        print("1 - Consultar clima")
        print("2 - Sair")

        print("=" * 50)

        opcao = input("Escolha uma opção: ")

        if opcao == "1":

            cidade = input("\n🏙️ Digite o nome da cidade: ").strip()

            if cidade == "":
                print("\n⚠️ Digite o nome de uma cidade.")
                continue

            dados = consultar_clima(cidade)

            mostrar_clima(dados)

        elif opcao == "2":

            print("\n👋 Programa encerrado.")
            break

        else:

            print("\n❌ Opção inválida.")


# ========================================================
# EXECUÇÃO
# ========================================================

if __name__ == "__main__":
    menu()
    
''''''