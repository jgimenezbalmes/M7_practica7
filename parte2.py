import json

# Funcion para cargar Datos
def cargarDatos():
    datas = """
    {
    "book": [
    {
      "titel":  "El Club de las 5 AM",
      "cover":  "Personas",
      "year":   1995,
      "pages":  326
    },
    {
      "titel":  "Cien Año de Soledad",
      "cover":  "100 perros",
      "year":   1976,
      "pages":  389
    },
    {
      "titel":  "El Lobo Estepario",
      "cover":  "Lobo",
      "year":   1956,
      "pages":  240
    },
    {
      "titel":  "Narnia",
      "cover":  "El Armario",
      "year":   1996,
      "pages":  295
    }
  ]
}
"""
    # Metodo para guardar nuestra informacion escrita a un archivo externo
    with open("jsonFile.json", 'w') as file:
        # Indicamos que la informacion guardada en la variable data, sera transalada al archivo creado
        json.dump(datas, file)


cargarDatos()

# Funcion para Leer JsonFile
def llegeixi():
    # Metodo para abrir en consola nuestro json en orden
    with open("jsonFile.json", 'r') as file:
        result = json.load(file)
        print(result)

llegeixi()