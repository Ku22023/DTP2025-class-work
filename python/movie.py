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

def SearchMovie():
    print()
    print("Search for Movie:")
    searchfor = str(input("Enter the name of the movie you would like to search for: "))
    if searchfor in movies[]]["title"]:
        print("success")
    else:
        print("no movie in there")

def AdminMenu():
    print()
    print("--- Admin Menu ---")
    print("1. Search for Movie")
    print("2. Add a Movie")
    print("3. Edit a Movie")
    admin_option = int(input("Enter An option: "))
    if admin_option == 1: #search for movie
        SearchMovie()
    elif admin_option == 2: #add movie
        AddMovie()
    elif admin_option == 3: #edit movie
        EditMovie()
    else:
        print("Error: Please enter a proper option!")
        AdminMenu()

def Login():
    print()
    password = str(input("Enter a password please: "))
    if password == users["admin"]["password"]:
        print("welcome admin")
        AdminMenu()
    else: #kyle u fix this later
        print("incorrect password")
        Login()
#        for i in users:
#            if users[i]["password"] == password:
#                print("welcome", i)
#            else:
#                print("wrong")

for i in range(1,100):
    print()
Login()

