import easygui
#python.exe -m pip install --upgrade pip
#pip install easygui
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

#DOESNT WORK YET!!
def LeaveReview(movie_id, username):
    print(f"hello {username}")
    review_values = []
    review_tags = [
        "rating:",
        "comment:",
    ]
    movie_title = movies[movie_id]["title"]
    review_values = easygui.multenterbox(f"Leaving a review for: ", "Leaving a review", review_tags)
    review_id = len(movies[movie_id]["reviews"]) + 1
    movies[movie_id]["reviews"][review_id]["name"] = username
    movies[movie_id]["reviews"][review_id]["rating"] = review_values[0]
    movies[movie_id]["reviews"][review_id]["comment"] = review_values[1]
    easygui.msgbox(movies[movie_id]["reviews"][review_id]["name"])
    easygui.msgbox(movies[movie_id]["reviews"][review_id]["rating"])
    easygui.msgbox(movies[movie_id]["reviews"][review_id]["comment"])

    

def DisplayMovieInfo(movie_id, userrank):
    valuelist = f"ID: {movie_id}\n"
    for key, value in movies[movie_id].items():
        if key == "reviews":
            print("yo")
        else:
            valuelist += (f"{key}: {value}\n")
    if userrank == "admin":
        user_option = easygui.buttonbox(f"Movie info:\n{valuelist}", choices=["Done", "Edit Movie Details"])
        if user_option != None: 
            if user_option != "Done":
                EditMovie(movie_id)
    else:
        user_option = easygui.buttonbox(f"Movie info:\n{valuelist}", choices=["Done", "Leave a Review"])
        if user_option != None: 
            if user_option != "Done":
                LeaveReview(movie_id, username=userrank)
                print("leaving a review")
            else:
                ViewMovies(userrank)
        else:
            ViewMovies(userrank)
    
def ViewMovies(userrank):
    print(userrank)
    choices = []
    for i in movies:
        moidtitle = movies[i]["title"]
        choices.append(f"{i}: {moidtitle}")
    user_option = easygui.choicebox("Pick the movie you would like to view:", choices=choices)
    if user_option != None:
        movie_id = user_option.split(":")[0].strip()
        DisplayMovieInfo(movie_id, userrank)
    else:
        if userrank == "admin":
            AdminMenu()
        else:
            UserMenu()

def EditMovie(movie_id):
    if movie_id == "none":
        ViewMovies(userrank="admin")
    else:
        movie_values = []
        movie_tags = [
            "title:",
            "genre:",
            "duration:",
            "seats:",
            "price:",
        ]
        default_values = []
        k = 1
        for i in movies[movie_id]:
            if k <= 5:
                k += 1
                default_values.append(movies[movie_id].get(i))
        print(default_values)
        movie_values = easygui.multenterbox(f"Enter the movie's info: ", "Editing Movie", movie_tags, default_values)
        if len(movie_values) != 5:
            movie_values = easygui.multenterbox(f"Please fill in all info", "Editing Movie", movie_tags, default_values)
        else:
            movies[movie_id] = {
            "title": movie_values[0],
            "genre": movie_values[1],
            "duration": movie_values[2],
            "seats": movie_values[3],
            "price": movie_values[4],
            }
            DisplayMovieInfo(movie_id, userrank="admin")
            AdminMenu()

     

def SearchMovie(userrank):
    searchfor = easygui.enterbox("Enter the name of the movie you would like to search for:")
    if searchfor != None:
        movie_index = 0
        for movie_id in movies:
            if searchfor == movies[movie_id]["title"]:
                DisplayMovieInfo(movie_id, userrank)
                SearchMovie(userrank)
            else:
                movie_index += 1
                if movie_index == len(movies):
                    if userrank ==  "admin":
                        user_choice = easygui.buttonbox(f"No movie with title {searchfor} found.\nWould you like to enter a new movie?", choices=["No", "Yes"])
                        if user_choice == "No":
                            SearchMovie(userrank)
                        else:
                            AddMovie()
                    elif userrank == "user":
                        easygui.msgbox(f"No movie with title {searchfor} found.")
                        SearchMovie(userrank)
    else:
        if userrank == "admin":
            AdminMenu()
        else:
            UserMenu()

def AddMovie():
    movie_values = []
    movie_tags = [
        "title:",
        "genre:",
        "duration:",
        "seats:",
        "price:",
    ]
    movie_values = easygui.multenterbox("Enter the movie's info: ", "Adding Movie", movie_tags, movie_values)
    if movie_values != None:
        for i in movie_values:
            j = 0
            if i == "":
                j += 1
                movie_values.pop(j)
        if len(movie_values) != 5:
            print(movie_values)
            easygui.msgbox("Error: Please fill in all the values!")
            AddMovie()
        else:
            newmovie = (f"M{len(movies) + 1}")
            movies[newmovie] = {
            "title": movie_values[0],
            "genre": movie_values[1],
            "duration": movie_values[2],
            "seats": movie_values[3],
            "price": movie_values[4],
            }
            DisplayMovieInfo(movie_id=newmovie, userrank="admin")
            AdminMenu()
    else:
        AdminMenu()

def AdminMenu():
    admin_option = easygui.buttonbox("Please choose your option:", choices=["Search for a Movie", "Add a Movie", "Edit a Movie", "View Movies", "Log Out"])
    if admin_option != None:
        if admin_option == "Search for a Movie": #search for movie
            SearchMovie(userrank="admin")
        elif admin_option == "Add a Movie": #add movie
            AddMovie()
        elif admin_option == "Edit a Movie": #edit movie
            EditMovie(movie_id="none")
        elif admin_option == "View Movies":
            ViewMovies(userrank="admin")
        elif admin_option == "Log Out": #quit
            easygui.msgbox("Sucessfully Logged out!")
            Login()
        else:
            easygui.msgbox("An unknown error occured.")
            AdminMenu()
    else:
        exit()

def UserMenu(username):
    user_option = easygui.buttonbox(f"Welcome, {username}!\nPlease choose your option:", choices=["Search for a Movie", "View Movies", "Log Out"])
    if user_option != None:
        if user_option == "Search for a Movie": #search for movie
            SearchMovie(userrank=username)
        elif user_option == "View Movies":
            ViewMovies(userrank=username)
        elif user_option == "Log Out": #quit
            easygui.msgbox("Sucessfully Logged out!")
            Login()        
        else:
            easygui.msgbox("An unknown error occured.")
            UserMenu()
    else:
        exit()

def Login():
    print()
    username = easygui.enterbox("Enter your username please: ")
    if username != None:
        password = easygui.passwordbox("Enter your password please: ")
        if password != None:
            if username in users:
                if password == users[username]["password"]:
                    if username == "admin":
                        AdminMenu()
                    else:
                        UserMenu(username)
                else:
                    easygui.msgbox("Error: Username or Password Incorrect")
                    Login()
            else:
                easygui.msgbox("Error: Username or Password Incorrect")
                Login()
        else:
            exit()
    else:
        exit()



Login()