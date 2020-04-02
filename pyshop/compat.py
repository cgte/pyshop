import sys
import platform

pypy = platform.python_implementation() == "PyPy"

if sys.version < "3":
    if pypy:
        unicode = __builtins__.unicode
    else:
        unicode = __builtins__["unicode"]
    bytes = str
    from cStringIO import StringIO

else:
    if pypy:
        __builtins__.bytes
    else:
        bytes = __builtins__["bytes"]

    unicode = str
    from io import StringIO


def to_unicode(text):
    if isinstance(text, bytes):
        return text.decode("utf-8")
    return text
