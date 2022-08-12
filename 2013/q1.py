import time

def increment_time(time, speed):
    time[0] += 1
    time[1] += speed

    hours = time[1] // 60
    time[0] += hours
    time[1] -= 60 * hours

    time[0] -= 24 * (time[0] // 24)

    return time

def get_first_match(speed1, speed2):
    clock1 = [0, 0]
    clock2 = [0, 0]
    count = 0
    while (1):
        clock1 = increment_time(clock1, speed1)
        clock2 = increment_time(clock2, speed2)

        count += 1

        if (clock1 == clock2):
            break

    return clock1, count

def q1c():
    best = 0
    for i in range(400):
        print(i)
        for x in range(400):
            _, hours = get_first_match(i, x)
            if hours > best:
                best = hours

    print(best)

def q1b():
    for i in range(21):
        print(0, i, get_first_match(0, i)[0])

def q1a():
    while (1):
        data = input().split(" ")
        clock1_speed, clock2_speed = int(data[0]), int(data[1])

        match, _ = get_first_match(clock1_speed, clock2_speed)

        hour = str(match[0])
        minute = str(match[1])
        if (len(hour) == 1):
            hour = '0' + hour

        if (len(minute) == 1):
            minute = '0' + minute

        print(hour + ":" + minute)



def main():
    print(get_first_match(1, 2))
    #q1c()

if __name__ == "__main__":
    main()