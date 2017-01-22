#!/usr/bin/python
import time

class Timer(object):
    def __init__(self, name=None, verbose=True):
        self.name = name
        self.verbose = verbose
        self.elapsed = None

    def __enter__(self):
        self.tstart = time.time()
        return self

    def __exit__(self, type, value, traceback):
        self.elapsed = time.time() - self.tstart
        if self.verbose:
            if self.name:
                print '[%s]' % self.name,
            print 'Elapsed: %s' % (self.elapsed)
