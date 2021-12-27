try: #импортируем библиотеку
    import matplotlib
    import matplotlib.pyplot
    import numpy
except: #если нет библиотеки качаем ее из интернета и пробуем еще раз
    os.system("pip install matplotlib")
    import matplotlib
    import matplotlib.pyplot
    import numpy

def Function(x):
    #y = 1 - numpy.exp(-x) #апериодический
    #y = 1 - numpy.exp(-x) * numpy.cos(x) #с перерегулированием
    y = 1 - numpy.exp(-x) * numpy.cos(numpy.pi*2*x) #с затухающими колебаниями
    #y = numpy.cos(9*x) #колебательный
    #y = numpy.exp(x/3) * numpy.cos(6*x) #уход в бесконечность
    return y

x = numpy.arange(0.0, 10.0, 0.01) #dx=0.01
#x = numpy.linspace(0.0, 5.0, 100) #100points
#print("x",x)
y = Function(x)
#print("y",y)
Figure, Axes = matplotlib.pyplot.subplots()
Axes.plot(x, y)
Axes.set(xlabel='x', ylabel='y', title='Function')
Axes.grid()
#Figure.savefig("test.png")
matplotlib.pyplot.show()

