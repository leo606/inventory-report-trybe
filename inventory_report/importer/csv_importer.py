from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    CSV_EXTENSION = "csv"

    @classmethod
    def import_data(cls, file_name):
        file_extension = cls.get_file_extension(file_name)
        if file_extension != cls.CSV_EXTENSION:
            raise ValueError("Arquivo inválido")

        with open(file_name) as file:
            file_data = csv.DictReader(file, delimiter=",", quotechar='"')
            return list(file_data)
