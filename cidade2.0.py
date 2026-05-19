import requests

API_KEY = ""
cidade = input("Escolha a cidade (Ex.: Maua,BR): ").lower()

url = (
    f"https://api.openweathermap.org/data/2.5/weather"
    f"?q={cidade}&appid={API_KEY}&units=metric&lang=pt_br"
)

resposta = requests.get(url)
dados = resposta.json()


def classificar_clima(temperatura, umidade):
    if temperatura >= 28 and umidade >= 70:
        print("Equatorial")
    elif temperatura >= 22:
        print("Tropical")
    elif temperatura <= 12:
        print("Frio")
    else:
        print("Outro")

if resposta.status_code == 200:

    temperatura = dados["main"]["temp"]
    umidade = dados["main"]["humidity"]
    vento = dados["wind"]["speed"]

    tipo_clima = classificar_clima(temperatura, umidade)

    print(f"\nCidade: {cidade}")
    print(f"Temperatura: {temperatura} °C")
    print(f"Umidade: {umidade}%")
    print(f"Vento: {vento} m/s")
    print(f"Classificação do clima: {tipo_clima}")

else:
    print("Erro:", dados["message"])