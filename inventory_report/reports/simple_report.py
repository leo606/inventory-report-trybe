from collections import Counter
from datetime import date


class SimpleReport:
    def generate(products):
        not_expired_dates = filter(
            lambda product: product["data_de_validade"] > str(date.today()),
            products,
        )

        oldest_product_date = min(
            [product["data_de_fabricacao"] for product in products]
        )
        nearest_expiration_date = min(
            product["data_de_validade"] for product in not_expired_dates
        )
        greater_stock_amount_company = Counter(
            product["nome_da_empresa"] for product in products
        ).most_common(1)[0][0]
        return (
            f"Data de fabricação mais antiga: {oldest_product_date}\n"
            f"Data de validade mais próxima: {nearest_expiration_date}\n"
            "Empresa com maior quantidade de "
            f"produtos estocados: {greater_stock_amount_company}\n"
        )
