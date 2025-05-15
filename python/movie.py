movies = {
    "M1": {
        "title": "Inception",
        "genre": "Sci-Fi",
        "duration": 148,
        "seats": 85,
        "rating": 6,
        "reviews": {
            1: {"name": "Adam", "rating": 6, "comment": "Amazing plot!"},
        },
        "price": 12,
    },
    "M2": {
        "title": "Interstellar",
        "genre": "Sci-Fi",
        "duration": 169,
        "seats": 110,
        "rating": 4.6,
        "reviews": {
            1: {"name": "Jane", "rating": 4.6, "comment": "Mind-expanding!"},
        },
        "price": 13,
    },
    "M3": {
        "title": "Joker",
        "genre": "Drama",
        "duration": 122,
        "seats": 100,
        "rating": 8.0,
        "reviews": {
            1: {"name": "Jason", "rating": 8.0, "comment": "Dark and intense."},
        },
        "price": 12,
    },
}
 
users = {
    "admin": {"password": "admin"},
    "Billy": {"password": "billy",
              "balance": 1250.50},
    "Bobby": {"password": "bobby",
              "balance": 820.00},
    "Bo": {"password": "bo",
           "balance": 312.75},
}

def SearchMovie(userrank):
    print()
    print("Search for Movie:")
    j = 0
    print("Type 'Return' to go back")
    searchfor = str(input("Enter the name of the movie you would like to search for: "))
    if searchfor.lower() != "return":
        for i in movies:
            if searchfor == movies[i]["title"]:
                print("Movie found!")
                print(movies[i])
                SearchMovie(userrank)
            else:
                j += 1
                if j == len(movies):
                    print("No movie found")
                    SearchMovie(userrank)
    else:
        if userrank == "admin":
            AdminMenu()
        else:
            UserMenu()

def AddMovie(movies):
    print()
    title = str(input("Enter the movie name: "))
    genre = str(input("Enter the movie genre: "))
    duration = str(input("Enter the duration of the movie (in minutes): "))
    seats = str(input("Enter how many seats there are: "))
    price = str(input("Enter how much the movie costs: "))

    confirm = str(input(f"Are you sure you want to add movie:\n {title} \n Type 'yes' or 'no': "))
    if confirm.lower() == "yes":
        newmovie = (f"M{len(movies) + 1}")
        movies[newmovie] = {
        "title": title,
        "genre": genre,
        "duration": duration,
        "seats": seats,
        "price": price,
        }
        print(f"Sucessfully added movie {title}\n Movie Info: \n {newmovie, title, genre, duration, seats, price}")
        AdminMenu()
    else:
        AdminMenu()
    
def AdminMenu():
    print()
    print("--- Admin Menu ---")
    print("1. Search for Movie")
    print("2. Add a Movie")
    print("3. Edit a Movie")
    print("4. Exit")
    admin_option = int(input("Enter An option: "))
    if admin_option == 1: #search for movie
        SearchMovie(userrank="admin")
    elif admin_option == 2: #add movie
        AddMovie(movies=movies)
    elif admin_option == 3: #edit movie
        EditMovie()
    elif admin_option == 4: #quit
        print("Quitting Program...")
    else:
        print("Error: Please enter a proper option!")
        AdminMenu()

def UserMenu():
    print()
    print("--- Main Menu ---")
    print("1. Search for Movie")
    print("2. Exit")
    user_option = int(input("Enter An option: "))
    if user_option == 1: #search for movie
        SearchMovie(userrank="user")
    elif user_option == 2: #quit
        print("Quitting Program...")
    else:
        print("Error: Please enter a proper option!")
        UserMenu()

def Login():
    print()
    username = str(input("Enter your Username please: "))
    password = str(input("Enter a password please: "))
    if username in users:
        if password == users[username]["password"]:
            print(f"Welcome {username}!")
            if username == "admin":
                AdminMenu()
            else:
                UserMenu()
        else:
            print("Error: Username or Password Incorrect")
            Login()
    else:
        print("Error: Username or Password Incorrect")
        Login()

for i in range(1,100):
    print()
    
print(len(movies))
Login()