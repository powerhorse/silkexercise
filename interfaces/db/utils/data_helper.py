"""
Author: Viswa V

Defines helper utils to pre-process data sources
"""
from collections import Counter

def preprocess_epoch_to_buckets(data, start_time=None):
    """
    This function processes a list of epoch times and processes them into 60 buckets,
    corresponding to 60 minutes in the hour. If a start_time is specified, that is used
    as the start of the window, else it defaults to the earliest entry in data.
    Args:
        data:           A list of tuples: [(epoch time)]
        start_time:     A start time from which to create a 60 minute window,
                        if set to None, defaults to the minimum epoch time.
    Returns:
        A tuple (bucket_count,  min_time)
        bucket_count:   A counter for instances in each minute interval.
        min_time:       Start time of the window
    """
    times = [x[0] for x in data]
    if start_time is None:
        min_time = min(times)
    else:
        min_time = start_time
    # Find the buckets these should be at.
    buckets = [(x-min_time)//60 for x in times]
    
    # Window for 60 minutes
    minutes = list(range(60))
    ctr = Counter(buckets)
    counts = [ctr.get(minute, 0) for minute in minutes]
    return counts, min_time
