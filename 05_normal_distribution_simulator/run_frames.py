import sys
sys.path.insert(0, ".")

from normal import normal_plot


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
