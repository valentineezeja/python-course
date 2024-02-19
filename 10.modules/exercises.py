import keyword


def contains_keyword(*args):
    for item in args:
        if keyword.iskeyword(item): return True
    return False