import unittest
from sajan_sort import SajanSort, generate_random_data, profile_function, profile_dynamic_adjustment, profile_real_time_data_handling

class TestSajanSort(unittest.TestCase):
    def setUp(self):
        self.sorter = SajanSort()

    def test_initial_sort(self):
        data = [5, 3, 8, 1, 9, 7]
        self.sorter.input_data(data)
        sorted_data = self.sorter.output_data()
        self.assertEqual(sorted_data, sorted(data))

    def test_large_data_set(self):
        data = generate_random_data(1000, 0, 1000)
        self.sorter.input_data(data)
        sorted_data = self.sorter.output_data()
        self.assertEqual(sorted_data, sorted(data))

    def test_empty_data_set(self):
        data = []
        self.sorter.input_data(data)
        sorted_data = self.sorter.output_data()
        self.assertEqual(sorted_data, data)

    def test_data_with_duplicates(self):
        data = [4, 2, 4, 2, 4, 2]
        self.sorter.input_data(data)
        sorted_data = self.sorter.output_data()
        self.assertEqual(sorted_data, sorted(data))

    def test_already_sorted_data(self):
        data = [1, 2, 3, 4, 5]
        self.sorter.input_data(data)
        sorted_data = self.sorter.output_data()
        self.assertEqual(sorted_data, data)

    def test_dynamic_adjustment_small_data_set(self):
        initial_data = [5, 3, 8]
        new_data = [1, 9, 7]
        self.sorter.input_data(initial_data)
        self.sorter.dynamic_adjustment(new_data)
        combined_data = initial_data + new_data
        sorted_data = self.sorter.output_data()
        self.assertEqual(sorted_data, sorted(combined_data))

    def test_dynamic_adjustment_large_data_set(self):
        initial_data = generate_random_data(500, 0, 500)
        new_data = generate_random_data(500, 500, 1000)
        self.sorter.input_data(initial_data)
        self.sorter.dynamic_adjustment(new_data)
        combined_data = initial_data + new_data
        sorted_data = self.sorter.output_data()
        self.assertEqual(sorted_data, sorted(combined_data))

    def test_real_time_data_handling(self):
        initial_data = generate_random_data(100, 0, 100)
        stream_data = generate_random_data(50, 100, 150)
        self.sorter.input_data(initial_data)
        self.sorter.real_time_data_handling(stream_data)
        combined_data = initial_data + stream_data
        sorted_data = self.sorter.output_data()
        self.assertEqual(sorted_data, sorted(combined_data))

    def test_adjust_sorting_strategy_with_frequent_items(self):
        data = [1, 1, 1, 1, 1, 2, 3, 4, 5]
        self.sorter.input_data(data)
        data_patterns = self.sorter.analyze_data_patterns(data)
        self.sorter.adjust_sorting_strategy(data_patterns)
        sorted_data = self.sorter.output_data()
        self.assertEqual(sorted_data, sorted(data))

    def test_adjust_sorting_strategy_with_edge_case(self):
        data = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        self.sorter.input_data(data)
        data_patterns = self.sorter.analyze_data_patterns(data)
        self.sorter.adjust_sorting_strategy(data_patterns)
        sorted_data = self.sorter.output_data()
        self.assertEqual(sorted_data, sorted(data))

    def test_adjust_sorting_strategy(self):
        data = [5, 3, 8, 1, 9, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.sorter.input_data(data)
        data_patterns = self.sorter.analyze_data_patterns(data)
        self.sorter.adjust_sorting_strategy(data_patterns)
        sorted_data = self.sorter.output_data()
        self.assertEqual(sorted_data.count(1), 11)
        self.assertTrue(all(x <= y for x, y in zip(sorted_data, sorted_data[1:])))  # Check if sorted

    def test_adjust_sorting_strategy_no_frequent_items(self):
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.sorter.input_data(data)
        data_patterns = self.sorter.analyze_data_patterns(data)
        self.sorter.adjust_sorting_strategy(data_patterns)
        sorted_data = self.sorter.output_data()
        self.assertEqual(sorted_data, sorted(data))

    def test_profile_dynamic_adjustment(self):
        initial_data = generate_random_data(10000, 0, 10000)
        new_data = generate_random_data(5000, 0, 10000)
        self.sorter.input_data(initial_data)
        self.sorter.dynamic_adjustment(new_data)
        combined_data = initial_data + new_data
        sorted_data = self.sorter.output_data()
        self.assertEqual(sorted_data, sorted(combined_data))

    def test_profile_real_time_data_handling(self):
        initial_data = generate_random_data(10000, 0, 10000)
        stream_data = generate_random_data(5000, 0, 10000)
        self.sorter.input_data(initial_data)
        self.sorter.real_time_data_handling(stream_data)
        combined_data = initial_data + stream_data
        sorted_data = self.sorter.output_data()
        self.assertEqual(sorted_data, sorted(combined_data))

    def test_main(self):
        """Ensure the __main__ section is covered."""
        profile_function(profile_dynamic_adjustment)
        profile_function(profile_real_time_data_handling)

if __name__ == '__main__':
    unittest.main()
