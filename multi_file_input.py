def quadratic_temperature(a, b, c, t):
    return a * (t ** 2) + b * t + c

with open("input_multi.txt", "r", encoding="utf-8") as f:
    for line in f:
        if line.strip():
            # Clean up strange characters
            parts = [p.strip().replace("Â", "") for p in line.split()]
            a, b, c, t = map(float, parts)
            
            temperature = quadratic_temperature(a, b, c, t)
            print(f"For coefficients (a={a}, b={b}, c={c}) and t={t} -> Predicted Temperature = {temperature}")