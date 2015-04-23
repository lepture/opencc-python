# coding: utf-8
from __future__ import absolute_import, unicode_literals

from opencc import convert
from opencc import OpenCC


def test_convert():
    text = '乾坤一擲'
    expect = '乾坤一掷'
    assert convert(text) == expect


def test_convert2():
    cc = OpenCC()
    text = '乾坤一擲'
    expect = '乾坤一掷'
    assert cc.convert(text) == expect

    text = '開放中文轉換'
    expect = '开放中文转换'
    assert cc.convert(text) == expect
