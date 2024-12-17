def window_max(data: list, n: int) -> list:
    """
    Calculate maximum value of every "n"-size window

    Args:
        data (list[int]): list of integers representing heart rate samples
        n (int): The size of your window
    Returns:
        list[int]: list of maximums from each window (size should be len(data)//6)
    """
    maximums = []
    for i in range(0,len(data),n):
       maximum = data[i:i + n]
       maximums.append(max(maximum))
    return maximums

    """
    Calculate average value of every "n"-size window

    Args:
        data (list[int]): list of integers representing heart rate samples
        n (int): The size of your window
    Returns:
        list[int]: list of averages from each window (size should be len(data)//6)
    """

def window_average(data: list, n: int) -> list:
   average = []

   for i in range(0,len(data), n):
       window = data[i:i + n]
       window_average = sum(window) /len(window)
       average.append(round(window_average,2))
   return average

   """
    Calculate standard dev value of every "n"-size window

    Args:
        data (list[int]): list of integers representing heart rate samples
        n (int): The size of your window
    Returns:
        list[int]: list of standard dev from each window (size should be len(data)//6)
    """
def window_stddev(data: list, n: int) -> list:
   stdev = []

   for i in range(0,len(data), n):
       window = data[i:i+n]
       if len(window) == 1:
           continue
       window_average = sum(window) / len(window)
       variance = sum((i- window_average)** 2 for i in window) / (len(window) -1)
       std_dev = variance ** 0.5
       stdev.append(round(std_dev,2))
   return stdev
