import tqdm as _tqdm

from tqdm_countdown.base import CountdownMixin

# as if there'll be another version of this...
__version__ = "0.1.0"
__all__ = ["tqdm", "trange"]


class tqdm(CountdownMixin, _tqdm.tqdm):
    pass


def trange(*args, **kwargs):
    return tqdm(range(*args), **kwargs)
