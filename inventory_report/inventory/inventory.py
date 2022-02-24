import csv
import json
import xml.etree.ElementTree as ET
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


class JSON_Reader:
    def read(path):
        with open(path) as file:
            file_data = json.load(file)
            return file_data


class XML_Reader:
    def read(path):
        tree = ET.ElementTree(file=path)
        root = tree.getroot()
        file_data = []
        for record in root:
            tags = [item.tag for item in record]
            texts = [item.text for item in record]
            item_dict = {key: value for (key, value) in zip(tags, texts)}
            file_data.append(item_dict)
        return file_data


class Serialize:
    def serialize(data_listed, type):
        if type == "simples":
            return SimpleReport.generate(data_listed)
        elif type == "completo":
            return CompleteReport.generate(data_listed)


class Inventory:
    @classmethod
    def import_data(cls, path, type):
        file_extension = path.split(".")[-1].lower()

        if file_extension == "csv":
            data_listed = FileReader(path, CSV_Reader).read()
            return Serialize.serialize(data_listed, type)
        elif file_extension == "json":
            data_listed = FileReader(path, JSON_Reader).read()
            return Serialize.serialize(data_listed, type)
        elif file_extension == "xml":
            data_listed = FileReader(path, XML_Reader).read()
            return Serialize.serialize(data_listed, type)


print(Inventory.import_data("inventory_report/data/inventory.xml", "completo"))
