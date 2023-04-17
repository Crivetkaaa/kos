import matplotlib.pyplot as plt
import matplotlib.animation as animation
fig = plt. figure()
ax = fig.add_subplot(1, 1, 1)

xs = []
ys = []
    
    
def animate(i):
    ax.clear()
    ax.plot(xs, ys)
    plt.xlabel('Дата')
    plt.ylabel('Цена')
    plt.title("График обновляемый в режиме реального времени")

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
