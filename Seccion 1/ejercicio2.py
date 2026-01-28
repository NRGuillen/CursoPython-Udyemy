"""La tarea consiste en crear un archivo llamado programa_manejo_de_nombres.py de la siguiente manera:

Se requiere desarrollar un programa que contenga los nombres de tres integrantes de tu familia o amigos como variables.

Se pide que por cada nombre de la persona se cree una nueva variable de tipo string, tomando el segundo carácter del
nombre convertido en mayúscula, seguido de un punto (.) y los dos últimos caracteres del nombre.

Por ejemplo, para el nombre Andres debe quedar como N.es.

Debe mostrar como resultado los tres nuevos nombres separados con un guion bajo (_), formando una única cadena.

Por ejemplo, un resultado final esperado para los nombres Andres, Maria y Pepe podría ser:

N.es_A.ia_E.pe"""
from turtledemo.penrose import start


def main():
    integrante1 = 'Ruben'
    integrante2 = 'Adolfo'
    integrante3 = 'Jorge'

    integrantes_final = ''

    """
    R u b e n
    0 1 2 3 4
    -5 - 4 - 3 - 2 - 1
    """

    integrantes_final += integrante1[1:2].upper()+'.' + integrante1[- 2:] +'_'
    integrantes_final += integrante2[1:2].upper()+'.' + integrante2[- 2:] +'_'
    integrantes_final += integrante3[1:2].upper()+'.' + integrante3[-2:]

    print(integrantes_final)

if __name__ == '__main__':
    main()