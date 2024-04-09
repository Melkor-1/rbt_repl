import matplotlib.pyplot as plt
from pylab import rcParams


# create a graphical representation of a binary tree (plot_tree, below, uses plot_node)
def plot_node(node, rb=True, level=1, posx=0, posy=0):
    if not node:
        return

    min_width = 100
    width = max(
        2000.0 * (0.5 ** (level)), min_width
    )  # This will be used to space nodes horizontally
    if node._color == 0 or not rb:
        plt.text(
            posx,
            posy,
            str(node._key),
            horizontalalignment="center",
            color="k",
            fontsize=10,
        )
    else:
        plt.text(
            posx,
            posy,
            str(node._key),
            horizontalalignment="center",
            color="r",
            fontsize=10,
        )

    if node.left:
        px = [posx, posx - width]
        py = [posy - 1, posy - 18]
        if node.left._color == 0 or not rb:
            plt.plot(px, py, "k-")
        else:
            plt.plot(px, py, "r-")
        plot_node(node.left, rb, level + 1, posx - width, posy - 20)

    if node.right:
        px = [posx, posx + width]
        py = [posy - 1, posy - 18]
        if node.right._color == 0 or not rb:
            plt.plot(px, py, "k-")
        else:
            plt.plot(px, py, "r-")
        plot_node(node.right, rb, level + 1, posx + width, posy - 20)


def plot_tree(node, figsize=(10, 6)):
    rcParams["figure.figsize"] = figsize
    fig, ax = plt.subplots()
    ax.axis("off")
    plot_node(node)
    plt.show()
    plt.close()
