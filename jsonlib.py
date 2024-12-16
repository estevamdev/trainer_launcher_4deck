import json
from pathlib import Path

class jsonlib():
    
    def get_json(cfg_file:str):
        # Opening JSON file
        json_file = open(cfg_file)

        # returns JSON object as 
        # a dictionary
        data = json.load(json_file)

        # Closing file
        json_file.close()

        return data