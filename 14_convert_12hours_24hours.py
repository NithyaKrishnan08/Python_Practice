# To convert time from 12 hour to 24 hour format
def convertTime(timeInput):
    if timeInput[-2:] == 'AM' and timeInput[:2] == '12':
        return '00' + timeInput[2:-2]
    elif timeInput[-2:] == 'AM':
        return timeInput[:-2]
    elif timeInput[-2:] == 'PM' and int(timeInput[:2]) < 12:
        hourTime = int(timeInput[:2]) + 12
        return str(hourTime) + timeInput[2:-2]
    elif timeInput[-2:] == 'PM' and timeInput[:2] == '12':
        return '12' + timeInput[2:-2]

timeInput = input('Enter time in the format (hh:mm:ss) AM/PM: ')
print(convertTime(timeInput))