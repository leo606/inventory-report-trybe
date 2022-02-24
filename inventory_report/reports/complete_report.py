from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def get_stock_amount_by_company(products):
        return (
            Counter(product["nome_da_empresa"] for product in products)
            .items()
        )

    @classmethod
    def generate(cls, products):
        stock_amount_by_company = cls.get_stock_amount_by_company(products)
        company_name_and_stock = ""
        for company in stock_amount_by_company:
            company_name_and_stock += f"- {company[0]}: {company[1]}\n"

        return (
            f"{super().generate(products)}\n"
            "Produtos estocados por empresa: \n"
            f"{company_name_and_stock}"
        )
