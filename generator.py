from itertools import permutations
from tqdm import tqdm
from colorama import Fore, Style, init

# Inicializar colorama para que los colores funcionen en Windows también
init()

print(Fore.CYAN + r"""
.___                             .__             .__                             .__       .__   
|   | ____    ____   ____   ____ |__| ___________|__|____      __________   ____ |__|____  |  |  
|   |/    \  / ___\_/ __ \ /    \|  |/ __ \_  __ \  \__  \    /  ___/  _ \_/ ___\|  \__  \ |  |  
|   |   |  \/ /_/  >  ___/|   |  \  \  ___/|  | \/  |/ __ \_  \___ (  <_> )  \___|  |/ __ \|  |__
|___|___|  /\___  / \___  >___|  /__|\___  >__|  |__(____  / /____  >____/ \___  >__(____  /____/
         \//_____/      \/     \/        \/              \/       \/           \/        \/      
""" + Fore.RESET)

def generar_permutaciones(elementos):
    # Generar todas las permutaciones posibles
    return [''.join(perm) for perm in permutations(elementos)]

def guardar_permutaciones(permutaciones, archivo='password.list'):
    # Guardar las permutaciones en un archivo
    with open(archivo, 'w') as f:
        for perm in tqdm(permutaciones, desc=f"{Fore.YELLOW}Guardando permutaciones{Style.RESET_ALL}", unit="perm"):
            f.write(f"{perm}\n")

def main():
    # Solicitar al usuario que ingrese los elementos separados por comas
    entrada = input(f"{Fore.YELLOW}Ingrese los elementos separados por comas (ejemplo: 09,septiembre,1941): {Style.RESET_ALL}")
    
    # Verificar si el usuario ingresó algo
    if not entrada:
        print(f"{Fore.RED}Error: No ha ingresado ninguna palabra.{Style.RESET_ALL}")
        return
    
    # Dividir la entrada en una lista de elementos
    elementos = entrada.split(',')
    
    # Calcular el número total de permutaciones posibles
    total_permutaciones = 1
    for i in range(1, len(elementos) + 1):
        total_permutaciones *= i
    
    print(f"{Fore.YELLOW}Generando {total_permutaciones} permutaciones...{Style.RESET_ALL}")
    
    # Generar las permutaciones con una barra de progreso
    permutaciones = []
    for i, perm in enumerate(tqdm(permutations(elementos), total=total_permutaciones, desc=f"{Fore.YELLOW}Generando permutaciones{Style.RESET_ALL}", unit="perm")):
        permutaciones.append(''.join(perm))
        print(f"{Fore.YELLOW}Creando posibles contraseñas: {i + 1} de {total_permutaciones}{Style.RESET_ALL}", end='\r')  # Contador
    
    # Guardar las permutaciones en el archivo
    guardar_permutaciones(permutaciones)
    
    print(f"{Fore.GREEN}\nSe han generado {len(permutaciones)} permutaciones y se han guardado en 'password.list'.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()