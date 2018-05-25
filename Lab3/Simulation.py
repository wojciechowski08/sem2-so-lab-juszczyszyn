import random

from Page import Page
from FIFO import executeFIFO
from LRU import executeLRU
from ALRU import executeALRU
from OPT import executeOPT
from RAND import executeRAND


def SIMULATE(Frames, Pages, PRL, ZLO):
    """
    PRL - Page Reference Lenght
    :param int Frames:
    :param int Pages:
    :param int PRL:
    :param boolean ZLO:
    :return:
    """

    pages = []
    for i in range(Pages):
        pages.append(Page(i))

    pageReferences = []

    if not ZLO:

        for index in range(PRL):
            pageReferences.append(pages[random.randint(0, len(pages)-1)])
    else:
        for index in range(PRL):
            odw = pages[index - 1].pageN - 5 + random.randint(0, 1+5*2)
            pageReferences.append(pages[max(0, min(Pages, odw))])


    executeFIFO(Frames,pageReferences)
    executeLRU(Frames,pageReferences)
    executeALRU(Frames,pageReferences)
    executeOPT(Frames,pageReferences)
    executeRAND(Frames,pageReferences)

SIMULATE(8, 30, 1000, False)