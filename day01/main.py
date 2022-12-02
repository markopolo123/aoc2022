#! /usr/bin/env python

d = [sum(map(int, x.split())) for x in open("01", "rt").read().strip().split("\n\n")]
print(max(d), sum(sorted(d)[-3:]))
