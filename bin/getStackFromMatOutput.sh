#!/bin/bash
# Script written to strip the table from MAT generated thread stacks so they're easier to read.
# c-huff++ for helping :)

file=$1

cat $file | awk '{$NF = ""; print $0}' | sed 's/|//g' | sed 's/-//g' | tail -n +2 | sed 's/ at/    at/g'
