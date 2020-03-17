#-----------------------------------------------------------------------------
# Style

STYLE = 'dark_background'
# ref: https://matplotlib.org/3.1.1/gallery/style_sheets/style_sheets_reference.html
STYLE_LIST = [
    "default",
    "classic", "classic_test",
    "Solarize_Light2",
    "bmh",
    "dark_background",
    "fast",
    "fivethirtyeight",
    "ggplot",
    "grayscale",
    "seaborn",
    "seaborn-bright", "seaborn-colorblind", "seaborn-dark",
    "seaborn-darkgrid", "seaborn-deep", "seaborn-muted",
    "seaborn-notebook", "seaborn-paper", "seaborn-pastel",
    "seaborn-poster", "seaborn-talk", "seaborn-ticks",
    "seaborn-white", "seaborn-whitegrid", "tableau-colorblind10"
]

# theme colors
THEME_COLOR = "skyblue"
AIDED_COLOR = "#666666"
# ref: https://matplotlib.org/3.1.0/gallery/color/named_colors.html
THEME_COLORS = {
    "gray": ["black", "dimgray", "dimgrey", "gray", "grey", "darkgray",
             "darkgrey", "silver", "lightgray", "lightgrey", "gainsboro",
             "whitesmoke", "white", "snow"],
    "red": ["rosybrown", "lightcoral", "indianred", "brown", "firebrick",
            "maroon", "darker", "red", "mistyrose", "salmon", "tomato",
            "darksalmon", "coral", "orangered", "lightsalmon", "sienna",
            "seashell", "chocolate", "saddlebrown", "peachpuff", "peru",
            "linen"],
    "yellow": ["bisque", "darkorange", "burlywood", "antiquewhite",
               "tan", "navajowhite", "blanchedalmond", "papayawhip",
               "moccasin", "orange", "wheat", "oldlace", "floralwhite",
               "darkgoldenrod", "goldenrod", "cornsilk", "gold",
               "lemonchiffon", "khaki", "palegoldenrod", "darkkhaki",
               "ivory", "beige", "lightyellow", "lightgoldenrodyellow",
               "olive", "yellow"],
    "green": ["olivedrab", "yellowgreen", "darkolivegreen", "greenyellow",
              "chartreuse", "lawngreen", "honeydew", "darkseagreen",
              "palegreen", "lightgreen", "forestgreen", "limegreen",
              "darkgreen", "green", "lime", "shagreen", "mediumseagreen",
              "springgreen", "mintcream", "mediumspringgreen",
              "mediumaquamarine", "aquamarine", "turquoise", "lightseagreen",
              "mediumturquoise", "azure", "lightcyan", "paleturquoise",
              "darkslategray", "darkslategrey", "teal", "darkcyan",
              "aqua", "cyan", "darkturquoise"],
    "blue": ["cadetblue", "powederblue", "lightblue", "deepskyblue",
             "sky-blue", "lightskyblue", "steelblue", "aliceblue",
             "dodgerblue", "lightslategray", "lightslategrey",
             "slategray", "slategrey", "lightsteelblue", "cornflowerblue",
             "royalblue", "ghostwrite", "lavender", "midnightblue",
             "navy", "darkblue", "mediumblue", "blue", "slateblue",
             "darkslateblue", "mediumslateblue"],
    "purple": ["mediumpurple", "rebeccapurple", "blueviolet", "indigo",
               "darkorchid", "darkviolet", "mediumorchid", "thistle",
               "plum", "violet", "purple", "darkmagenta", "fuchsia",
               "magenta", "orchid", "mediumvioletred"],
    "pink": ["deeppink", "hotpink", "lavenderblush", "palevioetred",
             "crimson", "pink", "lightpink"]
}

#-----------------------------------------------------------------------------
# Resolutions

# default: 100 dpi
# resolutions = figsize(w, h) * dpi
#             = (w * dpi, h * dpi)
# e.g.
#  figsize(6.4, 6.4)
#    6.4 inches * 100 dpi = 640 pixels

# Youtube
#       Resolution       Name   Quality
#       3840×2160	2160p	4K
#       2560×1440	1440p	2K
#       1920×1080	1080p	Maximum Youtube video resolution for HD
#       1280×720	720p	Minimum Youtube video resolution for HD
#       854×480	        480p	Standard definition
#       640×360	        360p	Traditional website resolution
#       426×240	        240p	Minimum YouTube video size

DPI = 100
FIGSIZES = {
    '1080p': (19.2, 10.8),
    '720p': (12.8, 7.2),
    '480p': (8.54, 4.8),
    '360p': (6.4, 3.6),
    '240p': (4.26, 2.4)
}
FIGSIZE = FIGSIZES['480p']

#-----------------------------------------------------------------------------
# Animation

FPS = 2
BITRATE = 1800

VIDEO_AUTHOR = "AUTHOR"

