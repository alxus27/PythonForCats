# -*- coding: utf-8 -*-
"""
Ejercicio nivel 4: Boletín Estadístico.
Módulo de funciones.

Temas:
* Recorridos de Matrices.
* Librerías de Matplotlib.

@author: zejiran
"""


def cargar_matriz_estadisticas(ruta_archivo: str) -> list:
    """
    Esta funcion carga la informacion de la matriz de estadísticas
    de las facultades a partir de un archivo CSV.
        ruta_archivo (str): la ruta del archivo que se quiere cargar
    Retorno: list
        La matriz con las estadisticas por facultad
    """
    archivo = open(ruta_archivo)
    linea = archivo.readline()
    facultades = 11
    elementos = 9
    estadisticas = list()
    for i in range(0, facultades + 1):
        estadisticas.append([0] * (elementos + 1))
    i = 0
    while len(linea) > 0:
        datos = linea.split(",")
        for j in range(0, elementos + 1):
            estadisticas[i][j] = datos[j].strip()
        i += 1
        linea = archivo.readline()
    archivo.close()
    return estadisticas


def cargar_matriz_puestos(ruta_archivo: str) -> list:
    """
    Esta funcion carga la informacion de la matriz de puestos estudiante 
    a partir de un archivo CSV.
        ruta_archivo (str): la ruta del archivo que se quiere cargar
    Retorno: list
        La matriz con los puestos estudiante de cada facultad
    """
    archivo1 = open(ruta_archivo)
    linea = archivo1.readline()
    oferentes = 11
    ocupantes = 12
    puestos = []
    for i in range(0, oferentes + 1):
        puestos.append([0] * (ocupantes + 1))
    i = 0
    while len(linea) > 0:
        datos = linea.split(",")
        for j in range(0, ocupantes + 1):
            puestos[i][j] = datos[j].strip()
        i += 1
        linea = archivo1.readline()
    archivo1.close()
    return puestos


def cargar_matriz_dobles(ruta_archivo: str) -> list:
    """
    Esta funcion carga la informacion de la matriz de dobles programas
    a partir de un archivo CSV.
        ruta_archivo (str): la ruta del archivo que se quiere cargar
    Retorno: list
        La matriz con los puestos estudiante de cada facultad
    """
    archivo2 = open(ruta_archivo)
    linea = archivo2.readline()
    programas = 35
    dobles = []
    for i in range(0, programas + 1):
        dobles.append([0] * (programas + 1))
    i = 0
    while len(linea) > 0:
        datos = linea.split(",")
        for j in range(0, programas + 1):
            dobles[i][j] = datos[j].strip()
        i += 1
        linea = archivo2.readline()
    archivo2.close()
    return dobles


def puestos_atendidos(matriz_puestos: list, facultad_interes: str) -> int:
    """
    Función 1 – Puestos estudiante ofrecidos (o atendidos) por una Facultad.

    :param matriz_puestos: la matriz de puestos estudiante.
    :param facultad_interes: facultad de interés.
    :return: retorna valor entero con la cantidad de puestos ofrecidos por dicha facultad.

    :type matriz_puestos: list.
    :type facultad_interes: str.
    :rtype: int.

    :Ejemplo: la Facultad de Economía atiende un total de 4107 puestos estudiante.
    """
    puestos_facultad = 0
    for fila in matriz_puestos:
        if fila[0].lower() == facultad_interes.lower():
            for columna in range(1, len(fila)):
                puestos_actual = fila[columna]
                puestos_facultad += int(puestos_actual)
    return puestos_facultad


def puestos_ocupados(matriz_puestos: list, facultad_interes: str) -> int:
    """
    Función 2 – Puestos estudiante ocupados por una Facultad.

    :param matriz_puestos: la matriz de puestos estudiante.
    :param facultad_interes: facultad de interés.
    :return: retorna la cantidad de puestos ocupados por estudiantes de dicha facultad.

    :type matriz_puestos: list.
    :type facultad_interes: str.
    :rtype: int.

    :Ejemplo: la Facultad de Educación ocupa un total de 185 puestos estudiante.
    """
    puestos_ocupados = 0
    for columna in range(1, len(matriz_puestos[0])):
        if matriz_puestos[0][columna].lower() == facultad_interes.lower():
            for fila in range(1, len(matriz_puestos)):
                puestos_actual = matriz_puestos[fila][columna]
                puestos_ocupados += int(puestos_actual)
    return puestos_ocupados


