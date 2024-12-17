def filter_nondigits(data: list) -> list:
    """
    Filter all strings from list that are not integers

    Args:
        data (list[str]): list of strings representing heart rate samples.
            Might contain invalid or missing data.
    Returns:
        list[int]: list of integers, with all non-digit strings removed
    """
    nondigits = []
    if len(data) == 0 or "":
        return data
    for rate in data:
        rate = rate.strip()
        if rate.isdigit():
            nondigits.append(int(rate))
        else:
            rate = rate
    return nondigits


def filter_outliers(data: list) -> list:
    """
    Filter all strings from list that are irregularities

    Args:
        data (list[str]): list of strings representing heart rate samples.
            Might contain errors in data that can affect accuracy of data caused by outliers.
    Returns:
        list[int]: list of integers, with all outlier strings removed
    """
    outliers = []
    if len(data) == 0 or "":
       return data
    for rate in data:
       if rate > 30 and rate < 250:
           outliers.append(rate)
    return outliers
