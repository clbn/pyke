# coding: utf-8

_vars = {}


def env(key, value=None, default=None):
    if value == None:
        return _vars.get(key, default)
    else:
        _vars[key] = value

def setenv(args):
    for key, value in args.items():
        env(key, value)
