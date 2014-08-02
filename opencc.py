# coding: utf-8

import os
import sys
from ctypes.util import find_library
from ctypes import CDLL, cast, c_char_p, c_int, c_size_t, c_void_p

if sys.version_info[0] == 3:
    text_type = str
else:
    text_type = unicode

__all__ = ['CONFIGS', 'convert']
__version__ = '0.1'
__author__ = 'Hsiaoming Yang <me@lepture.com>'

_libcfile = find_library('c') or 'libc.so.6'
libc = CDLL(_libcfile, use_errno=True)

_libopenccfile = os.environ.get('LIBOPENCC') or find_library('opencc')
if _libopenccfile:
    libopencc = CDLL(_libopenccfile, use_errno=True)
else:
    libopencc = CDLL('libopencc.so.1', use_errno=True)


libc.free.argtypes = [c_void_p]

libopencc.opencc_open.restype = c_void_p
libopencc.opencc_convert_utf8.argtypes = [c_void_p, c_char_p, c_size_t]
libopencc.opencc_convert_utf8.restype = c_void_p
libopencc.opencc_close.argtypes = [c_void_p]
libopencc.opencc_perror.argtypes = [c_char_p]
libopencc.opencc_dict_load.argtypes = [c_void_p, c_char_p, c_int]

CONFIGS = [
    'zhs2zhtw_p.ini', 'zhs2zhtw_v.ini', 'zhs2zhtw_vp.ini',
    'zht2zhtw_p.ini', 'zht2zhtw_v.ini', 'zht2zhtw_vp.ini',
    'zhtw2zhs.ini', 'zhtw2zht.ini', 'zhtw2zhcn_s.ini', 'zhtw2zhcn_t.ini',
    'zhs2zht.ini', 'zht2zhs.ini',
]


def convert(text, config='zht2zhs.ini'):
    assert config in CONFIGS

    if isinstance(text, text_type):
        # use bytes
        text = text.encode('utf-8')

    od = libopencc.opencc_open(c_char_p(config.encode('utf-8')))
    retv_i = libopencc.opencc_convert_utf8(od, text, len(text))
    if retv_i == -1:
        raise Exception('OpenCC Convert Error')
    retv_c = cast(retv_i, c_char_p)
    value = retv_c.value
    libc.free(retv_c)
    libopencc.opencc_close(od)
    return value.decode('utf-8')
