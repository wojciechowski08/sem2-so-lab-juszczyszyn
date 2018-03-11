
bt = []
n = int(input("Enter the number of process: "))
print("Enter the burst time of the processes: \n")
bt = list(map(int, raw_input().split()))
waitTime = []
avgWT = 0
turnAroundTime = []
avgTAT = 0
waitTime.insert(0, 0)
turnAroundTime.insert(0, bt[0])

for i in range(1, len(bt)):
    waitTime.insert(i, waitTime[i-1]+bt[i-1])
    turnAroundTime.insert(i, waitTime[i]+bt[i])
    avgWT += waitTime[i]
    avgTAT += turnAroundTime[i]

avgWT = float(avgWT)/n
avgTAT = float(avgTAT)/n

print("\n")
print("Process\t  Burst Time\t  Waiting Time\t  Turn Around Time")

for i in range(0, i):
    print(str(i) + "\t\t" + str(bt[i]) + "\t\t" + str(waitTime[i] + "\t\t" + str(turnAroundTime[i])))
    print("\n")

print("Average Waiting time is: "+str(avgWT))
print("Average Turn Arount Time is: "+str(avgTAT))