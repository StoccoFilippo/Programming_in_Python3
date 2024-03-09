# Organized in functions:
import os


def main():
    # Load list from file
    load_list()

    # Main loop for user interaction
    x = str(input("[A]dd [Q]uit: "))
    while x != "q":
        try:
            if x.lower() == "a":
                # Add item to the list
                add_item(movies)
            if x.lower() == "d":
                # Delete item from the list
                delete_item(movies)
            if x.lower() == "s":
                # Save list to file
                save_file(movies, filename)
            else:
                print("Invalid option. Please choose again.")
            # Print current list
            print_list(movies)
            x = str(input("[A]dd [D]elete [S]ave [Q]uit: "))
        except ValueError:
            print("Item not found in the list.")


def add_item(movies):
    # Add item to the list
    movie = str(input("Insert the item:"))
    movies.append(movie)
    return movies


def delete_item(movies):
    # Delete item from the list
    delete = int(input("Which movie you would like to delete (number)?"))
    movies.remove(movies[delete - 1])
    return movies


def save_file(movies, filename):
    # Save list to file
    confirm = input("Save unsaved changes (y/n): ")
    if confirm.lower() == "y":
        sorted_movies=sorted(movies)
        with open(filename, "w") as file:
            for movie in sorted_movies:
                file.write(movie + ",")
            print("Saved {0} items".format(len(sorted_movies)))
            file.close()
    else:
        print("Changes not saved")
    return movies


def print_list(movies):
    # Print items in the list
    movies=sorted(movies)
    #movie in alphabetical order
    for y in movies:
        print("{0} : {1}".format(movies.index(y) + 1, y))
    y = ""


def load_list():
    # Load list from file or create a new one
    path = input("Insert the directory, or press Enter to set the working directory: ")
    lst_files_found = False
    for filename in os.listdir():
        if filename.endswith(".lst"):
            print("Files and directories in:", filename)
            lst_files_found = True

    if not lst_files_found:
        with open("new.lst", "w") as movies:
            print(
                "Created new.lst because no .lst files were found in the current directory."
            )

    movies_file = input("Which file would you like to modify? ")

    if movies_file in os.listdir():
        with open(movies_file, "r") as movies_file:
            movies = movies_file.read().rstrip(",").split(",") #in this way the last empty "," is not considered
            movies = [movie.strip() for movie in movies]
            if not movies:
                print("-- no items are in the list--")
            else:
                for y in movies:
                    print("{0} : {1}".format(movies.index(y) + 1, y))
                y = ""
    return movies, filename


# Call main function
main()
