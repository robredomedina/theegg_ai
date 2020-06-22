import random
import itertools

deck = list(itertools.product(range(1,14), ['Spades', 'Diamonds', 'Clubs', 'Hearts']))
deck.append('comodin A')
deck.append('comodin B')


def separar_en_tokens(n, mensaje):

    mensaje = mensaje.strip()
    mensaje = mensaje.replace(" ", "")
    
    lista_tokens = [mensaje[i:i+n] for i in range(0, len(mensaje), n)]
    if len(lista_tokens[-1]) < n:
        lista_tokens[-1] += ("x"* (int(n)-len(lista_tokens[-1]))) 
    
    print(lista_tokens)
    return lista_tokens

def solitario(mensaje):
    pass
    # usa solitario para generar ristra de letras
    random.shuffle(deck)
    indexA = deck.index('comodin A')
    if indexA == 54:
        out = deck.pop()
        deck.insert(1, out)
    else:
        temp = deck[indexA]
        deck[indexA] = deck[indexA + 1]
        deck[indexA + 1] = temp

    indexB = deck.index('comodin B')
    if indexB == 54:
        out = deck.pop()
        deck.insert(3, out)
    else:
        temp = deck[indexA]
        deck[indexA] = deck[indexA + 1]
        deck[indexA + 1] = temp



def convertir_a_numeros(mensaje):
    
    diccionario = {
            'a': 1,
            'b': 2,
            'c': 3,
            'd': 4,
            'e': 5,
            'f': 6,
            'g': 7,
            'h': 8,
            'i': 9,
            'j': 10,
            'k': 11,
            'l': 12,
            'm': 13,
            'n': 14,
            'o': 15,
            'p': 16,
            'q': 17,
            'r': 18,
            's': 19,
            't': 20,
            'u': 21,
            'v': 22,
            'w': 23,
            'x': 24,
            'y': 25,
            'z': 26}

    mensaje_en_numeros = []
    for grupo in mensaje:
        letras = [letra for letra in grupo]        
        numeros = [diccionario.get(letra) for letra in letras]

        mensaje_en_numeros.append(numeros)
    print(mensaje_en_numeros)        
    return mensaje_en_numeros



def sumar_mensajes(mensaje1, mensaje2):
    pass
grupos_tokens = separar_en_tokens(5, "este es mi canaario, te guste o no")
codificado = solitario(mensaje) 
codificado_tokens = separar_en_tokens(5, codificado) 
original_numeros = convertir_a_numeros(grupos_tokens)
codificado_numeros = convertir_a_numeros(codificado_tokens)


#1. separar_en_tokens
#2. solitario
#3. convertir_a_numeros(mensaje)
#4. convertir_a_numeros(mansaje_cifrado)

