import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


importers = {"csv": CsvImporter, "json": JsonImporter, "xml": XmlImporter}


def main():
    if len(sys.argv) < 3:
        return print("Verifique os argumentos", file=sys.stderr)

    _, path, type = sys.argv

    file_extension = path.split(".")[-1].lower()
    inventory = InventoryRefactor(importers[file_extension])
    print(inventory.import_data(path, type), end='')
