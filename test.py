import matplotlib.pyplot as plt
import matplotlib.animation as animation



fig = plt. figure()

xs = []
ys = []
color = ['-g']
average = []

her = {}
all_values_from_test = []
vals = []
labels = []
color_diogram = []

def animate(i):
    fig.clear()
    plt.subplot(1,2,1)
    plt.plot(xs, ys, color[-1])
    plt.plot(xs, average, '-.r')
    plt.xlabel('Номер итерации')
    plt.ylabel('Значение')
    plt.title("График отношения номера итерации к результату")
    
    plt.subplot(1, 2, 2)
    

    plt.pie(vals, labels=labels)   
ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()
