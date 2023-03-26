from datetime import datetime


def convert_second_to_hour_minute_second(second):
    hour = second // 3600
    minute = (second // 60) - (hour * 60)
    sec = second - (minute * 60) - (hour * 3600)
    return hour, minute, sec


def fill_zero(num):
    return str(num).zfill(2)

def twenty_four(now, nuclear):
    now_time = datetime.strptime(now, '%H:%M:%S')
    nuclear_time = datetime.strptime(nuclear, '%H:%M:%S')
    remaining_time = nuclear_time - now_time
    remaining_sec = remaining_time.seconds
    hour, minute, sec = convert_second_to_hour_minute_second(remaining_sec)
    return f"{fill_zero(hour)}:{fill_zero(minute)}:{fill_zero(sec)}"


if __name__ == "__main__":
    now = input()
    nuclear = input()
    print(twenty_four(now, nuclear))