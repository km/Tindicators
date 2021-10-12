class MovingAverages:
    def __init__(self, prices):
        '''
        prices : list
                 List of prices in chronological order from earlist to latest
        '''
        self.prices = prices

    def SMA(self):
        sum = self.__sum(self.prices)
        return sum / len(self.prices)

    def EMA(self, period, backtrack = 0):
        '''
        period : int
               Time period of the EMA if the Period is equal to the amount of values in prices then it'll return the SMA
        backtrack
               By default it'll get the EMA of the latest day (0) if you want the EMA of the day before then (1) and etc       
        If prices aren't in earliest to latest chronological order this won't work!
        '''
        wm = 2 / (period+1)
        ema = self.__sum(self.prices[:period])/len(self.prices[:period])
        for pricen in range(period, len(self.prices)-backtrack):
                ema = (self.prices[pricen] - ema) * wm + ema
       
        return ema

    def __sum(self, l):
        sum = 0
        for x in l:
            sum = x + sum
        return sum
