import sys

from Page import Page


def executeALRU(nFrames, PageReferences):
    """

    :param int nFrames:
    :param list PageReferences:
    :return:
    """

    Frames = []
    for i in range(nFrames):            # tworzenie listy Frames'ow, gdzie index oznacza Frame
        Frames.append(None)


    pageHit = 0
    pageFault = 0

    for p in PageReferences:            # przechodzenie przez kazdy Page w PageRefenerces (obchodzenie referencji stron w podanej kolejnosci)

        isInFrames = False
        for frame in Frames:
            if frame == p:
                isInFrames = True

        if not isInFrames:  # jesli nie ma Page w Frame'sach

            if None in Frames:
                Frames.insert(0, p)
                Frames.pop()
                pageFault += 1
                continue

            smallestRef = sys.maxsize
            for frame in Frames:
                if frame.ref <= smallestRef:
                    smallestRef = frame.ref
                    frameToReplace = frame
            Frames[Frames.index(frameToReplace)] = p
            for frame in Frames:
                frame.ref = 0
            pageFault += 1


        else:                   #jesli Page jest juz w Frame'sach
            p.ref += 1
            pageHit += 1

    print("ALRU SIMULATION --- pageHit: " + str(pageHit) + ", pageFault: " + str(pageFault))

# test = [1,2,3,4,2,1,5,6,2,1,2,3,7,6,3,2,1,2,3,6]
# temp = []
# for i in test:
#     temp.append(Page(i))
# executeALRU(4, temp)