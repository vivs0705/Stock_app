import datetime
class StockData():
    trade_cntr = 0
    stocks = []
    def __init__(self,symbol,pval,lsdiv=0,type='Common',fixdiv=0):
        self.symbol = symbol
        if type != 'Common' and type != 'Preferred':
            raise TypeError('Type must be Common or Preferred')
        if not isinstance(lsdiv,int) and not isinstance(lsdiv,float):
            raise TypeError('Last Dividend must be Integer or Float')
        if not isinstance(fixdiv,int) and not isinstance(fixdiv,float):
            raise TypeError('Fixed Dividend must be Integer or Float')
        if not isinstance(pval,int) and not isinstance(pval,float):
            raise TypeError('Par Value must be Integer or Float')
        self.type = type
        self.lsdiv = lsdiv
        self.fixdiv = fixdiv
        self.pval = pval
        self.trade_dict = {}
        self.vwsp = 0
        self.stocks.append(self)
        print('Stock Entry Added: Symbol - {}, Type - {}, Last Dividend - {}, Fixed Divided - {}, Par Value - {}'.format(self.symbol,self.type,self.lsdiv,self.fixdiv,self.pval))
    def stockstats(self,price=1):
        if (not isinstance(price,int) and not isinstance(price,float)) or (price <= 0):
            raise TypeError('Price must be Integer or Float and must be greater than zero')
        if self.type == 'Common':
            div_yield = self.lsdiv/price
        else:
            div_yield = (self.fixdiv * self.pval)/(100*price)
        pe_ratio = 0
        if div_yield != 0:
            pe_ratio = price/div_yield
        print('Stock {}: Price: {}  - Dividend Yield: {}, P/E Ratio: {}'.format(self.symbol,price,div_yield,pe_ratio))
    def trade_stock(self,price=1,quantity=1):
        if (not isinstance(price,int) and not isinstance(price,float)) or (price <= 0):
            raise TypeError('Price must be Integer or Float and must be greater than zero')
        if (not isinstance(quantity,int) and not isinstance(quantity,float)) or (quantity <= 0):
            raise TypeError('Quantity must be Integer or Float and must be greater than zero')
        ts = datetime.datetime.now()
        self.trade_cntr += 1
        self.trade_dict['Trade' + str(self.trade_cntr)] = [ts,quantity,'Buy',price]
        self.trade_cntr += 1
        self.trade_dict['Trade' + str(self.trade_cntr)] = [ts, quantity, 'Sell', price]
        print('Stock Traded: Time Stamp: {}, Stock: {}, Price: {}, Quantity: {}'.format(ts.strftime("%d/%m/%Y (%H-%M:%S.%f)"),self.symbol, price, quantity))
    def volprice(self):
        wsp = 0
        wquantity = 0
        cut_off = datetime.datetime.now() - datetime.timedelta(minutes = 5)
        for trade in self.trade_dict:
            if self.trade_dict[trade][2] == 'Buy' and self.trade_dict[trade][0] > cut_off:
                wsp += self.trade_dict[trade][3] * self.trade_dict[trade][1]
                wquantity += self.trade_dict[trade][1]
        self.vwsp = wsp/wquantity
        print('Stock: {} - Volume Weighted Stock Price: {}'.format(self.symbol,self.vwsp))
def calc_gbce(allstocks):
    geo_mean = 1
    for stck in allstocks:
        if stck.vwsp > 0:
            geo_mean *= stck.vwsp
    gbce = 0
    if len(allstocks) > 0:
        gbce = geo_mean **(1/len(allstocks))
    print('GBCE All Share Index: {}'.format(gbce))
if __name__ == "__main__":
    # Stock Object Creation
    S1 = StockData(symbol = 'TEA', pval = 100)
    S2 = StockData(symbol='POP', lsdiv = 8, pval=100)
    S3 = StockData(symbol='ALE', lsdiv = 23, pval=60)
    S4 = StockData(symbol = 'GIN', type = 'Preferred', lsdiv = 8, fixdiv = 2, pval = 100)
    S5 = StockData(symbol='JOE', lsdiv = 13, pval=250)
    S1.stockstats(11)
    S1.stockstats(12)
    S1.stockstats(13)
    S1.stockstats(14)
    S1.stockstats(15)
    S1.trade_stock(11,10)
    S1.trade_stock(12,15)
    S1.trade_stock(13,17)
    S1.trade_stock(14,13)
    S1.trade_stock(15,19)
    S1.volprice()
    S2.stockstats(21)
    S2.stockstats(22)
    S2.stockstats(23)
    S2.stockstats(24)
    S2.stockstats(25)
    S2.trade_stock(21, 10)
    S2.trade_stock(22, 25)
    S2.trade_stock(23, 37)
    S2.trade_stock(24, 23)
    S2.trade_stock(25, 39)
    S2.volprice()
    S4.stockstats(31)
    S4.stockstats(32)
    S4.stockstats(33)
    S4.stockstats(34)
    S4.stockstats(35)
    S4.trade_stock(31, 20)
    S4.trade_stock(32, 25)
    S4.trade_stock(33, 17)
    S4.trade_stock(34, 53)
    S4.trade_stock(35, 19)
    S4.volprice()
    # Object Creation and Share Trading to be added before this line
    calc_gbce(StockData.stocks)
