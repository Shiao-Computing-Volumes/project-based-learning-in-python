
# coding: utf-8

# In[ ]:


import pandas as pd


# In[ ]:


import numpy as np


# In[ ]:


#rather perhaps superfluous
import math, re, operator, fnmatch, itertools


# In[ ]:


from itertools import islice


# In[ ]:


from networkx.utils import powerlaw_sequence


# After pasting citable pages from a book into a csv file, on the Home tab, in the Editing group, click the arrow next to the Clear button, and click Clear Formats.

# In[ ]:


pathToFile = "G:\pageNumberAdder\pagenumbers.csv"


# In[ ]:


#This program uses both dataReg and data
data = pd.read_csv(pathToFile, encoding="ISO-8859-1")


# In[ ]:


print("Where are the page numbers? \n1 the end of the page; \n2 the end of the page, except chapter title pages have no page number, only the chapter number at the top; \n3 the end of the page, except chapter title pages have no page number, Nor any chapter number at the top; \n4 the end of the page including chapter title pages, which also have chapter title page at the top; \n5 at the top of the page, except chapter title pages have no page number, Nor any chapter number at the top; \n6 the top of the page, except chapter title pages have no page number, only the chapter number at the top; \n7 the top of the page; \n8 the top of the page, except chapter title pages have the page number at the end of the page.")


# In[ ]:


paginationFormat = input("Please indicate where the page numbers are located: ")


# In[ ]:


print(paginationFormat)


# In[ ]:


chapterTitlePageList = input("What pages are chapter title pages?")


# In[ ]:


def chTitlePage(chapterTitlePageList)


# In[ ]:


chTitlePage()


# In[ ]:


def numberLayout(pageNumberPattern)
    rangeOfNumbers = 7

    for a in rangeOfNumbers:
        if pageNumberPattern == a:
            

    return


# In[ ]:


numberLayout()


# OKAY PRE-PROCESSING

# In[ ]:


#for actual processing, see mypreprocessing txt file


# In[ ]:


print("Please enter your list of page numbers: ")


# In[ ]:


#Remember to use just ENTER TWICE for input


# In[55]:


listy = [(x) for x in input().split(', ')]


# In[56]:


print(listy)


# In[57]:


#for actual processing, see myprocessing2 txt file


# In[58]:


def commaHyphenFix(lliissttyy):
    pageNumberList = []
    priorNumber = 0
    for stringchar, item in enumerate(lliissttyy):
        if "-" in item:
            splitNumber1, splitNumber2 = item.split('-')   
            if splitNumber1 == "":
                
                pageNumberList.append(str(priorNumber) + "-" + splitNumber2) 
        priorNumber = lliissttyy[stringchar]

    return pageNumberList
    


# In[59]:


print(commaHyphenFix(listy))


# Add page numbers indicated by '-'. Check every instance of a hyphen between two numbers. If they are not integers sequential by 1 integer, the program should loop through, adding each integer in between those 2 integers. For example, an input list of ‘29-34’ would be changed to '29, 30, 31, 32, 33, 34'.

# In[30]:


def addPages(lliisstt):
    pageNumberList = []
    for stringchar, item in enumerate(lliisstt):
        if "-" in item:
            splitNumber1, splitNumber2 = item.split('-')   
            rangy = int(splitNumber2) - int(splitNumber1) + 1
            for counter in range(rangy):          
                splitNumber = str(int(splitNumber1) + counter)
                pageNumberList.append(splitNumber) 
        else:
            pageNumberList.append(item) 
                
    return pageNumberList
    


# In[31]:


yayList = addPages(listy)


# In[32]:


print(yayList)


# In[33]:


#Delete apostrophes, and siphon through the page number program


# In[34]:





# OKAY PAGE NUMBER ADDER SECTION

# In[ ]:


