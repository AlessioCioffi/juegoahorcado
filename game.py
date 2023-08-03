from random import *


class Juego:

    # Creamos el constructor
    def __init__(self):
        self.vidas = 6
        self.letras_correctas = []
        self.letras_incorrectas = []
        self.palabras = ['perro', 'carretera', 'python']
        self.letra = ''
        self.palabra = ''

    def seleccionar_palabra(self, palabras):
        self.palabra = choice(palabras)
        return self.palabra

    def elegir_letra(self):
        letra_correcta = False
        while not letra_correcta:
            self.letra = input('Elige una letra:\n').lower()
            if len(self.letra) != 1:
                print('Elige solo una letra o no lo dejes en blanco!')
            elif not self.letra.isalpha():
                print('Solo puede escribir letras!')
            elif self.letra in self.letras_correctas or self.letra in self.letras_incorrectas:
                print('Ya has llamado esta letra! Escoge otra!')
            else:
                letra_correcta = True

        return self.letra

    def comprobar_letra(self, letra, palabra):
        if letra in palabra:
            print('\nMuy bien!')
            self.letras_correctas.append(letra)
        else:
            self.vidas -= 1
            print(f'\nLa palabra no contiene esta letra.\nTe quedan {self.vidas} vidas!')
            self.letras_incorrectas.append(letra)

    def grafico_juego(self):
        grafico = []
        for letra in self.palabra:
            if letra in self.letras_correctas:
                grafico.append(letra)
            else:
                grafico.append('_')
        print("".join(grafico) + '\n')
        return grafico


start = Juego()
start.palabra = start.seleccionar_palabra(start.palabras)
largo = len(start.palabra)

print(f'''\nBinenvenido al juego del ahorcado!!! Comenzamos!!!\n
La lapalabra se compone de {largo} letras\n''')
espaciado = '*'*50+'\n'
print(espaciado)

while start.vidas > 0:
    start.letra = start.elegir_letra()
    start.comprobar_letra(start.letra, start.palabra)
    evolucio_juego = start.grafico_juego()
    print(espaciado)

    if "".join(evolucio_juego) == start.palabra:
        print('Felicidades! Has adivinado la palabra!!!')
        break

else:
    print(f'Game over! La palabra oculta era "{start.palabra}"!')


