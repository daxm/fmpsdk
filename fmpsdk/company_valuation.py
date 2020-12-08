from .settings import (
    BASE_URL,
    FINANCIAL_STATEMENT_FILENAME,
    CASH_FLOW_STATEMENT_FILENAME,
    INCOME_STATEMENT_FILENAME,
    BALANCE_SHEET_STATEMENT_FILENAME,
    INCOME_STATEMENT_AS_REPORTED_FILENAME,
    BALANCE_SHEET_STATEMENT_AS_REPORTED_FILENAME,
    CASH_FLOW_STATEMENT_AS_REPORTED_FILENAME,
)
import shutil
from .url_methods import *
from urllib.request import urlopen


def company_profile(apikey: str, symbol: str) -> typing.List[typing.Dict]:
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
    path = f"profile/{symbol}"
    query_vars = {"apikey": apikey}
    return return_response(base=BASE_URL, path=path, query_vars=query_vars)


def quote(apikey: str, symbol: str) -> typing.List[typing.Dict]:
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
    path = f"quote/{symbol}"
    query_vars = {"apikey": apikey}
    return return_response(base=BASE_URL, path=path, query_vars=query_vars)


def key_executives(apikey: str, symbol: str) -> typing.List[typing.Dict]:
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
    path = f"key-executives/{symbol}"
    query_vars = {"apikey": apikey}
    return return_response(base=BASE_URL, path=path, query_vars=query_vars)


def search(
    apikey: str, query: str = "", limit: int = 1, exchange: str = ""
) -> typing.List[typing.Dict]:
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
    path = f"search/"
    query_vars = {
        "apikey": apikey,
        "limit": limit,
        "query": query,
        "exchange": set_exchange(value=exchange),
    }
    return return_response(base=BASE_URL, path=path, query_vars=query_vars)


def search_ticker(
    apikey: str, query: str = "", limit: int = 1, exchange: str = ""
) -> typing.List[typing.Dict]:
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
    path = f"search-ticker/"
    query_vars = {
        "apikey": apikey,
        "limit": limit,
        "query": query,
        "exchange": set_exchange(value=exchange),
    }
    return return_response(base=BASE_URL, path=path, query_vars=query_vars)


def financial_statement(
    apikey: str, symbol: str, filename: str = FINANCIAL_STATEMENT_FILENAME
) -> None:
    """Download company's financial statement."""
    path = f"financial-statements/{symbol}"
    query_vars = {
        "apikey": apikey,
        "datatype": "zip",  # Only ZIP format is supported.
    }
    url = make_url(base=BASE_URL, path=path, query_vars=query_vars)
    with urlopen(url) as response, open(filename, "wb") as out_file:
        logging.info(f"Saving {symbol} financial statement as {filename}.")
        shutil.copyfileobj(response, out_file)


def income_statement(
    apikey: str,
    symbol: str,
    period: str = "annual",
    limit: int = 120,
    download: bool = False,
    filename: str = INCOME_STATEMENT_FILENAME,
) -> typing.Union[typing.List[typing.Dict], None]:
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
    path = f"income-statement/{symbol}"
    query_vars = {"apikey": apikey, "limit": limit, "period": set_period(period)}
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        url = make_url(base=BASE_URL, path=path, query_vars=query_vars)
        with urlopen(url) as response, open(filename, "wb") as out_file:
            logging.info(f"Saving {symbol} financial statement as {filename}.")
            shutil.copyfileobj(response, out_file)
    else:
        return return_response(base=BASE_URL, path=path, query_vars=query_vars)


def balance_sheet_statement(
    apikey: str,
    symbol: str,
    period: str = "annual",
    limit: int = 120,
    download: bool = False,
    filename: str = BALANCE_SHEET_STATEMENT_FILENAME,
) -> typing.Union[typing.List[typing.Dict], None]:
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
    path = f"balance-sheet-statement/{symbol}"
    query_vars = {"apikey": apikey, "limit": limit, "period": set_period(period)}
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        url = make_url(base=BASE_URL, path=path, query_vars=query_vars)
        with urlopen(url) as response, open(filename, "wb") as out_file:
            logging.info(f"Saving {symbol} financial statement as {filename}.")
            shutil.copyfileobj(response, out_file)
    else:
        return return_response(base=BASE_URL, path=path, query_vars=query_vars)


def cash_flow_statement(
    apikey: str,
    symbol: str,
    period: str = "annual",
    limit: int = 120,
    download: bool = False,
    filename: str = CASH_FLOW_STATEMENT_FILENAME,
) -> typing.Union[typing.List[typing.Dict], None]:
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
    path = f"cash-flow-statement/{symbol}"
    query_vars = {"apikey": apikey, "limit": limit, "period": set_period(period)}
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        url = make_url(base=BASE_URL, path=path, query_vars=query_vars)
        with urlopen(url) as response, open(filename, "wb") as out_file:
            logging.info(f"Saving {symbol} financial statement as {filename}.")
            shutil.copyfileobj(response, out_file)
    else:
        return return_response(base=BASE_URL, path=path, query_vars=query_vars)


def financial_statement_symbol_lists(apikey: str) -> typing.List[typing.Dict]:
    """
    List of symbols that have financial statements

    Example:
    https://financialmodelingprep.com/api/v3/financial-statement-symbol-lists?apikey=demo
    [
      "02M.DE", "0A00.L", "0A02.L", "0A05.L", "0A0C.L", "0A0D.L", "0A0E.L", "0A0F.L", "0A0H.L", "0A0I.L",
      "0A0J.L", "0A0K.L", "0A0L.L", "0A0M.L", "0A0S.L", "0A0V.L", "0A0W.L", "0A0X.L", "0A10.L", "0A14.L",
      "0A15.L", "0A18.L", "0A1C.L", "0A1J.L", "0A1K.L", "0A1L.L", "0A1M.L", "0A1N.L", "0A1O.L", "0A1R.L",
      "0A1S.L", "0A1U.L", "0A1V.L", "0A1W.L", "0A1X.L", "0A20.L", "0A21.L", "0A23.L", "0A26.L", "0A27.L",
      "0A28.L", "0A29.L", "0A2A.L", "0A2G.L", "0A2H.L", "0A2I.L", "0A2O.L", "0A2P.L", "0A2S.L", "0A2T.L",
      "0A2X.L", "0A2Z.L", "0A33.L", "0A34.L", "0A36.L", "0A37.L", "0A39.L", "0ACT.L", "0AH3.L", "0AH7.L",
      "0AHI.L", "0AHJ.L", "0AI4.L", "0AJ1.L", "0AR9.L", "0B67.L", "0BDR.L", "0BFA.L", "0BJP.L", "0BNT.L",
      "0C6Y.L", "0CDX.L", "0CHZ.L", "0CIJ.L", "0CUM.L", "0CUN.L", "0CXC.L", "0D00.L", "0D1X.L", "0DDP.L",
      "0DH7.L", "0DHC.L", "0DHJ.L", "0DI7.L", "0DJI.L", "0DJV.L", "0DK7.L", "0DK9.L", "0DKX.L", "0DLI.L",
      "0DMQ.L", "0DNH.L", "0DNW.L", "0DO7.L", "0DOL.L", "0DOS.L", "0DP0.L", "0DP4.L", "0DPB.L", "0DPM.L",
      "0DPU.L", "0DQ7.L", "0DQK.L", "0DQZ.L", "0DRH.L", "0DRV.L", "0DSJ.L", "0DTF.L", "0DTI.L", "0DTK.L",
      "0DU3.L", "0DUI.L", "0DUK.L", "0DVE.L", "0DVR.L", "0DWL.L", "0DWV.L", "0DXG.L", "0DXU.L", "0DYD.L",
      "0DYQ.L", "0DZ0.L", "0DZC.L", "0DZJ.L", "0E1L.L", "0E1Y.L", "0E3C.L", "0E4K.L", "0E4Q.L", "0E5M.L",
      "0E6Y.L", "0E7S.L", "0E7Z.L", "0E9V.L", "0EA2.L", "0EAQ.L", "0EAW.L", "0EBQ.L", "0EDD.L", "0EDE.L", ...
    ]
    """
    path = f"financial-statement-symbol-lists"
    query_vars = {"apikey": apikey}
    return return_response(base=BASE_URL, path=path, query_vars=query_vars)


