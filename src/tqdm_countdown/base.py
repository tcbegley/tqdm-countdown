import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

# import pygame after environment variable is set
import pygame  # noqa

try:
    from importlib.resources import files  # type: ignore
except ImportError:
    # if using Python 3.8 import from the backport
    from importlib_resources import files

__all__ = ["CountdownMixin"]

pygame.mixer.init()
pygame.mixer.music.load(
    files("tqdm_countdown") / "resources" / "countdown-theme.mp3"
)


class CountdownMixin:
    def __iter__(self):
        iterable = super().__iter__()

        # If the bar is disabled, then just walk the iterable
        # (note: keep this check outside the loop for performance)
        if self.disable:
            yield from iterable
            return

        total = self.total
        n = self.n
        time = self._time
        rate = self._ema_dn() / self._ema_dt() if self._ema_dt() else None
        initial = self.initial

        music_playing = False

        try:
            for obj in iterable:
                yield obj

                # calculate time remaining and possibly start music
                n += 1

                if n - initial == 1:
                    # don't include initial iteration in elapsed time
                    # makes us sensitive to overhead from widget creation
                    # ... I think anyway?
                    time_1 = time()

                if not music_playing and n - initial >= 3:
                    elapsed = time() - time_1

                    if rate is None and elapsed:
                        rate = (n - initial - 1) / elapsed

                    remaining = (total - n) / rate if rate and total else None

                    if remaining is not None and remaining < 30:
                        # start a second later than calculated time remaining,
                        # seems to work well empirically
                        pygame.mixer.music.play(start=31 - remaining)
                        music_playing = True
        finally:
            pygame.mixer.music.fadeout(500)
