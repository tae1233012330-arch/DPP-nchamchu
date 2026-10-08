#!/usr/bin/env python3

for table in range(11):
    products = " ".join(str(table * multiplier) for multiplier in range(11))
    print(f"Table de {table}: {products}")