def income_statement_growth(
    apikey: str, symbol: str, limit: int = 120
) -> typing.List[typing.Dict]:
    """
    Income statements growth

    Example:
    https://financialmodelingprep.com/api/v3/income-statement-growth/AAPL?apikey=demo&limit=40
    [ {
        "date" : "2019-09-28",
        "symbol" : "AAPL",
        "period" : "FY",
        "growthRevenue" : -0.0204107758052674178,
        "growthCostOfRevenue" : -0.0120545201397200714,
        "growthGrossProfit" : -0.0338475436718742306,
        "growthGrossProfitRatio" : -0.0137154213078027384,
        "growthResearchAndDevelopmentExpenses" : 0.139154256813711713,
        "growthGeneralAndAdministrativeExpenses" : 0.0921879676743490029,
        "growthSellingAndMarketingExpenses" : 0,
        "growthOtherExpenses" : 0,
        "growthOperatingExpenses" : 0.113797226980382013,
        "growthCostAndExpenses" : 0.00794567969717047476,
        "growthInterestExpense" : 0.103703703703703701,
        "growthDepreciationAndAmortization" : 0.150784187838209655,
        "growthEBITDA" : -0.0430879293011946773,
        "growthEBITDARatio" : -0.0231486655986487197,
        "growthOperatingIncome" : -0.0982820389855849214,
        "growthOperatingIncomeRatio" : -0.0794935191428786103,
        "growthTotalOtherIncomeExpensesNet" : -1.95691609977324266,
        "growthIncomeBeforeTax" : -0.0982949947190101952,
        "growthIncomeBeforeTaxRatio" : -0.0795040967033286694,
        "growthIncomeTaxExpense" : -0.117166442048517519,
        "growthNetIncome" : -0.0718113251919168111,
        "growthNetIncomeRatio" : -0.0524712012920381735,
        "growthEPS" : -0.0262266179034436608,
        "growthEPSDiluted" : -0.0262266179034436608,
        "growthWeightedAverageShsOut" : -0.0702376688188197512,
        "growthWeightedAverageShsOutDil" : -0.0702376688188197512
      }, ...
    ]
    """
    path = f"income-statement-growth/{symbol}"
    query_vars = {
        "apikey": apikey,
        "limit": limit,
    }
    return return_response(base=BASE_URL, path=path, query_vars=query_vars)


def balance_sheet_statement_growth(
    apikey: str, symbol: str, limit: int = 120
) -> typing.List[typing.Dict]:
    """
    Balance Sheet statements growth

    Example:
    https://financialmodelingprep.com/api/v3/income-statement-growth/AAPL?apikey=demo&limit=40
    [ {
        "date" : "2019-09-28",
        "symbol" : "AAPL",
        "period" : "FY",
        "growthRevenue" : -0.0204107758052674178,
        "growthCostOfRevenue" : -0.0120545201397200714,
        "growthGrossProfit" : -0.0338475436718742306,
        "growthGrossProfitRatio" : -0.0137154213078027384,
        "growthResearchAndDevelopmentExpenses" : 0.139154256813711713,
        "growthGeneralAndAdministrativeExpenses" : 0.0921879676743490029,
        "growthSellingAndMarketingExpenses" : 0,
        "growthOtherExpenses" : 0,
        "growthOperatingExpenses" : 0.113797226980382013,
        "growthCostAndExpenses" : 0.00794567969717047476,
        "growthInterestExpense" : 0.103703703703703701,
        "growthDepreciationAndAmortization" : 0.150784187838209655,
        "growthEBITDA" : -0.0430879293011946773,
        "growthEBITDARatio" : -0.0231486655986487197,
        "growthOperatingIncome" : -0.0982820389855849214,
        "growthOperatingIncomeRatio" : -0.0794935191428786103,
        "growthTotalOtherIncomeExpensesNet" : -1.95691609977324266,
        "growthIncomeBeforeTax" : -0.0982949947190101952,
        "growthIncomeBeforeTaxRatio" : -0.0795040967033286694,
        "growthIncomeTaxExpense" : -0.117166442048517519,
        "growthNetIncome" : -0.0718113251919168111,
        "growthNetIncomeRatio" : -0.0524712012920381735,
        "growthEPS" : -0.0262266179034436608,
        "growthEPSDiluted" : -0.0262266179034436608,
        "growthWeightedAverageShsOut" : -0.0702376688188197512,
        "growthWeightedAverageShsOutDil" : -0.0702376688188197512
      }, ...
    ]
    """
    path = f"balance-sheet-statement-growth/{symbol}"
    query_vars = {
        "apikey": apikey,
        "limit": limit,
    }
    return return_response(base=BASE_URL, path=path, query_vars=query_vars)


