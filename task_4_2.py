import requests
from decimal import Decimal
# Я очень долго пыталась решить задачу с помощью BeautifullSoup (Поскольку читала и смотрела дополнительно как парсить сайты),
# но у меня не всегда выводились данные на экран.  Я не смогла понять почему. Возможно из-за того, что страница XML.
# В итоге пришлось делать со срезами, хотя я не очень хотела их использовать.
def currency_rates(corrency):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    content = response.content.decode(encoding=response.encoding)
    if corrency.upper() not in content:
        return None

    for element in content.split('<CharCode>')[1:]:
        char_code = element[:3]
        value = element.split('<Value>')[1:][0].split('</Value>')[:1][0]
        value = Decimal(f'{value.split(",")[0]}.{value.split(",")[1]}')
        if corrency.upper() == char_code:
            print(char_code, value)

currency_rates('UsD')
currency_rates('usd')
currency_rates('EUR')




