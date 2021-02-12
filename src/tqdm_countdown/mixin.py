import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

# import pygame after environment variable is set
import pygame  # noqa

try:
    from importlib.resources import files
except ImportError:
    # if using Python 3.8 import from the backport
    from importlib_resources import files

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
        start_t = self.start_t if hasattr(self, "start_t") else 0
        rate = self._ema_dn() / self._ema_dt() if self._ema_dt() else None
        initial = self.initial

        music_playing = False

        try:
            for obj in iterable:
                yield obj
                # Update and possibly print the progressbar.
                # Note: does not call self.update(1) for speed optimisation.
                n += 1

                elapsed = time() - start_t

                if rate is None and elapsed:
                    rate = (n - initial) / elapsed

                remaining = (total - n) / rate if rate and total else None

                if (
                    not music_playing
                    and remaining is not None
                    and remaining < 30
                ):
                    # sometimes finishes a bit early, so bump to 32 arbitrarily
                    pygame.mixer.music.play(start=31 - remaining)
                    music_playing = True
        finally:
            pygame.mixer.music.fadeout(500)