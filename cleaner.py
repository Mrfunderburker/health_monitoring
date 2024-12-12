def filter_nondigits(data: list) -> list:
    """
    Filter all strings from list that are not integers

    Args:
        data (list[str]): list of strings representing heart rate samples.
            Might contain invalid or missing data.
    Returns:
        list[int]: list of integers, with all non-digit strings removed
    """
    flower = []
    if len(data) == 0 or "":
        return data
    for rate in data:
        rate = rate.strip()
        if rate.isdigit():
            flower.append(int(rate))
        else:
            rate = rate
    return flower


def filter_outliers(data: list) -> list:
    pass