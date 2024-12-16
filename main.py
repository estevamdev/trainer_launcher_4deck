# Import the required libraries
import sys
import os
from os import listdir
from os.path import isfile, join
from jsonlib import *
from system_process import *
import argparse


class main():

    def __init__(self):
        #Clear the screen
        os.system('cls')

        GamesConfig_Path = ".\GamesConfig"

        #If the path{GamesConfig_Path} does not exist, create it!
        if not (os.path.isdir(GamesConfig_Path)):
            os.makedirs(GamesConfig_Path)

        #Get Args
        parser = argparse.ArgumentParser()
        parser.add_argument(f'--game_id', dest=f'game_id', type=str)
        parser.add_argument(f'--game_path', dest=f'game_path', type=str)
        parser.add_argument(f'--game_args', dest=f'game_args', type=str)
        parser.add_argument(f'--game_name', dest=f'game_name', type=str)
        parser.add_argument(f'--trainer_path', dest=f'trainer_path', type=str)
        args = parser.parse_args()
        game = {}

        if (args.game_path is None):
            #Checks if the argument/parameter was received
            if (args.game_id is None): 
                print (f'[ERROR] - Parameter (--game_id) not found')
                os.system("pause")
                sys.exit()
            
            if (not isfile(f'{GamesConfig_Path}\{args.game_id.strip()}.json')):
                print ("[ERROR] - Game config not found!")
                os.system("pause")
                sys.exit()

            game = jsonlib.get_json(f'{GamesConfig_Path}\{args.game_id.strip()}.json')
        else:
             game["path"] = args.game_path.strip()
             game["arguments"] = args.game_args.strip() if (args.game_args is not None) else ""
             game["trainer"] = args.trainer_path.strip() if (args.trainer_path is not None) else ""
             game["name"] = args.game_name.strip() if (args.game_name is not None) else ""
        
        
        #game_path = args.game_path if (args.game_path is not None) else game["path"]

        #Execute
        system_process(game["path"], game["name"], game["arguments"], game["trainer"])

        #Close the program
        sys.exit()