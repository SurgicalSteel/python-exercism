def slices(series, length):
    if len(series) <= 0 or length <= 0:
        raise ValueError("invalid arguments.")

    if length > len(series):
        raise ValueError(f"Cannot get {length} digit series from a {len(series)} digit string.")

    resultList = []

    diff = len(series) - length +1

    for i in range (diff):
        resultList.append(series[i:i+length])

    return resultList
