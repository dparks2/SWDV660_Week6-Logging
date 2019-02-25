import logging  
import logstash

test_logger = logging.getLogger('python-logstash-logger')
test_logger.setLevel(logging.INFO)
test_logger.addHandler(logstash.LogstashHandler('18.224.73.135', 5959, version=1))

extra = {
    'user_error': 'Yes'
}



def main():
    onGreen = 20
    green = raw_input('Did you hit it on the green (y/n)?')
    try:
        distance = int(raw_input('How far is the ball from the hole?'))
    except ValueError:
        test_logger.filter(UserWarning)
        test_logger.error('User entered string values for integer field.', extra=extra)
    validResponse = ['y', 'n']

    while green not in validResponse:
        test_logger.warning('User did not select a valid choice on "Did you hit on the green?". Choice was: ' + green)
        print('An invalid input was entered. Please use y(yes) or n(no).')
        green = raw_input('Did you hit it on the green (y/n)?')
        distance = int(raw_input('How far is the ball from the hole?'))
        break

    if green is 'y':
        if distance > onGreen:
            test_logger.info('User did not utilize application correctly. Distance is beyond the green which they said they were on.')
            print ('Your distance is beyond the green')
        else:
            print ('I recommend using your Putter.')

    if green is 'n':
        if distance < onGreen:
            print('You specified you are not on green but your yardage is on the green. Please Re-Evaluate.')
        elif distance > 200:
            print ('I recommend using your Driver.')
        elif 140 < distance < 200:
            print ('I recommend using your 5 - Iron')
        elif 100 < distance < 140:
            print ('I recommend using your 9 - Iron')
        else:
            print ('I recommend using a Pitching wedge.')


print ('Welcome to the Golf Club Helper')
print ('Tell me your situation, and Ill recommend a club')
main()