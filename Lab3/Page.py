

class Page():

    def __init__(self, pageN, AT=0):
        """

        :param int pageN:
        """
        self.pageN = pageN          # Number of Page
        self.AT = AT                # Time of Arrival
        self.LUT = 0                # Time of Last Usage
        self.usedRecently = False



