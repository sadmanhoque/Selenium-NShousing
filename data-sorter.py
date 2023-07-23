from bs4 import BeautifulSoup
import os
import csv

#function to remove whitespace
def removeSpace(string):
    return string.replace(" ", "")

#function to remove empty lines
def removeLine(text):
    lines = text.split('\n')
    non_empty_lines = filter(lambda line: line.strip() != '', lines)
    return '\n'.join(non_empty_lines)

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
    #soup = BeautifulSoup(content, 'html.parser')
    #print(soup.select('formValueSmall'))

    #going through all the table layers in the webpage until we get to the table with data
    soup = BeautifulSoup(content, 'lxml')
    #Adding a try catch exception for blank pages when roads had nothing on them
    try:
        tableOne = soup.find_all('table')[1]
        tableTwo = tableOne.find_all('tr')[0]
        tableThree = tableTwo.find_all('td')[0]
        tableFour = tableThree.find_all('table')[1]
        tableFive = tableFour.find_all('tr')[2]
        tableSix = tableFive.find_all('table')[0]

        #This saves the data in tableSix, used for figuring out how to parse data
        #tableSixFile = str(tableSix)
        #file_path = 'testing-webpages/tableSix.html'
        #with open(file_path, 'w', encoding='utf-8') as file:
        #    file.write(tableSixFile) 

        #Finding out how many properties are listed on this page
        textHeader = (tableFour.find_all('tr')[1]).text
        parsedTextHeader = textHeader.split(' ', 1)
        numberOfProperty = int(parsedTextHeader[0])
        #print(numberOfProperty)
        numberOfProperty = numberOfProperty * 13

        csvString = ""
        fileRow = []
        #Looping through each row now
        for x in range(0, numberOfProperty, 13):
            rows = []
            rowOne = tableSix.find_all('tr')[x+1]

            pid = (rowOne.find_all('td')[2]).text
            pid = removeLine(pid)
            pid = pid.strip()
            rows.append(pid)
            csvString += pid
            csvString += ","

            type = (rowOne.find_all('td')[4]).text
            type = removeLine(type)
            type = type.strip()
            rows.append(type)
            csvString += type
            csvString += ","

            status = (rowOne.find_all('td')[6]).text
            status = removeLine(status)
            status = status.strip()
            rows.append(status)
            csvString += status
            csvString += ","

            LRstatus = (rowOne.find_all('td')[8]).text
            LRstatus = removeLine(LRstatus)
            LRstatus = LRstatus.strip()
            rows.append(LRstatus)
            csvString += LRstatus
            csvString += ","

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
            csvString += owner
            csvString += ","

            mailingAddress = (rowOne.find_all('td')[13]).text
            mailingAddress = removeLine(mailingAddress)
            mailingAddress = mailingAddress.replace("\t", "")
            mailingAddress = mailingAddress.replace("\n", " ")
            mailingAddress = mailingAddress.strip()
            rows.append(mailingAddress)
            csvString += mailingAddress
            csvString += ","

            civicAddress = (rowOne.find_all('td')[16]).text
            civicAddress = removeLine(civicAddress)
            civicAddress = civicAddress.replace("\t", "")
            civicAddress = civicAddress.replace("\n", " ")
            civicAddress = civicAddress.strip()
            rows.append(civicAddress)
            csvString += civicAddress
            csvString += ","

            county = (rowOne.find_all('td')[18]).text
            county = removeLine(county)
            county = county.strip()
            rows.append(county)
            csvString += county
            csvString += ","

            area = (rowOne.find_all('td')[20]).text
            area = removeLine(area)
            area = area.strip()
            area = area.replace("SQUARE METERS", "")
            area = area.replace("\n", "")
            area = area.replace("\t", "")
            rows.append(area)
            csvString += area
            csvString += ","

            value = (rowOne.find_all('td')[25]).text
            value = removeLine(value)
            value = value.strip()
            value = value.replace(" (2023 RESIDENTIAL TAXABLE)", "")
            value = value.replace("$", "")
            value = value.replace(",", "")
            rows.append(value)
            csvString += value
            csvString += "\n"
            
            fileRow.append(rows)
            print(fileRow)
            #Making it so that each row has only one owner
            ownerList = rows[4].split("|")
            #print(ownerList)
            #x = 0
            #if len(ownerList) > 1:
            #    while len(ownerList) > 0:
            #        newRow = rows
            #        newRow[4] = ownerList[x]
            #        #print(newRow)
            #        ownerList.remove(ownerList[x])
                    #fileRow.append(newRow)
            #        x+=1
            #else:
                #fileRow.append(rows)
            
            #print(fileRow)

        #appending as a csv content\
        filename = "testing-csv-formats.csv"
        with open(filename, 'a') as csvfile:
            csvwriter = csv.writer(csvfile)
            #csvwriter.writerow(fields)
            csvwriter.writerows(fileRow)
    except:
        #print("an error occured for file "+fileList[a])
        file1 = open("problem-streets", "w")
        file1.write(fileList[a]+"\n")
        file1.close()