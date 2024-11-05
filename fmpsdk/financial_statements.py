import typing
import os
import requests
import logging
from bs4 import BeautifulSoup
import re

from .settings import (
    FINANCIAL_STATEMENT_FILENAME,
    INCOME_STATEMENT_FILENAME,
    BALANCE_SHEET_STATEMENT_FILENAME,
    CASH_FLOW_STATEMENT_FILENAME,
    INCOME_STATEMENT_AS_REPORTED_FILENAME,
    BALANCE_SHEET_STATEMENT_AS_REPORTED_FILENAME,
    CASH_FLOW_STATEMENT_AS_REPORTED_FILENAME,
    DEFAULT_LIMIT,
    BASE_URL_v3,
)
from .url_methods import (
    __return_json_v3,
    __return_json_v4,
    __validate_industry,
    __validate_period,
    __validate_sector,
)
from .data_compression import compress_json_to_tsv

API_KEY = os.getenv('FMP_API_KEY')
SEC_USER_AGENT = os.getenv('SEC_USER_AGENT')

def income_statement(
    symbol: str,
    period: str = "annual",
    limit: int = DEFAULT_LIMIT,
    download: bool = False,
    filename: str = INCOME_STATEMENT_FILENAME,
    tsv: bool = True
) -> typing.Union[typing.List[typing.Dict], str, None]:
    """
    Retrieve income statement data for a company.

    Provides real-time access to a company's revenue, expenses, and net income.
    Useful for tracking profitability, comparing with competitors, and
    identifying business trends. 

    :param symbol: Company ticker (e.g., 'AAPL').
    :param period: 'quarter' or 'annual'. Default is 'annual'.
    :param limit: Number of statements to retrieve. Default is 10.
    :param download: If True, download data as CSV. Default is False.
    :param filename: Name of saved file. Default is INCOME_STATEMENT_FILENAME.
    :param limit: Number of rows to return. Default is DEFAULT_LIMIT.
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts, TSV string, or None if download is True.
    :example: income_statement('AAPL', period='quarter', limit=5)
    """
    path = f"income-statement/{symbol}"
    query_vars = {"apikey": API_KEY, "limit": limit, "period": __validate_period(period)}
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        response = requests.get(f"{BASE_URL_v3}{path}", params=query_vars)
        open(filename, "wb").write(response.content)
        logging.info(f"Saving {symbol} financial statement as {filename}.")
        return None
    else:
        result = __return_json_v3(path=path, query_vars=query_vars)
        return compress_json_to_tsv(result) if tsv else result


def balance_sheet_statement(
    symbol: str,
    period: str = "annual",
    limit: int = DEFAULT_LIMIT,
    download: bool = False,
    filename: str = BALANCE_SHEET_STATEMENT_FILENAME,
    tsv: bool = True
) -> typing.Union[typing.List[typing.Dict], str, None]:
    """
    Retrieve balance sheet data for a company.

    Provides real-time access to a company's assets, liabilities, and equity.
    Useful for assessing financial health, identifying risks, and analyzing
    debt levels, cash flow, and equity position. 

    :param symbol: Company ticker (e.g., 'AAPL') or CIK (e.g., '0000320193').
    :param period: 'quarter' or 'annual'. Default is 'annual'.
    :param limit: Number of statements to retrieve. Default is 10.
    :param download: If True, download data as CSV. Default is False.
    :param filename: Name of saved file. Default is BALANCE_SHEET_STATEMENT_FILENAME.
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts, TSV string, or None if download is True.
    :example: balance_sheet_statement('AAPL', period='quarter', limit=5)
    """
    path = f"balance-sheet-statement/{symbol}"
    query_vars = {"apikey": API_KEY, "limit": limit, "period": __validate_period(period)}
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        response = requests.get(f"{BASE_URL_v3}{path}", params=query_vars)
        open(filename, "wb").write(response.content)
        logging.info(f"Saving {symbol} balance sheet statement as {filename}.")
        return None
    else:
        result = __return_json_v3(path=path, query_vars=query_vars)
        return compress_json_to_tsv(result) if tsv else result


