#functions in python

def enter_movie(movie_list):
    movie=input("> ")
    return movie
        
def show_movies(movie_list,movie):
    print("---Movies---")
    print("Recent added movie:",movie)
    for m in movie_list:
        print(" >",m)

def del_movie(movie_list,limit=3):
    if len(movie_list)==limit:
        del_movie=movie_list.pop(0) 
        return del_movie       

movie_list=["GOAT"]       
while True:
    print("Enter movie name:")
    movie=enter_movie(movie_list)
    if movie not in movie_list:
        movie_list.append(movie)
    else:
        print("Movie already in list")    
    
    show_movies(movie=movie,movie_list=movie_list)
    print("Recent deleted movie:",del_movie(movie_list)) 

