import sys
sys.path.insert(0, ".")

from studio.frames.frames_writer import frames_writer
from studio.charting.histograms import hist_density
from studio.datasets.sampling import normal_distribution


def normal_plot(params, outfile):
    datasets = []
    caption1_fmt = r"$n = {}, \bar x = {}, s = {}$"
    captions1 = []
    for param in params:
        n, mu, sigma = param[0], param[1], param[2]
        datasets.append(normal_distribution(mu, sigma, n))
        captions1.append(caption1_fmt.format(n, mu, sigma))

    suptitle = "Normal Distribution"
    title = "{}"
    caption2 = r"$P(x) = \frac{1}{\sigma\sqrt{2\pi}}e^{-(x-\mu)^2/(2\sigma^2)}$"
    animation = hist_density(datasets, suptitle, title, captions1, caption2)
    frames_writer(animation, outfile)


if __name__ == '__main__':
    # [n, mu, sigma]
    params = [
        [2000, 0, 2],
        [2000, 0, 4],
        [2000, 0, 6],
        [2000, 0, 8],
        [2000, 0, 10]
    ]
    outfile = "./_outputs/normal.mp4"
    normal_plot(params, outfile)