def cash_flow_statement(
    symbol: str,
    period: str = "annual",
    limit: int = DEFAULT_LIMIT,
    download: bool = False,
    filename: str = CASH_FLOW_STATEMENT_FILENAME,
    tsv: bool = True
) -> typing.Union[typing.List[typing.Dict], str, None]:
    """
    Retrieve cash flow statement data for a company.

    Provides real-time access to a company's cash inflows and outflows,
    categorized into operating, investing, and financing activities.
    Useful for assessing cash management, liquidity, and financial health.

    :param symbol: Company ticker (e.g., 'AAPL') or CIK (e.g., '0000320193').
    :param period: 'quarter' or 'annual'. Default is 'annual'.
    :param limit: Number of statements to retrieve. Default is 10.
    :param download: If True, download data as CSV. Default is False.
    :param filename: Name of saved file. Default is CASH_FLOW_STATEMENT_FILENAME.
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts, TSV string, or None if download is True.
    :example: cash_flow_statement('AAPL', period='quarter', limit=5)
    """
    path = f"cash-flow-statement/{symbol}"
    query_vars = {"apikey": API_KEY, "limit": limit, "period": __validate_period(period)}
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        response = requests.get(f"{BASE_URL_v3}{path}", params=query_vars)
        open(filename, "wb").write(response.content)
        logging.info(f"Saving {symbol} financial statement as {filename}.")
        return None
    else:
        result = __return_json_v3(path=path, query_vars=query_vars)
        return compress_json_to_tsv(result) if tsv else result


def income_statement_as_reported(
    symbol: str,
    period: str = "annual",
    limit: int = DEFAULT_LIMIT,
    download: bool = False,
    filename: str = INCOME_STATEMENT_AS_REPORTED_FILENAME,
    tsv: bool = True
) -> typing.Union[typing.List[typing.Dict], str, None]:
    """
    Query FMP /income-statement-as-reported/ API for company's as-reported income statement.

    :param symbol: Company ticker.
    :param period: 'quarter' or 'annual'. Default is 'annual'.
    :param limit: Number of rows to return. Default is DEFAULT_LIMIT.
    :param download: If True, download data as CSV. Default is False.
    :param filename: Name of saved file. Default is INCOME_STATEMENT_AS_REPORTED_FILENAME.
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts, TSV string, or None if download is True.
    :example: income_statement_as_reported('AAPL', period='quarter', limit=5)
    """
    path = f"income-statement-as-reported/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "limit": limit,
        "period": __validate_period(value=period),
    }
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        response = requests.get(f"{BASE_URL_v3}{path}", params=query_vars)
        open(filename, "wb").write(response.content)
        logging.info(f"Saving {symbol} financial statement as {filename}.")
        return None
    else:
        result = __return_json_v3(path=path, query_vars=query_vars)
        return compress_json_to_tsv(result) if tsv else result

def balance_sheet_statement_as_reported(
    symbol: str,
    period: str = "annual",
    limit: int = DEFAULT_LIMIT,
    download: bool = False,
    filename: str = BALANCE_SHEET_STATEMENT_AS_REPORTED_FILENAME,
    tsv: bool = True
) -> typing.Union[typing.List[typing.Dict], str, None]:
    """
    Query FMP /balance-sheet-statement-as-reported/ API for company's as-reported balance sheet.

    :param symbol: Company ticker.
    :param period: 'quarter' or 'annual'. Default is 'annual'.
    :param limit: Number of rows to return. Default is DEFAULT_LIMIT.
    :param download: If True, download data as CSV. Default is False.
    :param filename: Name of saved file. Default is BALANCE_SHEET_STATEMENT_AS_REPORTED_FILENAME.
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts, TSV string, or None if download is True.
    :example: balance_sheet_statement_as_reported('AAPL', period='quarter', limit=5)
    """
    path = f"balance-sheet-statement-as-reported/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "limit": limit,
        "period": __validate_period(value=period),
    }
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        response = requests.get(f"{BASE_URL_v3}{path}", params=query_vars)
        open(filename, "wb").write(response.content)
        logging.info(f"Saving {symbol} financial statement as {filename}.")
        return None
    else:
        result = __return_json_v3(path=path, query_vars=query_vars)
        return compress_json_to_tsv(result) if tsv else result

def cash_flow_statement_as_reported(
    symbol: str,
    period: str = "annual",
    limit: int = DEFAULT_LIMIT,
    download: bool = False,
    filename: str = CASH_FLOW_STATEMENT_AS_REPORTED_FILENAME,
    tsv: bool = True
) -> typing.Union[typing.List[typing.Dict], str, None]:
    """
    Query FMP /cash-flow-statement-as-reported/ API for company's as-reported cash flow statement.

    :param symbol: Company ticker.
    :param period: 'quarter' or 'annual'. Default is 'annual'.
    :param limit: Number of rows to return. Default is DEFAULT_LIMIT.
    :param download: If True, download data as CSV. Default is False.
    :param filename: Name of saved file. Default is CASH_FLOW_STATEMENT_AS_REPORTED_FILENAME.
    :param tsv: If True, return data as a TSV string. Defaults to True.
    :return: List of dicts, TSV string, or None if download is True.
    :example: cash_flow_statement_as_reported('AAPL', period='quarter', limit=5, download=True)
    """
    path = f"cash-flow-statement-as-reported/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "limit": limit,
        "period": __validate_period(value=period),
    }
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        response = requests.get(f"{BASE_URL_v3}{path}", params=query_vars)
        open(filename, "wb").write(response.content)
        logging.info(f"Saving {symbol} financial statement as {filename}.")
        return None
    else:
        result = __return_json_v3(path=path, query_vars=query_vars)
        return compress_json_to_tsv(result) if tsv else result


