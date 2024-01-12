import matplotlib.pyplot as plt
def Histogram(data):
  plt.hist(data,bins=5,color='skyblue',edgecolor='black')
  plt.xlabel('Values')
  plt.ylabel('Frequency')
  plt.title('Histogram')
  plt.show()