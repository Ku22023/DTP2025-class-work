movies = {
    "M001": {
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
    "M002": {
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
    "M003": {
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
                print(i)
                for k in movies[i]:
                    print(i[k])
                    print(k, i[k])
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

def AdminMenu():
    print()
    print("--- Admin Menu ---")
    print("1. Search for Movie")
    print("2. Add a Movie")
    print("3. Edit a Movie")
    admin_option = int(input("Enter An option: "))
    if admin_option == 1: #search for movie
        SearchMovie(userrank="admin")
    elif admin_option == 2: #add movie
        AddMovie()
    elif admin_option == 3: #edit movie
        EditMovie()
    else:
        print("Error: Please enter a proper option!")
        AdminMenu()

def UserMenu():
    print()
    print("--- Main Menu ---")
    print("1. Search for Movie")
    admin_option = int(input("Enter An option: "))
    if admin_option == 1: #search for movie
        SearchMovie(userrank="user")
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
Login()

