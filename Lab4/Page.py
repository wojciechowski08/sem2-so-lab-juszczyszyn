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
# PAGE CLASS

class Page():

    def __init__(self, pageNumber, process):
        """

        :param int pageN:
        :param int process:
        """
        self.pageN = pageNumber          # Number of Page
        self.process = process


    # def __eq__(self, other):
    #     if other == None or self == None :
    #         return False
    #     else:
    #         return self.pageN == other.pageN
    #
    # def __cmp__(self, other):
    #     if other == None or self == None:
    #         return False
    #     else:
    #         return self.pageN == other.pageN
    #
    # def __str__(self):
    #     return str(self.pageN)