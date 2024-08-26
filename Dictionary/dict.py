bio_data = {"name" : "Rakibul","age": 21,"branch":"CSE"}

# printing value by key
print(bio_data["name"])
print(bio_data.get("age"))

# change disct
bio_data["name"] = "Rakibul Islam"
print(bio_data.get("name"))
print(bio_data)

# Looping through dict
print("\n------Bio Data-------\n")
for data in bio_data:
    print(data,":",bio_data[data])

print("\n------Bio Data-------\n")
for key,value in bio_data.items():
    print(key,value)

# nasted dictionary
print("\n-----------------------\n")
books = {
    "love" : {
        "1st" : "Romeo and  Juliet",
        "2nd" : "It's End with us",
        "3rd" :"Twilight"
        },
    
    "horror" : {
        "1st" : "The Haunting of Hill House",
        "2nd" : "It",
        "3rd" :"Misery"
    },

    "thriller" : {
        "1st" : "The Silent Patient",
        "2nd" : "Gone Girl",
        "3rd" :"The Girl on the train"
    }
}

# Acces value 
print("\n----Show all the books!----\n")
for type in books:
    print(f"{type} type :")
    for index in books[type]:
        print(f"{index} : {books[type][index]}")
    print("\n")

print("\n----Show all the thriller books!-----\n")

for type in range(1):
    for index in books["thriller"]:
        print(index,":", books["thriller"][index])



# Squared Number in a dict

print("\n-----------------\n")

key = ["1st","2nd","3rd"]
value = ["Twilight","Gone Girl","Love"]
default = "LOVE"
my_dict = dict.fromkeys(key, default)

print(my_dict)