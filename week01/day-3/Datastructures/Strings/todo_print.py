

# Add " - Diablo" to the end of the todoText but with indention



# Expected outpt:



# My todo:

#  - Buy milk

#  - Download games

#      - Diablo



todoText = " - Buy milk\n"
# Add "My todo:" to the beginning of the todoText
list_todoText = []
list_todoText = list(todoText)
list_todoText.insert(0, "My todo:")
todoText = "".join(list_todoText)

# Add " - Download games" to the end of the todoText
n = list_todoText.index("\n")
list_todoText.insert(n, " - Download games")
todoText = "".join(list_todoText)


# Add " - Diablo" to the end of the todoText but with indention
n1 = list_todoText.index("\n")
list_todoText.insert(n1, " - Diablo")
todoText = "".join(list_todoText)

list_todoText = todoText.split(" ")
#print(list_todoText)
list_todoText.insert(2, "\n")
list_todoText.insert(6, "\n")
list_todoText.insert(10, "\n")    
todoText = " ".join(list_todoText)
print(todoText)