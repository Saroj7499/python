import matplotlib.pyplot as pt # alias kiya hua hai

x=[2,5,10]
y=[2,5,15]

pt.plot(x,y)
pt.xlabel("Population")
pt.ylabel("Expense")
pt.bar(x,y)
pt.show()