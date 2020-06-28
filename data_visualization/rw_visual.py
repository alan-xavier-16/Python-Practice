import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Keep making new walks while program is active
while True:
    # Make a walk
    rw = RandomWalk(50000)
    rw.fill_walk()

    plt.style.use("classic")
    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers,
               cmap=plt.cm.Blues, edgecolors="None", s=1)

    # Emphasize start and end position
    ax.scatter(0, 0, c="green", edgecolors="None", s=30)
    ax.scatter(rw.x_values[-1], rw.y_values[-1],
               c="red", edgecolors="None", s=30)

    # Remove Axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # Set size of tick labels
    ax.tick_params(axis="both", which="major", labelsize=14)

    plt.show()

    # Exit program prompt
    keep_running = input("Make another walk? (y/n): ")
    if keep_running.lower() == "n":
        break
