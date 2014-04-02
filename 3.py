#!/usr/bin/python
import pickle
from bs4 import BeautifulSoup
import requests

selectP = str("http://www.directv.com/DTVAPP/compare/printablePackageChannels.jsp?packageId=1150002&skuId=P000101049&referrer=https://support.directv.com/app/answers/detail/a_id/360/kw/printable%20channel%20list")
entertainmentP = str("http://www.directv.com/DTVAPP/compare/printablePackageChannels.jsp?packageId=1310002&skuId=sku2920002&referrer=https://support.directv.com/app/answers/detail/a_id/360/kw/printable%20channel%20list&referrer=https://support.directv.com/app/answers/detail/a_id/360/kw/printable%20channel%20list")
choiceP = str("http://www.directv.com/DTVAPP/compare/printablePackageChannels.jsp?packageId=960008&skuId=sku930008&referrer=https://support.directv.com/app/answers/detail/a_id/360/kw/printable%20channel%20list")
xtraP = str("http://www.directv.com/DTVAPP/compare/printablePackageChannels.jsp?packageId=960010&skuId=sku930012&referrer=https://support.directv.com/app/answers/detail/a_id/360/kw/printable%20channel%20list")
ultimateP = str("http://www.directv.com/DTVAPP/compare/printablePackageChannels.jsp?packageId=1120008&skuId=sku1140004&referrer=https://support.directv.com/app/answers/detail/a_id/360/kw/printable%20channel%20list")
premierP = str("http://www.directv.com/DTVAPP/compare/printablePackageChannels.jsp?packageId=960014&skuId=sku930016&referrer=https://support.directv.com/app/answers/detail/a_id/360/kw/printable%20channel%20list&referrer=https://support.directv.com/app/answers/detail/a_id/360/kw/printable%20channel%20list" )
  
urls = [selectP, entertainmentP, choiceP, xtraP, ultimateP, premierP]

def packAger(urL):
    if urL == selectP:
        Package = 'SelectP'
    elif urL == entertainmentP:
        Package = 'EntertainmentP'
    elif urL == choiceP:
        Package = 'ChoiceP'
    elif urL == xtraP:
        Package = 'xtraP'
    elif urL == ultimateP:
        Package = 'ultimateP'
    elif urL == premierP:
        Package = 'premierP'
    else:
        Package = 'Crap'
    return Package

for packageUrl in urls:
    r = requests.get(packageUrl)
    soup = BeautifulSoup(r.text)
    RoW = []
    MainT = soup.find_all('table', class_="package")
    for TablE in MainT:
        RoW.append(TablE)    
    TableS = RoW
    tableS = BeautifulSoup(str(TableS).strip(']').strip('['))
    UberDict = {}
    rowNum = 0
    rows = len(tableS.find_all('tr'))
    while (rowNum < rows):
        cell = tableS.find_all('tr')[rowNum]
        UberDict[str(cell.find('td', width='98%').text).strip().strip('*')] = [str(cell.find('td', class_="ch-no").text).strip()]
        rowNum += 1

for currentPack in urls:
    r = requests.get(packageUrl)
    soup = BeautifulSoup(r.text)
    RoW = []
    MainT = soup.find_all('table', class_="package")
    for TablE in MainT:
        RoW.append(TablE)    
    TableS = RoW
    tableS = BeautifulSoup(str(TableS).strip(']').strip('['))
    rowNum = 0
    rows = len(tableS.find_all('tr'))
    while (rowNum < rows):
        cell = tableS.find_all('tr')[rowNum]
        UberDict[str(cell.find('td', width='98%').text).strip().strip('*')].append(packAger(currentPack))        
        rowNum += 1

pickle.dump(UberDict,open('DTVDict.p', 'w'))
#print UberDict


