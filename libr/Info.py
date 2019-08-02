import os


module_dir = os.path.dirname(__file__)


def scores_info():
    print("""



    =====================================================================================================
    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>INFO<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    =====================================================================================================
        """)

    while True:
        print("\n")
        file_path = os.path.join(module_dir, 'SCORES.md')
        with open(file_path) as f:
            print(f.read())

        input("\n-- Press Enter when done.\n\n").lower()
        break


def imd_info():
    print("""



=====================================================================================================
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>INFO<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
=====================================================================================================
    """)

    while True:
        print("\n")
        file_path = os.path.join(module_dir, 'IMD_FPV.md')
        with open(file_path) as f:
            print(f.read())

        input("\n-- Press Enter when done.\n\n").lower()
        break
