class Record:

    """
    Record - class to track all process data
    such as burst time, arrival time,
    """

    def __init__(self, number, burstTime, arrivalTime=None):
        self.AT = arrivalTime
        self.N = number
        self.BT = burstTime
        self.WT = 0
        self.TAT = 0
        self.timeRemaining = self.BT  # time left

    def setAT(self, arrivalTime):
        pass

    def setWT(self, waitTime):
        self.WT = waitTime

    def setTAT(self, turnAroundTime):
        self.TAT = turnAroundTime

    def clone(self):
        r = Record(self.N, self.BT)
        r.WT = self.WT
        return r

    def __str__(self):
        return "Process number: " + str(self.N) + \
            "\t\tArrival time: " + str(self.AT) + \
            "\t\tWaiting time: " + str(self.WT) + \
            "\t\tTurn Around Time: " + str(self.TAT)

    def __eq__(self, other):
        if self.N == other.N and \
           self.AT == other.AT and \
           self.BT == other.BT:
            return True

    def __ne__(self, other):
        if self.N != other.N or \
           self.AT != other.AT or \
           self.BT != other.BT:
            return True







