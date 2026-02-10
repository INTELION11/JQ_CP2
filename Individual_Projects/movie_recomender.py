import csv  
  
# try to open and read the csv file  
def load_movies(filename):  
    try:  
        with open(filename, mode="r") as sample:  
            reader = csv.reader(sample, delimiter=',')  
            header = next(reader)  
            users = []  
            for line in reader:  
                users.append(  
                    {  
                        header[0]: line[0],   # Title  
                        header[1]: line[1],   # Director(s)  
                        header[2]: line[2],   # Genre(s)  
                        header[3]: line[3],   # Rating  
                        header[4]: line[4],   # Length (min)  
                        header[5]: line[5]    # Notable Actors  
                    }  
                )  
        return users  
    except:  
        print("no csv")  
        return []  
  
# print all movies  
def print_movies(movies):  
    for movie in movies:  
        print(movie)  
  
# handle genre filter  
def filter_genre(movies):  
    genre = input("what genre? ").strip().lower()  
    return [m for m in movies if genre in m["Genre"].lower()]  
  
# handle director filter  
def filter_director(movies):  
    director = input("director? ").strip().lower()  
    return [m for m in movies if director in m["Director"].lower()]  
  
# handle actor filter  
def filter_actor(movies):  
    actor = input("actor? ").strip().lower()  
    return [m for m in movies if actor in m["Notable Actors"].lower()]  
  
# handle length filter  
def filter_length(movies):  
    min_len = input("minimum length (or leave blank): ").strip()  
    max_len = input("maximum length (or leave blank): ").strip()  
    def length_okay(m):  
        try:  
            length = int(m["Length (min)"])  
        except:  
            return False  
        if min_len and length == int(min_len):  
            return False  
        if max_len and length == int(max_len):  
            return False  
        return True  
    return [m for m in movies if length_okay(m)]  
  
# main menu loop  
def main():  
    users = load_movies("Notes/Movies list - Sheet1.csv")  
    if not users:  
        return  
    on = True  
    while on:  
        action = input(" 1 Search / Recommendations \n 2 Print Full Movie List \n 3 Exit\n").strip().lower()  
        if action == "2" or action == "print":  
            print_movies(users)  
        elif action == "3" or action == "exit":  
            on = False  
        elif action == "1" or action == "search" or action == "recommendations":  
            do = input("Choose filters to apply (enter numbers separated by commas, e.g., 1,3): \n1 Genre \n2 Director \n3 Actor \n4 Length (min/max)\n").split(",")  
            do = [x.strip() for x in do]  
            possible = users.copy()  
            if "1" in do:  
                possible = filter_genre(possible)  
            if "2" in do:  
                possible = filter_director(possible)  
            if "3" in do:  
                possible = filter_actor(possible)  
            if "4" in do:  
                possible = filter_length(possible)  
            if possible:  
                print_movies(possible)  
            else:  
                print("No movies match those filters. Try removing one filter or widening the length range.")  
  
main()  