def cash_flow_statement_growth(
    apikey: str, symbol: str, limit: int = 120
) -> typing.List[typing.Dict]:
    """
    Cash Flow statements growth

    Example:
    https://financialmodelingprep.com/api/v3/income-statement-growth/AAPL?apikey=demo&limit=40
    [ {
        "date" : "2019-09-28",
        "symbol" : "AAPL",
        "period" : "FY",
        "growthRevenue" : -0.0204107758052674178,
        "growthCostOfRevenue" : -0.0120545201397200714,
        "growthGrossProfit" : -0.0338475436718742306,
        "growthGrossProfitRatio" : -0.0137154213078027384,
        "growthResearchAndDevelopmentExpenses" : 0.139154256813711713,
        "growthGeneralAndAdministrativeExpenses" : 0.0921879676743490029,
        "growthSellingAndMarketingExpenses" : 0,
        "growthOtherExpenses" : 0,
        "growthOperatingExpenses" : 0.113797226980382013,
        "growthCostAndExpenses" : 0.00794567969717047476,
        "growthInterestExpense" : 0.103703703703703701,
        "growthDepreciationAndAmortization" : 0.150784187838209655,
        "growthEBITDA" : -0.0430879293011946773,
        "growthEBITDARatio" : -0.0231486655986487197,
        "growthOperatingIncome" : -0.0982820389855849214,
        "growthOperatingIncomeRatio" : -0.0794935191428786103,
        "growthTotalOtherIncomeExpensesNet" : -1.95691609977324266,
        "growthIncomeBeforeTax" : -0.0982949947190101952,
        "growthIncomeBeforeTaxRatio" : -0.0795040967033286694,
        "growthIncomeTaxExpense" : -0.117166442048517519,
        "growthNetIncome" : -0.0718113251919168111,
        "growthNetIncomeRatio" : -0.0524712012920381735,
        "growthEPS" : -0.0262266179034436608,
        "growthEPSDiluted" : -0.0262266179034436608,
        "growthWeightedAverageShsOut" : -0.0702376688188197512,
        "growthWeightedAverageShsOutDil" : -0.0702376688188197512
      }, ...
    ]
    """
    path = f"cash-flow-statement-growth/{symbol}"
    query_vars = {
        "apikey": apikey,
        "limit": limit,
    }
    return return_response(base=BASE_URL, path=path, query_vars=query_vars)


def income_statement_as_reported(
    apikey: str,
    symbol: str,
    period: str = "annual",
    limit: int = 120,
    download: bool = False,
    filename: str = INCOME_STATEMENT_AS_REPORTED_FILENAME,
) -> typing.Union[typing.List[typing.Dict], None]:
    """
    Query FMP API for Income Statement as Reported.

    Example:
    https://financialmodelingprep.com/api/v3/income-statement-as-reported/AAPL?limit=10&apikey=demo
    [ {
        "date" : "2019-09-28",
        "symbol" : "AAPL",
        "period" : "FY",
        "costofgoodsandservicessold" : "161782000000.000000",
        "netincomeloss" : 5.5256E10,
        "researchanddevelopmentexpense" : 1.6217E10,
        "grossprofit" : 9.8392E10,
        "othercomprehensiveincomelossreclassificationadjustmentfromaociforsaleofsecuritiesnetoftax" : -2.5E7,
        "othercomprehensiveincomelossavailableforsalesecuritiesadjustmentnetoftax" : 3.827E9,
        "othercomprehensiveincomelossderivativesqualifyingashedgesnetoftax" : -6.38E8,
        "othercomprehensiveincomelossforeigncurrencytransactionandtranslationadjustmentnetoftax" : -4.08E8,
        "weightedaveragenumberofdilutedsharesoutstanding" : 4.648913E9,
        "weightedaveragenumberofsharesoutstandingbasic" : 4.617834E9,
        "othercomprehensiveincomeunrealizedgainlossonderivativesarisingduringperiodnetoftax" : -6.61E8,
        "operatingincomeloss" : 6.393E10,
        "othercomprehensiveincomelossreclassificationadjustmentfromaocionderivativesnetoftax" : -2.3E7,
        "incomelossfromcontinuingoperationsbeforeincometaxesextraordinaryitemsnoncontrollinginterest" : 6.5737E10,
        "earningspersharebasic" : 11.97,
        "incometaxexpensebenefit" : 1.0481E10,
        "revenuefromcontractwithcustomerexcludingassessedtax" : "260174000000.000000",
        "nonoperatingincomeexpense" : 1.807E9,
        "operatingexpenses" : 3.4462E10,
        "earningspersharediluted" : 11.89,
        "othercomprehensiveincomeunrealizedholdinggainlossonsecuritiesarisingduringperiodnetoftax" : 3.802E9,
        "sellinggeneralandadministrativeexpense" : 1.8245E10,
        "othercomprehensiveincomelossnetoftaxportionattributabletoparent" : 2.781E9,
        "comprehensiveincomenetoftax" : 5.8037E10
      }, ...
    ]
    """
    path = f"income-statement-as-reported/{symbol}"
    query_vars = {"apikey": apikey, "limit": limit, "period": set_period(value=period)}
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        url = make_url(base=BASE_URL, path=path, query_vars=query_vars)
        with urlopen(url) as response, open(filename, "wb") as out_file:
            logging.info(f"Saving {symbol} financial statement as {filename}.")
            shutil.copyfileobj(response, out_file)
    else:
        return return_response(base=BASE_URL, path=path, query_vars=query_vars)


def balance_sheet_statement_as_reported(
    apikey: str,
    symbol: str,
    period: str = "annual",
    limit: int = 120,
    download: bool = False,
    filename: str = BALANCE_SHEET_STATEMENT_AS_REPORTED_FILENAME,
) -> typing.Union[typing.List[typing.Dict], None]:
    """
    Query FMP API for Balance Sheet Statement as Reported.

    Example:
    https://financialmodelingprep.com/api/v3/balance-sheet-statement-as-reported/AAPL?limit=10&apikey=demo
    [ {
        "date" : "2019-09-28",
        "symbol" : "AAPL",
        "period" : "FY",
        "liabilitiesandstockholdersequity" : "338516000000.000000",
        "liabilities" : "248028000000.000000",
        "liabilitiescurrent" : "105718000000.000000",
        "commonstocksharesauthorized" : 1.26E10,
        "cashandcashequivalentsatcarryingvalue" : 4.8844E10,
        "retainedearningsaccumulateddeficit" : 4.5898E10,
        "liabilitiesnoncurrent" : "142310000000.000000",
        "propertyplantandequipmentnet" : 3.7378E10,
        "commonstocksincludingadditionalpaidincapital" : 4.5174E10,
        "commercialpaper" : 6.0E9,
        "longtermdebtcurrent" : 1.026E10,
        "commonstocksharesoutstanding" : 4.443236E9,
        "otherliabilitiesnoncurrent" : 5.0503E10,
        "marketablesecuritiescurrent" : 5.1713E10,
        "otherliabilitiescurrent" : 3.772E10,
        "assetscurrent" : "162819000000.000000",
        "longtermdebtnoncurrent" : 9.1807E10,
        "contractwithcustomerliabilitycurrent" : 5.522E9,
        "nontradereceivablescurrent" : 2.2878E10,
        "commonstocksharesissued" : 4.443236E9,
        "stockholdersequity" : 9.0488E10,
        "accountsreceivablenetcurrent" : 2.2926E10,
        "accountspayablecurrent" : 4.6236E10,
        "assets" : "338516000000.000000",
        "assetsnoncurrent" : "175697000000.000000",
        "otherassetscurrent" : 1.2352E10,
        "otherassetsnoncurrent" : 3.2978E10,
        "inventorynet" : 4.106E9,
        "marketablesecuritiesnoncurrent" : "105341000000.000000",
        "accumulatedothercomprehensiveincomelossnetoftax" : -5.84E8
      }, ...
    ]
    """
    path = f"balance-sheet-statement-as-reported/{symbol}"
    query_vars = {"apikey": apikey, "limit": limit, "period": set_period(value=period)}
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        url = make_url(base=BASE_URL, path=path, query_vars=query_vars)
        with urlopen(url) as response, open(filename, "wb") as out_file:
            logging.info(f"Saving {symbol} financial statement as {filename}.")
            shutil.copyfileobj(response, out_file)
    else:
        return return_response(base=BASE_URL, path=path, query_vars=query_vars)


