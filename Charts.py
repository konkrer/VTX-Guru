from libr.finder import get_charts
from time import sleep

while True:
    get_charts()
    loop = input(
        "\n-- Enter Q to Quit Charts Explorer. Press Enter to continue: \n\n"
            ).lower()
    if loop == 'q':
        sleep(.5)
        break
    else:
        print("-- Let's go again... --\n\n")
        sleep(.75)
