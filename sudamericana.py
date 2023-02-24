import requests
import matplotlib.pyplot as plt

url = "https://restcountries.com/v3.1/region/south%20america"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    countries = []
    populations = []
    for country in data:
        countries.append(country["name"]["common"])
        populations.append(country["population"])

    # Imprimir datos de la población en la consola
    for i in range(len(countries)):
        print(f"{countries[i]}: {populations[i]}")

    # Gráfico de barras
    fig, (ax1, ax2) = plt.subplots(1, 2)

    ax1.bar(countries, [pop / 1000000 for pop in populations])
    ax1.set_xticklabels(countries, rotation=90)
    ax1.set_ylabel("Población (millones)")
    ax1.set_title("Población de los países de Sudamérica")

    # Gráfico de torta
    ax2.pie(populations, labels=countries, autopct='%1.1f%%', radius=1.2, labeldistance=1.05)
    ax2.set_title("Distribución de la población en Sudamérica")

    # Guardar la figura en un archivo PNG
    plt.savefig("graficos_sudamerica.png", dpi=300, bbox_inches="tight")

    plt.show()
else:
    print("Error al obtener los datos de la API")
