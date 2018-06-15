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
# PROPORTIONAL - PAGE REPLACEMENT ALGORITHM

from typing import List

from Page import Page


def executeLRU(nFrames: int, PageReferences: List[Page]) -> int:


    Frames = []

    # tworzenie listy Frame'ow, gdzie index oznacza Frame
    for i in range(nFrames):
        Frames.append(None)

    pageFault = 0

    # przechodzenie przez kazdy Page w PageRefenerces (obchodzenie referencji stron w podanej kolejnosci)
    for p in PageReferences:

        # jesli nie ma Page w Frame'ach
        if not p in Frames:

            Frames.insert(0, p)
            Frames.pop()
            pageFault += 1

        # jesli Page jest juz w Frame'ach
        else:

            Frames.remove(p)
            Frames.insert(0, p)

    return pageFault

