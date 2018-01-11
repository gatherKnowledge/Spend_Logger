import matplotlib.pyplot as plt
class Graph:
	def __init__(self):
		"""
		plt.plot([1, 2, 3, 4])
		"""
		"""
		x = range(0, 100)
		y = [v * v for v in x]
		plt.plot(x, y)
		"""
		plt.figure(figsize=(6,4))
		plt.plot([1231, 1245, 1511, 2411] , [1, 2, 3, 4], label='sell')
		plt.plot([4, 3, 2, 1], label='buy')
		plt.xlabel('Time')
		plt.ylabel('Amount')
		plt.title('Title')
		plt.grid()
		plt.legend()

		plt.show()

Graph()