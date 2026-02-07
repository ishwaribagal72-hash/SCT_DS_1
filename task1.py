import matplotlib.pyplot as plt
import numpy as np

# Age values
age = np.arange(0, 80)

# Sample population distribution
population = (
    30*np.exp(-age/50) +
    10*np.exp(-(age-20)**2/200) +
    5*np.exp(-(age-40)**2/300)
)

plt.style.use("seaborn-v0_8-whitegrid")
plt.figure(figsize=(12,6))


# Fill areas
plt.fill_between(age[age<=20],
                 population[age<=20],
                 color='#FFD700',
                 alpha=0.9)

plt.fill_between(age[(age>20) & (age<=44)],
                 population[(age>20) & (age<=44)],
                 color='#1f77b4',
                 alpha=0.9)

plt.fill_between(age[age>44],
                 population[age>44],
                 color='#ff4da6',
                 alpha=0.9)

# Curve outline
plt.plot(age, population, color="black", linewidth=1.5)

# Title and labels
plt.title("India's Population Distribution by Age",
          fontsize=18, fontweight='bold')

plt.xlabel("Age", fontsize=12)
plt.ylabel("Population Index", fontsize=12)

# ---- TEXT INSIDE AREAS ----
plt.text(8, 18, "0–20 Years\n36%", 
         fontsize=12, fontweight='bold')

plt.text(28, 14, "21–44 Years\n59%", 
         fontsize=12, fontweight='bold', color="white")

plt.text(55, 5, "45+ Years\n5%", 
         fontsize=12, fontweight='bold')

plt.legend(["0-20 Years",
            "21-44 Years",
            "45+ Years"],
           loc="upper right",
           frameon=True)


# Clean layout
plt.tight_layout()
plt.savefig("population_age_distribution.png", dpi=300)


plt.show()
