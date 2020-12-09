import typing

BASE_URL: str = "https://financialmodelingprep.com/api/v3/"

DEFAULT_LIMIT: int = 10
INDUSTRY_VALUES: typing.List = [
        "Autos",
        "Banks",
        "Banks Diversified",
        "Software",
        "Banks Regional",
        "Beverages Alcoholic",
        "Beverages Brewers",
        "Beverages Non - Alcoholic",
    ]
SECTOR_VALUES: typing.List = [
        "Consumer Cyclical",
        "Energy",
        "Technology",
        "Industrials",
        "Financial Services",
        "Basic Materials",
        "Communication Services",
        "Consumer Defensive",
        "Healthcare",
        "Real Estate",
        "Utilities",
        "Industrial Goods",
        "Financial Services",
        "Conglomerates",
    ]
PERIOD_VALUES: typing.List = ["annual", "quarter"]
EXCHANGE_VALUES: typing.List = [
        "ETF",
        "MUTUAL_FUND",
        "COMMODITY",
        "INDEX",
        "CRYPTO",
        "FOREX",
        "TSX",
        "AMEX",
        "NASDAQ",
        "NYSE",
        "EURONEXT",
    ]

FINANCIAL_STATEMENT_FILENAME: str = "financial_statement.zip"
CASH_FLOW_STATEMENT_FILENAME: str = "cash_flow_statement.csv"
INCOME_STATEMENT_FILENAME: str = "income_statement.csv"
BALANCE_SHEET_STATEMENT_FILENAME: str = "balance_sheet_statement.csv"
INCOME_STATEMENT_AS_REPORTED_FILENAME: str = "income_statement_as_reported.csv"
BALANCE_SHEET_STATEMENT_AS_REPORTED_FILENAME: str = "balance_sheet_as_reported.csv"
CASH_FLOW_STATEMENT_AS_REPORTED_FILENAME: str = "cash_flow_as_reported.csv"
SEC_RSS_FEEDS_FILENAME: str = "sec_rss_feeds.csv"