# Gets row indexes that have a number NOT adjacent to a colon or period - or what might have been a 
# colon or period in the original (so as to not mistake a verse number or number in a numbered list
# for a page number). Will CAUSE problems if a scan has smushed a colon in with a block of text
# containing a real page number, OR if a scan has turned letter(s) into a number adjacent to a colon or period.
dataReg = open(pathToFile)
listOIndexes = []
def getRawIndexList():
    listToAvoid = ('0:','1:','2:','3:', '4:', '5:', '6:', '7:', '8:', '9:', ':0', ':1', ':2', ':3', ':4', ':5', ':6', ':7', ':8', ':9', '0:','1:','2:','3:', '4:', '5:', '6:', '7:', '8:', '9:', ':0', ':1', ':2', ':3', ':4', ':5', ':6', ':7', ':8', ':9', '0.','1.','2.','3.', '4.', '5.', '6.', '7.', '8.', '9.', '.0', '.1', '.2', '.3', '.4', '.5', '.6', '.7', '.8', '.9')
    for rowIndexes, row in enumerate(dataReg):
        if re.search('[0-9]', row):
            if row in listToAvoid:
                pass
            else:
                listOIndexes.append(rowIndexes)
    return listOIndexes


# In[ ]:


rawIndexList = getRawIndexList()


# In[ ]:


print(rawIndexList)


# Having gotten the indexes of the rows that contain numbers, which I'll use to assign the value 'pagebreaker' in relevant cells in the 'E' row, I now delete from the list indexes pertaining to any numbers that are in the text rather than being page number delimiters. I will manually add any page break rows the program didn't catch. 
# Later, running the list through something that makes sure there aren't any lengthy gaps between indexes (which would indicate the possible missing of a pagebreak) can help me find any I need to add.
# For this program, I'm assuming that the page numbers from this 'book' are the end of the pages.

# In[ ]:


data.head()


# In[ ]:


def initializeDictionaryOfRows(initializeListOfRows):
    rowDict = {k: v for v, k in enumerate(initializeListOfRows)}
    return(rowDict)


# In[ ]:


def assignListOfIndexesToDict(indexList):
    inDictMint = {k: v for v, k in enumerate(indexList)}
    return(inDictMint)


# In[ ]:


listOfRows = [None]*4346
dictOfRows = initializeDictionaryOfRows(listOfRows)
print(dictOfRows)

listOfIndexes = [1, 36, 73, 110, 147, 186, 222, 258, 294, 331, 369, 402, 437, 470, 506, 539, 576, 644, 678, 715, 751, 787, 823, 860, 895, 931, 965, 1001, 1028, 1064, 1100, 1135, 1170, 1204, 1240, 1277, 1314, 1349, 1386, 1422, 1458, 1494, 1529, 1564, 1591, 1627, 1664, 1702, 1739, 1776, 1810, 1844, 1880, 1917, 1952, 1984, 2023, 2060, 2095, 2131, 2168, 2205, 2239, 2276, 2312, 2345, 2381, 2417, 2453, 2490, 2527, 2562, 2599, 2636, 2673, 2710, 2747, 2782, 2818, 2855, 2891, 2926, 2962, 2996, 3033, 3071, 3109, 3144, 3182, 3219, 3255, 3289, 3326, 3363, 3398, 3435, 3471, 3508, 3545, 3582, 3617, 3654, 3717, 3750, 3786, 3820, 3857, 3894, 3931, 3966, 4003, 4040, 4075, 4110, 4146, 4183, 4219, 4254, 4291, 4328]
dictOfIndexes = assignListOfIndexesToDict(listOfIndexes)
print(dictOfIndexes)


# In[ ]:


def addPagebreakers(ur_Dict_Of_Rows, ur_Dict_Of_Indexes):
    #Take dictOfRows and add pagebreakers based on dictOfIndexes
    newDict = {}
    for k,cellValue in ur_Dict_Of_Rows.items():
        if cellValue in ur_Dict_Of_Indexes:
            newDict[cellValue] = 'pagebreaker'
        else:
            newDict[cellValue] = cellValue
    return newDict
    


# In[ ]:


morphingDict = addPagebreakers(dictOfRows, dictOfIndexes)
morphingDict


# In[ ]:


