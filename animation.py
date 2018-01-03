__author__ = "Charlie Friend <charles.d.friend@gmail.com>"

from utils import load_image


class Animation(object):
    """ Generic looping animation class - loops through several specified frames. """

    def __init__(self, frames, ticks_per_frame=1):
        """ Create an animation from a list of file paths (passed to utils/load_image) """
        # load frames from file, then duplicate references
        frames = [load_image(filename) for filename in frames]
        self._frames = []
        for frame in frames:
            self._frames.extend([frame for x in xrange(ticks_per_frame)])

        self._frameind = 0

    def next_frame(self):
        """ Get next frame in the animation. """
        next_frame = self._frames[self._frameind]
        self._frameind = (self._frameind + 1) % len(self._frames)
        return next_frame
