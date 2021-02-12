import os
import sys

try:
    get_ipython = sys.modules["IPython"].get_ipython
    if "IPKernelApp" not in get_ipython().config:
        raise ImportError("console")
    if "VSCODE_PID" in os.environ:
        raise ImportError("vscode")
except Exception:
    from tqdm_countdown import tqdm, trange
else:
    from tqdm_countdown.notebook import tqdm, trange

__all__ = ["tqdm", "trange"]
