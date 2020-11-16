
#   IMPORTING THIRD-PARTY LIBRARIES
import numpy

#   IMPORTING PROJECT FILES
from objects import Image

#   DEFINING FILE-WIDE VARIABLES
# -





def find_matches(image_main: Image, image_add: Image):

    # will have to find the best match (best similarity, best final size

    pass


def does_match(range_1: numpy.ndarray, range_2: numpy.ndarray):

    # IMPLEMENT SIMILARITY VALUE, AND RETURN BOOLEAN VALUE FOR MATCH // OR MATCH PROBABILITY, INSTEAD
    # will return similarity percentage (0.0 ≤ sim ≤ 1.0)

    if numpy.array_equal(range_1, range_2): return True, 1
    if range_1.shape != range_2.shape:   return False, 0

    # Calculating shape and number of elements
    shape_1 = range_1.shape

    matrix_size = 1
    for dimension_size in shape_1:
        matrix_size *= dimension_size

    sum_1 = range_1
    sum_2 = range_2

    # Adding together all terms of both matrices until one number left
    for dimension_index in range(len(shape_1)):
        sum_1 = sum(sum_1)
        sum_2 = sum(sum_2)

    # Calculating difference
    sum_difference = abs(sum_2 - sum_1)
    max_difference = numpy.ceil( matrix_size * (1 - self.default_similarity_threshold) )

    similarity = 1 - sum_difference / max_difference
    is_similar = (sum_difference <= max_difference)

    return is_similar, similarity