def cash_flow_statement_as_reported(
    apikey: str,
    symbol: str,
    period: str = "annual",
    limit: int = 120,
    download: bool = False,
    filename: str = CASH_FLOW_STATEMENT_AS_REPORTED_FILENAME,
) -> typing.Union[typing.List[typing.Dict], None]:
    """
    Query FMP API for Cash Flow Statement as Reported.

    Example:
    https://financialmodelingprep.com/api/v3/cash-flow-statement-as-reported/AAPL?limit=10&apikey=demo
    [ {
        "date" : "2019-09-28",
        "symbol" : "AAPL",
        "period" : "FY",
        "paymentsforrepurchaseofcommonstock" : 6.6897E10,
        "sharebasedcompensation" : 6.068E9,
        "netincomeloss" : 5.5256E10,
        "increasedecreaseinaccountspayable" : -1.923E9,
        "proceedsfrompaymentsforotherfinancingactivities" : -1.05E8,
        "paymentsrelatedtotaxwithholdingforsharebasedcompensation" : 2.817E9,
        "increasedecreaseinotheroperatingliabilities" : -4.7E9,
        "othernoncashincomeexpense" : 6.52E8,
        "paymentstoacquirebusinessesnetofcashacquired" : 6.24E8,
        "deferredincometaxexpensebenefit" : -3.4E8,
        "cashcashequivalentsrestrictedcashandrestrictedcashequivalents" : 5.0224E10,
        "cashcashequivalentsrestrictedcashandrestrictedcashequivalentsperiodincreasedecreaseincludingexchangerateeffect" : 2.4311E10,
        "netcashprovidedbyusedinoperatingactivities" : 6.9391E10,
        "proceedsfromsaleofavailableforsalesecuritiesdebt" : 5.6988E10,
        "repaymentsoflongtermdebt" : 8.805E9,
        "incometaxespaidnet" : 1.5263E10,
        "proceedsfromissuanceoflongtermdebt" : 6.963E9,
        "paymentstoacquireotherinvestments" : 1.001E9,
        "netcashprovidedbyusedininvestingactivities" : 4.5896E10,
        "increasedecreaseincontractwithcustomerliability" : -6.25E8,
        "interestpaidnet" : 3.423E9,
        "netcashprovidedbyusedinfinancingactivities" : -9.0976E10,
        "proceedsfromrepaymentsofcommercialpaper" : -5.977E9,
        "proceedsfromsaleandmaturityofotherinvestments" : 1.634E9,
        "paymentstoacquireavailableforsalesecuritiesdebt" : 3.963E10,
        "paymentstoacquirepropertyplantandequipment" : 1.0495E10,
        "paymentsforproceedsfromotherinvestingactivities" : 1.078E9,
        "increasedecreaseinotherreceivables" : -2.931E9,
        "paymentsofdividends" : 1.4119E10,
        "increasedecreaseininventories" : 2.89E8,
        "increasedecreaseinaccountsreceivable" : -2.45E8,
        "proceedsfromissuanceofcommonstock" : 7.81E8,
        "depreciationdepletionandamortization" : 1.2547E10,
        "proceedsfrommaturitiesprepaymentsandcallsofavailableforsalesecurities" : 4.0102E10,
        "increasedecreaseinotheroperatingassets" : -8.73E8
      }, ...
    ]
    """
    path = f"cash-flow-statement-as-reported/{symbol}"
    query_vars = {"apikey": apikey, "limit": limit, "period": set_period(value=period)}
    if download:
        query_vars["datatype"] = "csv"  # Only CSV is supported.
        url = make_url(base=BASE_URL, path=path, query_vars=query_vars)
        with urlopen(url) as response, open(filename, "wb") as out_file:
            logging.info(f"Saving {symbol} financial statement as {filename}.")
            shutil.copyfileobj(response, out_file)
    else:
        return return_response(base=BASE_URL, path=path, query_vars=query_vars)


