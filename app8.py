# name = "aman"
# age = 20
# course = "python"
# key or values :
# student ={
#     "name":"Aman",
#     "age":28,
#     "course":"Python"
# }

# print(student["name"])
# print(student["age"])

# menu_card = {
#     "Pizza":300,
#     "Burger":200,
#     "Cold Coffee":120
# }
# menu_card["French Fries"] = 100
# item = "French Fries"
# for i in menu_card:
#     print(f"{i} ka price hai  :  {menu_card[i]}")


# search_name  =  "jyoti"    
# print(search_name)


# name  =  "Ganesh Dutt"
# print( "Hello", name)
# print(f"Hello {name} ")


phonebook={
    "a":"76545678987654",
    "b":"234567654",
    "c":"00000076545678987654",
    "d":"87654376545678987654"
}
search_name =  "d"
if  search_name in phonebook:
    print(f"{search_name} ka number hai : {phonebook[search_name]}")
else:
    print(f"sorry")    