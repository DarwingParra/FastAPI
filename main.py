from fastapi import FastAPI,Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()
app.title = 'Mi aplicacion con FastAPI'

app.version = '0.0.1'

class Movie(BaseModel):
    id: Optional[int]=None
    title: str = Field(min_length=15, max_length=25)
    overview: str = Field(min_length=40, max_length=60)
    year:int = Field (led=2022)
    rating: float 
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


@app.get('/',tags=['home'])
def message():
    return HTMLResponse('<h1>Hello world</h1>')


@app.get('/movies', tags= ['movies'])
def get_movies():
    return movies

#Parametros de ruta
@app.get('/movies/{id}',tags= ['movies'])
def get_movie(id:int):
    return [movie for movie in movies if movie['id']==id]

#Parametros Query 
@app.get('/movies/',tags= ['movies'])
def get_movies_by_category(category: str, year: int):
    return [movie for movie in movies if movie['category']==category ]
    
@app.post('/movies', tags=['movies'])
def create_movie(movie:Movie):
    movies.append(movie)
    return movies

@app.delete('/movies/{id}',tags=['movies'])
def delete_movie(id:int):
   return [movie for movie in movies if movie['id']!=id]

@app.put('/movies/{id}', tags=['movies'])
def update_movies( id:int, movie:Movie):
    
    for mov in movies:
        if mov["id"]== id:
            mov.update(movie)
            return movies
         