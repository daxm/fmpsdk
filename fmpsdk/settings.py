import typing

BASE_URL: str = "https://financialmodelingprep.com/api/v3/"

DEFAULT_LIMIT: int = 10
INDUSTRY_VALUES: typing.List = ['Banks', 'Energy', 'Materials', 'Consumer Electronics', 'Software Infrastructure',
                                'Internet Retail', 'Internet Content & Information', 'Auto Manufacturers',
                                'Insurance Diversified', 'Food & Staples Retailing', '', 'Semiconductors',
                                'Credit Services', 'Discount Stores', 'Drug Manufacturers General',
                                'Banks Diversified', 'Household & Personal Products', 'Health Care Plans',
                                'Entertainment', 'Home Improvement Retail', 'Luxury Goods', 'Telecom Services',
                                'Beverages Non-Alcoholic', 'Footwear & Accessories', 'Software Application',
                                'Semiconductor Equipment & Materials', 'Medical Devices', 'Communication Equipment',
                                'Diagnostics & Research', 'Oil & Gas Integrated', 'Communication Services',
                                'Information Technology Services', 'Other Industrial Metals & Mining',
                                'Biotechnology', 'Restaurants', 'Integrated Freight & Logistics',
                                'Specialty Industrial Machinery', 'Utilities Regulated Electric',
                                'Beverages Alcoholic', 'Railroads', 'Specialty Chemicals', 'Insurance Life',
                                'Aerospace & Defense', 'Tobacco', 'Asset Management', 'Chemicals', 'Capital Markets',
                                'Beverages Brewers', 'REIT Specialty', 'Farm & Heavy Construction Machinery',
                                'Electronic Gaming & Multimedia', 'Medical Instruments & Supplies',
                                'Beverages Wineries & Distilleries', 'Metals & Mining', 'Travel Services',
                                'Oil & Gas Midstream', 'Confectioners', 'Apparel Retail',
                                'Drug Manufacturers General Specialty & Generic', 'Financial Data & Stock Exchanges',
                                'Staffing & Employment Services', 'Transportation', 'REIT Industrial',
                                'Banks Regional', 'Insurance Property & Casualty', 'Medical Instruments & Equipment',
                                'Oil & Gas E&P', 'Gold', 'Utilities Diversified', 'Specialty Business Services',
                                'Insurance Brokers', 'Computer Hardware', 'Agriculture', 'Medical Care Facilities',
                                'Software—Infrastructure', 'Insurance', 'Consulting Services', 'Copper',
                                'Waste Management', 'Grocery Stores', 'Leisure', 'Publishing',
                                'Engineering & Construction', 'Software—Application', 'Resorts & Casinos',
                                'Health Information Services', 'Consumer Packaged Goods',
                                'Lodging', 'Auto Parts', 'Education & Training Services', 'Electronic Components',
                                'REIT Office', 'Food Distribution', 'Business Services', 'Autos', 'Packaged Foods',
                                'Real Estate Services', 'Retail Apparel & Specialty', 'Oil & Gas Services',
                                'Pharmaceutical Retailers', 'Agricultural Inputs', 'Building Materials',
                                'Specialty Retail', 'Insurance Reinsurance', 'Building Products & Equipment',
                                'Apparel Manufacturing', 'Oil & Gas Equipment & Services',
                                'Oil & Gas Refining & Marketing', 'Packaging & Containers', 'Tools & Accessories',
                                'Broadcasting', 'Industrial Distribution', 'Airlines', 'REIT Retail', 'Farm Products',
                                'Medical Distribution', 'Utilities Regulated Water', 'REIT Healthcare Facilities',
                                'Residential Construction', 'Steel', 'Scientific & Technical Instruments', 'Trucking',
                                'Solar', 'REIT Residential', 'Drug Manufacturersâ€”Specialty & Generic', 'Gambling',
                                'Automobiles & Components', 'Personal Services', 'Utilities Renewable',
                                'Utilities Regulated', 'Health Care Equipment & Services', 'Conglomerates',
                                'Rental & Leasing Services', 'REITs', 'Auto & Truck Dealerships',
                                'Electrical Equipment & Parts', 'Paper & Paper Products', 'REIT Diversified',
                                'Advertising Agencies', 'Drug Manufacturers—Specialty & Generic',
                                'Utilitiesâ€”Renewable', 'Business Equipment & Supplies',
                                'Furnishings, Fixtures & Appliances', 'Medical Diagnostics & Research',
                                'REIT Mortgage', 'Industrial Products', 'Utilities Regulated Gas',
                                'Utilities Independent Power Producers', 'Insurance Specialty', 'Tobacco Products',
                                'Softwareâ€”Application', 'Security & Protection Services', 'Online Media',
                                'Airports & Air Services', 'REIT Hotel & Motel', 'Forest Products',
                                'Pollution & Treatment Controls', 'Silver', 'Travel & Leisure', 'Oil & Gas Drilling',
                                'Recreational Vehicles', 'Electronics & Computer Distribution',
                                'Financial Conglomerates', 'Uranium', 'Department Stores',
                                'Transportation & Logistics', 'REITâ€”Residential',
                                'Manufacturing Apparel & Furniture', 'Lumber & Wood Production',
                                'Independent Oil & Gas', 'Health Care Providers', 'Shell Companies',
                                'Metal Fabrication', 'Mortgage Finance', 'Insuranceâ€”Property & Casualty',
                                'Real Estate Diversified', 'Utilitiesâ€”Regulated Gas', 'Aluminum',
                                'Banksâ€”Regional', 'Other Precious Metals & Mining', 'Marine Shipping', 'N/A',
                                'REITâ€”Diversified', 'Infrastructure Operations', 'Real Estate Development',
                                'Consulting & Outsourcing', 'Textile Manufacturing',
                                'Pharmaceuticals, Biotechnology & Life Sciences', 'Coal', 'Real Estate',
                                'Softwarare Application', 'Brokers & Exchanges', 'Education', 'Retail Defensive',
                                'Homebuilding & Construction', 'Employment Services', 'Coking Coal',
                                'Diversified Financials', 'Thermal Coal', 'Software & Services',
                                'Utilities—Regulated Water', 'Closed-End Fund Debt', 'Media & Entertainment',
                                'Advertising & Marketing Services', 'Industrial Metals & Minerals', 'Utilities',
                                'Farm & Construction Machinery', 'Food, Beverage & Tobacco',
                                'Real Estateâ€”Development', 'Property Management', 'Consumer Services',
                                'Capital Goods', 'Industrial Electrical Equipment',
                                'Commercial  & Professional Services', 'Retailing', 'Apparel Stores',
                                'Mortgage Investment', 'Electronics Wholesale', 'Auto Dealerships'
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
PERIOD_VALUES: typing.List = [
    "annual",
    "quarter",
]
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
TIME_DELTA_VALUES: typing.List = [
    "1min",
    "5min",
    "15min",
    "30min",
    "1hour",
    "4hour",
]
TECHNICAL_INDICATORS_TIME_DELTA_VALUES: typing.List = [
    "1min",
    "5min",
    "15min",
    "30min",
    "1hour",
    "4hour",
    "daily",
]
SERIES_TYPE_VALUES: typing.List = [
    "line",
]
STATISTICS_TYPE_VALUES: typing.List = [
    "sma",
    "ema",
    "wma",
    "dema",
    "tema",
    "williams",
    "rsa",
    "adx",
    "standardDeviation",
]

FINANCIAL_STATEMENT_FILENAME: str = "financial_statement.zip"
CASH_FLOW_STATEMENT_FILENAME: str = "cash_flow_statement.csv"
INCOME_STATEMENT_FILENAME: str = "income_statement.csv"
BALANCE_SHEET_STATEMENT_FILENAME: str = "balance_sheet_statement.csv"
INCOME_STATEMENT_AS_REPORTED_FILENAME: str = "income_statement_as_reported.csv"
BALANCE_SHEET_STATEMENT_AS_REPORTED_FILENAME: str = "balance_sheet_as_reported.csv"
CASH_FLOW_STATEMENT_AS_REPORTED_FILENAME: str = "cash_flow_as_reported.csv"
SEC_RSS_FEEDS_FILENAME: str = "sec_rss_feeds.csv"
SP500_CONSTITUENTS_FILENAME: str = "sp500_constituents.csv"
NASDAQ_CONSTITUENTS_FILENAME: str = "nasdaq_constituents.csv"
DOWJONES_CONSTITUENTS_FILENAME: str = "dowjones_constituents.csv"
