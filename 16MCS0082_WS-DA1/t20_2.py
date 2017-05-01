# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 00:39:57 2017

@author: MANSI
"""

import pandas as p
#import vincent
from pandas import datetime
from pandas.tseries.offsets import DateOffset
from matplotlib import pyplot

tweets = p.read_csv('./tweets.csv')

tweets['created_at'] = p.to_datetime(p.Series(tweets['created_at']))

tweets.set_index('created_at', drop=False, inplace=True)
tweets.index = tweets.index.tz_localize('GMT')

tweets.index = tweets.index - DateOffset(hours = 24)

tweets_pm = tweets['created_at'].resample('10Min')
tweets_pm1 = tweets_pm.count()

tweets_pm1.plot()
pyplot.show()
