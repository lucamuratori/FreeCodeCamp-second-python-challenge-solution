def add_time(start, duration, day=None):
    hours = 0
    minutes = 0
    new_time = ''
    days_later = 0
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    # Split the start time into hours and minutes
    start_time = start.split(':')
    
    start_hours = int(start_time[0]) # Get the hours from the start time
    start_minutes = int(start_time[1].split(' ')[0]) # Get the minutes from the start time
    pm_am = start_time[1].split(' ')[1] # Split the minutes and AM/PM, returns PM or AM
    
    # Split the duration time into hours and minutes
    duration_time = duration.split(':')

    hours = int(duration_time[0]) # Get the hours from the duration
    minutes = int(duration_time[1]) # Get the minutes from the duration
    days_later = hours // 24 # Get the days later

    # If the minutes are greater than 60, add an hour and get the remaining minutes
    if minutes + start_minutes >= 60:
        hours += 1
        final_minutes = (int(duration_time[1]) + int(start_time[1].split(' ')[0])) % 60
    else:
        final_minutes = int(start_time[1].split(' ')[0]) + int(minutes)
    
    # add a 0 in front of the minutes if the minutes are less than 10
    if final_minutes < 10:
        final_minutes = f'0{final_minutes}'
    
    # Add a day if the time is PM and the hours are greater than 12
    if pm_am == 'PM' and (hours + start_hours) >= 12:
        days_later += 1 

    # Get the day of the week
    if day is not None:
        day = day.capitalize()
        index = days_of_week.index(day)
        new_index = (index + days_later) % 7
    
    # if the days later is 1, print (next day), if greater than 1, print (n days later)
    if days_later == 1:
        days_later = '(next day)'
    elif days_later > 1:
        days_later = f'({days_later} days later)'

    # If the hours are greater or equal to 12, swap the PM/AM
    if start_hours + hours >= 12:
        if ((start_hours + hours) // 12) % 2 != 0 or start_hours + hours == 12:
            if pm_am == 'PM':
                pm_am = 'AM'
            else:
                pm_am = 'PM'

    final_hours = (start_hours + hours) % 12
    # If the final hours is 0, set it to 12
    if final_hours == 0:
        final_hours = 12

    # if the days later is 1, return the n days later
    if days_later == 0:
        new_time = f'{final_hours}:{final_minutes} {pm_am}'
        if day is not None:
            new_time += f', {days_of_week[new_index]}'
    elif days_later != 0 and day is not None:
        new_time = f'{final_hours}:{final_minutes} {pm_am}, {days_of_week[new_index]} {days_later}'
    
    
    return new_time


print(add_time('10:10 PM', '1:50', 'monDay'))
