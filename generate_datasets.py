import random

def generate_small_dataset(size):
    """Generate a small dataset."""
    return [random.randint(0, 100) for _ in range(size)]

def generate_medium_dataset(size):
    """Generate a medium-sized dataset."""
    return [random.randint(0, 100) for _ in range(size)]

def generate_large_dataset(size):
    """Generate a large dataset."""
    return [random.randint(0, 1000) for _ in range(size)]

def generate_uniform_distribution(size):
    """Generate a dataset with uniform distribution."""
    return list(range(size))

def generate_random_distribution(size):
    """Generate a dataset with random distribution."""
    return [random.randint(0, size) for _ in range(size)]

def generate_specific_pattern(size):
    """Generate a dataset with a specific pattern."""
    pattern = [1, 2, 3, 4, 5] * (size // 5)
    remainder = size % 5
    if remainder:
        pattern += [random.randint(1, 5) for _ in range(remainder)]
    random.shuffle(pattern)
    return pattern

def generate_gradual_change_dataset(size):
    """Generate a dataset with a gradual increase followed by a gradual decrease."""
    increase = sorted(random.randint(0, 500) for _ in range(size // 2))
    decrease = sorted((random.randint(0, 500) for _ in range(size // 2)), reverse=True)
    return increase + decrease

def generate_clustered_dataset(size, clusters=3):
    """Generate a dataset with specified number of clusters."""
    cluster_size = size // clusters
    remainder = size % clusters
    data = []
    for i in range(clusters):
        cluster_value = random.randint(i * 100, i * 100 + 99)
        data.extend([random.randint(cluster_value, cluster_value + 10) for _ in range(cluster_size)])
    data.extend([random.randint(0, clusters * 100) for _ in range(remainder)])
    random.shuffle(data)
    return data

def generate_periodic_dataset(size, period=10):
    """Generate a dataset with a periodic pattern."""
    pattern = [random.randint(0, 10) for _ in range(period)]
    data = pattern * (size // period) + pattern[:size % period]
    random.shuffle(data)
    return data

def generate_datasets():
    """Generate and return a dictionary of different datasets."""
    datasets = {}
    sizes = [10, 100, 1000]  # Small, medium, and large dataset sizes
    for size in sizes:
        datasets[f"Small_{size}"] = generate_small_dataset(size)
        datasets[f"Medium_{size}"] = generate_medium_dataset(size)
        datasets[f"Large_{size}"] = generate_large_dataset(size)
    datasets["Uniform_Distribution"] = generate_uniform_distribution(1000)
    datasets["Random_Distribution"] = generate_random_distribution(1000)
    datasets["Specific_Pattern"] = generate_specific_pattern(1000)
    datasets["Gradual_Change"] = generate_gradual_change_dataset(1000)
    datasets["Clustered_Data"] = generate_clustered_dataset(1000)
    datasets["Periodic_Pattern"] = generate_periodic_dataset(1000)  # Add this line
    return datasets

if __name__ == "__main__":
    datasets = generate_datasets()
    for name, data in datasets.items():
        print(f"{name}: {data[:10]}... (Length: {len(data)})")
