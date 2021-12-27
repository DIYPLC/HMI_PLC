import os
try: #импортируем библиотеку
    import matplotlib.pyplot
except: #если нет библиотеки качаем ее из интернета и пробуем еще раз
    os.system("pip install matplotlib")
    import matplotlib.pyplot

ys = [16,9,4,1,0,1,4,9,16]
xs = [-4,-3,-2,-1,0,1,2,3,4]
matplotlib.pyplot.plot(xs,ys)
matplotlib.pyplot.title("title")
matplotlib.pyplot.xlabel("xlabel")
matplotlib.pyplot.ylabel("ylabel")
matplotlib.pyplot.scatter(0,1)
#matplotlib.pyplot.axis([-5,5,0,20])
matplotlib.pyplot.show()

