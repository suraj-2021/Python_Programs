import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 2, 1, 2, 1, 2, 1]

plt.plot(x, y)

y_error = 0.2
plt.errorbar(x, y, yerr=y_error, fmt='o')


plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Simple Line Plot with Error Bars")


plt.show()