def facultad_mas_servicial(matriz_puestos: list) -> tuple:
    """ TODO
    Función 3 – Facultad más servicial.
    La facultad más servicial es aquella que atiende un mayor número de puestos estudiante de otras facultades,
    comparativamente con sus propios puestos estudiante atendidos.

    :param matriz_puestos: la matriz de puestos estudiante.
    :return: retorna una tupla con la información de la facultad más servicial.

    :type matriz_puestos: list.
    :rtype: tuple.

    :Ejemplo: a facultad de medicina atiende un total de 4444 puestos estudiante. De estos puestos,
    4318 son de estudiantes de medicina y tan solo 126 son de otras facultades. Por consiguiente,
    la relación puestos de otras facultades/puestos propios es: 126/4444 = 0.028. Esto quiere decir que solo el 2.83%
    de los puestos estudiante de la Facultad de Medicina son tomados por estudiantes de otras facultades.
    Es fácil deducir que Medicina no es la facultad más servicial, según esta definición.
    La primera posición de la tupla que retorna esta función debe ser el nombre de la facultad más servicial
    y la segunda posición de la tupla, el porcentaje de puestos estudiante de las demás facultades que son atendidos
    por dicha facultad (redondeado a dos decimales).
    """


def hay_facultad_generosa(matriz_puestos: list, facultad: str, porcentaje_puestos: float) -> tuple:
    """ TODO
    Función 4 – Existe facultad generosa.
    Indica si en la Universidad existe alguna facultad que atienda un porcentaje de puestos estudiante
    de la facultad de interés, que sea igual o superior al ingresado por parámetro.

    :param matriz_puestos: matriz de puestos estudiante.
    :param facultad: nombre de una facultad de interés.
    :param porcentaje_puestos: un porcentaje (valor real de 0 a 100) de puestos estudiante
    :return: retorna:
        - Tupla cuyo primer valor sea el nombre de la facultad encontrada, y el segundo valor sea el porcentaje
        de puestos estudiante cubiertos por dicha facultad (redondeado a 2 decimales).
        - En caso de que ninguna facultad atienda más de este porcentaje de puestos estudiante, la función debe retornar
        la tupla (“No existe facultad generosa”, 0).
        - En caso de que varias facultades sobrepasen este porcentaje,
        la función debe retornar la primera que encuentre.

    :type matriz_puestos: list.
    :type facultad: str.
    :type porcentaje_puestos: float.
    :rtype: tuple.

    :Ejemplo: supongamos que la facultad de interés es Medicina y el porcentaje recibido por parámetro es 5.
    Sabemos que la Facultad de Medicina ocupa un total de 6350 puestos estudiante. El 5 por ciento de este valor es 317.
    Esta función debe entonces buscar en la matriz de puestos, una facultad que atienda al menos
    317 puestos estudiante de medicina. La Facultad de Ciencias cumple con esta condición,
    ya que atiende 1179 puestos estudiante de Medicina, lo cual equivale al 18.57% del total de puestos estudiante
    de Medicina. La Facultad de Ciencias Sociales cumple igualmente con esta condición, ya que atiende 477 puestos
    estudiante de Medicina, lo cual equivale al 7.51% del total de puestos estudiante de Medicina. Esta función
    debe entonces retornar alguna de estas dos facultades, la que encuentre primero, junto con el
    porcentaje de atención correspondiente.
    """


def calcular_autocubrimiento(matriz_puestos: list, matriz_facultades: list) -> list:
    """ TODO
    Función 5 – Porcentaje de autocubrimiento.
    Calcula el porcentaje de autocubrimiento de todas las facultades.

    El porcentaje de autocubrimiento de una facultad X es definido de la siguiente manera:
    𝑎𝑢𝑡𝑜𝑐𝑢𝑏𝑟𝑖𝑚𝑖𝑒𝑛𝑡𝑜 𝑑𝑒 𝑋 = 𝑝𝑢𝑒𝑠𝑡𝑜𝑠 𝑒𝑠𝑡𝑢𝑑𝑖𝑎𝑛𝑡𝑒 𝑜𝑐𝑢𝑝𝑎𝑑𝑜𝑠 𝑝𝑜𝑟 𝑋 / 𝑝𝑢𝑒𝑠𝑡𝑜𝑠 𝑒𝑠𝑡𝑢𝑑𝑖𝑎𝑛𝑡𝑒 𝑜𝑓𝑟𝑒𝑐𝑖𝑑𝑜𝑠 𝑝𝑜𝑟 𝑋
    Después de calcular esta información para cada facultad de la universidad, se agrega una
    nueva columna a la matriz de información estadística de facultades, en la cual guardará el valor calculado
    para cada una de las facultades (redondeados a 2 decimales).
    Se pone como título de columna 'Porcentaje de autocubrimiento'.
    Si ya existía la columna no importa, de todas formas se agrega.

    :param matriz_puestos: la matriz de puestos estudiante.
    :param matriz_facultades: la matriz de estadísticas de facultades.
    :return: retorna la matriz de estadísticas modificada.


     :type matriz_puestos: list.
     :type matriz_facultades: list.
     :rtype: list.
    """


