'''Module holding cross-platform class for reading keys from the keyboard,
without requiring the enter key.
'''

from builtins import object


class _Getch(object):
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self):
        return self.impl()


class _GetchUnix(object):
    def __init__(self):
        import tty  # noqa: F401
        import sys  # noqa: F401

    def __call__(self):
        import sys  # noqa: F401
        import tty  # noqa: F401
        import termios  # noqa: F401
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows(object):  # pragma: no cover
    def __init__(self):
        import msvcrt  # noqa: F401

    def __call__(self):
        import msvcrt
        return msvcrt.getch()