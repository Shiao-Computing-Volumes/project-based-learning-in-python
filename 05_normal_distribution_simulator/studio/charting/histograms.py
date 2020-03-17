import numpy as np
import scipy.stats
import matplotlib.pyplot as plt

from studio.settings.frames import STYLE, THEME_COLOR, AIDED_COLOR
from studio.settings.frames import FIGSIZE, DPI
from studio.frames.camera import Camera
from studio.charting.components.legends import captioning

plt.style.use(STYLE)


def hist_density(datasets, suptitle, title, captions1, caption2):
    fig = plt.figure(figsize=FIGSIZE, dpi=DPI)
    fig.suptitle(suptitle)

    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)
    ax1.spines['right'].set_visible(False)
    ax1.spines['top'].set_visible(False)
    ax1.spines['left'].set_color(AIDED_COLOR)
    ax1.spines['bottom'].set_color(AIDED_COLOR)
    ax2.spines['right'].set_visible(False)
    ax2.spines['top'].set_visible(False)
    ax2.spines['left'].set_color(AIDED_COLOR)
    ax2.spines['bottom'].set_color(AIDED_COLOR)

    camera = Camera(fig)

    for index in range(len(datasets)):
        n = len(datasets[index])
        if n < 101: step = int(n/5)
        else: step = int(n/10)
        for i in range(0, len(datasets[index]), step):
            single_histogram(ax1, datasets[index], i+step, title, captions1[index])
            single_density(ax2, datasets[index], i+step, title, caption2)
            camera.snap()

    return camera.animate()


def single_histogram(ax, data, i, title, caption):
    max_value = max(data)
    min_value = min(data)
    bin_width = (max_value - min_value) / float(len(data) - 1)
    n_bins = np.arange(min_value, max_value + bin_width, bin_width)

    ax.hist(data[:i], n_bins,
                       linewidth=1.2,
                       edgecolor=THEME_COLOR,
                       color=THEME_COLOR,
                       alpha=0.8)

    # captioning
    ax, legend = captioning(ax, caption)

    ax.set_title(title.format("Histogram"), fontsize=10, loc="left")
    # ax.set_xlabel("X")
    ax.set_ylabel("Frequency")
    ax.tick_params(axis='x', colors=AIDED_COLOR)
    ax.tick_params(axis='y', colors=AIDED_COLOR)
    return ax


def single_density(ax, data, i, title, caption):
    density = scipy.stats.gaussian_kde(data[:i])
    x = np.linspace(min(data), max(data), 500)
    ax.plot(x, density(x), color=THEME_COLOR)
    ax.fill_between(x, density(x), 0, facecolor=THEME_COLOR, alpha=0.5)

    # captioning
    ax, legend = captioning(ax, caption)

    ax.set_title(title.format("Density"), fontsize=10, loc="left")
    ax.set_xlabel("X")
    ax.set_ylabel("Density")
    ax.tick_params(axis='x', colors=AIDED_COLOR)
    ax.tick_params(axis='y', colors=AIDED_COLOR)
    return ax
