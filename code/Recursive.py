import time

def groundhog_day():
    '''A function that prints "Groundhog Day" recursively every second
    '''
    print('Did you mean: groundhog day ?')

    time.sleep(1)
    groundhog_day()

groundhog_day()





