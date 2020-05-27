import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def monty_hall(num_games, door_pick, k_s):
    win_count = 0;
    door_pick = door_pick.lower()
    k_s = k_s.lower()

    all_door = ["a", "b", "c"]

    for i in range(0, num_games):
        openable_set = ["a", "b", "c"]
        unpick_set = ["a", "b", "c"]
        unpick_set.remove(door_pick)
        win_door = np.random.choice(all_door, 1)

        if door_pick == win_door:
            openable_set.remove(win_door)
        else:
            openable_set.remove(door_pick)
            openable_set.remove(win_door)

        open_door = np.random.choice(openable_set, 1)
        unpick_set.remove(open_door)

        # Keep or Switch part

        if k_s == "k":
            if door_pick == win_door:
                win_count += 1
        if k_s == "s":
            if unpick_set[0] == win_door:
                win_count += 1
    return float(win_count)/float(num_games)

# Creating the visualization table
x_labels = ["10 games", "100 games", "1000 games", "10000 games"]
k_prob = [monty_hall(10, "a", "k"), monty_hall(100, "a", "k"), monty_hall(1000, "a", "k"), monty_hall(10000, "a", "k")]
s_prob = [monty_hall(10, "a", "s"), monty_hall(100, "a", "s"), monty_hall(1000, "a", "s"), monty_hall(10000, "a", "s")]

x = np.arange(len(x_labels))
width = 0.25

fig, ax = plt.subplots(figsize=(20, 10))
rects1 = ax.bar(x - width/2, k_prob, width, label='Keep')
rects2 = ax.bar(x + width/2, s_prob, width, label='Switch')

ax.set_ylabel("The Probability")
ax.set_title("Data visualization of Keep or Switch")
ax.set_xticks(x)
ax.set_xticklabels(x_labels)
ax.legend()

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

fig.tight_layout()
plt.show()
