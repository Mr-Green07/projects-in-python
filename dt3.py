import matplotlib.pyplot as plt
# import pandas as pd
import numpy as np


# x = [0, 1, 2, 3, 4, 5, 6]
# y = [2,3,4,5,6,7,8 ]

# plt.plot(x, y)

# plt.show()
# x = [5, 2, 7]
# y = [2, 16, 4]

# plt.plot(x, y)
# #plt.plot(y,x)

# plt.title('Amplitude Vs Time')
# plt.ylabel('Amplitude')
# plt.xlabel('Time')

# plt.show()
# x  = [1, 2, 3, 4, 5]
# y1 = [50, 40, 70, 80, 20]
# y2 = [80, 20, 20, 50, 60]
# y3 = [70, 20, 60, 40, 60]
# y4 = [80, 20, 20, 50, 60]

# plt.plot(x, y1, 'g', label='Enfield', linewidth=2)
# plt.plot(x, y2, 'c', label='Honda', linewidth=1)
# plt.plot(x, y3, 'k', label='Yahama', linewidth=3)
# plt.plot(x, y4, 'y', label='KTM', linewidth=2)

# plt.title('Bike details in line plot')
# plt.ylabel('Distance in kms')
# plt.xlabel('Days')

# plt.legend()           #Adding Legends

# plt.show()
# x = [50, 60, 30, 70, 20]
# y = ["A", "B", "C", "D", "E"]

# plt.bar(y, x, color = "green")

# plt.show()
# x1 = [0.25, 1.25, 2.25, 3.25, 4.25]
# y1 = [50, 40, 70, 80, 20]

# plt.bar(x1, y1, label="BMW", color='r')

# x2 = [.75, 1.75, 2.75, 3.75, 4.75]
# y2 = [80, 20, 20, 50, 60]
# plt.bar(x2, y2, label="Audi", color='y')

# plt.xlabel('Days')
# plt.ylabel('Distance (kms)')
# plt.title('Information')

# plt.legend()
# plt.show()
# x = [5, 6, 3, 7, 2]
# y = ["A", "B", "C", "D", "E"]

# plt.barh(y, x, color ="orange")

# plt.show()
# x = [5, 2, 9, 4, 7]    
# y = [10, 5, 8, 4, 2]       

# plt.scatter(x, y)        

# plt.show()  
# x = [35, 20, 29, 40, 57]     # x-axis values
# y = [100, 50, 80, 40, 200]         # Y-axis values

# plt.scatter(x, y)         # Function to plot scatter

# plt.xlabel('Salary * 1000')
# plt.ylabel('Age)')
# plt.title('Age Vs Salary')

# plt.show()               # function to show the plot
# x1 = [1, 1.5, 2, 2.5, 3, 3.5, 3.6]
# y1 = [7.5, 8, 8.5, 9, 9.5, 10, 10.5]

# x2 = [8, 8.5, 9, 9.5, 10, 10.5, 11]
# y2 = [3, 3.5, 3.7, 4, 4.5, 5, 5.2]

# plt.scatter(x1, y1, label='High income low saving',color='r')
# plt.scatter(x2, y2, label='Low income high savings', color='b')

# plt.xlabel('Saving*100')
# plt.ylabel('Income*1000')
# plt.title('Scatter Plot')

# plt.legend()

# plt.grid()
# plt.show()
# share = [3,4,2,1]
# bikes = ['Enfield','Honda','Yahama','KTM']

# plt.pie(share, labels=bikes, shadow= True, explode=(0,0.1,0.2,0),
#         autopct='%1.2f%%')

# plt.title('Bike Shares')

# plt.show()
# df = pd.read_csv('nba16.csv')
# df.head()

# x = df['Age']
# y = df['Salary']

# plt.xlabel('Age')
# plt.ylabel('Salary (in millions)')
# plt.title('Salary Vs Age')

# plt.bar(x, y, color = "purple")

# plt.show()
x = np.arange(0, 5 * np.pi, 0.1)

y_sin = np.sin(x)
y_cos = np.cos(x)

plt.plot(x, y_cos,'g--')
plt.plot(x, y_sin,'r--')
plt.title('Sine and Cosine')

plt.show()