from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Serialize:
    serialize_types = {"simples": SimpleReport, "completo": CompleteReport}

    @classmethod
    def serialize(cls, data_listed, type):
        return cls.serialize_types[type].generate(data_listed)


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, path, type):
        data_listed = self.importer.import_data(path)
        self.data.extend(data_listed)
        return Serialize.serialize(data_listed, type)

    def __iter__(self):
        return InventoryIterator(self.data)