def financial_statement_full_as_reported(
    apikey: str, symbol: str, period: str = "annual",
) -> typing.List[typing.Dict]:
    """
    Query FMP API for Financial Statement Full as Reported.

    Example:
    https://financialmodelingprep.com/api/v3/financial-statement-full-as-reported/AAPL?apikey=demo
    [ {
        "date" : "2019-09-28",
        "symbol" : "AAPL",
        "period" : "FY",
        "numberofsignificantvendors" : 2.0,
        "entitycurrentreportingstatus" : "Yes",
        "machineryequipmentandinternalusesoftwaremember" : 6.9797E10,
        "otherliabilitiesmember" : 1.05E8,
        "entityemerginggrowthcompany" : "false",
        "incometaxreconciliationtaxcreditsresearch" : 5.48E8,
        "sharebasedcompensation" : 6.068E9,
        "unrecordedunconditionalpurchaseobligationbalanceonsecondanniversary" : 2.386E9,
        "nonoperatingincomeexpense" : 1.807E9,
        "incometaxespaidnet" : 1.5263E10,
        "federalincometaxexpensebenefitcontinuingoperations" : 3.445E9,
        "japansegmentmember" : 9.369E9,
        "currentforeigntaxexpensebenefit" : 3.962E9,
        "debtsecuritiesavailableforsalecontinuousunrealizedlossposition12monthsorlonger" : 2.8167E10,
        "proceedsfromsaleofavailableforsalesecuritiesdebt" : 5.6988E10,
        "commonstocksharesoutstanding" : 4.443236E9,
        "unrecognizedtaxbenefitsthatwouldimpacteffectivetaxrate" : 8.6E9,
        "decreaseinunrecognizedtaxbenefitsisreasonablypossible" : 2.0E9,
        "deferredtaxassetsnet" : 1.964E10,
        "deferredtaxassetsgoodwillandintangibleassets" : 1.1433E10,
        "interestratecontractmember" : -7000000.0,
        "othercomprehensiveincomelossavailableforsalesecuritiesadjustmentnetoftax" : 3.827E9,
        "entitytaxidentificationnumber" : "94-2404110",
        "incometaxreconciliationforeignincometaxratedifferential" : -2.625E9,
        "paymentsrelatedtotaxwithholdingforsharebasedcompensation" : 2.817E9,
        "increasedecreaseinotheroperatingliabilities" : -4.7E9,
        "deferredtaxassetsliabilitiesnet" : 8.045E9,
        "debtinstrumentmaturityyearrangestart" : 2022.0,
        "propertyplantandequipmentnet" : 3.7378E10,
        "commonstocksincludingadditionalpaidincapital" : 4.5174E10,
        "weightedaveragenumberofdilutedsharesoutstanding" : 4.648913E9,
        "commercialpaper" : 6.0E9,
        "commonstockmember" : "NASDAQ",
        "employeeservicesharebasedcompensationnonvestedawardstotalcompensationcostnotyetrecognized" : 1.05E10,
        "stockrepurchasedandretiredduringperiodshares" : 3.452E8,
        "greaterchinasegmentmember" : 1.6232E10,
        "costofgoodsandservicessold" : "161782000000.000000",
        "longtermdebtcurrent" : 1.026E10,
        "accumulatedtranslationadjustmentmember" : -4.08E8,
        "cashcashequivalentsrestrictedcashandrestrictedcashequivalentsperiodincreasedecreaseincludingexchangerateeffect" : 2.4311E10,
        "debtinstrumentunamortizeddiscountpremiumanddebtissuancecostsnet" : 2.24E8,
        "repaymentsoflongtermdebt" : 8.805E9,
        "earningspersharediluted" : 11.89,
        "netincomeloss" : 5.5256E10,
        "proceedsfromissuanceoflongtermdebt" : 6.963E9,
        "unrecordedunconditionalpurchaseobligationbalanceonfifthanniversary" : 2.18E8,
        "incomelossfromcontinuingoperationsbeforeincometaxesextraordinaryitemsnoncontrollinginterest" : 6.5737E10,
        "incomelossfromcontinuingoperationsbeforeincometaxesforeign" : 4.43E10,
        "crosscurrencyinterestratecontractmember" : "P23Y",
        "localphonenumber" : "996-1010",
        "collateralalreadyreceivedaggregatefairvalue" : 1.6E9,
        "interestpaidnet" : 3.423E9,
        "gainlossfromcomponentsexcludedfromassessmentoffairvaluehedgeeffectivenessnet" : 7.77E8,
        "accumulateddepreciationdepletionandamortizationpropertyplantandequipment" : 5.8579E10,
        "othercomprehensiveincomeunrealizedgainlossonderivativesarisingduringperiodbeforetax" : -9.59E8,
        "proceedsfromrepaymentsofcommercialpaper" : -5.977E9,
        "proceedsfromsaleandmaturityofotherinvestments" : 1.634E9,
        "longtermdebtnoncurrent" : 9.1807E10,
        "maximumlengthoftimeforeigncurrencycashflowhedge" : "P12M",
        "stockissuedduringperiodvaluenewissues" : 7.81E8,
        "netcashprovidedbyusedinoperatingactivities" : 6.9391E10,
        "operatingleasesfutureminimumpaymentsdue" : 1.0838E10,
        "proceedsfromrepaymentsofshorttermdebtmaturinginthreemonthsorless" : -3.248E9,
        "stockrepurchasedandretiredduringperiodvalue" : 6.71E10,
        "proceedsfromrepaymentsofshorttermdebtmaturinginmorethanthreemonths" : -2.729E9,
        "restrictedinvestments" : 1.89E10,
        "leaseholdimprovementsmember" : 9.075E9,
        "standardproductwarrantyaccrualpayments" : 3.857E9,
        "accountsreceivablenetcurrent" : 2.2926E10,
        "performanceobligationsinarrangements" : 3.0,
        "sharespaidfortaxwithholdingforsharebasedcompensation" : 1.48E7,
        "currentstateandlocaltaxexpensebenefit" : 4.75E8,
        "repaymentsofshorttermdebtmaturinginmorethanthreemonths" : 1.6603E10,
        "derivativefairvalueofderivativenet" : -4.07E8,
        "upfrontpaymentunderacceleratedsharerepurchasearrangement" : 1.2E10,
        "americassegmentmember" : 3.5099E10,
        "deferredfederalincometaxexpensebenefit" : -2.939E9,
        "operatingleasesfutureminimumpaymentsduethereafter" : 5.373E9,
        "longtermmarketablesecuritiesmaturitiesterm" : "P1Y",
        "cashandcashequivalentsatcarryingvalue" : 4.8844E10,
        "documentannualreport" : "true",
        "otherassetscurrent" : 1.2352E10,
        "unfavorableinvestigationoutcomeeustateaidrulesmember" : 1.9E8,
        "othernonoperatingincomeexpense" : 4.22E8,
        "maximumlengthoftimehedgedininterestratecashflowhedge1" : "P8Y",
        "deferredtaxassetsunrealizedlossesonavailableforsalesecuritiesgross" : 0.0,
        "definedcontributionplanmaximumannualcontributionsperemployeeamount" : 19000.0,
        "debtsecuritiesavailableforsaleunrealizedlossposition" : 5.6318E10,
        "acceleratedsharerepurchasearrangementfebruary2019member" : 1.2E10,
        "increasedecreaseinotheroperatingassets" : -8.73E8,
        "accumulatednetunrealizedinvestmentgainlossmember" : 3.827E9,
        "restofasiapacificsegmentmember" : 6.055E9,
        "unrecordedunconditionalpurchaseobligationbalanceonfourthanniversary" : 1.162E9,
        "contractwithcustomerliability" : 8.1E9,
        "tradeaccountsreceivablemember" : 0.0,
        "securityexchangename" : "NASDAQ",
        "proceedsfromissuanceofcommonstock" : 7.81E8,
        "interestcostsincurred" : 3.2E9,
        "adjustmentstoadditionalpaidincapitaltaxeffectfromsharebasedcompensationincludingtransferpricing" : 0.0,
        "revenueremainingperformanceobligationpercentage" : 0.68,
        "liabilitiescurrent" : "105718000000.000000",
        "sharebasedcompensationarrangementbysharebasedpaymentawardofferingterm" : "P6M",
        "increasedecreaseinaccountspayable" : -1.923E9,
        "grossprofit" : 9.8392E10,
        "reclassificationfromaocicurrentperiodbeforetaxattributabletoparent" : 0.0,
        "sharebasedcompensationarrangementbysharebasedpaymentawardequityinstrumentsotherthanoptionsvestedinperiod" :
        4.2088E7,
        "retainedearningsaccumulateddeficit" : 4.5898E10,
        "proceedsfrompaymentsforotherfinancingactivities" : -1.05E8,
        "definedcontributionplanemployermatchingcontributionpercentofmatch" : 0.5,
        "othercomprehensiveincomelossreclassificationadjustmentfromaocionderivativesnetoftax" : -2.3E7,
        "losscontingencyestimateofpossibleloss" : 1.29E10,
        "currentfiscalyearenddate" : "--09-28",
        "employeestockpurchaseplanmaximumannualpurchasesperemployeeamount" : 25000.0,
        "longtermdebtfairvalue" : "107500000000.000000",
        "hedgeaccountingadjustmentsrelatedtolongtermdebt" : 6.12E8,
        "paymentstoacquirebusinessesnetofcashacquired" : 6.24E8,
        "investmentincomeinterestanddividend" : 4.961E9,
        "othercomprehensiveincomeunrealizedgainlossonderivativesarisingduringperiodnetoftax" : -6.61E8,
        "changeinunrealizedgainlossonhedgediteminfairvaluehedge1" : -3.086E9,
        "accruedincometaxesnoncurrent" : 2.9545E10,
        "operatingexpenses" : 3.4462E10,
        "cashmember" : 0.0,
        "operatingincomeloss" : 6.393E10,
        "deferredtaxassetstaxdeferredexpensecompensationandbenefitssharebasedcompensationcost" : 7.49E8,
        "a20132018debtissuancesmember" : 2047.0,
        "noncashactivitiesinvolvingpropertyplantandequipmentnetincreasedecreasetoaccountspayableandothercurrentliabilities" : -2.9E9,
        "sharebasedcompensationarrangementbysharebasedpaymentawardequityinstrumentsotherthanoptionsgrantsinperiod" :
        3.6852E7,
        "security12btitle" : "1.000% Notes due 2022",
        "derivativefairvalueofderivativeasset" : 6.85E8,
        "otherassetsmember" : 6.85E8,
        "paymentsforrepurchaseofcommonstock" : 6.6897E10,
        "paymentstoacquireotherinvestments" : 1.001E9,
        "netcashprovidedbyusedininvestingactivities" : 4.5896E10,
        "employeestockmember" : 25000.0,
        "unrecordedunconditionalpurchaseobligationbalanceonfirstanniversary" : 2.476E9,
        "assetscurrent" : "162819000000.000000",
        "sharebasedcompensationarrangementbysharebasedpaymentawardnumberofsharesavailableforgrant" : 1100000.0,
        "othernoncashincomeexpense" : 6.52E8,
        "netcashprovidedbyusedinfinancingactivities" : -9.0976E10,
        "paymentstoacquireavailableforsalesecuritiesdebt" : 3.963E10,
        "derivativeinstrumentsgainlossreclassifiedfromaccumulatedociintoincomeeffectiveportionnet" : -1.23E8,
        "restrictedcashandcashequivalentsatcarryingvalue" : 2.3E7,
        "restrictedcashandcashequivalentsnoncurrent" : 1.357E9,
        "debtsecuritiesavailableforsalecontinuousunrealizedlosspositionlessthan12monthsaccumulatedloss" : 1.38E8,
        "interestexpense" : 3.576E9,
        "entityinteractivedatacurrent" : "Yes",
        "debtsecuritiesavailableforsaleunrealizedlosspositionaccumulatedloss" : 2.81E8,
        "debtinstrumentcarryingamount" : "101679000000.000000",
        "contractwithcustomerliabilitycurrent" : 5.522E9,
        "weightedaveragenumberofsharesoutstandingbasic" : 4.617834E9,
        "documentfiscalyearfocus" : 2019.0,
        "sharebasedcompensationarrangementbysharebasedpaymentawardmaximumemployeesubscriptionrate" : 0.1,
        "documentperiodenddate" : "2019-09-28",
        "sharebasedcompensationarrangementbysharebasedpaymentawardequityinstrumentsotherthanoptionsnonvestednumber"
        : 8.1517E7,
        "unrecognizedtaxbenefitsincometaxpenaltiesandinterestexpense" : 7.3E7,
        "liabilities" : "248028000000.000000",
        "sharebasedcompensationarrangementbysharebasedpaymentawardequityinstrumentsotherthanoptionsgrantsinperiodweightedaveragegrantdatefairvalue" : 215.95,
        "debtinstrumentinterestratestatedpercentage" : 0.0295,
        "losscontingencyestimateofpossiblelossreductioninperiod" : 1.9E8,
        "operatingleasesfutureminimumpaymentsdueinfouryears" : 9.12E8,
        "commonstockparorstatedvaluepershare" : 1.0E-5,
        "availableforsaledebtsecuritiesaccumulatedgrossunrealizedgainbeforetax" : 1.202E9,
        "sharebasedcompensationarrangementbysharebasedpaymentawardpurchasepriceofcommonstockpercent" : 0.85,
        "incometaxreconciliationstateandlocalincometaxes" : 4.23E8,
        "fairvalueinputslevel1member" : 0.0,
        "lesseeoperatingleasetermofcontract" : "P10Y",
        "debtinstrumentinterestrateeffectivepercentage" : 0.0171,
        "contractwithcustomerliabilityrevenuerecognized" : 5.9E9,
        "unrecognizedtaxbenefitsreductionsresultingfromlapseofapplicablestatuteoflimitations" : 7.9E7,
        "entityfilercategory" : "Large Accelerated Filer",
        "longtermdebtmaturitiesrepaymentsofprincipalinyeartwo" : 8.75E9,
        "accountspayablecurrent" : 4.6236E10,
        "equitysecuritieswithoutreadilydeterminablefairvalueamount" : 2.9E9,
        "sharebasedcompensationarrangementbysharebasedpaymentawardequityinstrumentsotherthanoptionsnumberofsharesofcommonsharesawardeduponsettlement" : 1.0,
        "unrecordedunconditionalpurchaseobligationdueafterfiveyears" : 1.1E8,
        "weightedaveragenumberdilutedsharesoutstandingadjustment" : 3.1079E7,
        "accumulatedothercomprehensiveincomemember" : 2.781E9,
        "fairvaluehedgingmember" : -3.086E9,
        "derivativeassetsreductionformasternettingarrangements" : 2.7E9,
        "researchanddevelopmentexpense" : 1.6217E10,
        "allocatedsharebasedcompensationexpense" : 6.068E9,
        "availableforsalesecuritiesdebtsecurities" : "205898000000.000000",
        "liabilitiesandstockholdersequity" : "338516000000.000000",
        "availableforsaledebtsecuritiesamortizedcostbasis" : "204977000000.000000",
        "nontradereceivablemember" : 2.0,
        "incometaxreconciliationincometaxexpensebenefitatfederalstatutoryincometaxrate" : 1.3805E10,
        "entityaddresscityortown" : "Cupertino",
        "derivativenotionalamount" : 7.6868E10,
        "othercomprehensiveincomelossreclassificationadjustmentfromaociforsaleofsecuritiesnetoftax" : -2.5E7,
        "foreigncurrencydebtmember" : -5.8E7,
        "othercomprehensiveincomelosstaxportionattributabletoparent1" : -1.3E7,
        "employeeservicesharebasedcompensationnonvestedawardstotalcompensationcostnotyetrecognizedperiodforrecognition1" : "P2Y6M",
        "entityregistrantname" : "Apple Inc.",
        "cashcashequivalentsrestrictedcashandrestrictedcashequivalents" : 5.0224E10,
        "entityaddressaddressline1" : "One Apple Park Way",
        "reclassificationoutofaccumulatedothercomprehensiveincomemember" : -1.34E8,
        "stockissuedduringperiodsharessharebasedpaymentarrangementnetofshareswithheldfortaxes" : 3.3455E7,
        "landandbuildingmember" : 1.7085E10,
        "deferredtaxliabilitiesminimumtaxonforeignearnings" : 1.0809E10,
        "europesegmentmember" : 1.9195E10,
        "effectiveincometaxratereconciliationsharebasedcompensationexcesstaxbenefitamount" : -6.39E8,
        "numberofcustomerswithsignificantaccountsreceivablebalance" : 0.0,
        "marketablesecuritiesnoncurrent" : "105341000000.000000",
        "sharebasedcompensationarrangementbysharebasedpaymentawardawardvestingperiod1" : "P4Y",
        "derivativecounterpartycreditriskexposure" : 3.23E8,
        "changeinunrealizedgainlossonfairvaluehedginginstruments1" : 3.088E9,
        "operatingleasesrentexpensenet" : 1.3E9,
        "othercurrentliabilitiesmember" : 1.6E9,
        "amendmentflag" : "false",
        "sharebasedcompensationarrangementbysharebasedpaymentawardequityinstrumentsotherthanoptionsnonvestedweightedaveragegrantdatefairvalue" : 169.18,
        "foreignexchangecontractmember" : "P12M",
        "unrecognizedtaxbenefits" : 1.5619E10,
        "increasedecreaseincontractwithcustomerliability" : -6.25E8,
        "sharebasedcompensationarrangementbysharebasedpaymentawardequityinstrumentsotherthanoptionsforfeituresweightedaveragegrantdatefairvalue" : 162.85,
        "deferredincometaxexpensebenefit" : -3.4E8,
        "entityaddressstateorprovince" : "CA",
        "propertyplantandequipmentusefullife" : "P30Y",
        "unrecognizedtaxbenefitsincreasesresultingfrompriorperiodtaxpositions" : 5.845E9,
        "documenttype" : "10-K",
        "paymentsforproceedsfromotherinvestingactivities" : 1.078E9,
        "entitysmallbusiness" : "false",
        "revenuefromcontractwithcustomerexcludingassessedtax" : "260174000000.000000",
        "currentfederaltaxexpensebenefit" : 6.384E9,
        "sharebasedcompensationarrangementbysharebasedpaymentawardequityinstrumentsotherthanoptionsaggregateintrinsicvaluenonvested" : 1.7838E10,
        "amountutilizedundersharerepurchaseprogram" : 9.61E10,
        "debtinstrumentmaturityyearrangeend" : 2049.0,
        "commonstocksharesauthorized" : 1.26E10,
        "deferredtaxassetsdeferredincome" : 1.372E9,
        "paymentsofdividends" : 1.4119E10,
        "debtsecuritiesavailableforsalecontinuousunrealizedlossposition12monthsorlongeraccumulatedloss" : 1.43E8,
        "entityincorporationstatecountrycode" : "CA",
        "effectiveincometaxratecontinuingoperations" : 0.159,
        "factorbywhicheachrsugrantedreducesandeachrsucanceledorsharewithheldfortaxesincreasessharesavailableforgrant
        " : 2.0,
        "increasedecreaseininventories" : 2.89E8,
        "ocibeforereclassificationsbeforetaxattributabletoparent" : -4.21E8,
        "dividends" : 1.4129E10,
        "entitywellknownseasonedissuer" : "Yes",
        "increasedecreaseinaccountsreceivable" : -2.45E8,
        "entityvoluntaryfilers" : "No",
        "otherliabilitiescurrent" : 3.772E10,
        "otheraccruedliabilitiesnoncurrent" : 2.0958E10,
        "operatingleasesfutureminimumpaymentsduecurrent" : 1.306E9,
        "proceedsfrommaturitiesprepaymentsandcallsofavailableforsalesecurities" : 4.0102E10,
        "revenues" : 2.06E8,
        "retainedearningsmember" : 6.7101E10,
        "depreciation" : 1.13E10,
        "longtermdebtmaturitiesrepaymentsofprincipalafteryearfive" : 5.3802E10,
        "cityareacode" : 408.0,
        "employeeservicesharebasedcompensationtaxbenefitfromcompensationexpense" : 1.967E9,
        "accumulatednetgainlossfromdesignatedorqualifyingcashflowhedgesmember" : -6.38E8,
        "sharebasedcompensationarrangementbysharebasedpaymentawardequityinstrumentsotherthanoptionsforfeitedinperiod
        " : 5402000.0,
        "entityaddresspostalzipcode" : 95014.0,
        "comprehensiveincomenetoftax" : 5.8037E10,
        "adjustmentstoadditionalpaidincapitalsharebasedcompensationrequisiteserviceperiodrecognitionvalue" : 6.194E9,
        "fairvalueinputslevel2member" : "107500000000.000000",
        "deferredincometaxliabilities" : 1.1595E10,
        "othercomprehensiveincomelossforeigncurrencytransactionandtranslationadjustmentnetoftax" : -4.08E8,
        "concentrationriskpercentage1" : 0.59,
        "stockholdersequity" : 9.0488E10,
        "effectiveincometaxratereconciliationtaxcutsandjobsactof2017amount" : 0.0,
        "cashflowhedgingmember" : -1.23E8,
        "propertyplantandequipmentgross" : 9.5957E10,
        "tradingsymbol" : "AAPL",
        "foreignincometaxexpensebenefitcontinuingoperations" : 6.628E9,
        "operatingleasesfutureminimumpaymentsdueintwoyears" : 1.276E9,
        "sharebasedcompensationarrangementbysharebasedpaymentawardequityinstrumentsotherthanoptionsvestedinperiodweightedaveragegrantdatefairvalue" : 135.21,
        "employeestockplan2014planmember" : 2.464E8,
        "a2019debtissuancemember" : 2049.0,
        "documenttransitionreport" : "false",
        "othercomprehensiveincomelossderivativesqualifyingashedgesnetoftax" : -6.38E8,
        "liabilitiesnoncurrent" : "142310000000.000000",
        "shorttermdebtweightedaverageinterestrate" : 0.0224,
        "incometaxreconciliationotheradjustments" : 6.5E7,
        "depreciationdepletionandamortization" : 1.2547E10,
        "deferredforeignincometaxexpensebenefit" : 2.666E9,
        "unrecordedunconditionalpurchaseobligationbalanceonthirdanniversary" : 1.859E9,
        "operatingleasesfutureminimumpaymentsdueinthreeyears" : 1.137E9,
        "definedcontributionplanemployermatchingcontributionpercent" : 0.06,
        "debtsecuritiesavailableforsalecontinuousunrealizedlosspositionlessthan12months" : 2.8151E10,
        "deferredtaxassetstaxdeferredexpensereservesandaccruals" : 5.389E9,
        "unrecognizedtaxbenefitsdecreasesresultingfrompriorperiodtaxpositions" : 6.86E8,
        "stateandlocalincometaxexpensebenefitcontinuingoperations" : 4.08E8,
        "deferredstateandlocalincometaxexpensebenefit" : -6.7E7,
        "otherliabilitiesnoncurrent" : 5.0503E10,
        "commonstockincludingadditionalpaidincapitalmember" : 0.0,
        "deferredtaxassetsother" : 6.97E8,
        "standardproductwarrantyaccrual" : 3.57E9,
        "deferredtaxliabilitiesundistributedforeignearnings" : 3.3E8,
        "marketablesecuritiescurrent" : 5.1713E10,
        "derivativefairvalueofderivativeliability" : 1.05E8,
        "unrecognizedtaxbenefitsdecreasesresultingfromsettlementswithtaxingauthorities" : 8.52E8,
        "longtermdebtmaturitiesrepaymentsofprincipalinyearfour" : 9.29E9,
        "othergeneralandadministrativeexpense" : 5.803E9,
        "longtermdebtmaturitiesrepaymentsofprincipalinyearfive" : 1.0039E10,
        "commonstockdividendspersharedeclared" : 3.0,
        "directorplanmember" : 1100000.0,
        "adjustmentsrelatedtotaxwithholdingforsharebasedcompensation" : 1.029E9,
        "unrecordedunconditionalpurchaseobligationbalancesheetamount" : 8.211E9,
        "incometaxexpensebenefit" : 1.0481E10,
        "othercomprehensiveincomelossnetoftaxportionattributabletoparent" : 2.781E9,
        "restrictedstockunitsrsumember" : 3.0E9,
        "derivativeliabilitiesreductionformasternettingarrangements" : 2.7E9,
        "nontradereceivablescurrent" : 2.2878E10,
        "sharebasedcompensationarrangementbysharebasedpaymentawardequityinstrumentsotherthanoptionsvestedinperiodtotalfairvalue" : 8.6E9,
        "othercomprehensiveincomeunrealizedholdinggainlossonsecuritiesarisingduringperiodnetoftax" : 3.802E9,
        "inventorynet" : 4.106E9,
        "increasedecreaseinotherreceivables" : -2.931E9,
        "entitycentralindexkey" : 320193.0,
        "paymentstoacquirepropertyplantandequipment" : 1.0495E10,
        "debtinstrumentterm" : "P9M",
        "revenueremainingperformanceobligationexpectedtimingofsatisfactionperiod1" : "P1Y",
        "availableforsaledebtsecuritiesaccumulatedgrossunrealizedlossbeforetax" : 2.81E8,
        "unrecognizedtaxbenefitsincometaxpenaltiesandinterestaccrued" : 1.3E9,
        "entityfilenumber" : "001-36743",
        "assets" : "338516000000.000000",
        "seniornotes" : 1.0E9,
        "assetsnoncurrent" : "175697000000.000000",
        "earningspersharebasic" : 11.97,
        "documentfiscalperiodfocus" : "FY",
        "standardproductwarrantyaccrualwarrantiesissued" : 3.735E9,
        "proceedsfromshorttermdebtmaturinginmorethanthreemonths" : 1.3874E10,
        "entityshellcompany" : "false",
        "sellinggeneralandadministrativeexpense" : 1.8245E10,
        "deferredtaxliabilitiesother" : 4.56E8,
        "operatingleasesfutureminimumpaymentsdueinfiveyears" : 8.34E8,
        "netinvestmenthedgingmember" : 1.0E9,
        "longtermdebtmaturitiesrepaymentsofprincipalinyearthree" : 9.528E9,
        "effectiveincometaxratereconciliationatfederalstatutoryincometaxrate" : 0.21,
        "noncurrentassets" : 3.7378E10,
        "otherassetsnoncurrent" : 3.2978E10,
        "commonstocksharesissued" : 4.443236E9,
        "antidilutivesecuritiesexcludedfromcomputationofearningspershareamount" : 1.55E7,
        "unrecognizedtaxbenefitsincreasesresultingfromcurrentperiodtaxpositions" : 1.697E9,
        "longtermdebtmaturitiesrepaymentsofprincipalinnexttwelvemonths" : 1.027E10,
        "accumulatedothercomprehensiveincomelossnetoftax" : -5.84E8
      }, ...
    ]
    """
    path = f"financial-statement-full-as-reported/{symbol}"
    query_vars = {"apikey": apikey, "period": set_period(value=period)}
    return return_response(base=BASE_URL, path=path, query_vars=query_vars)


