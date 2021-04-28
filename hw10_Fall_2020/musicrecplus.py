'''
Created on 4/20/21
@author:   Avery Cunningham
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Hw 10
'''


def getUsers():
    """Handle creating and opening musicrecplus.txt"""
    try:
        with open("musicrecplus.txt",
                  "r") as temp:  # using with simplifies file operations
            data = temp.read()
    except IOError:
        with open("musicrecplus.txt", "w") as temp:
            pass
        with open("musicrecplus.txt", "r") as temp:
            data = temp.read()

    users = data.splitlines()
    userData = {}

    for user in users:
        user = user.split(":")
        userData.update({user[0]: user[1].split(",")})

    return userData


def saveUsers(userData):
    """Save data from userData into file"""
    data = ""
    for user in sorted(userData):
        artists = sorted(set(userData[user]))
        data += f"{user}:{','.join(artists)}\n"
    with open("musicrecplus.txt", "w") as temp:
        temp.write(data)
    # return userData


def enterPreferences(user, userData):
    """Prompts the user to input their preferences and saves."""
    userData[user] = []
    while True:
        artist = input("Enter an artist that you like (Enter to finish): ")
        if artist == "":
            break
        userData[user].append(artist.title())

    saveUsers(userData)
    return userData


def getArtists(userDict):
    """Return a list of all artists mentioned in userDict"""
    artists = []
    for user in userDict:
        artists += userDict[user]
    return artists


def getArtistCounts(userData):
    """Return a dictionary of artists as keys and their occurrences as values."""
    artists = getArtists(userData)

    counts = {}
    for artist in artists:
        if artist in counts:
            counts[artist] += 1
        else:
            counts[artist] = 1

    sortedKeys = sorted(counts, key=counts.get, reverse=True)
    sortedCounts = {}

    for key in sortedKeys:
        sortedCounts[key] = counts[key]
    return sortedCounts


def publicUsers(userData):
    """Remove all private users from userData"""
    userData = userData.copy()
    for user in list(userData):
        if user[-1] == "$":
            userData.pop(user)
    return userData


def menuChoice():
    """Get user input from main menu"""
    menu = \
    """Enter a letter to choose an option:
    e - Enter preferences
    r - Get recommendations
    p - Show most popular artists
    h - How popular is the most popular
    m - Which user has the most likes
    q - Save and quit
    """
    return input(menu)


def getRecommendations(currentUser, userData):
    """Gets artist recommendations for currentUser from userData prints them."""
    userData = publicUsers(userData)
    userArtists = userData[currentUser]

    mostSimilar = None
    bestSimilarity = 0

    def getSimilarity(a, b):  # use the intersect function we learned in class
        if set(a) <= set(b):  #ignore subsets
            return 0
        else:
            return len(list(filter(lambda x: x in a, b)))

    for user in userData:
        similarity = getSimilarity(userArtists, userData[user])
        if similarity > bestSimilarity:
            bestSimilarity = similarity
            mostSimilar = user

    if mostSimilar is None:
        print("No recommendations available at this time.")
    else:
        for artist in userData[mostSimilar]:
            if artist not in userArtists:
                print(artist)


def popular(currentUser, userData):
    """Prints the top three most popular artists."""
    userData = publicUsers(userData)
    sortedCounts = getArtistCounts(userData)

    for i in range(3):
        print(list(sortedCounts)[i])


def popularity(currentUser, userData):
    """Prints the number of likes the most popular artist has."""
    userData = publicUsers(userData)
    sortedCounts = getArtistCounts(userData)
    print(list(sortedCounts.values())[0])


def mostLikes(currentUser, userData):
    """Prints the name of the public user who likes the most music."""
    userData = publicUsers(userData)
    mostLikes = 0
    name = ""

    for user in userData:
        userLikes = len(userData[user])
        if userLikes > mostLikes:
            mostLikes = userLikes
            name = user
    if mostLikes == 0:
        name = "Sorry, no user found."
    print(name)
    return name


def shutdown(currentUser, userData):
    """Saves userData in preperation of stopping the program."""
    saveUsers(userData)


# all choices for user input with coresponding functions
# if i were to do this again i probably wouldn't do it this way since
# i ended up passing a lot of unnecessary values for the few functions that needed them
# but i did this to avoid using using global variables
menuChoices = {
    "e": enterPreferences,
    "r": getRecommendations,
    "p": popular,
    "h": popularity,
    "m": mostLikes,
    "q": shutdown,
}


def main():
    """Main function that handles user interaction with the program."""
    userData = getUsers()

    currentUser = input(
        "Enter your name (put a $ symbol after your name if you wish your preferences to remain private): "
    )

    if currentUser not in userData:
        userData = enterPreferences(currentUser, userData)

    choice = None
    while (choice != "q"):
        choice = menuChoice()
        # if choice == "e" add this in so all the menu functions dont need currentUser as an argument
        if choice in menuChoices:
            menuChoices[choice](currentUser, userData)
        else:
            print("Invalid command, try again.")


if __name__ == "__main__":
    main()