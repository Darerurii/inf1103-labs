import json

FILENAME= "inventory.json"
 
class FileHandling:
    def __init__(self, filename=FILENAME):
        self.__filename = filename
 
    def load_file(self):
        try:
            with open(self.__filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []
 
    def save_file(self, data):
        with open(self.__filename, "w") as file:
            json.dump(data, file, indent=4)
        return True
 
    def get_filename(self):
        # Needed as __filename is private
        return self.__filename