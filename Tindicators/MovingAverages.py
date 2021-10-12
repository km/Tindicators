class MovingAverages:
    def __init__(self, prices):
        '''
        prices : list
                 List of prices in chronological order from earlist to latest
        '''
        self.prices = prices

    def SMA(self, period, backtrack = 0):
        '''
        period : int
               Time period of the SMA
        backtrack
               By default it'll get the SMA of the latest day (0) if you want the SMA of the day before then (1) and etc       
        '''
        l1 = self.prices[:len(self.prices)-backtrack]
        l2 = l1[len(l1)-period:]
        sum = self.__sum(l2)

        return sum / len(l2)

    def EMA(self, period, backtrack = 0):
        '''
        period : int
               Time period of the EMA. If the Period is equal to the amount of values in prices then it'll return the SMA
        backtrack
               By default it'll get the EMA of the latest day (0) if you want the EMA of the day before then (1) and etc       
        If prices aren't in earliest to latest chronological order this won't work!
        '''
        wm = 2 / (period+1)
        ema = self.__sum(self.prices[:period])/len(self.prices[:period])
        for pricen in range(period, len(self.prices)-backtrack):
                ema = (self.prices[pricen] - ema) * wm + ema
       
        return ema

    def WMA(self, period, backtrack = 0):
        '''
        period : int
               Time period of the WMA
        backtrack
               By default it'll get the WMA of the latest day (0) if you want the WMA of the day before then (1) and etc       
        '''
        l1 = self.prices[:len(self.prices)-backtrack]
        l2 = l1[len(l1)-period:]
        factor = 0
        llength = len(l2)
        wma = 0
        for x in range(0, llength):
            factor = factor + (llength-x)
        for price in range(0, llength):
            wma = wma + (l2[price]*((price+1)/factor))

        return wma

    def __sum(self, l):
        sum = 0
        for x in l:
            sum = x + sum
            
        return sum
