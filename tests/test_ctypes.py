# coding: utf-8

from opencc import convert


def test_convert():
    text = '乾坤一擲'
    expect = '乾坤一掷'
    assert convert(text) == expect
