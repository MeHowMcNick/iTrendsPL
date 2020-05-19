import update, scrap
import time, argparse


def main():
    parser = argparse.ArgumentParser(description='Collect information about the number of job offers in IT industry from main Polish portals.')
    parser.add_argument('-u', '--update', help='update database', action="store_true")
    parser.add_argument('-d', '--display', help='display current database', action="store_true")
    args = parser.parse_args()

    threads = list()
    print("Welcome to iTrendsPL!")

    if vars(args)['update']:
        for language in scrap.languages:
            update.update(language)
    elif vars(args)['display'] == True:
        update.open()
        time.sleep(1)


if __name__ == "__main__":
    main()
