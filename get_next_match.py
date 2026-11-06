from services.ApiPalmeiras import ApiPalmeiras
import datetime
import os

def run():
    today_month = datetime.date.today().month
    year_month = datetime.date.today().year

    api_palmeiras = ApiPalmeiras()
    matches_of_the_month = api_palmeiras.get_matches_of_the_month(month=today_month, year=year_month)    
    
    return matches_of_the_month


if __name__ == "__main__":
    next_match = run()
    print(next_match)