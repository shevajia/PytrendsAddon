# PytrendsAddon
An add-on function for obtaining city-level Google trends results while working with pytrends

Example:



```python
from PytrendsAddon import interest_by_city
from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US', tz=360)
kw_list = ["weather"]
pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo= 'US-IL-602', gprop='')

interest_by_city(pytrends)
```

The last line should be able to return results identical to [https://trends.google.com/trends/explore?date=today%205-y&geo=US-IL-602&q=weather](https://trends.google.com/trends/explore?date=today 5-y&geo=US-IL-602&q=weather).