from fastapi import FastAPI,Body,Path,Query
from fastapi.responses import HTMLResponse, JSONResponse # JSON : Enviar contenido en formato Json hacia el cliente
from pydantic import BaseModel, Field
from typing import Optional,List

app = FastAPI()
app.title = 'Mi aplicacion con FastAPI'

app.version = '0.0.1'


class Movie(BaseModel):   # ge = mayor o igual   le : menor o igual
                          # min_length : minimo de caracteres  max_length : maximo de caracteres 
    id: Optional[int]=None
    title: str = Field(min_length=15, max_length=25)
    overview: str = Field(min_length=40, max_length=60)
    year:int = Field(led=2022)
    rating: float = Field(ge=1, le=10)
    category: str = Field(min_length=10, max_length=15)
    
    class Config:
        
        schema_extra={
            "example":{
            'id': 1,
            'title': 'Mi pelicula',
            'overview': 'Descripcion de la pelicula',
            'year':2022,
            'rating': 8.3,
            'category': 'Categoria de la pelicula'
        }
    }

movies= [
     {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    },
    {
        'id': 2,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    } 
]

# 
@app.get('/',tags=['home'])
def message():
    return HTMLResponse('<h1>Hello world</h1>')

# Obtenemos la lista de peliculas agregadas de manera por ahora estatica
@app.get('/movies', tags= ['movies'], response_model=List[Movie])
def get_movies() -> List[Movie]:
    return JSONResponse(content= movies)

#Parametros de ruta
@app.get('/movies/{id}',tags= ['movies'])
def get_movie(id:int = Path(ge=1 , le=2000 )) -> Movie:
    for item in movies:
        if item['id']==id:
            return JSONResponse(content= item)
        
    return JSONResponse(content= [])
            
    

#Parametros Query 
#Importamos categoria Query y añadimos las validaciones 
@app.get('/movies/',tags= ['movies'], response_model=List[Movie])
def get_movies_by_category(category: str = Query(min_length=5, max_length= 15)) -> List[Movie]:
    data = [movie for movie in movies if movie['category']==category ]
    return JSONResponse(content= data)

@app.post('/movies', tags=['movies'], response_model = dict)
def create_movie(movie:Movie) -> dict:
    movies.append(movie)
    return JSONResponse(content={'message':'Se ha registrado la pelicula'})

@app.delete('/movies/{id}',tags=['movies'], response_model = dict)
def delete_movie(id:int) -> dict:
   for movie in movies:
       if movie['id'] == id:
           movies.remove(movie)
           return JSONResponse(content= {'message':'Se ha eliminado la pelicula'})
           

@app.put('/movies/{id}', tags=['movies'],response_model = dict)
def update_movies( id:int, movie:Movie) -> dict:
    
    for mov in movies:
        if mov["id"]== id:
            mov.update(movie)
            return movies
         