from collections import Counter
from datetime import date


class SimpleReport:
    def get_oldest_product_date(products):
        return min([product["data_de_fabricacao"] for product in products])

    def get_nearest_expiration_date(products):
        not_expired_dates = filter(
            lambda product: product["data_de_validade"] > str(date.today()),
            products,
        )
        return min(
            product["data_de_validade"] for product in not_expired_dates
        )

    def get_greater_stock_amount_company(products):
        return Counter(
            product["nome_da_empresa"] for product in products
        ).most_common(1)[0][0]

    @classmethod
    def generate(cls, products):
        oldest_product_date = cls.get_oldest_product_date(products)
        nearest_expiration_date = cls.get_nearest_expiration_date(products)
        greater_stock_amount_company = cls.get_greater_stock_amount_company(
            products
        )

        return (
            f"Data de fabricação mais antiga: {oldest_product_date}\n"
            f"Data de validade mais próxima: {nearest_expiration_date}\n"
            "Empresa com maior quantidade de "
            f"produtos estocados: {greater_stock_amount_company}\n"
        )
