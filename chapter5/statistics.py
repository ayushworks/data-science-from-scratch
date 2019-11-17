from collections import Counter
import matplotlib.pyplot as plt

num_friends = [10, 20, 10, 15, 30, 20, 70, 70, 10, 20, 15, 15, 10, 20]

friends_counter = Counter(num_friends)  # {100:1, 70:1, 90:1, 87:1, 40:1, 67:1}

xs = range(101)  # maximum value allowed is 100

ys = [friends_counter[x] for x in xs]

plt.bar(xs, ys)
plt.axis([0, 101, 0, 25])
plt.title("Histogram of Friend Counts")
plt.xlabel("# of friends")
plt.ylabel("# of people")


plt.show()
