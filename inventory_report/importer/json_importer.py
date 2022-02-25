from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    JSON_EXTENSION = "json"

    @classmethod
    def import_data(cls, file_name):
        file_extension = cls.get_file_extension(file_name)
        if file_extension != cls.JSON_EXTENSION:
            raise ValueError("Arquivo inválido")

        with open(file_name) as file:
            file_data = json.load(file)
            return file_data
