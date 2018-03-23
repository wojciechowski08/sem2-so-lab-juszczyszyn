from Record import Record

def executeSRTF(records):

    """
    :param list records:
    :return:
    """
    queue = []
    currentTime = 0
    rIter = 0
    avgWT = 0
    avgTAT = 0


    while rIter < len(records) or len(queue) > 0:


        while rIter < len(records) and records[rIter].AT == currentTime:

            queue.insert(0, records[rIter])
            rIter += 1                      # dodanie procesu w czasie przybycia do kolejki

            queue.sort(reverse=True)                    # sortowanie procesow

        if len(queue) > 0:

            actual = queue.pop()            # wybranie procesu z kolejki
            actual.timeRemaining -= 1       # -- pozostaly czas obslugiwanego procesu

            for i in queue:                 # ++ czas oczekujący w procesow w kolejce
                i.WT += 1

            if actual.timeRemaining <= 0:

                # actual.TAT = currentTime - actual.AT      #daje o 1 mniejsze
                actual.TAT = actual.WT + actual.BT
                avgTAT += actual.TAT
                avgWT += actual.WT          # powiekszenie ogolnego czasu oczekiwania o czas oczekiwania wykonanego procesu
                #queue.sort(reverse=True)  # sortowanie kolejki wedlug czasu pozostalego

            else:

                queue.append(actual)        # powrot procesu do kolejki do kontynuacji obslugiwania
                queue.sort(reverse=True)    # sortowanie kolejki wedlug czasu pozostalego

        currentTime += 1                    # ++ jednostka czasu


    avgWT = avgWT / len(records)
    avgTAT = avgTAT / len(records)

    print("\nShortest-Remaining-Time-First simulation:")

    print("Average Waiting time: " + str(avgWT) +
          "\t\t Average Turn Around Time: " + str(avgTAT) + "\n")


