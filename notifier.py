from nsetools import Nse
import json
import requests
import time
from datetime import datetime, timedelta
import logging

IFTTT_WEBHOOKS_URL = 'https://maker.ifttt.com/trigger/{}/with/key/cDipGnE4T-XHuKQ5qG-fPf'
nse = Nse()

def get_stock_details(company):
    message_details = {}
    if nse.is_valid_code(company):
        company_details = nse.get_quote(company)
        message_details['last_traded_price'] = company_details['lastPrice']
        message_details['upper_circuit'] = company_details['pricebandupper']
        message_details['lower_circuit'] = company_details['pricebandlower']
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        message_details['OccurredAt'] = dt_string
        message_details['company_name'] = company_details['companyName']
    else:
        message_details = {}
    return message_details

def post_ifttt_webhook(event, message_details):
    print("entered the fun")
    data = {
        'value1': message_details['company_name'],
        'value2': "Upper: "+str(message_details['upper_circuit'])+" , Lower: "+str(message_details['lower_circuit']),
        'value3': "Price: "+str(message_details['last_traded_price'])+" at: "+str(message_details['OccurredAt'])
    }
    ifttt_event_url = IFTTT_WEBHOOKS_URL.format(event)
    print("Before Post")
    response = requests.post(ifttt_event_url, json=data)
    print(response.status_code)

def check_upper_or_lower(company_details):
    if company_details['last_traded_price'] != (company_details['upper_circuit'] or company_details['lower_circuit']):
        return True
    return False

def loop_companies(company_list):
    while True:
        for i in company_list:
            print("Company Name: "+i)
            company_details = get_stock_details(i)
            if check_upper_or_lower(company_details):
                post_ifttt_webhook('notify_stock', company_details)
        time.sleep(30)
