#
# DANIEL ERYK WOJCIECHOWSKI
# WROCLAW 2018
#
# WROCLAW UNIVERSITY OF SCIENCE AND TECHNOLOGY
# FACULTY OF COMPUTER SCIENCE AND MANAGEMENT
# YEAR 1, SEM 2
# OPERATING SYSTEMS
#
#
# PROCESS CLASS

class Process:

    def __init__(self, processNumber, framesAssigned, referenceTable):

        self.processN = processNumber
        self.framesAssigned = framesAssigned
        self.referenceTable = referenceTable

    def __init__(self, processNumber, referenceTable):

        self.processN = processNumber
        self.framesAssigned = None
        self.referenceTable = referenceTable
