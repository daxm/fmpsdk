import typing
import os
from .url_methods import __return_json_v3, __return_json_v4
from .data_compression import compress_json_to_tsv

API_KEY = os.getenv('FMP_API_KEY')

def quote_short(
    symbol: str,
    tsv: bool = True
) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Retrieve a simple, real-time stock quote.

    Provides a quick snapshot of a stock's performance, including current price,
    price change, and trading volume. Useful for rapid market analysis,
    calculating stock valuations, or making quick investment decisions.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: Stock quote data or None if request fails.
    :example: quote_short('AAPL')
    """
    path = f"quote-short/{symbol}"
    query_vars = {"apikey": API_KEY}
    result = __return_json_v3(path=path, query_vars=query_vars)
    
    return compress_json_to_tsv(result) if tsv else result

def historical_stock_dividend(
    symbol: str,
    tsv: bool = True
) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Retrieve historical dividend payments for a publicly traded company.

    Provides valuable insights for dividend analysis, including payment dates,
    ex-dividend dates, and dividend per share. Useful for analyzing dividend
    history, identifying consistent dividend payers, and tracking dividend growth.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: Historical dividend data or None if request fails.
    :example: historical_stock_dividend('AAPL')
    """
    path = f"historical-price-full/stock_dividend/{symbol}"
    query_vars = {"apikey": API_KEY}
    result = __return_json_v3(path=path, query_vars=query_vars)
    
    if result and isinstance(result, dict) and 'historical' in result:
        result = result['historical']
    
    if result and isinstance(result, list):
        return compress_json_to_tsv(result) if tsv else result
    else:
        return None

def historical_stock_split(
    symbol: str,
    tsv: bool = True
) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Retrieve historical stock splits for a publicly traded company.

    Provides information on past stock splits, including the date, split ratio,
    and type of split. Useful for analyzing a company's growth history,
    identifying rapidly growing companies, and understanding stock price trends.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: Historical stock split data or None if request fails.
    :example: historical_stock_split('AAPL')
    """
    path = f"historical-price-full/stock_split/{symbol}"
    query_vars = {"apikey": API_KEY}
    result = __return_json_v3(path=path, query_vars=query_vars)
    
    if result:
        if isinstance(result, dict) and 'historical' in result:
            result = result['historical']
        elif isinstance(result, str):
            # If the result is a string, it might be an error message
            print(f"API returned an unexpected result: {result}")
            return None
        
        if isinstance(result, list):
            return compress_json_to_tsv(result) if tsv else result
        else:
            print(f"Unexpected result format: {type(result)}")
            return None
    else:
        return None

def historical_price_full(
    symbol: typing.Union[str, typing.List[str]],
    from_date: str = None,
    to_date: str = None,
    tsv: bool = True
) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Retrieve full historical price data for one or multiple symbols.

    Provides comprehensive historical price data, including open, high, low,
    close prices, and trading volume. Useful for technical analysis, backtesting
    trading strategies, and studying long-term price trends.

    :param symbol: Company ticker or list of tickers (e.g., 'AAPL' or ['AAPL', 'GOOGL']).
    :param from_date: Start date in 'YYYY-MM-DD' format.
    :param to_date: End date in 'YYYY-MM-DD' format.
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: Historical price data or None if request fails.
    :example: historical_price_full('AAPL', from_date='2023-01-01', to_date='2023-12-31')
    """
    if isinstance(symbol, list):
        symbol = ','.join(symbol)
    
    path = f"historical-price-full/{symbol}"
    query_vars = {"apikey": API_KEY}
    
    if from_date:
        query_vars["from"] = from_date
    if to_date:
        query_vars["to"] = to_date

    result = __return_json_v3(path=path, query_vars=query_vars)
    
    if result and 'historical' in result:
        result = result['historical']
    
    return compress_json_to_tsv(result) if tsv else result

def stock_dividend(
    symbol: str,
    tsv: bool = True
) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Retrieve dividend information for a specific stock.

    Provides detailed dividend data, including dividend amount, ex-dividend date,
    and payment date. Useful for dividend investors, income-focused strategies,
    and analyzing a company's dividend policy.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: Dividend data or None if request fails.
    :example: stock_dividend('AAPL')
    """
    path = f"stock_dividend/{symbol}"
    query_vars = {"apikey": API_KEY}
    result = __return_json_v4(path=path, query_vars=query_vars)
    
    return compress_json_to_tsv(result) if tsv else result

def stock_split(
    symbol: str,
    tsv: bool = True
) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Retrieve stock split information for a specific stock.

    Provides details on past stock splits, including split ratios and dates.
    Useful for understanding a company's stock price history, adjusting
    historical data, and identifying growth patterns.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: Stock split data or None if request fails.
    :example: stock_split('AAPL')
    """
    path = f"stock_split/{symbol}"
    query_vars = {"apikey": API_KEY}
    result = __return_json_v4(path=path, query_vars=query_vars)
    
    return compress_json_to_tsv(result) if tsv else result