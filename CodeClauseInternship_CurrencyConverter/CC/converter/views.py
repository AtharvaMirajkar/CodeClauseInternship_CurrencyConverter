import requests
from django.shortcuts import render


def index(request):
    context = {}
    return render(request, "index.html", context)


def convert_currency(request):
    exchange_rate = None
    amount1 = None
    amount2 = None
    from_currency = "USD"
    to_currency = "INR"

    if request.method == "POST":
        amount1 = request.POST.get("amount1")
        amount2 = request.POST.get("amount2")
        from_currency = request.POST.get("from_currency")
        to_currency = request.POST.get("to_currency")

        
        if amount1:
            amount1 = float(amount1)
        elif amount2:
            amount2 = float(amount2)

        api_url = f"https://v6.exchangerate-api.com/v6/738a1adeb60b2daaa4ce639d/latest/{from_currency}"
        response = requests.get(api_url).json()
        exchange_rate = response["conversion_rates"].get(to_currency, 1)

        if amount1 is not None:
            amount2 = round(amount1 * exchange_rate, 2)
        elif amount2 is not None:
            amount1 = round(amount2 / exchange_rate, 2)

    context = {
        "exchange_rate": exchange_rate,
        "amount1": amount1,
        "amount2": amount2,
        "from_currency": from_currency,
        "to_currency": to_currency,
    }
    return render(request, "index.html", context)

