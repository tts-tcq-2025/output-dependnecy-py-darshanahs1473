

def sensorStub():
    return {
        'temperatureInC': 50,
        'precipitation': 70,
        'humidity': 26,
        'windSpeedKMPH': 52
    }


def report(sensorReader):
    readings = sensorReader()
    weather = "Sunny Day"

    if (readings['temperatureInC'] > 25):
        if readings['precipitation'] >= 20 and readings['precipitation'] < 60:
            weather = "Partly Cloudy"
        elif readings['windSpeedKMPH'] > 50:
            weather = "Alert, Stormy with heavy rain"
    return weather


def testRainy():
    weather = report(sensorStub)
    print(weather)
    assert("rain" in weather.lower())  # FAILS because logic doesn’t check for precip > 60


def testHighPrecipitation():
    # This instance of stub needs to be different-
    # to give high precipitation (>60) and low wind-speed (<50)
    def high_precip_stub():
    return {
        'temperatureInC': 50,
        'precipitation': 80,  # > 60
        'humidity': 40,
        'windSpeedKMPH': 20  # Low wind => should be just 'rain', not storm
    }

    weather = report(sensorStub)

    # strengthen the assert to expose the bug
    # (function returns Sunny day, it should predict rain)
    assert(len(weather) > 0);
    weather = report(high_precip_stub)
    print(weather)
    assert("rain" in weather.lower())  # Fails, as rain not predicted at all


if __name__ == '__main__':
    testRainy()
    testHighPrecipitation()
    print("All is well (maybe!)");
