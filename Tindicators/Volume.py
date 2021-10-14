class Volume:
    def __init__(self, volumes, prices):
        '''
        volumes : list
                 List of volumes in chronological order from earlist to latest
        prices
                 List of prices in chronological order from earlist to latest
        '''
        self.volumes = volumes
        self.prices = prices

    def OBV(self, backtrack = 0):
        lastprice = self.prices[0]
        obv = 0
        for n in range(1, len(self.prices)-backtrack):
            if self.prices[n] > lastprice:
                obv = obv + self.volumes[n]
            elif self.prices[n] < lastprice:
                obv = obv - self.volumes[n]
            lastprice = self.prices[n]

        return obv