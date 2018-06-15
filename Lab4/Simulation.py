import copy
import random

from Process import Process
from Page import  Page
from FRAME_ALLOCATION.EQUAL import allocateEQUAL
from FRAME_ALLOCATION.PROP import allocatePROPORTIONALLY

def SIMULATE():

    nFrames = int(input("Enter number of available frames for all processes: "))

    nProcesses = int(input("Enter number of processes to handle: "))

    processesTable = []

    for p in range(nProcesses):

        nPages = int(input("Enter number of Pages for process " + str(p+1) + " : "))
        nReferences = int(input("Enter number of Page References for process " + str(p+1) + " : "))

        pages = []

        for i in range(nPages):
            pages.append(Page(i, p))

        pageReferences = []

        for index in range(nReferences):
            if random.randint(1,100) <= 50 and len(pageReferences) != 0:
                pageReferences.append(pageReferences[-1])
            else:
                pageReferences.append(pages[random.randint(0, len(pages)-1)])
            # pageReferences.append(pages[random.randint(0, len(pages) - 1)])
        processesTable.append(Process(p, pageReferences))


    x = copy.deepcopy(processesTable)
    allocateEQUAL(x, nFrames)
    y = copy.deepcopy(processesTable)
    allocatePROPORTIONALLY(y, nFrames)


SIMULATE()