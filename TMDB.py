#5009e52baf2daaaf193df11aa48a32fe
#https://image.tmdb.org/t/p/w500 image
#https://api.themoviedb.org/3/discover/movie?api_key=5009e52baf2daaaf193df11aa48a32fe&language=en-US&region=MX&sort_by=popularity.desc&page=1&with_watch_providers=MX&watch_region=MX&with_watch_monetization_types=flatrate
from ast import Return
import requests
import random
URL= "https://api.themoviedb.org/3/discover/movie?api_key=5009e52baf2daaaf193df11aa48a32fe&sort_by=original_title.asc&with_watch_providers=MX&watch_region=MX&with_watch_monetization_types=flatrate"

def Get_Page():
    Raw = requests.get(URL)
    jRaw = Raw.json()
    Total_Pages = jRaw['total_pages']
    Page = random.randint(1,Total_Pages)
    while Page>=500:
        Page = random.randint(1,Total_Pages)
    return Page

def Get_Overview(ID):
    Newurl = "https://api.themoviedb.org/3/movie/" + str(ID) +"?api_key=5009e52baf2daaaf193df11aa48a32fe&language=es"
    Overview = requests.get(Newurl) 
    Overview = Overview.json()
    Overview = Overview['overview']
    return Overview

def Get_Image(ID):
    #https://api.themoviedb.org/3/movie/{movie_id}/images?api_key=<<api_key>>&language=es&include_image_language=es
    try:
        Newurl = "https://api.themoviedb.org/3/movie/"+ str(ID) +"/images?api_key=5009e52baf2daaaf193df11aa48a32fe&language=es&include_image_language=es"
        Image_path = requests.get(Newurl)
        Image_path = Image_path.json()
        Image_path = Image_path['posters'][0]['file_path']
        return Image_path
    except:
        #print("No se encontro en es")
        try:
            Newurl = "https://api.themoviedb.org/3/movie/"+ str(ID) +"/images?api_key=5009e52baf2daaaf193df11aa48a32fe&language=es-mx"
            Image_path = requests.get(Newurl)
            Image_path = Image_path.json()
            Image_path = Image_path['posters'][0]['file_path']
        except:
            #print("No se encontro en mx")
            try:
                Newurl = "https://api.themoviedb.org/3/movie/"+ str(ID) +"/images?api_key=5009e52baf2daaaf193df11aa48a32fe"
                Image_path = requests.get(Newurl)
                Image_path = Image_path.json()
                Image_path = Image_path['posters'][0]['file_path']
            except:
                #print("No se encontro en general")
                Image_path=0
    finally:
        if (Image_path == 0):
            return 0
        else:
            Newurl = "https://image.tmdb.org/t/p/w500" + str(Image_path)
            return Newurl

def Get_Movie():
    Page = random.randint(1,Get_Page())
    NewURL = URL + '&page=' + str(Page)
    movies = requests.get(NewURL)
    jmovies = movies.json()
    Total_Movies = len(jmovies['results'])
    Movie_Pick = random.randint(0,Total_Movies-1)
    Id_Movie = jmovies['results'][Movie_Pick]['id']
    Overview = Get_Overview(Id_Movie)
    Original_title = jmovies['results'][Movie_Pick]['original_title']
    Image_og = Get_Image(Id_Movie)
    print(Image_og)
    print(Original_title, Overview)
    
    

Get_Movie()