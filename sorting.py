class Label:
    firstLine = None
    secondLine = 0.0
    thirdLine = None
    year = 0
    version = None
    def __init__(self, first,  second,  third,  newYear, newVersion):
        self.firstLine = first
        self.secondLine = float(second)
        self.thirdLine = third
        self.year = int(newYear)
        self.version = newVersion
    def getFirstLine(self):
        return self.firstLine
    def getSecondLine(self):
        return self.secondLine
    def getThirdLine(self):
        return self.thirdLine
    def getYear(self):
        return self.year
    def compareTo(self, o):
        #  Compare string on first line
        if self.firstLine != o.getFirstLine():
            if self.firstLine < o.getFirstLine():
            
               return -1
            else:
                return 1
        else:
            #  Compare doubles on second line
            if self.secondLine != o.secondLine:
                return self.secondLine - o.secondLine
            else:
                #  Compare the first char on third line
                if self.thirdLine[0] != o.thirdLine[0]:
                    if self.thirdLine[0] < o.thirdLine[0]:
                        return -1
                    else:
                        return 1
                else:
                    #  Compare the int on third line
                    intInThirdLine = int(self.thirdLine[1 : len(self.thirdLine)])
                    intInOtherThirdLine = int(o.thirdLine[1 : len(o.thirdLine)])
                    if intInThirdLine - intInOtherThirdLine != 0:
                        return intInThirdLine - intInOtherThirdLine
                    else:
                        #  Compare the year
                        if self.year - o.year != 0:
                            return self.year - o.year
                        else:
                            # Compare the version
                            if (self.version == None and o.version == None):
                                return 0
                            elif (self.version != None and o.version == None):
                                return 1
                            elif (self.version == None and o.version != None):
                                return -1
                            else:
                                if self.version != o.version:
                                    if self.version < o.version:
                                        return -1
                                    else:
                                        return 1
                                else:
                                    return 0
    def  equals(self, o):
        return self.firstLine == o.firstLine and self.secondLine == o.secondLine and self.thirdLine == o.thirdLine and self.year == o.year

# Python program for implementation of MergeSort
def mergeSort(arr):
	if len(arr) > 1:

		# Finding the mid of the array
		mid = len(arr)//2

		# Dividing the array elements
		L = arr[:mid]

		# into 2 halves
		R = arr[mid:]

		# Sorting the first half
		mergeSort(L)

		# Sorting the second half
		mergeSort(R)

		i = j = k = 0

		# Copy data to temp arrays L[] and R[]
		while i < len(L) and j < len(R):
			if L[i].compareTo(R[j]) <= 0:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1

		# Checking if any element was left
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1

# Code to print the list


def printList(arr):
	for i in range(len(arr)):
		print(arr[i], end=" ")
	print()

l1 = Label("DS", "799.8", "J536", "2019", "Test")
l2 = Label("DS", "799.8", "J536", "2019", None)
l3 = Label("DS", "799.8", "J536", "2019", None)
l4 = Label("DS", "799.8", "J536", "2019", None)

arrayOfLabels = [l1, l2, l3, l4]
arrayOfLabelsCopy = [0] * len(arrayOfLabels)
arrayOfIndex = [0] * len(arrayOfLabels)
for i in range(len(arrayOfLabels)):
    arrayOfLabelsCopy[i] = arrayOfLabels[i]
    arrayOfIndex[i] = i
mergeSort(arrayOfLabels)
print("For these " + str(len(arrayOfLabels)) + " books with labels in the image,")
print("From the left,")
for i in range(len(arrayOfLabels)):
    for j in range(len(arrayOfIndex)):
        if arrayOfLabelsCopy[i] == arrayOfLabels[arrayOfIndex[j]]:
            print("Book " + str((i + 1)) + " should be in position " + str((arrayOfIndex[j] + 1)))
            del arrayOfIndex[j]
            break
