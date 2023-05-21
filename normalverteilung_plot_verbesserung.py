import numpy as np
import matplotlib.pyplot as plt

# Erzeugung der Daten für die Normalverteilung
mu = 0
sigma = 1
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
y = (1/(sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu)/sigma)**2)

plt.plot(x, y, color='black', linewidth=2)

# Fläche unter der Kurve entsprechend der 68-95-99,7-Regel einfärben
plt.fill_between(x, y, where=((x >= mu - sigma) & (x <= mu + sigma)), color='lightblue', alpha=0.7)
plt.fill_between(x, y, where=((x >= mu - 2*sigma) & (x <= mu + 2*sigma)), color='skyblue', alpha=0.7)
plt.fill_between(x, y, where=((x >= mu - 3*sigma) & (x <= mu + 3*sigma)), color='deepskyblue', alpha=0.7)

# Linien ziehen um 68-95-99,7-Regel um besser zu erkennen
plt.axvline(x=mu - sigma, color='blue', linestyle='-', linewidth=1)
plt.axvline(x=mu + sigma, color='blue', linestyle='-', linewidth=1)
plt.axvline(x=mu - 2*sigma, color='blue', linestyle='-', linewidth=1)
plt.axvline(x=mu + 2*sigma, color='blue', linestyle='-', linewidth=1)
plt.axvline(x=mu - 3*sigma, color='blue', linestyle='-', linewidth=1)
plt.axvline(x=mu + 3*sigma, color='blue', linestyle='-', linewidth=1)

plt.xticks([mu - 3*sigma, mu - 2*sigma, mu - sigma, mu, mu + sigma, mu + 2*sigma, mu + 3*sigma],
           ['μ-3σ', 'μ-2σ', 'μ-σ', 'μ', 'μ+σ', 'μ+2σ', 'μ+3σ'])

plt.xlabel('x')
plt.ylabel('Probability Density')
plt.title('68-95-99.7 Regel')

plt.savefig("68-95-99.7_Regel.png", dpi=300)
plt.show()
