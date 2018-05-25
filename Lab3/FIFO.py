
def executeFIFO(nFrames, PageReferences):
    """

    :param int nFrames:
    :param list PageReferences:
    :return:
    """

    Frames = []
    for i in range(nFrames):            # tworzenie listy Frames'ow, gdzie index oznacza Frame
        Frames.append(None)

    pointer = 0                         #wskazuje na najstarszy Page we Frame'ach
    pageHit = 0
    pageFault = 0

    for p in PageReferences:            # przechodzenie przez kazdy Page w PageRefenerces (obchodzenie referencji stron w podanej kolejnosci)

        toContinue = False              # boolean zapewniajacy prawidlowa obsluge petli przy pustych Frame'ach

        if not p in Frames:             #jesli nie ma Page w Frame'sach

            if None in Frames:
                for frame in Frames:        # wpisuje jesli Frame's nie sa zapelnione Stronami
                    if frame == None:
                        Frames[Frames.index(frame)] = p
                        pageFault += 1
                        toContinue = True
                        break
                if toContinue:
                    continue

            Frames[pointer] = p
            pageFault += 1
            if pointer == nFrames-1:
                pointer = 0
            else:
                pointer += 1


        else:                   #jesli Page jest juz w Frame'sach
            pageHit += 1

    print("FIFO SIMULATION --- pageHit: " + str(pageHit) + ", pageFault: " + str(pageFault))

# test = [1,2,3,4,2,1,5,6,2,1,2,3,7,6,3,2,1,2,3,6]
# executeFIFO(4, test)