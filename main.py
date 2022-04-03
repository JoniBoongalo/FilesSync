from modules import file_grabber as gb
from modules import file_checker as chck
from modules import logger
from config import *


def lastTime(newtime=None):

    if newtime:
        with open('last_time.py', 'w') as file:
            file.write(str(newtime))

    with open('last_time.py', 'r') as file:
        number = file.readline()
        return int(number)



def main():

    print(lastTime())


if __name__ == "__main__":
    main()
