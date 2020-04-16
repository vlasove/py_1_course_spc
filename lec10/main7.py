d = {"one":1, "two":2, "three":3}
print(d["one"] + d["two"])

if None == d.pop("four",None):
    print("Key 'four' not found")


if "one" in d:
    print("YESS")