def financial_ratios_ttm(apikey: str, symbol: str) -> typing.List[typing.Dict]:
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
    path = f"ratios-ttm/{symbol}"
    query_vars = {"apikey": apikey}
    return return_response(base=BASE_URL, path=path, query_vars=query_vars)


def financial_ratios(
    apikey: str, symbol: str, period: str = "annual", limit: int = 120
) -> typing.List[typing.Dict]:
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
    path = f"ratios/{symbol}"
    query_vars = {"apikey": apikey, "limit": limit, "period": set_period(value=period)}
    return return_response(base=BASE_URL, path=path, query_vars=query_vars)


def enterprise_values(
    apikey: str, symbol: str, period: str = "annual", limit: int = 120
) -> typing.List[typing.Dict]:
    """
    Query FMP API for Enterprise Values.

    Example:
    https://financialmodelingprep.com/api/v3/enterprise-values/AAPL?limit=40&apikey=demo
    [ {
        "symbol" : "AAPL",
        "date" : "2019-09-28",
        "stockPrice" : 62.262501,
        "numberOfShares" : 4648913000,
        "marketCapitalization" : 289452950311.413,
        "minusCashAndCashEquivalents" : 48844000000,
        "addTotalDebt" : 97787000000,
        "enterpriseValue" : 338395950311.413
      },
      {
        "symbol" : "AAPL",
        "date" : "2018-09-29",
        "stockPrice" : 53.060001,
        "numberOfShares" : 5000109000,
        "marketCapitalization" : 265305788540.109,
        "minusCashAndCashEquivalents" : 25913000000,
        "addTotalDebt" : 105699000000,
        "enterpriseValue" : 345091788540.109
      }, ...
    ]
    """
    path = f"enterprise-values/{symbol}"
    query_vars = {"apikey": apikey, "limit": limit, "period": set_period(value=period)}
    return return_response(base=BASE_URL, path=path, query_vars=query_vars)
