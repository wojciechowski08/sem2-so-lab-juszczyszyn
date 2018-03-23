
from Record import Record
import random

def generate(n, btMIN, btMAX, atMAX, atMIN=0):
    """

    :param int n:
    :param int btMIN:
    :param int btMAX:
    :param int atMAX:
    :param int atMIN:
    :return None:
    """

    records = []

    arrivalTimes = []

    for i in range(0, n):
        at = random.randint(atMIN, atMAX)
        arrivalTimes.append(at)
        while at in arrivalTimes:
            at = random.randint(atMIN, atMAX)
        bt = random.randint(btMIN, btMAX)
        r = Record(i+1, bt, at)
        records.append(r)

    return records

# l = generate(10, 1, 10, 10, 0)
# print(*l, sep='\n')