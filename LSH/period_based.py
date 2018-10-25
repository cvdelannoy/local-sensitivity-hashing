from LSH.numba_helpers import *
from LSH.lsh import VecorsInLSH


class Periods:
    def __init__(self, list_of_coords, bin_list=(0, 0.001, 3, 6, 9, 12, 18, 25, 35), max_period_len=50):
        self.bin_array = np.array(list(bin_list), dtype=np.float64)
        self.periods = multiple_coordinates_to_periods(list_of_coords, max_len=max_period_len)
        self.vectors, self.ranges = np.histogram(self.periods, bins=self.bin_array)


def periods_to_hash_buckets(list_of_coords, number_of_buckets):
    p = Periods(list_of_coords)
    periods = p.periods
    return VecorsInLSH(number_of_buckets, periods)


def coordinates_to_periods(coordinates):
    c1 = np.array(coordinates[:-1])
    c2 = np.array(coordinates[1:])
    return c2 - c1


def multiple_coordinates_to_periods(multiple_coordinates, max_len=100):
    res = np.zeros((len(multiple_coordinates), max_len))
    for i in range(res.shape[0]):
        periods = coordinates_to_periods(multiple_coordinates[i])
        shape = periods.shape[0]
        res[i,:shape] = periods
    return res


if __name__ == "__main__":
    coords = [[1,5,20,30,35,37,100],[2,4,20,25,30,35,50]]
    res = multiple_coordinates_to_periods(coords, max_len=7)

