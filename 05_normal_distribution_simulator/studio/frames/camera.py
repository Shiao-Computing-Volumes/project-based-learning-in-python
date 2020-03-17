from typing import Dict, List
from collections import defaultdict

from matplotlib.figure import Figure
from matplotlib.artist import Artist
from matplotlib.animation import ArtistAnimation


class Camera:

    def __init__(self, figure: Figure) -> None:
        self.figure = figure
        # need to keep track off artists for each axis
        self.offsets: Dict[str, Dict[int, int]] = {
            k: defaultdict(int) for k in [
                'collections',
                'patches',
                'lines',
                'texts',
                'artists',
                'images'
            ]
        }
        self.photos: List[List[Artist]] = []


    def snap(self) -> List[Artist]:
        """
        """
        frame_artists: List[Artist] = []
        for i, axis in enumerate(self.figure.axes):
            if axis.legend_ is not None:
                axis.add_artist(axis.legend_)

            for name in self.offsets:
                new_artists = getattr(axis, name)[self.offsets[name][i]:]
                frame_artists += new_artists
                self.offsets[name][i] += len(new_artists)

        self.photos.append(frame_artists)
        return frame_artists


    def animate(self, *args, **kwargs) -> ArtistAnimation:
        return ArtistAnimation(self.figure, self.photos, *args, **kwargs)
