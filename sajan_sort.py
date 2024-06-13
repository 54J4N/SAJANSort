import bisect
import cProfile
import io
import pstats
import random
from sortedcontainers import SortedList

class SajanSort:
    """
    SajanSort class for dynamically sorting data and adapting to new incoming data.
    """

    def __init__(self):
        """Initialize SajanSort with an empty data list and a SortedList."""
        self.data = []
        self.sorted_data = SortedList()

    def input_data(self, data):
        """
        Handle data input and perform initial sorting.

        Args:
            data (list): A list of data to be sorted.
        """
        self.data = data
        self.initial_sort()

    def initial_sort(self):
        """Perform initial sorting using SortedList."""
        self.sorted_data.update(self.data)

    def dynamic_adjustment(self, new_data):
        """
        Insert new items into the sorted data and adjust dynamically.

        Args:
            new_data (list): A list of new data to be added to the sorted list.
        """
        for item in new_data:
            self.sorted_data.add(item)
        self.adaptive_learning(new_data)

    def real_time_data_handling(self, stream_data):
        """
        Handle real-time data streams by dynamically adjusting the sorted data.

        Args:
            stream_data (list): A list of data points arriving in real-time.
        """
        for item in stream_data:
            self.dynamic_adjustment([item])

    def adaptive_learning(self, new_data):
        """
        Adaptive learning mechanism to improve sorting strategy based on new data patterns.

        Args:
            new_data (list): A list of new data to analyze for patterns.
        """
        data_patterns = self.analyze_data_patterns(new_data)
        self.adjust_sorting_strategy(data_patterns)

    def analyze_data_patterns(self, new_data):
        """
        Analyze data patterns to determine adjustments.

        Args:
            new_data (list): A list of new data to analyze.

        Returns:
            dict: A dictionary with the frequency of each item in the new data.
        """
        pattern = {}
        for item in new_data:
            if item in pattern:
                pattern[item] += 1
            else:
                pattern[item] = 1
        return pattern

    def adjust_sorting_strategy(self, data_patterns):
        """
        Adjust sorting strategy based on data patterns.

        Args:
            data_patterns (dict): A dictionary with the frequency of each item in the data.
        """
        frequent_items = {k: v for k, v in data_patterns.items() if v > 10}  # threshold for frequent items
        if frequent_items:
            # Temporarily remove and re-insert frequent items
            self.sorted_data = SortedList(item for item in self.sorted_data if item not in frequent_items)
            for item, count in frequent_items.items():
                self.sorted_data.update([item] * count)

    def output_data(self):
        """
        Handle the output of sorted data.

        Returns:
            list: The sorted data.
        """
        return list(self.sorted_data)

def profile_function(func, *args, **kwargs):
    """
    Profile a given function and print the profiling results.

    Args:
        func (function): The function to profile.
        *args: Arguments to pass to the function.
        **kwargs: Keyword arguments to pass to the function.
    """
    pr = cProfile.Profile()
    pr.enable()
    func(*args, **kwargs)
    pr.disable()

    s = io.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()

    with open(f"profile_output_{func.__name__}.txt", "w") as f:
        f.write(s.getvalue())

def generate_random_data(size, range_start, range_end):
    """
    Generate a list of random integers within a specified range.

    Args:
        size (int): The number of random integers to generate.
        range_start (int): The starting range for the random integers.
        range_end (int): The ending range for the random integers.

    Returns:
        list: A list of randomly generated integers.
    """
    return [random.randint(range_start, range_end) for _ in range(size)]

def profile_dynamic_adjustment():
    """Profile the dynamic adjustment method of the SajanSort class."""
    sajan_sort = SajanSort()
    initial_data = generate_random_data(10000, 0, 10000)  # Generate in bulk
    sajan_sort.input_data(initial_data)
    new_data = generate_random_data(5000, 0, 10000)  # Generate in bulk
    sajan_sort.dynamic_adjustment(new_data)

def profile_real_time_data_handling():
    """Profile the real-time data handling method of the SajanSort class."""
    sajan_sort = SajanSort()
    initial_data = generate_random_data(10000, 0, 10000)  # Generate in bulk
    sajan_sort.input_data(initial_data)
    stream_data = generate_random_data(5000, 0, 10000)  # Generate in bulk
    sajan_sort.real_time_data_handling(stream_data)

if __name__ == "__main__":
    profile_function(profile_dynamic_adjustment)
    profile_function(profile_real_time_data_handling)
