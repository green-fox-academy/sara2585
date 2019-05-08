telebook = {"William A. Lathan": "405-709-1865", "John K. Miller": "402-247-8568", "Hortensia E. Foster": "606-481-6467", "Amanda D. Newland": "319-243-5613", "Brooke P. Askew": "307-687-2982"}
#What is John K. Miller's phone number?
print(telebook["John K. Miller"])

#Whose phone number is 307-687-2982?
n = ""
for key in telebook:
    if telebook[key] == "307-687-2982":
        print(key)
#Do we know Chris E. Myers' phone number?

print("Chris E. Myer" in telebook)