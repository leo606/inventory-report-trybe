from collections import Counter
from simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def get_stock_amount_by_company(products):
        return Counter(
            product["nome_da_empresa"] for product in products
        ).most_common()

    @classmethod
    def generate(cls, products):
        oldest_product_date = cls.get_oldest_product_date(products)
        nearest_expiration_date = cls.get_nearest_expiration_date(products)
        greater_stock_amount_company = cls.get_greater_stock_amount_company(
            products
        )
        stock_amount_by_company = cls.get_stock_amount_by_company(products)
        company_name_and_stock = ""
        for company in stock_amount_by_company:
            company_name_and_stock += f"- {company[0]}: {company[1]}\n"

        return (
            f"Data de fabricação mais antiga: {oldest_product_date}\n"
            f"Data de validade mais próxima: {nearest_expiration_date}\n"
            "Empresa com maior quantidade de "
            f"produtos estocados: {greater_stock_amount_company}\n"
            "\nProdutos estocados por empresa:\n"
            f"{company_name_and_stock}"
        )


stock = [
    {
        "id": 1,
        "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP",
        "nome_da_empresa": "Forces of Nature",
        "data_de_fabricacao": "2020-07-04",
        "data_de_validade": "2023-02-09",
        "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
        "instrucoes_de_armazenamento": "in blandit ultrices enim",
    },
    {
        "id": 2,
        "nome_do_produto": "sodium ferric gluconate complex",
        "nome_da_empresa": "sanofi-aventis U.S. LLC",
        "data_de_fabricacao": "2020-05-31",
        "data_de_validade": "2023-01-17",
        "numero_de_serie": "SE95 2662 8860 5529 8299 2861",
        "instrucoes_de_armazenamento": "duis bibendum morbi",
    },
    {
        "id": 3,
        "nome_do_produto": "Dexamethasone Sodium Phosphate",
        "nome_da_empresa": "sanofi-aventis U.S. LLC",
        "data_de_fabricacao": "2019-09-13",
        "data_de_validade": "2023-02-13",
        "numero_de_serie": "BA52 2034 8595 7904 7131",
        "instrucoes_de_armazenamento": "morbi quis tortor id",
    },
    {
        "id": 4,
        "nome_do_produto": "Uricum acidum, Benzoicum acidum",
        "nome_da_empresa": "Newton Laboratories",
        "data_de_fabricacao": "2019-11-08",
        "data_de_validade": "2019-11-25",
        "numero_de_serie": "FR38 9203 3060 400T QQ8B HHS0 Q46",
        "instrucoes_de_armazenamento": "velit eu est congue elementum",
    },
]

print(CompleteReport.generate(stock))
# report = CompleteReport.generate(stock)
