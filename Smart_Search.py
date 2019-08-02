from libr.finder import smart_lookup
from time import sleep


def main():
    while True:
        smart_lookup()
        loop = input(
            "\n-- Enter Q to Quit Smart Search. Press Enter to continue: \n\n"
                ).lower()
        if loop == 'q':
            sleep(.5)
            break
        else:
            print("-- Let's go again... --\n\n")
            sleep(.75)


if __name__ == '__main__':
    main()
