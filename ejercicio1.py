# Importamos el xml
import xml.etree.ElementTree as ET

# Funcion del XML Students
def students():
    # Crear el elemento padre "students"
    padre = ET.Element('students')
    # Recorreger 5 veces el hijo student con sus subhijos
    for i in range(5):
        # Incrementar el id por cada students que haya
        i += 1
        # Crear el elemento hijo "student"
        hijos = ET.SubElement(padre, "student")
        # Agregar un atributo (id y lo vamos incrementando)
        hijos.set('id', str(i))
        # Agregamos los subhijos name surname email y dni
        subHijoN = ET.SubElement(hijos, 'name')
        subHijoS = ET.SubElement(hijos, 'surname')
        subHijoE = ET.SubElement(hijos, 'email')
        subHijoD = ET.SubElement(hijos, 'dni')

    # Añadir nombre al elemento name
    padre[0].find("name").text = "Jonathan"
    padre[1].find("name").text = "Maravillas"
    padre[2].find("name").text = "Emilio"
    padre[3].find("name").text = "Estrella"
    padre[4].find("name").text = "Evaristo"

    # Añadir el apellido al elemento surname
    padre[0].find("surname").text = "Valle"
    padre[1].find("surname").text = "Perez"
    padre[2].find("surname").text = "Marrero"
    padre[3].find("surname").text = "Rio"
    padre[4].find("surname").text = "Betancon"

    # Añadir el email al elemento email
    padre[0].find("email").text = "jvalle@jaumebalmes.net"
    padre[1].find("email").text = "maravillasPerez@jaumebalmes.net"
    padre[2].find("email").text = "emilioMarrero@jaumebalmes.net"
    padre[3].find("email").text = "estrellaRio@jaumebalmes.net"
    padre[4].find("email").text = "EvaristoBet@jaumebalmes.net"

    # Añadir el dni al elemento dni
    padre[0].find("dni").text = "26634404J"
    padre[1].find("dni").text = "56970932R"
    padre[2].find("dni").text = "57689547G"
    padre[3].find("dni").text = "86939702R"
    padre[4].find("dni").text = "23796572J"

    # Indentación de los elementos
    ET.indent(padre)
    # Mostrar por consola
    ET.dump(padre)
    # Escribimos como queda el archivo XML
    tree = ET.ElementTree(padre)
    # Escribir en el archivo students.xml (Si no esta creado lo crea automaticamente)
    tree.write('students.xml')
# Llamamos a la funcion
students()
