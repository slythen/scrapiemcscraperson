from bs4 import BeautifulSoup
import requests

selectP = str("http://www.directv.com/DTVAPP/compare/printablePackageChannels.jsp?packageId=1150002&skuId=P000101049&referrer=https://support.directv.com/app/answers/detail/a_id/360/kw/printable%20channel%20list")
entertainmentP = str("http://www.directv.com/DTVAPP/compare/printablePackageChannels.jsp?packageId=1310002&skuId=sku2920002&referrer=https://support.directv.com/app/answers/detail/a_id/360/kw/printable%20channel%20list&referrer=https://support.directv.com/app/answers/detail/a_id/360/kw/printable%20channel%20list")
choiceP = str("http://www.directv.com/DTVAPP/compare/printablePackageChannels.jsp?packageId=960008&skuId=sku930008&referrer=https://support.directv.com/app/answers/detail/a_id/360/kw/printable%20channel%20list")
xtraP = str("http://www.directv.com/DTVAPP/compare/printablePackageChannels.jsp?packageId=960010&skuId=sku930012&referrer=https://support.directv.com/app/answers/detail/a_id/360/kw/printable%20channel%20list")
ultimateP = str("http://www.directv.com/DTVAPP/compare/printablePackageChannels.jsp?packageId=1120008&skuId=sku1140004&referrer=https://support.directv.com/app/answers/detail/a_id/360/kw/printable%20channel%20list")
premierP = str("http://www.directv.com/DTVAPP/compare/printablePackageChannels.jsp?packageId=960014&skuId=sku930016&referrer=https://support.directv.com/app/answers/detail/a_id/360/kw/printable%20channel%20list&referrer=https://support.directv.com/app/answers/detail/a_id/360/kw/printable%20channel%20list" )


r = requests.get(premierP)
soup = BeautifulSoup(r.text)

def overTable():
    RoW = []
    MainT = soup.find_all('table', class_="package")
    for TablE in MainT:
        RoW.append(TablE)
    return RoW

TableS = overTable()


tableS = BeautifulSoup(str(TableS).strip(']').strip('['))

UberDict = {}

tableS.tr.next_sibling
rowNum = 0
rows = len(tableS.find_all('tr'))
while (rowNum < rows):
    cell = tableS.find_all('tr')[rowNum]
    UberDict[str(cell.find('td', width='98%').text).strip()] = [str(cell.find('td', class_="ch-no").text).strip()]
    rowNum += 1




#rowS = []
#for i in TableS:
#    rowS.append(BeautifulSoup(str(i)).find_all('tr'))

#for i in rowS:
#    help(i)
    
    



#first 4 are en espanol
#print RoW[0]