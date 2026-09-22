def add_time(start, duration, day = None):
    # Transform the start time
    meridiem = start[-2:]
    start_hours, start_min = start[:-2].split(':')
    start_hours = int(start_hours)
    start_min = int(start_min)

    # Transform the start hours to 24 format
    if meridiem == 'PM':
        start_hours += 12

    # Transform the duration time
    duration_hours, duration_min = duration.split(':')
    duration_hours = int(duration_hours)
    duration_min = int(duration_min)
    
    # Calculate the minutes and update the hours if needed
    new_time_min = (start_min + duration_min) % 60
    if new_time_min // 10 == 0:
        new_time_min = '0' + str(new_time_min)
    else:
        new_time_min = str(new_time_min)
    duration_hours += (start_min + duration_min) // 60
    
    # Calculate the updated hours and how many days
    new_time_hours = (start_hours + duration_hours) % 24
    next_days = (start_hours + duration_hours) // 24

    # Calculate the meridiem is it AM or PM and update the hours
    if ((new_time_hours) // 12) == 1:
        new_time_hours -= 12
        new_time_meridiem = 'PM'
    else:
        new_time_meridiem = 'AM'
    
    # seem like the project doesn't want a 0 hour display, it prefer 12 instead
    if new_time_hours == 0:
        new_time_hours = 12

    # Specify what to write for the days (nothing, next day, or n days later)
    days = ''
    if next_days == 1:
        days = ' (next day)'
    elif next_days > 1:
        days = f' ({next_days} days later)'

    # if the day var is none than we should return the calculated time else we need to calculate the day and return the total calculated string
    if not day:
        new_time = f'{new_time_hours}:{new_time_min} {new_time_meridiem}{days}'
    else:   
        # First we define the weeks
        week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        # Calculate the index of the calculated date
        day_index = [i.lower() for i in week_days].index(day.lower())
        new_day_index = (day_index + next_days) % 7

        # assign the final value for new_time
        new_time = f'{new_time_hours}:{new_time_min} {new_time_meridiem}, {week_days[new_day_index]}{days}'

    return new_time

print(add_time('3:30 PM', '2:12', 'Monday'))
