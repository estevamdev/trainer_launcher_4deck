import sys
import os
from os.path import isfile

class system_process():

    def __init__(self, path:str, name:str, arguments:str="", trainer:str=""):
        if (path == ""):
            print(f'[ERROR] - Set the path to the game executable!')
            os.system("pause")
            sys.exit()
        
        print(f'[INFO] - Executing the game: {name}')
        system_process.execute(path, arguments)

        if (not trainer == ""):
            print(f'[INFO] - Executing the Trainer: {name}')
            system_process.execute(trainer)
        elif (not trainer == "") and (not isfile(trainer)):
            print(f'[ERROR] - The trainer path is not valid!')
            os.system("pause")
            sys.exit()
        
    def execute(exec:str, args:str=""):
        os.system(f'start "" "{exec}" {args}')