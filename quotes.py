#create variable
name = input("Enter name and see the qoute: ").strip().lower()

#make list with quotes
quote = ["The greatest glory in living lies not in never falling, but in rising every time we fall.",
"The way to get started is to quit talking and begin doing.",
"Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma – which is living with the results of other people's thinking.",
"If life were predictable it would cease to be life, and be without flavor.",
"Life is what happens when you're busy making other plans."
]

#check conditionals to print answer
if name == "nelson" or name == "Mandela":
   print(f"{name} said, \"{quote[0]}\"")
elif name == "walt" or name == "disney":
   print(f"{name} said, \"{quote[1]}\"")
elif name == "steve" or name == "jobs":
   print(f"{name} said, \"{quote[2]}\"")
elif name == "eleanor" or name == "roosevelt":
   print(f"{name} said, \"{quote[3]}\"")
elif name == "john" or name == "lennon":
   print(f"{name} said, \"{quote[4]}\"")
else:
   print("try again")
