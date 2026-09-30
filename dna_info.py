#!/usr/bin/python3
import sys
sequence = sys.argv[1]

print("Sequence:", sequence)
print("Length:", len(sequence))
print("A:", sequence.count("A"))
print("T:", sequence.count("T"))
print("G:", sequence.count("G"))
print("C:", sequence.count("C"))
gc = (sequence.count("G") + sequence.count("C"))
print("GC:", gc)

