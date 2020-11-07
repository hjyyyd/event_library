import numpy as np


def get_generator(events: np.array, **kwargs):
    for event in events:
        yield event


def display():
    raise NotADirectoryError
