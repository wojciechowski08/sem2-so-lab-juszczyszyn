from Record import  Record

#n = input("Enter number of processes: ")
# bt = str(input("Enter burst times for processes: ")).split(" ")         # burst times
# ct = []         # completion times
# wt = []         # wait times
# tat = []        # turn around times
#avgWT = 0
#avgTAT = 0


def executeFCFS(records):
    """

    :param list records:
    :return:
    """
    queue = []
    currentTime = 0
    queueIter = 0
    avgWT = 0
    avgTAT = 0

    while queueIter < len(records) or len(queue) > 0:

        while queueIter < len(records) and records[queueIter].AT == currentTime:

            queue.insert(0, records[queueIter])
            queueIter += 1

        if len(queue) > 0:

            actual = queue.pop()            # wybranie procesu z kolejki
            actual.timeRemaining -= 1       # -- pozostaly czas obslugiwanego procesu

            for i in queue:                 # ++ czas oczekujący w procesow w kolejce
                i.WT += 1

            if actual.timeRemaining <= 0:

                actual.TAT = currentTime - actual.AT
                avgTAT += actual.TAT
                avgWT += actual.WT          # powiekszenie ogolnego czasu oczekiwania o czas oczekiwania wykonanego procesu

            else:

                queue.append(actual)        # powrot procesu do kolejki do kontynuacji obslugiwania

        currentTime += 1                    #++ jednostka czasu

    print("Average Waiting time: " + str(avgWT) +
          "\t\t Average Turn Around Time: " + str(avgTAT))











