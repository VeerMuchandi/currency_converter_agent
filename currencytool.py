"""Tool that downloads 10k report for a corporation."""

import requests


def get_exchange_rate(
    currency_from: str, #= "USD",
    currency_to: str, #= "EUR",
    currency_date: str #= "latest",
):
    """Retrieves the exchange rate between two currencies on a specified date."""

    response = requests.get(
        f"https://api.frankfurter.app/{currency_date}",
        params={"from": currency_from, "to": currency_to},
    )
    return response.json()