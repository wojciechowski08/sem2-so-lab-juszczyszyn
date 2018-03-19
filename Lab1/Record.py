class Record:

    """
    Record - class to track all process data
    such as burst time, arrival time, waiting time,
    turn around time
    """

    def __init__(self, number, burstTime, arrivalTime=None):
        self.AT = arrivalTime
        self.N = number
        self.BT = burstTime
        self.WT = 0
        self.TAT = 0
        self.timeRemaining = self.BT  # time left

    def setAT(self, arrivalTime):
        self.AT = arrivalTime

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
            "\t\tBurst time: " + str(self.BT) +\
            "\t\tWaiting time: " + str(self.WT) + \
            "\t\tTurn Around Time: " + str(self.TAT)

    def __eq__(self, other):
        if self.N == other.N and \
           self.AT == other.AT and \
           self.BT == other.BT:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.N != other.N or \
           self.AT != other.AT or \
           self.BT != other.BT:
            return True
        else:
            return False

    def __lt__(self, other):

        return self.timeRemaining < other.timeRemaining

    def __le__(self, other):

        return self.timeRemaining <= other.timeRemaining

    def __gt__(self, other):

        return self.timeRemaining > other.timeRemaining

    def __ge__(self, other):

        return self.timeRemaining >= other.timeRemaining



