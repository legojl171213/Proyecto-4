import requests #se utiliza para realizar solicitudes HTTP a servidores web
import pandas as pd #Libreria para manipulación y el análisis de datos
import matplotlib.pyplot as plt #Para mostrar imagen
from PIL import Image #Para trabajar con imagenes
from urllib.request import urlopen #Para abrir el contenido de una URL

pokemon = input ("introduce el nombre de un pokemon: ") #Ingreso de datos
url="https://pokeapi.co/api/v2/pokemon/" + pokemon #buscas en la api con el url el nombre del poquemon que ingresaste en la variable
response = requests.get(url) #obtienes el resultado de la busqueda y lo almacenas en una variable

if response.status_code == 200: #conexión exitosa

    pokemon_info = response.json() #Obtenemos la información de PokéAPI nombre, movimientos, habilidades y tipos
    name = pokemon_info['name']
    moves = pokemon_info['moves']
    abilities = pokemon_info['abilities']
    types = pokemon_info['types']
    
    try :   #Obtenemos la url de la imagen del pokémon y abrimos su contenido
        url_sprite = pokemon_info['sprites']['front_default']
        sprite = Image.open(urlopen(url_sprite))
    except :    #en dado caso que no tenga imagen dará este mensaje
        print('El pokemon no tiene imagen')
        exit()
    
    plt.title(name) 
    imgplot = plt.imshow(sprite)
    plt.show()  # muestra la imagen del pokémon

    info = {    #se obtiene información general del pokémon
                    'id' :  pokemon_info['id'],
                    'Nombre' : pokemon_info['name'],
                    'Peso' : pokemon_info['weight'],
                    'Tamaño' : pokemon_info['height'],
                }  
   
    df_pokemon = pd.json_normalize(info) #Con ayuda de la libreria pandas se crea un data frame para mostrar los datos ordenados
    print(df_pokemon)
   
    print('Movimientos de ' + name + ':') 
    for i in range (int(len(moves))) :      #al ser varios movimientos, habilidades y tipos... con ayuda de un ciclo for se leen todos los datos
        move = moves[i]['move']['name']
        print(move) 
    
    print('Habilidades:')
    for i in range (int(len(abilities))) :
        ability = abilities[i]['ability']['name']
        print(ability) 
    
    print('Tipos:')
    for i in range (int(len(types))) :
        type = types[i]['type']['name']
        print(type)
            
else: #Conexión fallida
    print("pokemon no encontrado") 
    exit()

