import types


class Page():

    def __init__(self, pageN, ref=0):
        """

        :param int pageN:
        """
        self.pageN = pageN          # Number of Page
        #self.AT = AT                # Time of Arrival
        #self.LUT = 0                # Time of Last Usage
        #self.usedRecently = usedRecently   # Parity Bit
        self.ref = ref


    def __eq__(self, other):
        if other == None or self == None :
            return False
        else:
            return self.pageN == other.pageN

    def __cmp__(self, other):
        if other == None or self == None:
            return False
        else:
            return self.pageN == other.pageN

    def __str__(self):
        return str(self.pageN)



