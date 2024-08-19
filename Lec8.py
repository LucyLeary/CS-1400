# Warmup Problem:
def number_series(upper_bound):
    series = ""
    for count in range(upper_bound + 1):
        series = series + str(count)
    return series


def main():
    series = number_series(7)
    print(series)


if __name__ == "__main__":
    main()
