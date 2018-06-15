from typing import List

from Process import Process


class CPU:

    def __init__(self, n: int):

        self.n = n
        self.usage = 0
        self.processes: List[Process] = []
        self.usageAVG = 0
        self.usageAVGdeviation = 0
        self.Helper = 0
        self.dHelper = 0

    def __str__(self):
        return "CPU No. " + str(self.n) + \
            "\t\tAverage load: " + str("%.2f") % round(self.usageAVG, 3) + \
            "\t\tAverage deviation: " + str("%.2f") % round(self.usageAVGdeviation, 3)