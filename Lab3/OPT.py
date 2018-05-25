
def executeOPT(nFrames, PageReferences):
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
    pIndex = 0

    for p in PageReferences:            # przechodzenie przez kazdy Page w PageRefenerces (obchodzenie referencji
                                        # stron w podanej kolejnosci)

        toContinue = False              # boolean zapewniajacy prawidlowa obsluge petli przy pustych Frame'ach

        if not p in Frames:             # jesli nie ma Page w Frame'sach

            if None in Frames:
                for frame in Frames:        # wpisuje jesli Frame's nie sa zapelnione Stronami
                    if frame == None:
                        Frames[Frames.index(frame)] = p
                        pageFault += 1
                        toContinue = True
                        break
                if toContinue:
                    continue

            max = 0
            for frame in Frames:            # okresla optymalne miejsce w Frame'ach do zmiany Page'a
                howClose = 0        # odl od najblizszej referencji
                for i in range(pIndex,len(PageReferences)):
                    if PageReferences[i] != frame:
                        howClose += 1
                if howClose >= max:
                    max = howClose
                    frameToReplace = frame

            Frames[Frames.index(frameToReplace)] = p
            pageFault += 1


        else:                   #jesli Page jest juz w Frame'sach
            pageHit += 1

        pIndex += 1

    print("OPT SIMULATION --- pageHit: " + str(pageHit) + ", pageFault: " + str(pageFault))

# test = [1,2,3,4,2,1,5,6,2,1,2,3,7,6,3,2,1,2,3,6]
# executeOPT(4, test)