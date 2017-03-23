# -*- coding: utf-8 -*-

import hashlib


def calculate_md5(file_):
    if not file_:
        return ''
    md5 = hashlib.md5()
    for chunk in file_.chunks():
        md5.update(chunk)
    return md5.hexdigest()
