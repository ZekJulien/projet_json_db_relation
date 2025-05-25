import json
import os
from datetime import datetime
##repositories
###models
import repositories.models 


class Encoder(json.JSONEncoder):
    """    
    Custom JSON encoder to handle serialization of custom objects.
    This class herits from json.JSONEncoder and overrides the default method to handle custom objects.
    """
    def default(self, obj):
        """
        Custom method to serialize custom objects into JSON format.
        This method checks the type of the object and returns a dictionary representation of it.
        Args:
            obj (any): Object to be serialized.
        Returns:
            dict: Dictionary representation of the object.
        """
        if isinstance(obj, datetime):
            return obj.isoformat()
        elif hasattr(obj, '__dict__'):
            data = {
                key: value for key, value in obj.__dict__.items() 
                if not key.startswith('_')
            }
            return {
                "__type__": obj.__class__.__name__,
                **data
            }
        return super().default(obj)
    
class Decoder:

    _models_dict = {
    name: obj
    for name, obj in repositories.models.__dict__.items()
    if hasattr(obj, '__dict__') and isinstance(obj, type)
    }

    @staticmethod
    def decoder_hook(dct):
        """
        Custom JSON decoder to handle deserialization of custom objects.
        This method checks the '__type__' key in the dictionary and returns the corresponding object.
        Args:
            dct (dict): Dictionary to be decoded.
        Returns:
            object: The corresponding object based on the '__type__' key.
        """
        if '__type__' in dct:
            type_name = dct.pop('__type__')
            model = Decoder._models_dict.get(type_name)
            if model is not None:
                return model(**dct)
        return dct

class JsonStorage:
    
    @staticmethod
    def _encode(jsonFile, data):
        """
        Save data to a JSON file.
        Args:
            jsonFile (str): Path to the JSON file where data will be saved.
            data (any): Data to be saved in JSON format.
        """
        try:
            with open(jsonFile, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4, cls=Encoder)
        except Exception as e:
            print(f'Erreur lors de la sauvegarde JSON : {e}')

    @staticmethod
    def _decode(jsonFile):
        """
        Load data from a JSON file.
        Args:
            jsonFile (str): Path to the JSON file from which data will be loaded.
        Returns:
            any: Data loaded from the JSON file.
        """
        try:
            with open(jsonFile, 'r', encoding='utf-8') as file:
                data = json.load(file, object_hook=Decoder.decoder_hook)
                return data
        except Exception as e:
            print(f"Erreur lors de la récupération du JSON : {e}")

    @staticmethod
    def save_all(path, data):
        """
        Saves the list of authors to the JSON file.
        If the file doesn't exist, it creates a new one.
        """
        JsonStorage._encode(path, data)

    @staticmethod
    def load_all(path):
        """
        Loads the list of authors from the JSON file.
        If the file doesn't exist, it returns an empty list.
        """
        if os.path.isfile(path):
            data = JsonStorage._decode(path)
            return data
        else:
            return []




# class Encoder(json.JSONEncoder):
#     """    
#     Custom JSON encoder to handle serialization of custom objects.
#     This class herits from json.JSONEncoder and overrides the default method to handle custom objects.
#     """
#     def default(self, obj):
#         """
#         Custom method to serialize custom objects into JSON format.
#         This method checks the type of the object and returns a dictionary representation of it.
#         Args:
#             obj (any): Object to be serialized.
#         Returns:
#             dict: Dictionary representation of the object.
#         """
#         if isinstance(obj, datetime):
#             return obj.isoformat()
#         elif isinstance(obj, Author):
#             return {
#                 "__type__": "author",
#                 "id": obj.id,
#                 "full_name": obj.full_name
#             }
#         elif isinstance(obj, Theme):
#             return {
#                 "__type__": "theme",
#                 "id": obj.id,
#                 "name": obj.name
#             }
#         elif isinstance(obj, Book):
#             return {
#                 "__type__": "book",
#                 "isbn": obj.isbn,
#                 "title": obj.title,
#                 "date": obj.date,
#                 "price": obj.price
#             }
#         elif isinstance(obj, BookTheme):
#             return{
#                 "__type__": "book_theme",
#                 "isbn_book": obj.isbn_book,
#                 "id_theme": obj.id_theme
#             }
#         elif isinstance(obj, BookAuthor):
#             return{
#                 "__type__": "book_author",
#                 "isbn_book": obj.isbn_book,
#                 "id_author": obj.id_author
#             }
#         return super().default(obj)
    
# class Decoder:

#     @staticmethod
#     def decoder_hook(dct):
#             """
#             Custom JSON decoder to handle deserialization of custom objects.
#             This method checks the '__type__' key in the dictionary and returns the corresponding object.
#             Args:
#                 dct (dict): Dictionary to be decoded.
#             Returns:
#                 object: The corresponding object based on the '__type__' key.
#             """
#             if '__type__' in dct:
#                 type_ = dct.pop('__type__')
#                 match type_:
#                     case "author":
#                         return Author(**dct)
#                     case "theme":
#                         return Theme(**dct)
#                     case "book":
#                         dct['date'] = datetime.fromisoformat(dct['date']).strftime("%d-%m-%Y")
#                         return Book(**dct)
#                     case "book_theme":
#                         return BookTheme(**dct)
#                     case "book_author":
#                         return BookAuthor(**dct)
#             return dct

# class JsonStorage:
    
#     @staticmethod
#     def _encode(jsonFile, data):
#         """
#         Save data to a JSON file.
#         Args:
#             jsonFile (str): Path to the JSON file where data will be saved.
#             data (any): Data to be saved in JSON format.
#         """
#         try:
#             with open(jsonFile, 'w', encoding='utf-8') as file:
#                 json.dump(data, file, indent=4, cls=Encoder)
#         except Exception as e:
#             print(f'Erreur lors de la sauvegarde JSON : {e}')

#     @staticmethod
#     def _decode(jsonFile):
#         """
#         Load data from a JSON file.
#         Args:
#             jsonFile (str): Path to the JSON file from which data will be loaded.
#         Returns:
#             any: Data loaded from the JSON file.
#         """
#         try:
#             with open(jsonFile, 'r', encoding='utf-8') as file:
#                 data = json.load(file, object_hook=Decoder.decoder_hook)
#                 return data
#         except Exception as e:
#             print(f"Erreur lors de la récuparation du JSON : {e}")

#     @staticmethod
#     def save_all(path, data):
#         """
#         Saves the list of authors to the JSON file.
#         If the file doesn't exist, it creates a new one.
#         """
#         JsonStorage._encode(path, data)

#     @staticmethod
#     def load_all(path):
#         """
#         Loads the list of authors from the JSON file.
#         If the file doesn't exist, it returns an empty list.
#         """
#         if os.path.isfile(path):
#             data = JsonStorage._decode(path)
#             return data
#         else:
#             return []

