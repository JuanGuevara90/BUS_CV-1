# Detector de Rostros en un Bus

### Directorios importantes:
* database ->Conexion con la BD , operaciones y archivo de BD.
* deteccion -> detectorRostroVideo.py / Algoritmo de OpenCV
* serial -> Comuncación con arduino
* utiles -> getDateCurrent.py / Fecha actual del sistema
* ini.py -> Punto de Inicio del programa
* controlador.py -> Archivo que maneja la lógica del programa
### Lenguajes usados:

* Python 

### Librerias:
* OpenCV
* Sqlite3
* serial
* DotEnv

### Comandos Jetson Nano
> **Nota**: Abrir un terminal y ejecutar cada comando / dentro del raspberry/src.
#### 1. Activar ambiente
```bash
$ source tf/bin/activate
```
#### 2. Ruta del proyecto
```bash
$ cd /home/iw/tensorflow1/models/research/object_detection
```
#### 3. Comando para ejecutar
```bash
$ python -m raspberry.ini      
```

