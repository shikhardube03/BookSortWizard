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