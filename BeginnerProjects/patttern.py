def pattern_h(n):
    if n > 1:
        pattern_h(n-1)
    print("*", end="")

def pattern_v(n):
    if n > 1:
        pattern_v(n-1)
    pattern_h(n)
    print()

pattern_v(5)
