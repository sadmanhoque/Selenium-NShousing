from bs4 import BeautifulSoup
import os
import csv
from util import coordinateFinder, removeSpace, removeLine, fileWriter

#reading list of html files    
path_of_the_directory= 'testing-webpages/'
print("Files and directories in a specified path:")
fileList = []
for filename in os.listdir(path_of_the_directory):
    f = os.path.join(path_of_the_directory,filename)
    if os.path.isfile(f):
        print(f)
        fileList.append(f)

#Looping through every file in the dir
for a in range(len(fileList)):
    f = open(fileList[a])
    print(fileList[a])
    content = f.read()

    #going through all the table layers in the webpage until we get to the table with data
    soup = BeautifulSoup(content, 'lxml')
    #Adding a try catch exception for pages with some sort of error in 'em
    try:
        
        #Skipping if it's a blank page
        if len(soup.find_all('table')) == 0:
            continue

        tableOne = soup.find_all('table')[1]
        tableTwo = tableOne.find_all('tr')[0]
        tableThree = tableTwo.find_all('td')[0]
        tableFour = tableThree.find_all('table')[1]
        tableFive = tableFour.find_all('tr')[2]
        tableSix = tableFive.find_all('table')[0]

        #Finding out how many properties are listed on this page
        textHeader = (tableFour.find_all('tr')[1]).text
        parsedTextHeader = textHeader.split(' ', 1)
        numberOfProperty = int(parsedTextHeader[0])
        if numberOfProperty > 250:
            numberOfProperty = 250
        numberOfProperty = numberOfProperty * 13

        
        fileRow = []
        #Looping through each row now
        for x in range(0, numberOfProperty, 13):
            rows = []
            rowOne = tableSix.find_all('tr')[x+1]

            pid = (rowOne.find_all('td')[2]).text
            pid = removeLine(pid)
            pid = pid.strip()
            rows.append(pid)

            type = (rowOne.find_all('td')[4]).text
            type = removeLine(type)
            type = type.strip()
            rows.append(type)

            status = (rowOne.find_all('td')[6]).text
            status = removeLine(status)
            status = status.strip()
            rows.append(status)

            LRstatus = (rowOne.find_all('td')[8]).text
            LRstatus = removeLine(LRstatus)
            LRstatus = LRstatus.strip()
            rows.append(LRstatus)

            owner = (rowOne.find_all('td')[11])
            owner = str(owner)
            owner = owner.replace("<br/>", " | ")
            owner = owner.replace("</td>", "")
            owner = owner.replace("<td class=\"formValueSmall\">", "")
            owner = owner.replace("\t", "")
            owner = owner.replace("\n", " ")
            owner = removeLine(owner)
            owner = owner.strip()
            owner = owner[:-3]
            rows.append(owner)

            mailingAddress = (rowOne.find_all('td')[13]).text
            mailingAddress = removeLine(mailingAddress)
            mailingAddress = mailingAddress.replace("\t", "")
            mailingAddress = mailingAddress.replace("\n", " ")
            mailingAddress = mailingAddress.strip()
            rows.append(mailingAddress)

            civicAddress = (rowOne.find_all('td')[16]).text
            civicAddress = removeLine(civicAddress)
            civicAddress = civicAddress.replace("\t", "")
            civicAddress = civicAddress.replace("\n", " ")
            civicAddress = civicAddress.strip()
            rows.append(civicAddress)

            rows.append(coordinateFinder(civicAddress))

            county = (rowOne.find_all('td')[18]).text
            county = removeLine(county)
            county = county.strip()
            rows.append(county)  

            area = (rowOne.find_all('td')[20]).text
            area = removeLine(area)
            area = area.strip()
            area = area.replace("SQUARE METERS", "")
            area = area.replace("\n", "")
            area = area.replace("\t", "")
            rows.append(area)

            value = (rowOne.find_all('td')[25]).text
            value = removeLine(value)
            value = value.strip()
            value = value.replace(" (2023 RESIDENTIAL TAXABLE)", "")
            value = value.replace("$", "")
            value = value.replace(",", "")
            rows.append(value)

            #Making it so that each row has only one owner
            ownerList = rows[4].split("|")
            print(ownerList)
            ownerCount = len(ownerList)
            if len(ownerList) > 1:
                while len(ownerList) > 0:
                    newRow = rows
                    newRow[4] = ownerList[ownerCount]
                    newRow[4] = newRow[4].strip()
                    fileRow.append(newRow)
                    ownerList.remove(ownerList[ownerCount])
                    ownerCount=-1 
            else:
                fileRow.append(rows)
            
            print(fileRow)

        #appending as a csv content\
        filename = "testing-owner-list.csv"
        with open(filename, 'a') as csvfile:
            csvwriter = csv.writer(csvfile)
            #csvwriter.writerow(fields)
            csvwriter.writerows(fileRow)
    except Exception as e: 
        print(e)
        file1 = open("problem-streets", "w")
        file1.write(fileList[a]+"\n")
        file1.close()