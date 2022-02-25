from abc import ABC, abstractmethod


class Importer(ABC):
    def get_file_extension(file_name):
        return file_name.split(".")[-1].lower()

    @abstractmethod
    def import_data(file_name):
        raise NotImplementedError
