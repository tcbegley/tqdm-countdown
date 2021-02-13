# tqdm-countdown

Have you ever been monitoring the progress of your code but felt like there just wasn't enough drama? Well, `tqdm-countdown` is here to help! It creates a [tqdm](https://github.com/tqdm/tqdm) progress bar that plays the countdown music from the British game show [Countdown](https://en.wikipedia.org/wiki/Countdown_(game_show)) when there is 30 seconds or less left to go on your progress bar. Cheer on your code as it races to complete its task before the time runs out, all to the soundtrack of the tensest game show music on television!

## Installation

It's as easy as

```sh
pip install git+https://github.com/tcbegley/tqdm-countdown.git
```

## Example

The interface is the same as `tqdm`.

```python
import time

from tqdm_countdown import tqdm

for i in tqdm(range(65)):
    time.sleep(0.5)
```

Or try it in a notebook

```python
import time

from tqdm_countdown.notebook import tqdm

for i in tqdm(range(65)):
    time.sleep(0.5)
```

You can even let `tqdm_countdown` figure out whether it is being used in a script or a notebook.

```python
from tqdm_countdown.autonotebook import tqdm
```

## FAQ

**Q: Can this be used as a drop-in replacement for `tqdm`?**

Sure! As long as you don't want to use one of the features of `tqdm` that I haven't implemented.

**Q: Is there a performance penalty to using this over `tqdm`?**

Probably? But it's way more fun, and since time flies when you're having fun your code might _feel_ faster.

**Q: How stable is this?**

I've tested it on _both_ of the examples above and it was fine.

**Q: Hold on... isn't it possible the music ends at the wrong time if the time taken per iteration is not fixed?**

PRs welcome smartypants.
