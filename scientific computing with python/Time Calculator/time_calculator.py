def get_hours(time_str):
    """Extract hours from 'HH:MM' format."""
    return int(time_str.split(':')[0])

def get_minutes(time_str):
    """Extract minutes from 'HH:MM' format."""
    return int(time_str.split(':')[1])

def pad_time(value):
    """Return a 2-digit string with leading zeros if needed."""
    return f"{value:02d}"

def calculate_time(start, duration):
    """Return total hours and minutes after adding duration."""
    start_hours = get_hours(start)
    start_minutes = get_minutes(start)
    duration_hours = get_hours(duration)
    duration_minutes = get_minutes(duration)

    total_minutes = start_minutes + duration_minutes
    total_hours = start_hours + duration_hours + (total_minutes // 60)
    total_minutes %= 60

    return total_hours, total_minutes


def add_time(start, duration, day=''):
    WEEKDAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Parse start time and meridiem
    time_str, meridiem = start.split()
    start_hours, start_minutes = map(int, time_str.split(':'))

    # Convert to 24-hour format
    if meridiem.upper() == 'PM' and start_hours != 12:
        start_hours += 12
    if meridiem.upper() == 'AM' and start_hours == 12:
        start_hours = 0

    # Calculate totals
    hours_total, minutes_total = calculate_time(f"{start_hours}:{start_minutes}", duration)
    days_later = hours_total // 24
    hours_total %= 24

    # Determine AM/PM for result
    meridiem_result = 'PM' if hours_total >= 12 else 'AM'
    display_hours = hours_total % 12 or 12

    # Calculate new day if provided
    new_day = ''
    if day:
        day_cap = day.capitalize()
        if day_cap in WEEKDAYS:
            new_day_index = (WEEKDAYS.index(day_cap) + days_later) % 7
            new_day = f", {WEEKDAYS[new_day_index]}"

    # Add info about days later
    if days_later == 1:
        day_suffix = ' (next day)'
    elif days_later > 1:
        day_suffix = f' ({days_later} days later)'
    else:
        day_suffix = ''

    # Format final time
    result = f"{display_hours}:{pad_time(minutes_total)} {meridiem_result}{new_day}{day_suffix}"
    return result


# Example tests
if __name__ == "__main__":
    print(add_time('3:30 PM', '2:12'))
    print(add_time('2:59 AM', '24:00', 'Saturday'))
    print(add_time('11:59 PM', '24:05', 'Wednesday'))
    print(add_time('8:16 PM', '466:02', 'Tuesday'))
