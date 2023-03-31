# cl-aim-ns

En Chile, sobre todo en estudios de mercado, encuestas de opinión pública y otras aplicaciones de ciencias sociales es muy común ocupar la tipología AIM (Asociación de Investigadores de Mercado y Opinión Pública) de niveles socioeconómicos para categorizar a las personas: esta organiza a las personas, de mayor a menor 'nivel socioeconómico', en los grupos AB, C1a, C2b, C2, C3, D y E, donde AB significa básicamente gerentes, ejecutivos y dueños de empresas que ganan decenas de millones de pesos y tienen educacion universitaria, y D y E representan a cerca de la mitad de la población nacional, con unos ingresos cercanos a la mediana y ocupaciones menos académizadas y prestigiosas. A pesar de que el concepto de "nivel socioeconómico" es altamente cuestionable, es el estándar que se utiliza en diferentes industrias y, por lo tanto, tiene sentido que exista una herramienta para calcularlo de manera rápida y fácil. En el fondo, este paquete te entrega una funcion a la que le pasas el ingreso, cantidad de personas del hogar, ocupación y nivel edudacional del principal sostenedor del hogar, y te devuelve la categoría de NSE a la que la persona o el hogar pertenecen. Como no encontré una herramienta así en internet, es posible que esta herramienta exista, pero como no la encontré, la programé. 

MANUAL

Baja el repositorio y ponlo en el directorio en que lo vayas a ocupar (no es un módulo o una librería, no se instala con pip install, es una simple carpeta con un script y dos .csv), y luego lo importas con 

    from nsclaim import nse

Usa la función nse.get() para obtener el nivel socioeconomico de una persona u
hogar. esta funcion toma cuatro parametros: ingreso, personas, neduc y ocup.

También puedes usar la funcion nse.ayuda() para ver este mismo manual de uso. 
    
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

Así, si tienes un sujeto, por ejemplo, que dice que a su hogar entran al mes 900 mil pesos, vive con su señora y su hermano, él es el principal sostenedor del hogar, trabaja de uber y estudió periodismo, tendrías que usar:

    nse.get(ingreso=900000,personas=3,neduc=9,ocup=5)

o simplemente

    nse.get(9e5, 3, 9, 5)

y esa función te devolvería el NSE correspondiente: en este caso C2 (esta librería fué escrita en 2023). Lo normal sería usarla iterando a lo largo de una lista de personas. 
