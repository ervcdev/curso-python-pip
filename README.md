# Game project

para correr el juego debes segir las siguientes instrucciones en la terminal:

```sh
cd game
python3 main.py
```
# creación de entornos virtuales

## crear el entorno virtual

```sh
python3 -m venv env
```

## activar el entorno virtual
```sh
source env/bin/activate
```

## desactivar el entorno virual
```sh
deactivate
```

## ver las librerias y paquetes instalados
```sh
pip3 freeze
```

## agregar todos las dependencias a requirements.txt

```sh
pip3 freeze >requeriments.txt
```
## instalar todas las depencias de requirements

```sh
pip3 install -r requirements.txt
```

# App Proyect

```sh
git clone
cd app
python3 -m venv env
source env/bin/activate
pip3 inst
all -r requirements.txt
python3 main.py

```
# Comandos para FastApi

```sh
pip3 install fastapi
```

## instalar uvicorn

```sh
pip3 install "uvicorn[standard]"
```

## lanzar el servidor

```sh
uvicorn main:app --reload
```

## Docker


```sh
docker-compose build
```

correr el docker que se creo
```sh
docker-compose up -d
```
ver el estado del contenedor
```sh
docker-compose ps
```

ingresar al contenedor creado
```sh
docker-compose exec app-csv bash

```

```sh

```


```sh

```





