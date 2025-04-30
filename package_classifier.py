from doctest import testmod 

# Configs
MASS_LIMIT = 20
DIMENSION_LIMIT = 150
VOLUME_LIMIT = 1000000
TEST = True


def bulk_evaluator(width:float, height:float, length:float):
    # True: Small
    # False: Bulky
    try:
        dimensions = [width, height, length]
        dimensions_eval = list(map(lambda x: False if x >= DIMENSION_LIMIT else True, dimensions))
        if False in dimensions_eval:
            return False

    except Exception as err:
        print(f"DimensionsEvaluatorException: {err}")
        return False

    try:
        result = width * height * length

    except Exception as err:
        print(f"SizeEvaluatorException: {err}")
        return False

    if result >= VOLUME_LIMIT or result <= 0:
        return False

    return True


def weight_evaluator(mass:float):
    # True: Light
    # False: Heavy
    if mass >= MASS_LIMIT or mass <= 0:
        return False

    return True


def sort(width:float, height:float, length:float, mass:float):
    """
    This function classifies packages based on their dimensions and mass
    >>> sort(10, 10, 10, 1)  # Dimensions ok, mass ok
    'STANDARD'
    >>> sort(1000, 1000, 1000, 1)  # Volume > 1000000
    'SPECIAL'
    >>> sort(1, 150, 1, 1)  # Dimension == 150
    'SPECIAL'
    >>> sort(1, 1, 1, 20)  # mass == 20
    'SPECIAL'
    >>> sort(1000, 1000, 1000, 21)  # Volume > 1000000 and mass > 20
    'REJECTED'
    """

    # Dimensions: cms
    # mass: Kgs
    size_eval = bulk_evaluator(
        width=width,
        height=height,
        length=length
    )

    weight_eval = weight_evaluator(mass=mass)

    return "STANDARD" if size_eval * weight_eval == 1 else "REJECTED" if True not in [size_eval, weight_eval] else "SPECIAL"


if TEST is True:
    # call the testmod function 
    if __name__ == '__main__': 
        testmod(name ='sort', verbose = True) 
