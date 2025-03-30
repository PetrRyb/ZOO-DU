def mocnina(x, n):
    if n == 0:
        return 1
    else:
        return x * mocnina(x, n - 1)
print(f"mocnina ")