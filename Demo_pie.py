import matplotlib.pyplot as mp

#Data to plot
labels=["Python","C++","PHP","JAVA","C#"]
sizes=[25,45,12,67,98]
colors=["red","yellow","blue","orange","green"]
explode=(0.1,0,0,0,0.12)

#plot and autopct is use to show percentage in 10th place
mp.pie(sizes,explode=explode,labels=labels,colors=colors,autopct="%1.1f%%",shadow=True,startangle=140)

#in plt.axis equal is use to make circle
mp.axis('equal')
mp.show()