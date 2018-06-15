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
# PROPORTIONAL - FRAME ALLOCATION ALGORITHM

from Page import Page
from Process import Process
from PAGE_REPLACEMENT.LRU import executeLRU
from typing import List

def allocatePROPORTIONALLY(processes: List[Process], nFrames: int):

    pageFault = 0

    for p in processes:
        p.framesAssigned = nFrames * len(p.referenceTable) // sum(len(x.referenceTable) for x in processes)

    for p in processes:
        pageFault += executeLRU(p.framesAssigned, p.referenceTable)

    print("PROP ALLOCATION - Page Fault: " + str(pageFault))

