import sys
from pathlib import Path
import random
sys.path.insert(0, str(Path.cwd().parent))
from pyindi.device import device

"""
This file uses a skeleton xml file to initialize and 
define properties. Similar to this example at indilib
https://www.indilib.org/developers/driver-howto.html#h2-properties
"""


class SkeletonDevice(device):

    def ISGetProperties(self, device=None):
        pass

    def initProperties(self):

        self.buildSkeleton("skeleton.xml")


    @device.repeat(1000)
    def do_repeate(self):
        conn = self.__getitem__("CONNECTION")
        if conn["CONNECT"].value == 'Off':
            return

        states = ('Alert', 'Busy', 'Idle', 'Ok')
        lights = self.IUFind('Light Property')

        for light in lights:
            light.value = random.choice(states)

        self.IDSet(light)


sk = SkeletonDevice()
sk.start()