import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class FileReader:
    def __init__(self, path, reader):
        self.path = path
        self.reader = reader

    def read(self):
        return self.reader.read(self.path)


class CSV_Reader:
    def read(path):
        with open(path) as file:
            file_data = csv.DictReader(file, delimiter=",", quotechar='"')
            return list(file_data)


class Inventory:
    @classmethod
    def import_data(cls, path, type):
        file_extension = path.split(".")[-1]

        if file_extension == "csv":
            data_listed = FileReader(path, CSV_Reader).read()
            if type == "simples":
                return SimpleReport.generate(data_listed)
            elif type == "completo":
                return CompleteReport.generate(data_listed)
