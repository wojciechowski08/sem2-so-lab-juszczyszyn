import random

from Processor import CPU
from Process import Process
from typing import List

def SIMULATE(nCPUs: int, nProcesses: int):
    """
    :var List[CPU] CPUs:
    :var List[Process] queue:
    :param nCPUs:
    :param nProcesses:
    :return:
    """

    # wygenerowanie processorow
    CPUs: List[CPU] = []
    for u in range(nCPUs):
        CPUs.append(CPU(u))

    # generowanie procesow
    queue: List[Process] = []
    for p in range(nProcesses):
        # at = random.randint(0, nProcesses*2//3)
        at = p
        bt = random.randint(70, 100)
        usage = random.randint(2, 15)
        temp = Process(at, bt, usage)
        queue.append(temp)
    queue.sort(key=lambda x: x.AT)

    temp = ""
    for i in queue:
        temp += str(i.AT) + "\t"
    print(temp)
    temp = ""
    for i in queue:
        temp += str(i.BT) + "\t"
    print(temp)
    temp = ""
    for i in queue:
        temp += str(i.usage) + "\t"
    print(temp)

    pointer = 0
    time = 1
    done = False
    migrations = 0

    # run simulation until all processes are executed
    while not done:

        # at current moment executing processes in CPU's
        for u in CPUs:

            for p in u.processes:

                # if execution of process is finished
                if p.progress == p.BT:
                    u.usage -= p.usage
                    u.processes.remove(p)

                # if not finished
                else:
                    p.progress += 1

        # list of processes to load into CPU's
        toLoad: List[Process] = []


        # checking queue for processes
        for p in queue:

            # checking if processes are arriving at current time
            if p.AT == time:
                toLoad.append(p)
                queue.remove(p)

            elif p.AT > time:
                break

        # pkt 1.
        # loading processes to CPU's at current time
        for p in toLoad:

            # list of tried CPU's
            tried = []

            # adding current CPU to tried
            tried.append(CPUs[pointer])

            # checking all  CPU's left
            while len(tried) != len(CPUs):

                # picking random CPU
                temp = random.randint(0,len(CPUs)-1)

                # checking if picked CPU was not tried before
                if not CPUs[temp] in tried:

                    # checking if CPU is not overloaded
                    if CPUs[temp].usage < 70:
                        CPUs[temp].processes.append(p)
                        CPUs[temp].usage += p.usage
                        break

                    # adding CPU to tried if overloaded
                    else:
                        tried.append(CPUs[temp])

            # making sure process is loaded if none of above conditions were True
            if len(tried) == len(CPUs):
                CPUs[pointer].processes.append(p)
                CPUs[pointer].usage += p.usage

            # process added - removing from waiting
            toLoad.remove(p)

            # iterating pointer at CPU
            if pointer < len(CPUs)-1:
                pointer += 1
            else:
                pointer = 0

            # print(str(len(tried)) + " " + str(len(CPUs)))

        # pkt 2. i 3.
        for u in CPUs:

            # list of tried CPU's
            tried = []

            # pkt 2.
            # checking if CPU is overloaded
            if u.usage > 70:

                # adding current CPU to tried
                tried.append(u)

                # checking all  CPU's left
                while len(tried) != len(CPUs):

                    # picking random CPU
                    temp = random.randint(0, len(CPUs) - 1)

                    # checking if picked CPU was not tried before
                    if not CPUs[temp] in tried:

                        # checking if CPU is not overloaded
                        if CPUs[temp].usage < 70:

                            # moving 5 processes from current CPU to other CPU
                            for foo in range(5):
                                p = u.processes.pop()
                                CPUs[temp].processes.append(p)
                                CPUs[temp].usage += p.usage
                                u.usage -= p.usage
                            break

                        # adding CPU to tried if overloaded
                        else:
                            tried.append(CPUs[temp])

            # pkt 3.
            #ckecking if CPU is underloaded
            elif u.usage < 30:

                # adding current CPU to tried
                tried.append(u)

                # checking all  CPU's left
                while len(tried) != len(CPUs):

                    # picking random CPU
                    temp = random.randint(0, len(CPUs) - 1)

                    # checking if picked CPU was not tried before
                    if not CPUs[temp] in tried:

                        # checking if CPU is overloaded
                        if CPUs[temp].usage > 70:

                            # moving 5 processes from other CPU to current CPU
                            for foo in range(5):
                                p = CPUs[temp].processes.pop()
                                u.processes.append(p)
                                u.usage += p.usage
                                CPUs[temp].usage -= p.usage
                            break

                        # adding CPU to tried if not overloaded
                        else:
                            tried.append(CPUs[temp])

        # updating stats for all CPU's
        for u in CPUs:
            u.Helper += u.usage
            u.usageAVG = u.Helper/time
            u.dHelper += u.usageAVG - u.usage
            u.usageAVGdeviation = u.dHelper/time




        time += 1
        if len(queue) == 0 or time == 1500:
            done = True
        print("t "+str(time))
        print(len(queue))

    for u in CPUs:
        print(u)



SIMULATE(50, 1000)