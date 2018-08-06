__author__ = 'Gabriel Gitonga'


'''
1: First, the application must allow to add new movies to the collection;
2:  The application must allow users to view all the movies in their collection;
3:  The application must also allow users to find any particular movie by any of its attributes (more info in the next page...)

'''
movies = []
def menu():
    user_input = input('Enter a to add a movie: \n enter l to list all your movies: \n enter f to find a movie: \nenter q to quit the program: ')
    while user_input != 'q':

        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movies(movies)
        elif user_input == 'f':
            find_movie()
        else:
            print("invalid input")

        user_input = input('\nEnter a to add a movie:  enter l to list all your movies:  enter f to find a movie: enter q to quit the program: ')

def add_movie():
    name = input('Enter the movie name: ')
    director = input('Enter the name of directors: ')
    year = input('Enter the year of production: ')
    movies.append({
        'name' : name,
        'director': director,
        'year': year
    })


def show_movies(movie_list):
    for movi in movie_list:
        show_details(movi)
def show_details(movi):
    print(f"Name: {movi['name']}")
    print(f"Director: {movi['director']}")
    print(f"Year releases: {movi['year']}")

def find_movie():

    find_by = input('What are you looking for? year, name, director')
    looking_for = input('What are you searching for')

    found_movies = find_by_attribute(movies,looking_for,lambda x: x[find_by])
    show_movies(found_movies)

def find_by_attribute(items,expected,finder):
    found = []
    for i in items:
        if finder(i) == expected:
            found.append(i)
    return found
menu()
