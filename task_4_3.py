import requests
from decimal import Decimal
from datetime import date

def currency_rates(corrency):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    content = response.content.decode(encoding=response.encoding)
    if corrency.upper() not in content:
        return None
    currency_date = content.split('Date="')[1][:10].split('.')
    currency_date = date(day=int(currency_date[0]), month=int(currency_date[1]), year=int(currency_date[2]))

    for element in content.split('<CharCode>')[1:]:
        char_code = element[:3]
        value = element.split('<Value>')[1:][0].split('</Value>')[:1][0]
        value = Decimal(f'{value.split(",")[0]}.{value.split(",")[1]}')
        if corrency.upper() == char_code:
            print(char_code, value, currency_date)

currency_rates('UsD')
currency_rates('usd')
currency_rates('EUR')
currency_rates('asd')
