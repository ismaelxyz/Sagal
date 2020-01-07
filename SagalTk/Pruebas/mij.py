# json 
# dumps (Recive una cadena y la trasforma de python a json)
# loads (Recive una cadena y la trasforma de json a python)

import argparse


letra = "\u00f1"
numero = "0xA"
"\N{GREEK CAPITAL LETTER THETA}"
"\N{LATIN SMALL LETTER E}"

def sopa(algo):
    print(algo, "Z")

def licencia():
    print("GPL")

"""parser = argparse.ArgumentParser(prog="Sagal", description='Process some integers.')

parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')

parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))"""

parser = argparse.ArgumentParser(prog="Sagal", description='Sagal (Soberania Global).')

parser.add_argument('strins', metavar='M', type=str,
                    help='El modo con el que desea iniciar la interacción:')

parser.add_argument('--modo', action='store_const',
                    const=sopa, dest='funcion',
                    help='Iniciar Sagal en el modo deseado')

parser.add_argument('--lice', action='store_const',
                    const=licencia, dest='activar',
                    help='Ver la licencia del programa.')

args = parser.parse_args()
# args.accumulate(args.strins)

args.funcion(args.strins)