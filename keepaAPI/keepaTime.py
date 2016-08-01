# -*- coding: utf-8 -*-
"""
Module to convert keepa time
"""

import numpy as np

keepa_st_ordinal = np.datetime64('2011-01-01')

def KeepaMinutesToTime(minutes):
    """
    Accepts an array or list of minutes and converts it to a numpy datetime
    array.  Assumes that keepa time is from keepa minutes from ordinal.
    """
    
    # Convert
    dt = np.array(minutes, dtype='timedelta64[m]')
    return keepa_st_ordinal + dt
