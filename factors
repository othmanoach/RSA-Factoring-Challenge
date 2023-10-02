#!/bin/bash

# Check for correct usage
if [ $# -ne 1 ]; then
    echo "Usage: $0 <file>"
    exit 1
fi

# Use awk to factorize numbers and print the results
awk '{
    n = $1
    for (i = 2; i <= n; i++) {
        while (n % i == 0) {
            printf("%d=%d*%d\n", n, i, n/i)
            n = n / i
        }
    }
}' "$1"