def addPageNumbers(dictInProgress, yayIndexListAgain, pageNumberList, rowList, indexList):
    finalList = []
    counter = 0

    for i, v in enumerate(dictInProgress):
        if dictInProgress[v] == "pagebreaker":
            counter += 1
            finalList.append("pageBreaker")
        else:
            if counter < len(yayIndexListAgain):
                finalList.append(str(pageNumberList[counter]))
                
    print(finalList)

    return finalList


# In[ ]:


listOfPageNumbers = [5, 6, 7, 8, 9, 10, 13, 14, 15, 17, 26, 27, 28, 36, 37, 38, 39, 42, 43, 44, 45, 46, 47, 48, 49, 54, 55, 56, 57, 58, 59, 60, 61, 62, 65, 67, 71, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 110, 111, 114, 117, 120, 121, 123, 124, 127, 128, 129, 130, 131, 132, 141, 145, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 174, 175, 176, 177, 178, 179, 180, 181]
youGotItToyotaList = addPageNumbers(morphingDict, dictOfIndexes, listOfPageNumbers, listOfRows, listOfIndexes)


# Make sure you've inserted the current list of page numbers AND the dictionary from above:

# In[ ]:


listOfPageNumbers = [5, 6, 7, 8, 9, 10, 13, 14, 15, 17, 26, 27, 28, 36, 37, 38, 39, 42, 43, 44, 45, 46, 47, 48, 49, 54, 55, 56, 57, 58, 59, 60, 61, 62, 65, 67, 71, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 110, 111, 114, 117, 120, 121, 123, 124, 127, 128, 129, 130, 131, 132, 141, 145, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 174, 175, 176, 177, 178, 179, 180, 181]

#initialize dictionary
pgDict = {
    1: 0, 36: 1, 73: 2, 110: 3, 147: 4, 186: 5, 222: 6, 258: 7, 294: 8, 331: 9, 369: 10, 402: 11, 437: 12, 470: 13, 506: 14, 539: 15, 576: 16, 644: 17, 678: 18, 715: 19, 751: 20, 787: 21, 823: 22, 860: 23, 895: 24, 931: 25, 965: 26, 1001: 27, 1028: 28, 1064: 29, 1100: 30, 1135: 31, 1170: 32, 1204: 33, 1240: 34, 1277: 35, 1314: 36, 1349: 37, 1386: 38, 1422: 39, 1458: 40, 1494: 41, 1529: 42, 1564: 43, 1591: 44, 1627: 45, 1664: 46, 1702: 47, 1739: 48, 1776: 49, 1810: 50, 1844: 51, 1880: 52, 1917: 53, 1952: 54, 1984: 55, 2023: 56, 2060: 57, 2095: 58, 2131: 59, 2168: 60, 2205: 61, 2239: 62, 2276: 63, 2312: 64, 2345: 65, 2381: 66, 2417: 67, 2453: 68, 2490: 69, 2527: 70, 2562: 71, 2599: 72, 2636: 73, 2673: 74, 2710: 75, 2747: 76, 2782: 77, 2818: 78, 2855: 79, 2891: 80, 2926: 81, 2962: 82, 2996: 83, 3033: 84, 3071: 85, 3109: 86, 3144: 87, 3182: 88, 3219: 89, 3255: 90, 3289: 91, 3326: 92, 3363: 93, 3398: 94, 3435: 95, 3471: 96, 3508: 97, 3545: 98, 3582: 99, 3617: 100, 3654: 101, 3717: 102, 3750: 103, 3786: 104, 3820: 105, 3857: 106, 3894: 107, 3931: 108, 3966: 109, 4003: 110, 4040: 111, 4075: 112, 4110: 113, 4146: 114, 4183: 115, 4219: 116, 4254: 117, 4291: 118, 4328: 119
    }

for key in pgDict:
    if pgDict[key] < 10:
        print(key, pgDict[key])


# I could cycle through the indexes backwards, adding the last number in the list through until the second-to-last index, etc., then assign the list or whatever to a new column.

# In[40]:


newcol = np.log(data['PageNumbers'])
newcol = pd.Series(youGotItToyotaList)
data.assign(PageNumbers=newcol)