def financial_statement_full_as_reported(
    symbol: str,
    period: str = "annual",
    tsv: bool = True
) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Query FMP /financial-statement-full-as-reported/ API for company's full as-reported financial statement.

    :param symbol: Company ticker.
    :param period: 'quarter' or 'annual'. Default is 'annual'.
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts or TSV string with full as-reported financial statement data.
    :example: financial_statement_full_as_reported('AAPL', period='quarter')
    """
    path = f"financial-statement-full-as-reported/{symbol}"
    query_vars = {"apikey": API_KEY, "period": __validate_period(value=period)}
    result = __return_json_v3(path=path, query_vars=query_vars)
    return compress_json_to_tsv(result) if tsv else result

def earnings_surprises(
    symbol: str,
    tsv: bool = True
) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Retrieve earnings surprises for a company.

    Provides insights into a company's financial performance vs. market expectations.
    Useful for identifying earnings beats/misses and analyzing trends that can
    impact stock prices and investor sentiment.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts or TSV string with earnings surprises data.
    :example: earnings_surprises('AAPL')
    """
    path = f"earnings-surprises/{symbol}"
    query_vars = {"apikey": API_KEY}
    result = __return_json_v3(path=path, query_vars=query_vars)
    return compress_json_to_tsv(result) if tsv else result

