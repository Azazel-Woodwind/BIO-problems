DAYS_IN_UINAL = 20
DAYS_IN_TUN = 18 * DAYS_IN_UINAL 
DAYS_IN_KATUN = 20 * DAYS_IN_TUN
DAYS_IN_BAKTUNS = 20 * DAYS_IN_KATUN
START_DATE_MAYAN = [13, 20, 7, 16, 3]

def daysIn(date):
    return date[4] + DAYS_IN_UINAL * date[3] + DAYS_IN_TUN * date[2] + DAYS_IN_KATUN * date[1] + DAYS_IN_BAKTUNS * date[0]

def main():
    mayan_date = input().split(" ")
    mayan_date = [int(x) for x in mayan_date]
    
    days_after = daysIn(mayan_date) - daysIn(START_DATE_MAYAN)

    date = [1, 1, 2000]

    while (1):
        if (date[2] % 4 == 0):
            if days_after > 365:
                days_after -= 366
            else:
                break
        else:
            if days_after > 364:
                days_after -= 365
            else:
                break
        date[2] += 1

    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if (date[2] % 4 == 0):
        months[1] = 29

    for i in months:
        if days_after > i:
            date[1] += 1
            days_after -= i
        else:
            date[0] += days_after
            break

    print(date)

if __name__ == "__main__":
    while (1):
        main()

# 1b
# 13 20 7 17 14 = 1 February 2000
# 13 20 8 16 9 = 1 January 2001

# 1c
# 2880000
# thursday
