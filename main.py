#!/usr/bin/env python3

import sys
from browser import browser




    
def main():
    obj = browser()
    if (obj == False):
        sys.exit(1)
    obj.openUrl()
    obj.search()
    if(obj.getResultsNum() < obj.getActualResultsNum()):
        print ("Expected results num %d, actual %d" % (obj.resultNum, obj.actualResultsNum))

    nameList = obj.getItemsWithoutRating()
    if (nameList):
        print ("Items without rating: ")
        for i in range (len(nameList)):
            print ("%d - %s " % (i + 1, nameList[i]) )


if __name__ == "__main__":
    main()
    sys.exit(0)
