import tqdm.notebook as _tqdm_notebook

from tqdm_countdown.base import CountdownMixin

__all__ = ["tqdm", "tqdm_notebook", "trange", "tnrange"]


class tqdm_notebook(CountdownMixin, _tqdm_notebook.tqdm_notebook):
    pass


def tnrange(*args, **kwargs):
    return tqdm_notebook(range(*args), **kwargs)


# aliases
tqdm = tqdm_notebook
trange = tnrange
