def transform_sequence(sequence, transformations):
    return ''.join(transformations.get(c, c) for c in sequence)

def transform_multiple(sequence, transformations, iterations):
    for _ in range(iterations):
        sequence = transform_sequence(sequence, transformations)
    return sequence