def doble_mas_comun(matriz_dobles: list) -> tuple:
    """ TODO
    Función 6 – Doble programa más popular.
    Indica cuál es el doble programa más popular entre los estudiantes.
    Es equivalente estar inscrito en el Programa1 y tener un doble programa con el programa2,
    que estar inscrito en el Programa2 y hacer doble con el Programa1.

    :param matriz_dobles: matriz de dobles programas.
    :return: retorna una tupla, cuya primera posición es una cadena de caracteres de la forma “Programa1 – Programa2”
    y la segunda posición es el número de estudiantes que cursan este doble programa.

    :type matriz_dobles: list.
    :rtype: tuple.

    :Ejemplo: Hay 15 estudiantes inscritos en Ingeniería Mecánica y que están cursando Diseño como segundo programa.
    Por otra parte, hay 1 estudiante de Diseño, cursando Ingeniería Mecánica como segundo programa.
    Por consiguiente el doble programa “Ing. Mecanica – Diseño” cuenta con 16 estudiantes.
    """


def dobles_de_un_programa(matriz_dobles: list, programa_interes: str) -> dict:
    """ TODO
    Función 7 – Dobles programas con un programa de interés.
    Es equivalente estar inscrito en el Programa1 y hacer un doble programa con el programa2,
     que estar inscrito en el Programa2 y hacer doble programa con el Programa1.

    :param matriz_dobles: matriz de dobles programas.
    :param programa_interes: nombre de un programa de interés.
    :return: diccionario, cuyas llaves son los nombres de todos los programas diferentes al programa de interés
    y los valores de cada llave, son el número de personas que realizan dicho doble programa
    (siempre y cuando este número sea mayor a cero).

    :type matriz_dobles: list.
    :type programa_interes: str.
    :rtype: dict.

    :Ejemplo: si el programa de interés es Geociencias, esta función debe retornar un diccionario con las
    siguientes parejas llave-valor:
    {'Administracion': 1, 'Musica': 1, 'Biologia': 5, 'Fisica': 12, 'Quimica': 1, 'Antropologia': 1,
    'Ciencia Politica': 1, 'Historia': 1, 'Lenguas y Cultura': 1, 'Derecho': 1, 'Gobierno y A. Publicos': 2,
    'Ing. Ambiental': 13, 'Ing. Civil': 36, 'Ing. Electronica': 1,
    'Ing. Industrial': 2, 'Ing. Mecanica': 5, 'Ing. Quimica': 2}
    """


def estadisticas_pga(matriz_estadisticas: list) -> list:
    """ TODO
    Función 8 – Estadísticas del PGA.

    :param matriz_estadisticas: matriz de estadísticas.
    :return: lista con 3 tuplas, que corresponden respectivamente a:
        - La facultad con mayor PGA promedio.
        - La facultad con menor PGA promedio.
        - La facultad con el PGA promedio igual a la mediana de los PGA de todas las facultades.
    Cada tupla tiene 2 posiciones, en la primera posición debe ir el nombre de la facultad
    y en la segunda posición su PGA promedio.

    :type matriz_estadisticas: list.
    :rtype: list.
    """


def hay_facultad_con_porcentaje_estudiantes(matriz_estadisticas: list, genero: str, porcentaje: float) -> tuple:
    """ TODO
    Función 9 – Existe facultad con un determinado porcentaje de estudiantes de un género dado.
    Indica si existe alguna facultad, que tenga un porcentaje de estudiantes
    del género dado por parámetro superior al porcentaje dado.

    :param matriz_estadisticas: matriz de estadísticas.
    :param genero: una cadena que represents un género de la forma “mujer”/”hombre”.
    :param porcentaje: un porcentaje (valor real entre 0 y 100).
    :return: tupla de 3 posiciones.
        - La primera posición sea True o False, según se haya encontrado o no una facultad con dicha característica.
        - La segunda posición el nombre de la facultad, o la cadena vacía en caso de no encontrar ninguna.
        - La tercera posición el porcentaje que supera al ingresado por parámetro, o 0 en caso de que no se haya
         encontrado ninguna facultad.
         En caso de que varias facultades sobrepasen este porcentaje, la función debe retornar la primera que encuentre.

    :type matriz_estadisticas: list.
    :type genero: str.
    :type porcentaje: float.
    :rtype: tuple.

    :Ejemplo: Supongamos que los parámetros de entrada son: “femenino” (para el género) y 60 (para el porcentaje).
    En este caso estamos preguntando al programa si existe al menos una facultad que tenga más del 60% de
    estudiantes mujeres. La función debe entonces calcular, para cada facultad, la cantidad total de
    estudiantes (teniendo en cuenta tanto hombres como mujeres) y el porcentaje de estudiantes mujeres
    con respecto a este total. Posteriormente, debe buscar si existe alguna facultad, cuyo porcentaje
    de estudiantes mujeres sea superior al 60%. La Facultad de Arquitectura y Diseño, así como la Facultad de
    Ciencias Sociales cumplen con esta condición. La primera con un 64.04% de estudiantes mujeres y la segunda
    con un 65.68%. Esta función debe entonces retornar alguna de estas dos facultades, la que encuentre primero,
    junto con True y el porcentaje de mujeres correspondiente.
    """
