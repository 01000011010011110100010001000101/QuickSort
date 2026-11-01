#Quick Sort
import random

def QuickSort(List):

    if len(List) <= 1:
        return List
    
    Pivot = List[random.randint(0,len(List) - 1)]

    Bigger = []
    Smaller = []
    Equal = []
    for X in List:
        
        if X > Pivot:
            Bigger.append(X)
        
        elif X < Pivot:
            Smaller.append(X)
        
        else:
            Equal.append(X)


    return QuickSort(Smaller) + Equal + QuickSort(Bigger)


List = []

for i in range(10):
    List.append(random.randint( 1, 10 ))
print(List)
print(QuickSort(List))