def Median(data):
    sorted_data = sorted(data)
    data_len = len(sorted_data)
    middle = (data_len - 1) // 2
    if middle % 2:
      return sorted_data[middle]
    else:
        return (sorted_data[middle] + sorted_data[middle + 1]) / 2.0