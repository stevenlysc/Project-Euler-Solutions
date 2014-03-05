def day_of_week(year, month, day):
    template = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if month < 3:
        year -= month - 1
    return (year + year/4 - year/100 + year/400 + template[month - 1] + day) % 7

if __name__ == '__main__':
    print day_of_week(2014, 3, 4)