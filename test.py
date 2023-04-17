import matplotlib.pyplot as plt
import matplotlib.animation as animation
fig = plt. figure()
ax = fig.add_subplot(1, 1, 1)

xs = []
ys = []
color = ['-g']
    
def animate(i):
    ax.clear()
    ax.plot(xs, ys, color[-1])
    plt.xlabel('Номер итерации')
    plt.ylabel('Значение')
    plt.title("График отношения номера итерации к результату")

ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()
