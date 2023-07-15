from bs4 import BeautifulSoup
#import pandas as pd

f =  open('webpages/A Y JACKSONCOURT.html')
content = f.read()
#soup = BeautifulSoup(content, 'html.parser')
#print(soup.select('formValueSmall'))

soup = BeautifulSoup(content, 'lxml')
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
#print(numberOfProperty)

for x in range(numberOfProperty):
    print(x)

#Make a loop here to go through each row as each represents a property
rowOne = tableSix.find_all('tr')[1]
pid = rowOne.find_all('td')[2]

type = rowOne.find_all('td')[4]

status = rowOne.find_all('td')[6]

LRstatus = rowOne.find_all('td')[8]

owner = rowOne.find_all('td')[11]

mailingAddress = rowOne.find_all('td')[13]

civicAddress = rowOne.find_all('td')[16]

county = rowOne.find_all('td')[18]

area = rowOne.find_all('td')[20]

value = rowOne.find_all('td')[25]

print(owner.text)