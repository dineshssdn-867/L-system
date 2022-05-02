from math import pi, sin, cos
from math import isnan

DEGREES_TO_RADIANS = pi / 180


def turtle_to_coords(turtle_program, turn_amount=45):
    state = (0.0, 0.0, 90.0)

    yield 0.0, 0.0

    for command in turtle_program:
        x, y, angle = state

        if command in 'Ff':
            state = (x - cos(angle * DEGREES_TO_RADIANS),
                     y + sin(angle * DEGREES_TO_RADIANS),
                     angle)

            if command == 'f':
                yield float('nan'), float('nan')

            yield state[0], state[1]

        elif command == '+':
            state = (x, y, angle + turn_amount)

        elif command == '-':
            state = (x, y, angle - turn_amount)


def print_coords(coords):
    for (x, y) in coords:
        if isnan(x):
            print('<gap>')
        else:
            print('({:.2f}, {:.2f})'.format(x, y))

