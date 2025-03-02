### README.md

```markdown
# Script de Fuerza Bruta y Generación de Permutaciones

Este repositorio contiene dos scripts principales:

1. **Script de Fuerza Bruta (password_cracker.py)**: Este script utiliza Selenium para probar una lista de contraseñas en una página de inicio de sesión de Google.
2. **Script de Generación de Permutaciones (generator.py)**: Este script genera todas las permutaciones posibles de una lista de elementos y las guarda en un archivo (password.list) para su uso en el script de fuerza bruta.

## Requisitos

- Python 3.x
- Selenium
- tqdm
- colorama

## Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/frankmiller-crypto/ingenieria_social.git
   cd ingenieria_social
   ```

2. Instala las dependencias necesarias:

   ```bash
   pip install -r requirements.txt
   ```

3. Descarga el `chromedriver` compatible con tu versión de Chrome y colócalo en la carpeta `chromedriver` dentro del proyecto.

## Uso

### Script de Fuerza Bruta

1. Asegúrate de tener un archivo `password.list` con las contraseñas que deseas probar.
2. Ejecuta el script:

   ```bash
   python password_cracker.py
   ```

### Script de Generación de Permutaciones

1. Ejecuta el script:

   ```bash
   python generator.py
   ```

2. Ingresa los elementos separados por comas cuando se te solicite. Por ejemplo:

   ```
   Ingrese los elementos separados por comas (ejemplo: 09,septiembre,1941): 09,septiembre,1941
   ```

3. Las permutaciones generadas se guardarán en el archivo `password.list`.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request si tienes alguna mejora o corrección.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.
```

### requirements.txt

```plaintext
selenium==4.1.0
tqdm==4.62.3
colorama==0.4.4
```

### Notas adicionales

- Asegúrate de que el `chromedriver` esté en la ruta correcta y que sea compatible con la versión de Chrome que tienes instalada.
- El archivo `password.list` debe contener una lista de contraseñas, una por línea, para que el script de fuerza bruta funcione correctamente.
- Si deseas ejecutar el navegador en modo headless (sin interfaz gráfica), descomenta la línea `# options.add_argument('--headless')` en el script de fuerza bruta.

¡Espero que esto te sea útil! Si tienes alguna otra pregunta, no dudes en preguntar.