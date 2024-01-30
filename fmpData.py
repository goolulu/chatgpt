import json
from datetime import time, datetime
import os
from dotenv import load_dotenv
import typing
import fmpsdk

import requests
import inspect

load_dotenv('api.env')
apikey1 = os.environ.get("apikey")

BASE_URL = 'https://financialmodelingprep.com/api/v3/'


def calculate_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' took {execution_time.total_seconds()} seconds to execute.")
        return result

    return wrapper


@calculate_execution_time
def get_financial_score(symbol: str):
    url = f'https://financialmodelingprep.com/api/v4/score?symbol={symbol}&apikey={apikey1}'
    return json.dumps(requests.get(url).json())


@calculate_execution_time
def get_advanced_dcf_valuation(ticker):
    url = f'https://financialmodelingprep.com/api/v4/advanced_discounted_cash_flow?symbol={ticker}&apikey={apikey1}'
    return json.dumps(requests.get(url).json())


def get_levered_dcf_valuation(symbol):
    url = f'https://financialmodelingprep.com/api/v4/advanced_levered_discounted_cash_flow?symbol={symbol}&apikey={apikey1}'
    return json.dumps(requests.get(url).json())


def get_price_target(symbol):
    url = f'https://financialmodelingprep.com/api/v4/price-target?symbol={symbol}&apikey={apikey1}'
    return json.dumps(requests.get(url).json())


def get_price_target_summary(symbol):
    url = f'https://financialmodelingprep.com/api/v4/price-target-summary?symbol={symbol}&apikey={apikey1}'
    return json.dumps(requests.get(url).json())


def get_price_target_by_company(company):
    url = f'https://financialmodelingprep.com/api/v4/price-target-analyst-company?company={company}&apikey={apikey1}'
    return json.dumps(requests.get(url).json())


def get_price_target_consensus(symbol):
    url = f'https://financialmodelingprep.com/api/v4/price-target-consensus?symbol={symbol}&apikey={apikey1}'
    return json.dumps(requests.get(url).json())


def get_stock_price_change(symbol):
    url = f'https://financialmodelingprep.com/api/v3/stock-price-change/{symbol}&apikey={apikey1}'
    return json.dumps(requests.get(url).json())


available_functions = {
    "get_income_statement": fmpsdk.income_statement,
    "get_balance_statement": fmpsdk.balance_sheet_statement,
    "get_cash_flow_statement": fmpsdk.cash_flow_statement,
    "get_key_metrics": fmpsdk.key_metrics,
    "get_financial_ratios": fmpsdk.financial_ratios,
    "get_key_metrics_TTM": fmpsdk.key_metrics_ttm,
    "get_financial_ratios_TTM": fmpsdk.financial_ratios_ttm,
    "get_cashflow_growth": fmpsdk.cash_flow_statement_growth,
    "get_income_growth": fmpsdk.income_statement_growth,
    "get_balance_sheet_growth": fmpsdk.balance_sheet_statement_growth,
    "get_financial_growth": fmpsdk.financial_growth,
    "get_financial_score": get_financial_score,
    "get_enterprise_values": fmpsdk.enterprise_values,
    "get_dcf_valuation": fmpsdk.discounted_cash_flow,
    "get_advanced_dcf_valuation": get_advanced_dcf_valuation,
    "get_levered_dcf_valuation": get_levered_dcf_valuation,
    "get_company_rating": fmpsdk.company_profile,
    "get_historical_rating": fmpsdk.historical_rating,
    "get_price_target": get_price_target,
    "get_price_target_summary": get_price_target_summary,
    "get_price_target_by_company": get_price_target_by_company,
    "get_price_target_consensus": get_price_target_consensus,
    "get_full_quote": fmpsdk.quote,
    "get_stock_price_change": get_stock_price_change,

}
