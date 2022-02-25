from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    XML_EXTENSION = "xml"

    @classmethod
    def import_data(cls, file_name):
        file_extension = cls.get_file_extension(file_name)
        if file_extension != cls.XML_EXTENSION:
            raise ValueError("Arquivo inválido")

        tree = ET.ElementTree(file=file_name)
        root = tree.getroot()
        file_data = []
        for record in root:
            tags = [item.tag for item in record]
            texts = [item.text for item in record]
            item_dict = {key: value for (key, value) in zip(tags, texts)}
            file_data.append(item_dict)
        return file_data
