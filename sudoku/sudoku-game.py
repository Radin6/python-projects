# Imports
import random
import copy

# Function 1 - Imprime el array 9x9 que se le pase
def imprim(sudoP):

    print('=====================') # Separador
    for fila in range(9):
        if fila == 3 or fila == 6:
                print('---------------------') # Separador de 1/3 y 2/3
        for columna in range(9):
            if columna == 3 or columna == 6:
                print('|', end =' ')
            print(sudoP[fila][columna], end =' ')
        print('')
    print('=====================') # Separador

# Function 2 - Verifica que el número a colocar no se encuentre en la fila y columna
def verif_FC(sudoFC, filaFC, columnaFC, nFC):
     
    veri = True
    for x in range(9):
        if sudoFC[filaFC][x] == nFC or sudoFC[x][columnaFC] == nFC:
            # Da resultado falso si encuentra el mismo número nFC en la fila o columna
            veri = False
    
    return veri                   

# PART 0 - Iniciamos

# Iniciar/Borrar a 0 el sudoku 9x9
sudo = [[0 for fila in range(9)] for columna in range(9)]

# Iniciamos y definimos
n = 0
fila = 0
columna = 0
intentos = 0
# Se puede modificar los intentos máximos
intMax = 30
intMaxBreak = False

# PART 1 - LLenar un tablero de forma correcta con todos los números

# Aveces se llega a completar hasta una cierta etapa el sudoku y no tiene solución posible
# Entonces hay que reiniciarlo a 0 y volver a intentar llenarlo
# Por eso cuando los [intentos] alcanzan a los intentos máximos [intMax] cortamos el bucle con intMaxBreak = True
while True:
    
    # Iniciamos a 0 el sudoku en el caso que sea la segunda o más veces que se intenta
    # Iniciamos la variable de intentos máximos a False, 
    intMaxBreak = False
    sudo = [[0 for fila in range(9)] for columna in range(9)]

    # Llena los 9 números necesarios n=[1,2,3,4,5,6,7,8,9], cuando completa los 9 unos(1), pasa a los 9 dos(2) y así...
    for n in (range(1,10)):
        # En los 2 siguientes for lo que se hace es pasar por las 9 cuadrículas de 3x3 y para poner solo 1 número [n] por cuadrícula
        for x3 in range(0,7,3):
            for y3 in range(0,7,3):

                # Cada vez que salta a otra cuadrícula de 3x3 necesitamos reiniciar los intentos para que no se acumulen
                intentos = 0

                # El tipo de llenado de [n] que hacemos es aleatorio
                while True:
                    # Se busca posiciones aleatorias
                    fila = random.randint(0,2) + x3
                    columna = random.randint(0,2) + y3

                    # Se verifica que esa posición sea 0 y el número [n] no se encuentre en la fila y columna con la función [verif_FC]
                    if sudo[fila][columna] == 0 and verif_FC(sudo, fila, columna, n) == True:
                        
                        # Se dan las condiciones anteriores y se procede a colocar el número
                        sudo[fila][columna] = n
                        break

                    elif intentos == intMax:
                        # se alcanzaron los intentos máximos, suponemos que no hay solución y queremos reiniciar todo el ciclo 
                        intMaxBreak = True
                        break
                    else:
                        intentos = intentos + 1

    # Si no se llegó al número de intento máximos suponemos que se resolvió y salimos con break
    if intMaxBreak == False:
        break

# PART 2 - Ya tenemos la solución, resta quitar los números para que el jugador adivine

dificultad = int(input('Elije tu dificultad [ 0=Super Fácil | 1=Fácil | 2=Moderado | 3=Dificil ]: '))
num_sacar = 0

if dificultad == 1:
    num_sacar = 5
elif dificultad == 2:
    num_sacar = 6
elif dificultad == 3:
    num_sacar = 7
elif dificultad == 0:
    num_sacar = 2

# Sudo es el tablero ya resuelto por lo tanto la solución
# Copio a sudo como sudoJ
# A sudoJ se le van a esconder algunos números para que el usuario puede jugar y adivinar cuales son
# Si al final sudoJ (completado) es igual a sudo se gana el juego
sudoJ = copy.deepcopy(sudo)


for n in (range(num_sacar)):
        # En los 2 siguientes for lo que se hace es pasar por las 9 cuadrículas de 3x3 y para poner solo 1 número [n] por cuadrícula
        for x3 in range(0,7,3):
            for y3 in range(0,7,3):

                while True:
                    # Se busca posiciones aleatorias
                    fila = random.randint(0,2) + x3
                    columna = random.randint(0,2) + y3

                    if sudoJ[fila][columna] != 0:
                        
                        # Se dan las condiciones anteriores y se procede a colocar el número
                        sudoJ[fila][columna] = 0
                        break

# PART 3 - Jugar e ir comprobando que los número son correctos
fila = 0
columna = 0
num = 0

max_intentos = 3 # Máximo de equivocaciones que permite el juego
intentos_jugados = 0
imprim(sudoJ)

while True:
    print('¿Cuál es tu siguiente jugada?')
    fila = 0
    columna = 0
    num = 0

    # Asegura que [fila] esté entre 1 y 9 incluidos
    while fila not in range(1,10):
        try:
            fila = int(input('Fila [1-9]: '))
            if fila not in range(1,10):
                print('Valor introducido incorrecto, elija un numero del 1 al 9')
        except:
            print('Valor introducido incorrecto, elija un numero del 1 al 9')

    # Asegura que [columna] esté entre 1 y 9 incluidos
    while columna not in range(1,10):
        try:
            columna = int(input('Columna [1-9]: '))
            if columna not in range(1,10):
                print('Valor introducido incorrecto, elija un numero del 1 al 9')
        except:
            print('Valor introducido incorrecto, elija un numero del 1 al 9')

    # Asegura que [num] esté entre 1 y 9 incluidos
    while num not in range(1,10):
        try:
            num = int(input('Número[1-9]: '))
            if num not in range(1,10):
                print('Valor introducido incorrecto, elija un numero del 1 al 9')
        except:
            print('Valor introducido incorrecto, elija un numero del 1 al 9')
    
    # Se los resta porque la fila 1 en el array es 0
    fila -= 1
    columna -= 1

    # Se comprueba que el número elegido en la posición elegida es el correcto
    if sudo[fila][columna] == num:
        sudoJ[fila][columna] = num
        print(' ')
        print('ACERSTASTE')
        imprim(sudoJ)
        if sudoJ == sudo:
            print('##################################')
            print('Felicitaciones, GANASTE la partida')
            print('##################################')
            break
    else:
        intentos_jugados = intentos_jugados + 1
        print('Fallaste')
        if intentos_jugados == max_intentos:
            print('###################################')
            print('Usaste todos tus intentos. PERDISTE')
            print('###################################')
            break
