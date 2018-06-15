

class Process:

    def __init__(self, arrivalTime: int, burstTime: int, usage: int):

        self.AT = arrivalTime
        self.BT = burstTime
        self.usage = usage
        self.progress = 0
