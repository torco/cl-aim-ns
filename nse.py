import pandas as pd
import os, pathlib
x = pathlib.Path(__file__).parent.resolve()
os.chdir(x)

tabla = pd.read_csv('nse1.csv').astype(str)
tabla2 = pd.read_csv('nse2.csv')

def get(ingreso, personas, neduc, ocup):
    #turn all the inputs into integers if they were given as floats or whatever. 
    personas = int(personas)
    ingreso = int(ingreso)
    neduc = int(neduc)
    ocup = int(ocup) 
    #this is because that's how the AIM tables work
    if personas > 7:
        personas = 7
    #let's think in thousands of pesps
    ingreso = ingreso/1000-0.5
    #only select the rows that correspond to the number of people
    s1 = tabla2[tabla2.personas == personas]
    # get the 'tramo de ingreso'
    s2 = s1[(ingreso > s1.lower)&(ingreso <= s1.upper)]
    percap = list(s2.tramo)[0]
    neduc = str(neduc)
    ocup = str(ocup)
    #applies a filter to the table
    for index, item in tabla.iterrows():
        tabla.at[index,'fil']=(neduc in item.neduc.split(','))&(ocup in item.ocup.split(','))
    k = tabla[tabla.fil]
    #get the column corresponding to the 'tramo de ingreso'. since we should 
    #only at this point have one row, this yields on cell. 
    colname = f"yper_{percap}"
    cell = list(set(k[colname]))
    return cell[0].capitalize()

def ayuda():
    g = """
    
MANUAL
    
Usa la función nse.get() para obtener el nivel socioeconomico de una persona u
hogar. esta funcion toma cuatro parametros: ingreso, personas, neduc y ocup.
    
ingreso(int): en pesos chilenos, cuanto es el ingreso del hogar. 
    
personas(int): cuántas personas tiene el hogar.
    
neduc(int): el nivel educacional del principal sostenedor del hogar. la clave es la siguiente:
    
    1. Sin estudios formales
    2. Básica incompleta; primaria o preparatoria incompleta
    3. Básica completa; primaria o preparatoria completa
    4. Media científico humanista o media técnico profesional incompleta; humanidades
    incompletas
    5. Media científico humanista o media técnico profesional completa; humanidades
    completas
    6. Instituto técnico (CFT) o instituto profesional incompleto (carreras de 1 a 3 años)
    7. Instituto técnico (CFT) o instituto profesional completo (carreras de 1 a 3 años); hasta
    suboficial de FFAA y Carabineros
    8. Universitaria incompleta (carreras de 4 o más años)
    9. Universitaria completa (carreras de 4 o más años); oficial de FFAA y Carabineros
    10. Postgrado (postítulo, master, magíster, doctor)

ocup(int): la ocupacion del principal sostenedor del hogar. la clave es la siguiente:

    1. Trabajadores no calificados en ventas y servicios, peones agropecuarios, forestales, construcción, etc
    2. Obreros, operarios y artesanos de artes mecánicas y de otros oficios
    3. Trabajadores de los servicios y vendedores de comercio y mercados
    4. Agricultores y trabajadores calificados agropecuarios y pesqueros
    5. Operadores de instalaciones y máquinas y montadores / conductores de vehículos
    6. Empleados de oficina públicos y privados
    7. Técnicos y profesionales de nivel medio (incluye hasta suboficiales FFAA y
    Carabineros)
    8. Profesionales, científicos e intelectuales
    9. Alto ejecutivo (gerente general o gerente de área o sector) de empresa privadas o
    públicas. Director o dueño de grandes empresas. Alto directivo del poder ejecutivo,
    de los cuerpos legislativos y la administración pública (incluye oficiales de FFAA y
    Carabineros)
    10. Otros grupos no identificados (incluye rentistas, incapacitados, etc.)
    
Así, si tienes un sujeto, por ejemplo, que dice que a su hogar entran al mes 900 mil pesos,
vive con su señora y su hermano, él es el principal sostenedor del hogar, trabaja de uber
y estudió periodismo, tendrías que usar algo como:

nse.get(ingreso=900000,personas=3,neduc=9,ocup=5)
nse.get(9e5, 3, 9, 5)

>>> 'C2'

    """
    print(g)