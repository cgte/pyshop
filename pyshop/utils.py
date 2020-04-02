import random
import string
import os
from copy import copy


urandom = copy(os.urandom)

urandom_patch_status = []

def fake_urandom(k):
    import random
    import string

    alpha = string.ascii_letters + string.digits

    return bytes("".join(random.choices(alpha, k=k)), "utf-8")


def patched_urandom(k):
    if 'ok' in urandom_patch_status:
        return urandom(k)
    if 'ko' in urandom_patch_status:
        return fake_urandom(k)
    try:
        res = urandom(k)
        urandom_patch_status.append('ok')
    except NotImplementedError:
        urandom_patch_status.append('ko')
        return fake_urandom(k)
    else:
        return res
