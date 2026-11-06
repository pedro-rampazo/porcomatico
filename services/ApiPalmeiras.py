import requests
import os

class ApiPalmeiras:
    def __init__(self):
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/jxl,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Cookie': os.environ.get('PALMEIRAS_TOKEN_API'),
            'Priority': 'u=0, i',
            'Sec-Ch-Ua': '"Not:A-Brand";v="8", "Chromium";v="156", "Google Chrome";v="156"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/156.0.0.0 Safari/537.36'
            }

    def request_api(self, endpoint, headers, timeout=10):
        response = requests.get(endpoint, headers=headers, timeout=timeout)
        response.raise_for_status()
        return response.json()


    def get_matches_of_the_month(self, month, year):
        url = 'https://palmeiras.com.br/wp-json/apiverdao/v1/jogos-mes/?mes={month}&ano={year}&v=1'
        response = self.request_api(endpoint=url.format(month=month, year=year), headers=self.headers)
        return response