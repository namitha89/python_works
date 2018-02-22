#!/usr/bin/python

n = int(raw_input())
integer_list = map(int, raw_input().split())
print hash(tuple(integer_list))
