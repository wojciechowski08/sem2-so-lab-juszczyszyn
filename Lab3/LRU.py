
def executeLRU(nFrames, PageReferences):
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

        toContinue = False              # boolean zapewniajacy prawidlowa obsluge petli przy pustych Frame'ach

        if not p in Frames:             #jesli nie ma Page w Frame'sach

            Frames.insert(0,p)
            Frames.pop()
            pageFault += 1

        else:                   #jesli Page jest juz w Frame'sach
            Frames.remove(p)
            Frames.insert(0,p)
            pageHit += 1

    print("LRU SIMULATION --- pageHit: " + str(pageHit) + ", pageFault: " + str(pageFault))

# test = [1,2,3,4,2,1,5,6,2,1,2,3,7,6,3,2,1,2,3,6]
# executeLRU(4, test)