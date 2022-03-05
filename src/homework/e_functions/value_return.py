def get_hour(epoch_seconds):
    return epoch_seconds // 3600

def get_minutes(epoch_seconds):
    return (epoch_seconds // 60) % 60

def get_seconds(epoch_seconds):
    return epoch_seconds % 60

def time_from_utc(utc_offset, utc_zero):
    return utc_offset + utc_zero

def get_time(hour, minutes, seconds, time_type, meridiem='AM'):
    if minutes < 0 or minutes > 59:
        return 'Invalid minutes(range 0-59)'

    if seconds < 0 or seconds > 59:
        return 'Invalid seconds(range 0-59)'

    if time_type == 24:
        if hour < 0 or hour > 23:
            return 'Invalid hours(range 0-23)'

    elif time_type == 12:
        if hour < 0 or hour > 12:
            return 'Invalid hours(range 1-12)'
    else:
        return 'Invalid time_type(12 or 24 only)'

    if hour < 10:
        hour = "0" + str(hour)

    if minutes < 10:
        minutes  = "0" + str(minutes)

    if seconds < 10:
        seconds = "0" + str(seconds)

    time = str(hour) + ":" + str(minutes) + ":" + str(seconds)

    if time_type == 12:
        time = time + " " + meridiem

    return  time
