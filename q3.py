# -*- coding: utf-8 -*-

def main():
    d = {}
    while True:
        line = input().strip()
        if line == 'Q':
            break
        key, value = line.split(maxsplit=1)
        if key not in d:
            d[key] = value
    print("keys:", " ".join(d.keys()), end=" \n")
    print("vals:", " ".join(d.values()))

if __name__ == "__main__":
    main()