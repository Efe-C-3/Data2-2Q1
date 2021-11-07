def meters_to_feet(meters: float) -> float:
    """
    This function takes a float representing a measurement in meters
    and returns the corresponding value converted to feet.
    The result is rounded to 2 decimal places.
    :param meters: A float representing a measurement in meters.
    :return: A float representing the input measurement converted to feet.
    """
    feet = float(meters) * 3.281
    return float(round(feet, 2))


def feet_to_meters(feet: float) -> float:
    """
    This function takes a float representing a measurement in feet
    and returns the corresponding value converted to meters.
    The result is rounded to 2 decimal places.
    :param feet: A float representing a measurement in feet.
    :return: A float representing the input measurement converted to meters.
    """
    meters = float(feet) / 3.281
    return float(round(meters, 2))
