#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ts=4 sts=4 expandtab ai

import sys, random

def check_number(digits):
    _sum = 0
    alt = False
    for d in reversed(str(digits)):
        d = int(d)
        assert 0 <= d <= 9
        if alt:
            d *= 2
            if d > 9:
                d -= 9
        _sum += d
        alt = not alt
    return (_sum % 10) == 0

def mod10(kid):
    _sum = 0
    alt = True
    for s in reversed(str(kid)):
        d = int(s)
        assert 0 <= d <= 9
        if alt:
            d *= 2
            if d > 9:
                d -= 9
        _sum += d
        alt = not alt

    controlbit = 10 - (_sum % 10)
    if controlbit == 10:
        controlbit = 0

    return controlbit

def kid_add_controlbit(kid):
    new_kid = str((int(kid) * 10) + mod10(kid))
    new_kid = new_kid.zfill(len(kid)+1)
    return new_kid


if __name__ == '__main__':
    kid = str(234567)
    for i in range(10):
        nkid = kid_add_controlbit(kid)
        correct = check_number(nkid)

        print "%s\t%s\t(fra %s, nr %3d)" % (nkid, correct, kid, i)

        if (not correct):
            sys.exit()

        kid = str(random.randrange(100000000, 999999999))
