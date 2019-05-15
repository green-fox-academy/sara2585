import xml.dom.minidom

dom = xml.dom.minidom.parse("transactions.xml")
root = dom.documentElement

transaction = root.getElementsByTagName('transaction')
amount = root.getElementsByTagName("amount")
from1 = root.getElementsByTagName("from")
to = root.getElementsByTagName("to")

for j in range(len(amount)):
    if amount[j].getAttribute("currency") == "USD":
        print(f"from: {from1[j].firstChild.data}, to: {to[j].firstChild.data}, use: {amount[j].firstChild.data} USD")

#    amount = transaction[i].getElementsByTagName('amount')


#print(amount)





    