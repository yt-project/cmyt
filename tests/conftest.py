import matplotlib


def pytest_configure(config):
    matplotlib.use("Agg")
