# Manejo de FastApi

```sh
py -m venv env
pip install fastapi
pip install uvicorn
pip freeze > requeriments.txt
uvicorn main: app --reload
```

# Para trabajar con la API en el movil

```sh
uvicorn main:app --reload --port[el que desees] --host 0.0.0.0
```
Para poder trabajar con la API en el celular debes buscar la direccion de tu IPv4 en tu pc y escribirla en el celular con el puerto que escogiste