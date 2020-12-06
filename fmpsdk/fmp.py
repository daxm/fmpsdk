import typing
import logging
import json
from urllib.request import urlopen
from urllib import parse
import shutil

BASE_URL: str = "https://financialmodelingprep.com/api/v3/"
LIMIT: int = 1  # Default limit value.
FINANCIAL_STATEMENT_FILENAME: str = "financial_statement.zip"
CASH_FLOW_STATEMENT_FILENAME: str = "cash_flow_statement.csv"
INCOME_STATEMENT_FILENAME: str = "income_statement.csv"
BALANCE_SHEET_STATEMENT_FILENAME: str = "balance_sheet_statement.csv"


class FMPSDK:
    def __init__(self, apikey: str, **kwargs):
        """
        Initialize class holding methods common to all main Classes
        :param str apikey: Your API key
        """
        # URL related stuff
        self.__url: typing.Dict = {
            "base": "",
            "path": "",
            "query": {},
        }
        self.url_base: str = BASE_URL
        self.url_path: str = ""  # Empty default value
        self.url_query: typing.Dict = {}  # Empty default value
        self.api_key = apikey  # Store api_key as place that doesn't get erased when clearing URL Query Vars.
        self.symbol = ""

        # Take kwargs and set to values
        for key, value in kwargs.items():
            setattr(self, key, value)

    # ---------------------- API Calls Related methods ----------------------
    def company_profile(self) -> typing.List:
        """
        Query FMP Company Profile API.

        Example:
        https://financialmodelingprep.com/api/v3/profile/AAPL?apikey=demo
        [ {
          "symbol" : "AAPL",
          "price" : 113.02,
          "beta" : 1.34434,
          "volAvg" : 172070917,
          "mktCap" : 1932924420000,
          "lastDiv" : 0.7825,
          "range" : "53.1525-137.98",
          "changes" : -3.77,
          "companyName" : "Apple Inc",
          "currency" : "USD",
          "isin" : "US0378331005",
          "cusip" : "037833100",
          "exchange" : "Nasdaq Global Select",
          "exchangeShortName" : "NASDAQ",
          "industry" : "Consumer Electronics",
          "website" : "https://www.apple.com/",
          "description" : "Apple, Inc. engages in the design, manufacture, and sale of smartphones, personal computers,
           tablets, wearables and accessories, and other variety of related services. The company is headquartered in
           Cupertino, California and currently employs 137,000 full-time employees. The company is considered one of
           the Big Four technology companies, alongside Amazon, Google, and Microsoft. The firm's hardware products
           include the iPhone smartphone, the iPad tablet computer, the Mac personal computer, the iPod portable media
           player, the Apple Watch smartwatch, the Apple TV digital media player, the AirPods wireless earbuds and the
           HomePod smart speaker. Apple's software includes the macOS, iOS, iPadOS, watchOS, and tvOS operating
           systems, the iTunes media player, the Safari web browser, the Shazam acoustic fingerprint utility, and the
           iLife and iWork creativity and productivity suites, as well as professional applications like Final Cut
           Pro, Logic Pro, and Xcode. Its online services include the iTunes Store, the iOS App Store, Mac App Store,
           Apple Music, Apple TV+, iMessage, and iCloud. Other services include Apple Store, Genius Bar, AppleCare,
           Apple Pay, Apple Pay Cash, and Apple Card.",
          "ceo" : "Mr. Timothy Cook",
          "sector" : "Technology",
          "country" : "US",
          "fullTimeEmployees" : "137000",
          "phone" : "14089961010",
          "address" : "1 Apple Park Way",
          "city" : "Cupertino",
          "state" : "CALIFORNIA",
          "zip" : "95014",
          "dcfDiff" : 89.92,
          "dcf" : 123.527,
          "image" : "https://financialmodelingprep.com/image-stock/AAPL.jpg",
          "ipoDate" : "1980-12-12"
        } ]
       """
        self.__init_url_query_vars()
        self.url_path = f"profile/{self.symbol}"
        response = urlopen(self.url)
        data = response.read().decode("utf-8")
        return json.loads(data)

    def quote(self) -> typing.List:
        """
        Query FMP Company Quote API

        Example:
        https://financialmodelingprep.com/api/v3/quote/AAPL?apikey=demo
        [ {
            "symbol" : "AAPL",
            "name" : "Apple Inc.",
            "price" : 120.96000000,
            "changesPercentage" : 0.07000000,
            "change" : 0.08000000,
            "dayLow" : 110.89000000,
            "dayHigh" : 123.70000000,
            "yearHigh" : 137.98000000,
            "yearLow" : 52.76750000,
            "marketCap" : 2068718419968.00000000,
            "priceAvg50" : 112.15875000,
            "priceAvg200" : 85.41895000,
            "volume" : 332607163,
            "avgVolume" : 165778904,
            "exchange" : "NASDAQ",
            "open" : 120.07000000,
            "previousClose" : 120.88000000,
            "eps" : 3.29600000,
            "pe" : 36.69902800,
            "earningsAnnouncement" : "2020-07-30T16:30:00.000+0000",
            "sharesOutstanding" : 17102500165,
            "timestamp" : 1599435459
          } ]
        """
        self.__init_url_query_vars()
        self.url_path = f"quote/{self.symbol}"
        response = urlopen(self.url)
        data = response.read().decode("utf-8")
        return json.loads(data)

    def key_executives(self) -> typing.List:
        """
        Query FMP Company Quote API.

        Example:
        https://financialmodelingprep.com/api/v3/key-executives/AAPL?apikey=demo
        [ {
            "symbol" : "AAPL",
            "yearBorn" : 1950,
            "pay" : 557922,
            "currencyPay" : "USD",
            "name" : "Dr. Arthur Levinson",
            "title" : "Independent Chairman of the Board",
            "gender" : "male",
            "titleSince" : "2011"
          }, {
            "symbol" : "AAPL",
            "yearBorn" : 1960,
            "pay" : 11555466,
            "currencyPay" : "USD",
            "name" : "Mr. Timothy Cook",
            "title" : "Chief Executive Officer, Director",
            "gender" : "male",
            "titleSince" : "2011"
          }, ...
        ]
        """
        self.__init_url_query_vars()
        self.url_path = f"key-executives/{self.symbol}"
        response = urlopen(self.url)
        data = response.read().decode("utf-8")
        return json.loads(data)

    def search(self, query="", limit=1, exchange=""):
        """
        Query FMP Ticker Search API.  Regex via 'query' var for ticker or company name.

        Example:
        https://financialmodelingprep.com/api/v3/search?query=AA&limit=10&exchange=NASDAQ&apikey=demo
        [ {
            "symbol" : "PRAA",
            "name" : "PRA Group, Inc.",
            "currency" : "USD",
            "stockExchange" : "NasdaqGS",
            "exchangeShortName" : "NASDAQ"
          },
          {
            "symbol" : "PAAS",
            "name" : "Pan American Silver Corp.",
            "currency" : "USD",
            "stockExchange" : "NasdaqGS",
            "exchangeShortName" : "NASDAQ"
          }, ...
        ]
        """
        self.__init_url_query_vars()
        self.url_path = f"search/"
        self.query = query
        self.limit = limit
        self.exchange = exchange
        response = urlopen(self.url)
        data = response.read().decode("utf-8")
        return json.loads(data)

    def search_ticker(self, query="", limit=1, exchange=""):
        """
        Query FMP Ticker Search API.  Regex via 'query' var only for ticker.

        Example:
        https://financialmodelingprep.com/api/v3/search?query=AA&limit=10&exchange=NASDAQ&apikey=demo
        [ {
            "symbol" : "PRAA",
            "name" : "PRA Group, Inc.",
            "currency" : "USD",
            "stockExchange" : "NasdaqGS",
            "exchangeShortName" : "NASDAQ"
          },
          {
            "symbol" : "PAAS",
            "name" : "Pan American Silver Corp.",
            "currency" : "USD",
            "stockExchange" : "NasdaqGS",
            "exchangeShortName" : "NASDAQ"
          }, ...
        ]
        """
        self.__init_url_query_vars()
        self.url_path = f"search-ticker/"
        self.query = query
        self.limit = limit
        self.exchange = exchange
        response = urlopen(self.url)
        data = response.read().decode("utf-8")
        return json.loads(data)

    def financial_statement(self):
        """Download company's financial statement."""
        self.__init_url_query_vars()
        self.url_path = f"financial-statements/{self.symbol}"
        self.datatype = "zip"  # Only ZIP format is supported.
        with urlopen(self.url) as response, open(
            FINANCIAL_STATEMENT_FILENAME, "wb"
        ) as out_file:
            logging.info(
                f"Saving {self.symbol} financial statement as {FINANCIAL_STATEMENT_FILENAME}."
            )
            shutil.copyfileobj(response, out_file)

    def income_statement(
        self, period: str = "annual", download: bool = False, limit: int = 120
    ):
        """
        Query FMP API for CIncome Statement.

        Example:
        https://financialmodelingprep.com/api/v3/income-statement/AAPL?limit=120&apikey=demo'
        [ {
            "date" : "2019-09-28",
            "symbol" : "AAPL",
            "fillingDate" : "2019-10-31 00:00:00",
            "acceptedDate" : "2019-10-30 18:12:36",
            "period" : "FY",
            "revenue" : 260174000000,
            "costOfRevenue" : 161782000000,
            "grossProfit" : 98392000000,
            "grossProfitRatio" : 0.378178,
            "researchAndDevelopmentExpenses" : 16217000000,
            "generalAndAdministrativeExpenses" : 18245000000,
            "sellingAndMarketingExpenses" : 0.0,
            "otherExpenses" : 1807000000,
            "operatingExpenses" : 34462000000,
            "costAndExpenses" : 196244000000,
            "interestExpense" : 3576000000,
            "depreciationAndAmortization" : 12547000000,
            "ebitda" : 81860000000,
            "ebitdaratio" : 0.314636,
            "operatingIncome" : 63930000000,
            "operatingIncomeRatio" : 0.24572,
            "totalOtherIncomeExpensesNet" : 422000000,
            "incomeBeforeTax" : 65737000000,
            "incomeBeforeTaxRatio" : 0.252666,
            "incomeTaxExpense" : 10481000000,
            "netIncome" : 55256000000,
            "netIncomeRatio" : 0.212381,
            "eps" : 2.97145,
            "epsdiluted" : 2.97145,
            "weightedAverageShsOut" : 18595652000,
            "weightedAverageShsOutDil" : 18595652000,
            "link" :
                "https://www.sec.gov/Archives/edgar/data/320193/000032019319000119/0000320193-19-000119-index.html",
            "finalLink" : "https://www.sec.gov/Archives/edgar/data/320193/000032019319000119/a10-k20199282019.htm"
          }, ...
        ]
        """
        self.__init_url_query_vars()
        self.url_path = f"income-statement/{self.symbol}"
        self.limit = limit
        self.period = period
        if download:
            self.datatype = "csv"  # Only CSV is supported.
            with urlopen(self.url) as response, open(
                INCOME_STATEMENT_FILENAME, "wb"
            ) as out_file:
                logging.info(
                    f"Saving {self.symbol} financial statement as {INCOME_STATEMENT_FILENAME}."
                )
                shutil.copyfileobj(response, out_file)
        else:
            response = urlopen(self.url)
            data = response.read().decode("utf-8")
            return json.loads(data)

    def balance_sheet_statement(
        self, period: str = "annual", download: bool = False, limit: int = 120
    ):
        """
        Query FMP API for Balance Sheet Statement.

        Example:
        https://financialmodelingprep.com/api/v3/balance-sheet-statement/AAPL?apikey=demo&limit=120'
        [ {
            "date" : "2019-09-28",
            "symbol" : "AAPL",
            "fillingDate" : "2019-10-31 00:00:00",
            "acceptedDate" : "2019-10-30 18:12:36",
            "period" : "FY",
            "cashAndCashEquivalents" : 48844000000,
            "shortTermInvestments" : 51713000000,
            "cashAndShortTermInvestments" : 100557000000,
            "netReceivables" : 45804000000,
            "inventory" : 4106000000,
            "otherCurrentAssets" : 12352000000,
            "totalCurrentAssets" : 162819000000,
            "propertyPlantEquipmentNet" : 37378000000,
            "goodwill" : 0.0,
            "intangibleAssets" : 0.0,
            "goodwillAndIntangibleAssets" : 0.0,
            "longTermInvestments" : 105341000000,
            "taxAssets" : 0.0,
            "otherNonCurrentAssets" : 32978000000,
            "totalNonCurrentAssets" : 175697000000,
            "otherAssets" : 45330000000,
            "totalAssets" : 338516000000,
            "accountPayables" : 46236000000,
            "shortTermDebt" : 5980000000,
            "taxPayables" : 0.0,
            "deferredRevenue" : 5522000000,
            "otherCurrentLiabilities" : 43242000000,
            "totalCurrentLiabilities" : 105718000000,
            "longTermDebt" : 91807000000,
            "deferredRevenueNonCurrent" : 0.0,
            "deferredTaxLiabilitiesNonCurrent" : 0.0,
            "otherNonCurrentLiabilities" : 50503000000,
            "totalNonCurrentLiabilities" : 142310000000,
            "otherLiabilities" : 50503000000,
            "totalLiabilities" : 248028000000,
            "commonStock" : 45174000000,
            "retainedEarnings" : 45898000000,
            "accumulatedOtherComprehensiveIncomeLoss" : -58579000000,
            "othertotalStockholdersEquity" : -1291000000,
            "totalStockholdersEquity" : 90488000000,
            "totalLiabilitiesAndStockholdersEquity" : 338516000000,
            "totalInvestments" : 157054000000,
            "totalDebt" : 108047000000,
            "netDebt" : 59203000000,
            "link" :
                "https://www.sec.gov/Archives/edgar/data/320193/000032019319000119/0000320193-19-000119-index.html",
            "finalLink" : "https://www.sec.gov/Archives/edgar/data/320193/000032019319000119/a10-k20199282019.htm"
          }, ...
        ]
        """
        self.__init_url_query_vars()
        self.url_path = f"balance-sheet-statement/{self.symbol}"
        self.limit = limit
        self.period = period
        if download:
            self.datatype = "csv"  # Only CSV is supported.
            with urlopen(self.url) as response, open(
                BALANCE_SHEET_STATEMENT_FILENAME, "wb"
            ) as out_file:
                logging.info(
                    f"Saving {self.symbol} financial statement as {BALANCE_SHEET_STATEMENT_FILENAME}."
                )
                shutil.copyfileobj(response, out_file)
        else:
            response = urlopen(self.url)
            data = response.read().decode("utf-8")
            return json.loads(data)

    def cash_flow_statement(
        self, period: str = "annual", download: bool = False, limit: int = 120
    ):
        """
        Query FMP API for Cash Flow Statement.

        Example:
        https://financialmodelingprep.com/api/v3/cash-flow-statement/AAPL?apikey=demo&limit=120
        [ {
            "date" : "2019-09-28",
            "symbol" : "AAPL",
            "fillingDate" : "2019-10-31 00:00:00",
            "acceptedDate" : "2019-10-30 18:12:36",
            "period" : "FY",
            "netIncome" : 55256000000,
            "depreciationAndAmortization" : 12547000000,
            "deferredIncomeTax" : -340000000,
            "stockBasedCompensation" : 6068000000,
            "changeInWorkingCapital" : -3488000000,
            "accountsReceivables" : 245000000,
            "inventory" : -289000000,
            "accountsPayables" : -1923000000,
            "otherWorkingCapital" : 57101000000,
            "otherNonCashItems" : 5416000000,
            "netCashProvidedByOperatingActivities" : 69391000000,
            "investmentsInPropertyPlantAndEquipment" : -10495000000,
            "acquisitionsNet" : -624000000,
            "purchasesOfInvestments" : -107528000000,
            "salesMaturitiesOfInvestments" : 98724000000,
            "otherInvestingActivites" : 65819000000,
            "netCashUsedForInvestingActivites" : 45896000000,
            "debtRepayment" : -8805000000,
            "commonStockIssued" : 781000000,
            "commonStockRepurchased" : -66116000000,
            "dividendsPaid" : -14119000000,
            "otherFinancingActivites" : -1936000000,
            "netCashUsedProvidedByFinancingActivities" : -90976000000,
            "effectOfForexChangesOnCash" : 0.0,
            "netChangeInCash" : 24311000000,
            "cashAtEndOfPeriod" : 50224000000,
            "cashAtBeginningOfPeriod" : 25913000000,
            "operatingCashFlow" : 69391000000,
            "capitalExpenditure" : -10495000000,
            "freeCashFlow" : 58896000000,
            "link" :
                "https://www.sec.gov/Archives/edgar/data/320193/000032019319000119/0000320193-19-000119-index.html",
            "finalLink" : "https://www.sec.gov/Archives/edgar/data/320193/000032019319000119/a10-k20199282019.htm"
          }, ...
        ]
        """
        self.__init_url_query_vars()
        self.url_path = f"cash-flow-statement/{self.symbol}"
        self.limit = limit
        self.period = period
        if download:
            self.datatype = "csv"  # Only CSV is supported.
            with urlopen(self.url) as response, open(
                CASH_FLOW_STATEMENT_FILENAME, "wb"
            ) as out_file:
                logging.info(
                    f"Saving {self.symbol} financial statement as {CASH_FLOW_STATEMENT_FILENAME}."
                )
                shutil.copyfileobj(response, out_file)
        else:
            response = urlopen(self.url)
            data = response.read().decode("utf-8")
            return json.loads(data)

    def financial_ratios_ttm(self):
        """
        Query FMP API for Financial Ratios TTM.

        Formulas explained here: https://financialmodelingprep.com/developer/docs/formula/

        Example:
        https://financialmodelingprep.com/api/v3/ratios-ttm/AAPL?apikey=demo
        [ {
          "dividendYielTTM" : 0.006824034334763949,
          "dividendYielPercentageTTM" : 0.682403433476394900,
          "peRatioTTM" : 34.73454758318499,
          "pegRatioTTM" : 53.78668006069268,
          "payoutRatioTTM" : 0.23702974531014653,
          "currentRatioTTM" : 1.4694496317589543,
          "quickRatioTTM" : 1.3124488554103106,
          "cashRatioTTM" : 0.35022765899410396,
          "daysOfSalesOutstandingTTM" : 42.74995709439598,
          "daysOfInventoryOutstandingTTM" : 8.577479515823178,
          "operatingCycleTTM" : 19.118564826770132,
          "daysOfPayablesOutstandingTTM" : 76.16879434299995,
          "cashConversionCycleTTM" : -31.30384229949688,
          "grossProfitMarginTTM" : 0.3818781334784212,
          "operatingProfitMarginTTM" : 0.2451571440569348,
          "pretaxProfitMarginTTM" : 0.24946231062196694,
          "netProfitMarginTTM" : 0.21333761780783403,
          "effectiveTaxRateTTM" : 0.1448102229313348,
          "returnOnAssetsTTM" : 0.1841030553594837,
          "returnOnEquityTTM" : 0.808278686256606,
          "returnOnCapitalEmployedTTM" : 0.30769819750839994,
          "netIncomePerEBTTTM" : 0.8551897770686652,
          "ebtPerEbitTTM" : 1.0,
          "ebitPerRevenueTTM" : 0.24946231062196694,
          "debtRatioTTM" : 0.7722282444287587,
          "debtEquityRatioTTM" : 3.3903599789712513,
          "longTermDebtToCapitalizationTTM" : 0.5670699568758985,
          "totalDebtToCapitalizationTTM" : 0.5942085939166657,
          "interestCoverageTTM" : 22.406362741882585,
          "cashFlowToDebtRatioTTM" : 0.1881070254336571,
          "companyEquityMultiplierTTM" : 4.390359978971252,
          "receivablesTurnoverTTM" : 8.538020265003897,
          "payablesTurnoverTTM" : 4.791988676574664,
          "inventoryTurnoverTTM" : 42.55329311211664,
          "fixedAssetTurnoverTTM" : 6.245171147750336,
          "assetTurnoverTTM" : 0.8629657406473732,
          "operatingCashFlowPerShareTTM" : 1.1429947910208258,
          "freeCashFlowPerShareTTM" : 0.9835725642671928,
          "cashPerShareTTM" : 5.3403862599051894,
          "operatingCashFlowSalesRatioTTM" : 0.07270217668345158,
          "freeCashFlowOperatingCashFlowRatioTTM" : 0.8605223505775992,
          "cashFlowCoverageRatiosTTM" : 0.1881070254336571,
          "shortTermCoverageRatiosTTM" : 1.783091527852409,
          "capitalExpenditureCoverageRatioTTM" : -7.169607490097227,
          "dividendPaidAndCapexCoverageRatioTTM" : -7.169607492149744,
          "priceBookValueRatioTTM" : 28.075194488254336,
          "priceToBookRatioTTM" : 28.075194488254336,
          "priceToSalesRatioTTM" : 7.410185637029544,
          "priceEarningsRatioTTM" : 34.73454758318499,
          "priceToFreeCashFlowsRatioTTM" : 118.44576011206443,
          "priceToOperatingCashFlowsRatioTTM" : 101.92522390758413,
          "priceCashFlowRatioTTM" : 101.92522390758413,
          "priceEarningsToGrowthRatioTTM" : 53.78668006069268,
          "priceSalesRatioTTM" : 7.410185637029544,
          "dividendYieldTTM" : 0.006824034334763949,
          "enterpriseValueMultipleTTM" : 25.353649718331948,
          "priceFairValueTTM" : 28.075194488254336
        } ]
        """
        self.__init_url_query_vars()
        self.url_path = f"ratios-ttm/{self.symbol}"
        response = urlopen(self.url)
        data = response.read().decode("utf-8")
        return json.loads(data)

    def financial_ratios(self, period: str = "annual", limit: int = 120):
        """
        Query FMP API for Financial Ratios.

        Formulas explained here: https://financialmodelingprep.com/developer/docs/formula/

        Example:
        https://financialmodelingprep.com/api/v3/ratios-ttm/AAPL?apikey=demo
        [ {
          "dividendYielTTM" : 0.006824034334763949,
          "dividendYielPercentageTTM" : 0.682403433476394900,
          "peRatioTTM" : 34.73454758318499,
          "pegRatioTTM" : 53.78668006069268,
          "payoutRatioTTM" : 0.23702974531014653,
          "currentRatioTTM" : 1.4694496317589543,
          "quickRatioTTM" : 1.3124488554103106,
          "cashRatioTTM" : 0.35022765899410396,
          "daysOfSalesOutstandingTTM" : 42.74995709439598,
          "daysOfInventoryOutstandingTTM" : 8.577479515823178,
          "operatingCycleTTM" : 19.118564826770132,
          "daysOfPayablesOutstandingTTM" : 76.16879434299995,
          "cashConversionCycleTTM" : -31.30384229949688,
          "grossProfitMarginTTM" : 0.3818781334784212,
          "operatingProfitMarginTTM" : 0.2451571440569348,
          "pretaxProfitMarginTTM" : 0.24946231062196694,
          "netProfitMarginTTM" : 0.21333761780783403,
          "effectiveTaxRateTTM" : 0.1448102229313348,
          "returnOnAssetsTTM" : 0.1841030553594837,
          "returnOnEquityTTM" : 0.808278686256606,
          "returnOnCapitalEmployedTTM" : 0.30769819750839994,
          "netIncomePerEBTTTM" : 0.8551897770686652,
          "ebtPerEbitTTM" : 1.0,
          "ebitPerRevenueTTM" : 0.24946231062196694,
          "debtRatioTTM" : 0.7722282444287587,
          "debtEquityRatioTTM" : 3.3903599789712513,
          "longTermDebtToCapitalizationTTM" : 0.5670699568758985,
          "totalDebtToCapitalizationTTM" : 0.5942085939166657,
          "interestCoverageTTM" : 22.406362741882585,
          "cashFlowToDebtRatioTTM" : 0.1881070254336571,
          "companyEquityMultiplierTTM" : 4.390359978971252,
          "receivablesTurnoverTTM" : 8.538020265003897,
          "payablesTurnoverTTM" : 4.791988676574664,
          "inventoryTurnoverTTM" : 42.55329311211664,
          "fixedAssetTurnoverTTM" : 6.245171147750336,
          "assetTurnoverTTM" : 0.8629657406473732,
          "operatingCashFlowPerShareTTM" : 1.1429947910208258,
          "freeCashFlowPerShareTTM" : 0.9835725642671928,
          "cashPerShareTTM" : 5.3403862599051894,
          "operatingCashFlowSalesRatioTTM" : 0.07270217668345158,
          "freeCashFlowOperatingCashFlowRatioTTM" : 0.8605223505775992,
          "cashFlowCoverageRatiosTTM" : 0.1881070254336571,
          "shortTermCoverageRatiosTTM" : 1.783091527852409,
          "capitalExpenditureCoverageRatioTTM" : -7.169607490097227,
          "dividendPaidAndCapexCoverageRatioTTM" : -7.169607492149744,
          "priceBookValueRatioTTM" : 28.075194488254336,
          "priceToBookRatioTTM" : 28.075194488254336,
          "priceToSalesRatioTTM" : 7.410185637029544,
          "priceEarningsRatioTTM" : 34.73454758318499,
          "priceToFreeCashFlowsRatioTTM" : 118.44576011206443,
          "priceToOperatingCashFlowsRatioTTM" : 101.92522390758413,
          "priceCashFlowRatioTTM" : 101.92522390758413,
          "priceEarningsToGrowthRatioTTM" : 53.78668006069268,
          "priceSalesRatioTTM" : 7.410185637029544,
          "dividendYieldTTM" : 0.006824034334763949,
          "enterpriseValueMultipleTTM" : 25.353649718331948,
          "priceFairValueTTM" : 28.075194488254336
        } ]
        """
        self.__init_url_query_vars()
        self.url_path = f"ratios/{self.symbol}"
        self.limit = limit
        self.period = period
        response = urlopen(self.url)
        data = response.read().decode("utf-8")
        return json.loads(data)

    # ---------------------- URL Related methods ----------------------
    def __init_url_query_vars(self) -> None:
        """
        Reset the URL Query Vars for each API method.
        :return None:
        """
        self.__clear_url_query_vars()
        self.apikey = self.api_key

    def __add_url_query_var(self, key: str, value) -> None:
        """
        Add a key/value to the query portion of the URL. (i.e. after the "?"
        :param str key: Name of query
        :param value: Value of query
        :return None:
        """
        self.__url["query"][key] = value

    def __remove_url_query_var(self, key: str) -> None:
        """
        Remove a key/value from URL query.
        :param str key: Name of query
        :return None:
        """
        if key in self.__url["query"]:
            del self.__url["query"][key]

    def __clear_url_query_vars(self) -> None:
        """
        Remove all URL query values (i.e. everything after "?" in URL)
        :return None:
        """
        self.url_query = {}

    @property
    def url_base(self) -> str:
        """
        Return base part of URL.
        :return str:
        """
        return self.__url["base"]

    @url_base.setter
    def url_base(self, value: str) -> None:
        """
        Set the base part of the URL.
        :param str value:
        :return None:
        """
        self.__url["base"] = value

    @property
    def url_path(self) -> str:
        """
        Return path part of URL.
        :return str:
        """
        return self.__url["path"]

    @url_path.setter
    def url_path(self, value: str) -> None:
        """
        Set the path part of the URL.
        :param str value:
        :return None:
        """
        self.__url["path"] = value

    @property
    def url_query(self) -> typing.Dict:
        """
        Return Dict of parts of URL query.
        :return typing.Dict:
        """
        return self.__url["query"]

    @url_query.setter
    def url_query(self, value: typing.Dict) -> None:
        """
        Set the path part of the URL.
        :param typing.Dict value:
        :return None:
        """
        self.__url["query"] = value

    @property
    def url(self) -> str:
        """
        Return the composed URL.
        :return str:
        """
        tmp = parse.urlsplit(self.url_base)
        return parse.urlunsplit(
            (
                tmp.scheme,
                tmp.netloc,
                f"{tmp.path}{self.url_path}",
                parse.urlencode(self.url_query),
                "",
            )
        )

    @property
    def apikey(self) -> str:
        """
        Return API key.
        :return str:
        """
        if "apikey" in self.__url["query"]:
            return self.__url["query"]["apikey"]
        else:
            return ""

    @apikey.setter
    def apikey(self, value: str) -> None:
        """
        Set apikey.
        :param str value:
        :return None:
        """
        self.__add_url_query_var(key="apikey", value=value)

    @property
    def symbol(self) -> str:
        """
        Return stock symbol.
        :return str:
        """
        return self.__symbol

    @symbol.setter
    def symbol(self, value: str) -> None:
        """
        Set stock symbol.
        :param str value:
        :return None:
        """
        self.__symbol = value

    @property
    def query(self) -> str:
        """
        Return query value.
        :return str:
        """
        if "query" in self.__url["query"]:
            return self.__url["query"]["query"]
        else:
            return ""

    @query.setter
    def query(self, value: str) -> None:
        """
        Set query value
        :param str value: Query string
        :return None:
        """
        self.__add_url_query_var(key="query", value=value)

    @property
    def exchange(self) -> str:
        """
        Return exchange value.
        :return str:
        """
        if "exchange" in self.__url["query"]:
            return self.__url["query"]["exchange"]
        else:
            return ""

    @exchange.setter
    def exchange(self, value: str) -> None:
        """
        Set exchange value
        :param str value: Query string
        :return None:
        """
        valid_exchanges = [
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

        if value in valid_exchanges:
            self.__add_url_query_var(key="exchange", value=value)
        else:
            logging.error(
                f"Value: {value}: Invalid exchange.  Select from {valid_exchanges}."
            )
            self.__add_url_query_var(key="exchange", value="")

    @property
    def limit(self) -> int:
        """
        Return limit value.
        :return int:
        """
        if "limit" in self.__url["query"]:
            return self.__url["query"]["limit"]
        else:
            return LIMIT

    @limit.setter
    def limit(self, value: int) -> None:
        """
        Set limit value
        :param int value: Limit value
        :return None:
        """
        self.__add_url_query_var(key="limit", value=value)

    @property
    def datatype(self) -> str:
        """
        Return data type of file to download.
        :return str:
        """
        if "datatype" in self.__url["query"]:
            return self.__url["query"]["datatype"]
        else:
            return "zip"

    @datatype.setter
    def datatype(self, value: str) -> None:
        """
        Set datatype value
        :param str value: datatype value
        :return None:
        """
        self.__add_url_query_var(key="datatype", value=value)

    @property
    def period(self) -> str:
        """
        Return period of query (Annual or Quarterly).
        :return str:
        """
        if "period" in self.__url["query"]:
            return self.__url["query"]["period"]
        else:
            return "annual"

    @period.setter
    def period(self, value: str) -> None:
        """
        Set period value
        :param str value: period value
        :return None:
        """
        valid_values = ["annual", "quarter"]
        if value in valid_values:
            self.__add_url_query_var(key="period", value=value)
