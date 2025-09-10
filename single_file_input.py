with open("inputs_single.txt", "r") as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

a = float(lines[0])
b = float(lines[1])
c = float(lines[2])
t = float(lines[3])

T = a * t**2 + b * t + c

print(f"Predicted temperature at t={t}: {T:.2f}°C")