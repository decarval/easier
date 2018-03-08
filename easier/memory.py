from __future__ import print_function
import psutil

py_proc = psutil.Process()


def mem_get():
    return int(py_proc.memory_full_info().uss / float(2 ** 20))

def mem_show(tag=''):
    print('__memory__: {}M  {}'.format(mem_get(), tag))
