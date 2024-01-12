import matplotlib.pyplot as plt
def Line_graph(x,y):
  plt.plot(x_value,y_value,marker='o',color='b',label='Line Graph')
  plt.xlabel('X-axis')
  plt.ylabel('Y-axis')
  plt.title('Line Graph ')
  plt.legend()
  plt.show()