import matplotlib.pyplot as plt

# Sample population age data
ages = [5, 12, 18, 25, 30, 35, 40, 45, 50, 60, 70, 80]

plt.hist(ages, bins=5)
plt.title("Population Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of People")
plt.show()
