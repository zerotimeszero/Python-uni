import requests
import datetime
class Rate:
    def __init__(self, format='value'):
        self.format = format
    def exchange_rates(self):
        r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        return r.json()['Valute']

    def make_format(self, currency):

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
        return self.make_format('EUR')

    def usd(self, diff=False):
        if diff:
            return self.get_currency_diff('USD')
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
        url = f"https://www.cbr-xml-daily.ru/archive/{start_date.year}/{start_date.month:02d}/{start_date.day:02d}/daily_json.js"
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            if 'Valute' in data:
                if 'USD' in data['Valute']:
                    return data['Valute']['USD']['Value']
        return 'Нет данных'

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