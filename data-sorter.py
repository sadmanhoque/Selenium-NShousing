from bs4 import BeautifulSoup
import os

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

#f =  open('webpages/A Y JACKSONCOURT.html')
for a in range(len(fileList)):
    f = open(fileList[a])
    content = f.read()
    #soup = BeautifulSoup(content, 'html.parser')
    #print(soup.select('formValueSmall'))

    #going through all the table layers in the webpage until we get to the table with data
    soup = BeautifulSoup(content, 'lxml')
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

    #Looping through each row now
    for x in range(0, numberOfProperty, 13):
        #print(x)
    #x = 13
        rowOne = tableSix.find_all('tr')[x+1]

        pid = (rowOne.find_all('td')[2]).text
        pid = removeLine(pid)
        csvString += pid
        csvString += ","

        type = (rowOne.find_all('td')[4]).text
        type = removeLine(type)
        type = type.strip()
        csvString += type
        csvString += ","

        status = (rowOne.find_all('td')[6]).text
        status = removeLine(status)
        status = status.strip()
        csvString += status
        csvString += ","

        LRstatus = (rowOne.find_all('td')[8]).text
        LRstatus = removeLine(LRstatus)
        LRstatus = LRstatus.strip()
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
        #owner = owner.strip()
        #print(owner)
        csvString += owner
        csvString += ","

        mailingAddress = (rowOne.find_all('td')[13]).text
        mailingAddress = removeLine(mailingAddress)
        mailingAddress = mailingAddress.replace("\t", "")
        mailingAddress = mailingAddress.replace("\n", " ")
        #print(mailingAddress)
        csvString += mailingAddress
        csvString += ","

        civicAddress = (rowOne.find_all('td')[16]).text
        civicAddress = removeLine(civicAddress)
        civicAddress = civicAddress.replace("\t", "")
        civicAddress = civicAddress.replace("\n", " ")
        #print(civicAddress)
        csvString += civicAddress
        csvString += ","

        county = (rowOne.find_all('td')[18]).text
        county = removeLine(county)
        county = county.strip()
        #print(county)
        csvString += county
        csvString += ","

        area = (rowOne.find_all('td')[20]).text
        area = removeLine(area)
        area = area.strip()
        area = area.replace("SQUARE METERS", "")
        area = area.replace("\n", "")
        area = area.replace("\t", "")
        #print(area)
        csvString += area
        csvString += ","

        value = (rowOne.find_all('td')[25]).text
        value = removeLine(value)
        value = value.strip()
        value = value.replace(" (2023 RESIDENTIAL TAXABLE)", "")
        value = value.replace("$", "")
        value = value.replace(",", "")
        #print(value)
        csvString += value
        csvString += "\n"
        #print(csvString)

    #appending to an existing blank csv file
    file1 = open("sampleOutput.csv", "a")
    file1.write(csvString)
    file1.close()