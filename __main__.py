import update, scrap
import time


print("Welcome to iTrendPL!")

while True:
    command = input("What would you like to do? ('u' - update database, 'd' - display current database, 'q' - quit)\n")

    if command == "u":
        for language in scrap.languages:
            update.update(language)
        break
    elif command == "d":
        update.open()
        time.sleep(5)
        break
    elif command == "q":
        break
    else:
        print("Commend does not exist. Try again.")
