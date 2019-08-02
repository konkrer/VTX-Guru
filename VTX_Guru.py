from time import sleep
import libr.Info
from Smart_Search import main as smart_search
import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR, tail = os.path.split(__file__)

if BASE_DIR:
    BASE_DIR += '\\'

while True:

    print("""\n\n\n\n
=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=
|o7o|o7o|o7o|o7o|o7o|o7o|o7o|o7o|o7o|o7o|>GURU<|o7o|o7o|o7o|o7o|o7o|o7o|o7o|o7o|o7o|o7o|o7o|o7o
=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=


                          ~ VTX GURU ~

                     FPV MULTI PILOT VIDEO CLARITY TOOLS




-- 1. Smart Search   - Find a high clarity VTX channel group for 3 to 6 pilots.
                       Works with the channels pilots are already on,
                       so as few as possible pilots need to change channel.


-- 2. IMD Ace        - Analyzes entered 5 GHZ VTX channel group
                       and produces video clarity score.


-- 3. Charts         - See charts of channel groups possessing a passing video
      Explorer         clarity score. See what the best scoring groups are!


-- 4. EZ Investigate - Used to investigate all possible combinations of VTX channel
                       groups. Produces a scored list, from best to worst. (Use this
                       if the included 40 channel, U.S. legal channels only, or
                       40 channel plus lowband charts don't meet your needs.)



-- 5. What is IMD?   - IMD and why it matters for FPV pilots.


-- 6. About VTX GURU - How the scores are calculated.




        """)

    while True:
        choice = input(
            "-- Enter the number for the tool you'd like to use.\n\n"
            "-- Enter Q to Quit VTX Guru. ==========> "
                ).lower().strip()

        if choice in ('1', '2', '3', '4', '5', '6', 'q'):
            break
        else:
            sleep(.5)
            print("\n\n-- Not a valid choice. Let's try again. --\n\n")
            sleep(2)

    if choice == '1':
        sleep(.5)
        smart_search()  # exec(open(BASE_DIR + 'Smart_Search.py').read())
    if choice == '2':
        sleep(.5)
        exec(open(BASE_DIR + 'IMD_Analyzer.py').read())
    if choice == '3':
        sleep(.5)
        exec(open(BASE_DIR + 'Charts.py').read())
    if choice == '4':
        sleep(.5)
        exec(open(BASE_DIR + 'Investigate.py').read())
    if choice == '5':
        libr.Info.imd_info()  # exec(open('libr/Info2.py').read())
    if choice == '6':
        libr.Info.scores_info()  # exec(open('libr/Info.py').read())
    if choice == 'q':
        print('\n\n')
        break
