def switch_lights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] == 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] == 'red'
        elif stoplight[key] == 'red':
            stoplight[key] == 'green'

    assert 'red' in stoplight.values(),'赤信号がない！' + str(stoplight)
