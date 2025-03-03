def permute(s, prefix=""):
    if len(s) == 0:
        print(prefix)
    else:
        seen = set()
        for i in range(len(s)):
            if s[i] not in seen:
                seen.add(s[i])
                remaining = s[:i] + s[i + 1:]
                permute(remaining, prefix + s[i])



string = "gab"
print(f"Permutações de '{string}':")
permute(string)
