import matplotlib.pyplot as plt # type: ignore
import numpy as np # type: ignore

# Quadratic Model coefficients
a, b, c = -0.2, 1.5, 24

def quadratic_weather_model(t):
    return a * (t**2) + b * t + c

days = np.arange(0, 31, 1)  # 0 to 30 days

# ===== 1. QUADRATIC MODEL =====
temps = [quadratic_weather_model(d) for d in days]
plt.figure(figsize=(7,5))
plt.plot(days, temps, 'bo-', label="T = -0.2t² + 1.5t + 24")
plt.title("Weather Modeling (Quadratic Model)")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.legend()
plt.savefig("graph_quadratic.png")
plt.close()

# ===== 2. ITERATIVE MODEL =====
plt.figure(figsize=(7,5))
for i, step in enumerate([10, 20, 30], start=1):
    subset_days = np.arange(0, step+1, 1)
    temps_iter = [quadratic_weather_model(d) for d in subset_days]
    plt.plot(subset_days, temps_iter, label=f"Iteration {i}")
plt.title("Iterative Model Weather Curve")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.legend()
plt.savefig("graph_iterative.png")
plt.close()

# ===== 3. AGILE MODEL =====
plt.figure(figsize=(7,5))
for i, step in enumerate([7, 14, 21, 30], start=1):
    subset_days = np.arange(0, step+1, 1)
    temps_agile = [quadratic_weather_model(d) for d in subset_days]
    plt.plot(subset_days, temps_agile, label=f"Sprint {i}")
plt.title("Agile Model Weather Curve")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.legend()
plt.savefig("graph_agile.png")
plt.close()

# ===== 4. WATERFALL MODEL =====
plt.figure(figsize=(7,5))
phases = [(0, 7), (7, 14), (14, 21), (21, 30)]  # Sequential phases
for i, (start, end) in enumerate(phases, start=1):
    subset_days = np.arange(start, end+1, 1)
    temps_waterfall = [quadratic_weather_model(d) for d in subset_days]
    plt.plot(subset_days, temps_waterfall, label=f"Phase {i}")
plt.title("Waterfall Model Weather Curve")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.legend()
plt.savefig("graph_waterfall.png")
plt.close()

# ===== 5. INCREMENTAL MODEL =====
plt.figure(figsize=(7,5))
increments = [5, 10, 20, 30]  # Each increment delivers part of curve
for i, step in enumerate(increments, start=1):
    subset_days = np.arange(0, step+1, 1)
    temps_incr = [quadratic_weather_model(d) for d in subset_days]
    plt.plot(subset_days, temps_incr, label=f"Increment {i}")
plt.title("Incremental Model Weather Curve")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.legend()
plt.savefig("graph_incremental.png")
plt.close()

print("Graphs generated: graph_quadratic.png, graph_iterative.png, graph_agile.png, graph_waterfall.png, graph_incremental.png")