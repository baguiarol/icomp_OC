#!/bin/bash
for ((i = 10; i <= 1000; i += 10)); do
    for ((j = 0; j < 10; j++)); do
        (sudo perf stat -e cache-misses,cache-references ./not_friendly $i /dev/null) > out 2>&1 && cat out | grep cache-misses >> run$i.txt
    done
done