def earning_call_transcript(
    symbol: str,
    year: int,
    quarter: int,
    tsv: bool = True
) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Retrieve the earning call transcript for a specific quarter and year.

    Provides insights into a company's financial performance and management discussions.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param year: Year of the transcript (e.g., 2023).
    :param quarter: Quarter of the transcript (1-4).
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts or TSV string with earning call transcript data.
    :example: earning_call_transcript('AAPL', 2023, 1)
    """
    path = f"earning_call_transcript/{symbol}"
    query_vars = {"apikey": API_KEY, "year": year, "quarter": quarter}
    result = __return_json_v3(path=path, query_vars=query_vars)
    return compress_json_to_tsv(result) if tsv else result


def batch_earning_call_transcript(
    symbol: str,
    year: int,
    tsv: bool = True
) -> typing.Union[typing.List[typing.Dict], str]:
    """
    Retrieve batch earning call transcripts for a specific year.

    Provides insights into a company's financial performance and management discussions
    for multiple quarters in a single year.

    :param symbol: Company ticker (e.g., 'AAPL').
    :param year: Year of the transcripts (e.g., 2023).
    :param tsv: If True, return data in TSV format. Defaults to True.
    :return: List of dicts or TSV string with batch earning call transcript data.
    :example: batch_earning_call_transcript('AAPL', 2023)
    """
    path = f"batch_earning_call_transcript/{symbol}"
    query_vars = {"apikey": API_KEY, "year": year}
    result = __return_json_v4(path=path, query_vars=query_vars)
    return compress_json_to_tsv(result) if tsv else result


def earning_call_transcripts_available_dates(
    symbol: str
) -> typing.Optional[typing.List[typing.List]]:
    """
    Retrieve available dates for earning call transcripts.

    Useful for planning and accessing transcripts for specific quarters and years.

    :param symbol: Company ticker (e.g., 'AAPL').
    :return: List of lists with available dates for earning call transcripts.
    :example: earning_call_transcripts_available_dates('AAPL')
    """
    path = f"earning_call_transcript"
    query_vars = {"apikey": API_KEY, "symbol": symbol}
    return __return_json_v4(path=path, query_vars=query_vars)


def sec_filings(
    symbol: str,
    filing_type: str = "",
    limit: int = DEFAULT_LIMIT
) -> typing.Optional[typing.List[typing.Dict]]:
    """
    Retrieve SEC filing links for a specific company.

    This function provides links to various SEC filings such as 10-K, 10-Q, 8-K, etc.,
    allowing investors to review important financial and operational information.

    :param symbol: The stock symbol of the company (e.g., 'AAPL' for Apple Inc.)
    :param filing_type: The type of SEC filing (e.g., '10-K', '10-Q', '8-K', etc.).
                        If empty, returns all types of filings.
    :param limit: The maximum number of filings to retrieve (default is DEFAULT_LIMIT)
    :return: A list of dictionaries containing SEC filing data,
             or None if the request fails
    :example: sec_filings('AAPL', filing_type='10-K', limit=5)
    """
    path = f"sec_filings/{symbol}"
    query_vars = {
        "apikey": API_KEY,
        "type": filing_type,
        "limit": limit
    }
    return __return_json_v3(path=path, query_vars=query_vars)


def clean_html_content(soup):
    """Convert SEC filing HTML to clean Markdown while preserving document flow."""
    # Remove XBRL and metadata elements
    for element in soup.find_all(['ix:header', 'ix:hidden', 'ix:references', 'ix:resources']):
        element.decompose()
    
    # Get the main content - look specifically for the filing content
    body = soup.find('body')
    if not body:
        return None
        
    def process_element(element):
        """Process each element and convert to appropriate Markdown."""
        if element.name in ['script', 'style']:
            return ''
            
        # Handle headings
        if element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            level = int(element.name[1])
            return f"{'#' * level} {element.get_text().strip()}\n\n"
            
        # Handle paragraphs and div blocks
        if element.name in ['p', 'div']:
            text = element.get_text().strip()
            if not text:
                return ''
                
            # Check for styling
            style = element.get('style', '')
            if 'text-align:center' in style:
                return f"\n<center>{text}</center>\n\n"
            if 'font-weight:700' in style or 'font-weight:bold' in style:
                text = f"**{text}**"
            if 'font-style:italic' in style:
                text = f"*{text}*"
                
            return f"{text}\n\n"
            
        # Handle lists
        if element.name in ['ul', 'ol']:
            items = []
            for li in element.find_all('li', recursive=False):
                prefix = '* ' if element.name == 'ul' else '1. '
                items.append(f"{prefix}{li.get_text().strip()}")
            return '\n'.join(items) + '\n\n'
            
        # Handle tables more naturally - convert to text blocks if they're not data tables
        if element.name == 'table':
            # Check if this is a signature/header table or data table
            if 'signature' in str(element).lower() or len(element.find_all('tr')) < 3:
                text_blocks = []
                for row in element.find_all('tr'):
                    cells = [cell.get_text().strip() for cell in row.find_all(['td', 'th'])]
                    text_blocks.extend(cell for cell in cells if cell)
                return '\n\n'.join(text_blocks) + '\n\n'
            else:
                # Preserve as table for actual tabular data
                return str(element) + '\n\n'
        
        # Recursively process child elements
        return ''.join(process_element(child) for child in element.children if hasattr(child, 'name'))
    
    # Process the document
    markdown_content = process_element(body)
    
    # Clean up extra whitespace and line breaks
    markdown_content = re.sub(r'\n{3,}', '\n\n', markdown_content)
    markdown_content = re.sub(r'^\s+', '', markdown_content)
    
    return markdown_content

def sec_filings_data(symbol, filing_type='10-K', limit=1):
    """:param symbol: Company ticker (e.g., 'AAPL').
    :param filing_type: SEC filing type (e.g., '10-K', '10-Q', '8-K'). Default is all types.
    :param limit: Number of records to retrieve. Default is 1.
    NOTE to LLM's: Limit to maximum of 2 records at a time.
    :return: Final content of the filing rendered as clean Markdown
    :example: sec_filings_data('AAPL', filing_type='10-K', limit=1)
    Note: This function returns unredacted full text of the filings and 
    may not be suitable for LLM processing without very long context windows.
    """
    filings = sec_filings(symbol, filing_type, limit)
    
    if not filings:
        return None

    headers = {'User-Agent': SEC_USER_AGENT}
    finalcontent = """"""
    # Process only the first filing (or up to limit)
    for filing in filings:
        final_link = filing.get('finalLink')

        if final_link:
            try:
                response = requests.get(final_link, headers=headers)
                response.raise_for_status()
                
                soup = BeautifulSoup(response.content, 'html.parser')
                content = clean_html_content(soup)
                
                # Return just the formatted content with minimal metadata
                finalcontent += (f"""\n # {symbol} {filing_type} Filing
                Date: {filing.get('fillingDate')}
                Link: {final_link}

                ---

                {content}""")                
            except requests.RequestException as e:
                finalcontent.append(f"Error fetching content: {str(e)}")
    return finalcontent