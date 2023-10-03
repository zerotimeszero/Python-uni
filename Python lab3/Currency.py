import requests
import datetime
class Rate:
    def __init__(self, format='value'):
        self.format = format
    def exchange_rates(self):
        """
        Возвращает ответ сервиса с информацией о валютах в виде:

        {
            'AMD': {
                'CharCode': 'AMD',
                'ID': 'R01060',
                'Name': 'Армянских драмов',
                'Nominal': 100,
                'NumCode': '051',
                'Previous': 14.103,
                'Value': 14.0879
                },
            ...
        }
        """
        r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        return r.json()['Valute']

    def make_format(self, currency):
        """
        Возвращает информацию о валюте currency в двух вариантах:
        - полная информация о валюте при self.format = 'full':
        Rate('full').make_format('EUR')
        {
            'CharCode': 'EUR',
            'ID': 'R01239',
            'Name': 'Евро',
            'Nominal': 1,
            'NumCode': '978',
            'Previous': 79.6765,
            'Value': 79.4966
        }

        Rate('value').make_format('EUR')
        79.4966
        """
        response = self.exchange_rates()

        if currency in response:
            if self.format == 'full':
                return response[currency]

            if self.format == 'value':
                return response[currency]['Value']
            if self.format =='wName':
                return f"{response[currency]['Name']} {response[currency]['Value']} руб"

        return 'Error'

    def eur(self, diff=False):
        if diff:
            return self.get_currency_diff('EUR')
        """Возвращает курс евро на сегодня в формате self.format"""
        return self.make_format('EUR')

    def usd(self, diff=False):
        if diff:
            return self.get_currency_diff('USD')
        """Возвращает курс доллара на сегодня в формате self.format"""
        return self.make_format('USD')

    def get_currency_diff(self,currency):
        response = self.exchange_rates()
        if currency in response:
            return response[currency]['Value'] - response[currency]['Previous']
        return 'Error'

    def get_currency_info(self,currency):
        return self.make_format(currency)

    def max_currency(self):
        response = self.exchange_rates()
        max_currency = max(response, key=lambda x: response[x]['Value'])
        return f"{response[max_currency]['Name']} {response[max_currency]['Value']}"

    def min_currency(self):
        response = self.exchange_rates()
        min_currency = min(response, key=lambda x: response[x]['Value'])
        return f"{response[min_currency]['Name']} {response[min_currency]['Value']}"

    def usd_for_weeks(self,weeks=1):
        end_date = datetime.datetime.now()
        start_date = end_date - datetime.timedelta(weeks=weeks)
        url = f"https://www.cbr-xml-daily.ru/archive/2023/09/27/daily_json.js"
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            if 'Valute' in data:
                if 'USD' in data['Valute']:
                    return data['Valute']['USD']['Value']
        return 'No data'

    def currency_for_weeks(self,currency,weeks=1):
        end_date = datetime.datetime.now()
        start_date = end_date - datetime.timedelta(weeks=weeks)
        url = f"https://www.cbr-xml-daily.ru/archive/{start_date.year}/{start_date.month:02d}/{start_date.day:02d}/daily_json.js"
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            if 'Valute' in data:
                if currency in data['Valute']:
                    return data['Valute'][currency]['Value']
        return 'No data'