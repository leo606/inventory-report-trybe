from abc import ABC, abstractmethod
from collections import Counter
from datetime import date


class Report(ABC):
    def __init__(self, products):
        self.products = products

    def get_oldest_product_date(self):
        return min(
            [product["data_de_fabricacao"] for product in self.products]
        )

    def get_nearest_expiration_date(self):
        not_expired_dates = filter(
            lambda product: product["data_de_validade"] > str(date.today()),
            self.products,
        )

        return min(
            product["data_de_validade"] for product in not_expired_dates
        )

    def get_greater_stock_amount_company(self):
        # https://stackoverflow.com/questions/29511131/python-get-the-most-frequent-value-in-a-list-of-dictionaries
        return Counter(
            product["nome_da_empresa"] for product in self.products
        ).most_common(1)[0][0]

    def build(self):
        self.oldest_product_date = self.get_oldest_product_date()
        self.nearest_expiration_date = self.get_nearest_expiration_date()
        self.greater_stock_amount_company = (
            self.get_greater_stock_amount_company()
        )

    @abstractmethod
    def generate(self):
        raise NotImplementedError


class SimpleReport(Report):
    def generate(cls):
        cls.build()
        return (
            "Data de fabricação mais antiga: %s\n"
            "Data de validade mais próxima: %s\n"
            "Empresa com maior quantidade de produtos estocados: %s"
        ) % (
            cls.oldest_product_date,
            cls.nearest_expiration_date,
            cls.greater_stock_amount_company,
        )
