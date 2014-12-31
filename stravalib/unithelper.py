"""
Helpers for converting Strava's units to something more practical.

These are really just thin wrappers to the brilliant 'units' python library. 
"""
from units import unit
import units.predefined

# Setup the units we will use in this module.
units.predefined.define_units()

meter = meters = unit('m')
second = seconds = unit('s')
hour = hours = unit('h')
foot = feet = unit('ft')
mile = miles = unit('mi')
kilometer = kilometers = unit('km')

meters_per_second = meter / second
miles_per_hour = mph = mile / hour
kilometers_per_hour = kph = kilometer / hour

kilogram = kilograms = kg = kgs = unit('kg')
pound = pounds = lb = lbs = unit('lb')

def c2f(celsius):
    """ Convert Celcius to Farenheit """
    return 9.0/5.0 * celsius + 32

def timedelta_to_seconds(td):
    """
    Converts a timedelta to total seconds, including support for microseconds.
    
    Return value is (potentially truncated) integer.
    
    (This is built-in in Python >= 2.7, but we are still supporting Python 2.6 here.)
    :param td: The timedelta object
    :type td: :class:`datetime.timedelta`
    :return: The number of total seconds in the timedelta object.
    :rtype: int
    """
    if td is None:
        return None
    return (td.microseconds + (td.seconds + td.days * 24 * 3600) * 10**6) / 10**6
