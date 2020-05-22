#!/usr/bin/env python
# coding: utf-8

import json
import pandas as pd
import requests
from pytrends.request import TrendReq

INTEREST_BY_REGION_URL = 'https://trends.google.com/trends/api/widgetdata/comparedgeo'


def interest_by_city(self, inc_low_vol=True):
    """Request data from Google's Interest by City section and return a dataframe"""

    # make the request
    resolution = 'CITY'
    region_payload = dict()
    self.interest_by_region_widget['request'][
        'resolution'] = resolution

    self.interest_by_region_widget['request'][
        'includeLowSearchVolumeGeos'] = inc_low_vol

    # convert to string as requests will mangle
    region_payload['req'] = json.dumps(
        self.interest_by_region_widget['request'])
    region_payload['token'] = self.interest_by_region_widget['token']
    region_payload['tz'] = self.tz

    # parse returned json
    req_json = self._get_data(
        url=TrendReq.INTEREST_BY_REGION_URL,
        method='get',
        trim_chars=5,
        params=region_payload,
    )
    df = pd.DataFrame(req_json['default']['geoMapData'])
    if (df.empty):
        return df

    # rename the column with the search keyword
    df = df[['geoName', 'coordinates', 'value', 'hasData']].set_index(
        ['geoName']).sort_index()
    # split list columns into seperate ones, remove brackets and split on comma
    result_df = df['value'].apply(lambda x: pd.Series(
        str(x).replace('[', '').replace(']', '').split(',')))

    # rename each column with its search term
    for idx, kw in enumerate(self.kw_list):
        result_df[kw] = result_df[idx].astype('int')
        del result_df[idx]

    return result_df




