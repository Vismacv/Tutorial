import matplotlib.pyplot as plt
def Bar_diagram(subject,marks):
  plt.bar(subject,marks,color='skyblue')
  plt.xlabel('Subjects')
  plt.ylabel('Marks')
  plt.title('Bar Diagram')
  plt.show()