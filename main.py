import datetime
print('I want to send (write who or what) ')
who = input()
print('I want to send a ', who, ' to (write anywhere in the world) ')
where = input()
while (1):
    print(
        'I want to send a ', who, ' to ', where,
        ' in (write the date you want in the year-month-date format, for example, 2028-06-09) ')
    when = input()
    when = datetime.datetime.strptime(when, '%Y-%m-%d')
    when = when.date()
    now = datetime.datetime.now()
    now = now.date()
    tdelta = when - now
    tdelta = tdelta.days
    if tdelta <= 0:
        print(
            "You may have entered a past date, please note that the machine can only move objects into the future! Try again, please! ")
    else:
        break
print('Time machine is sending a ', who, ' to ', where,' ', str(tdelta), ' days forward')