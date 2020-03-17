import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from studio.settings.frames import AIDED_COLOR

def captioning(ax, text):
    """
    """
    # null = _empty_space()
    # legend = ax.legend([null], [text], loc='center left', bbox_to_anchor=(1, 0.5))
    legend = ax.legend([text], loc='upper right')
    legend.get_frame().set_linewidth(0.0)
    plt.setp(legend.get_texts(), color=AIDED_COLOR)
    return ax, legend


def _empty_space():
    return Rectangle((0, 0), 0, 0, fill=False, edgecolor='none', linewidth=0)
