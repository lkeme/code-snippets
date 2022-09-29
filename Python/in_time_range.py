# python判断当前时间是否在某个时间段里
import time

def in_time_range(ranges):
    now = time.strptime(time.strftime("%H%M%S"),"%H%M%S")
    ranges = ranges.split(",")
    for range in ranges:
        r = range.split("-")
        if time.strptime(r[0],"%H%M%S") <= now <= time.strptime(r[1],"%H%M%S") or time.strptime(r[0],"%H%M%S") >= now >=time.strptime(r[1],"%H%M%S"):
            return True
    return False

# 例如是否在9:30-11:30和13:30-15:30之间
# in_time_range("093000-113000,133000-153000")