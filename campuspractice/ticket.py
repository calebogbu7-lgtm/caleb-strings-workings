# # def create_ticket():
# #      print("\n---- CREATE TICKET ----")
# #      title = input("enter a title: ")
# #      category = input("enter category(Network, Hardware, software, other): ")
# #      urgency = input("enter urgency(low, medium, high): ")
# #      try:
# #         affected_users = int(input("Enter number of affected users: "))
# #      except ValueError:
# #         print("Error: Enter a valid whole number.")
# #         return
     
# #      print(f"affected users: {affected_users}")
# #      if not title.strip():
# #         print("Error: Title cannot be empty")
# #         return

# # create_ticket()


# def create_tickets():
#     print("\n----CREATE TICKET----")
#     title = input("enter a title: ")
#     urgency = input("enter your urgency(low, medium, high): ")
#     category = input ("enter your category(network, software, hardware, others): ")
#     status = input ("enter your status (in progess, resolved)")
#     try:
#         affected_users = int(input("enter number of affected users: "))

#     except ValueError:
#         print("Error: print a valid whole number")
#         return
#     print(f"affected users: {affected_users}")
#     if not title.strip():
#         print("Errror title cannot be blank")
#         return
#     if urgency.strip().lower() not in ("(low, medium, high):"):
#         print("Error invalid urgency")
#         return
#     if category.strip().lower() not in ("network, hardware, software, others" ):
#         print("Error inavalid category.")
#         return
#     if status.strip().lower() not in ("in progress, resolved"):
#         print("Error invalid status.")
#     if affected_users < 1:
#         print("error number must atleast be 1")
#         return
#     if urgency.strip().lower() == "high" and affected_users >= 10:
#         priority = "critical"
#     elif urgency.strip().lower() == "high" or affected_users >= 10:
#         priority = ("high")
#     elif urgency.strip().lower() == "medium" or affected_users >= 3:

#         priority = ("medium")
#     else:
#         priority = ("low")
#     print(f"priority: {priority}")
#     print("ticket created sucesssfully")
# create_tickets()
def create_ticket ():
    print("\n---- CREATE TICKET----")
    title = input ("enter your title ")
    category = input ("enter your category( network, software, hardware, others): ").strip().lower()
    urgency = input("enter your urgency(low, meiudm, high): ").strip().lower()
    try:
        affected_user = int(input("number of affected user: "))

    except ValueError:
        print("Error: Enter a valid whole number")
        return
    if not title.strip().lower():
        print("enter a valid title")
        return
    if category not in ("network", "software", "hardware", "others"):
        print("error enter a valid category")
        return
    if urgency not in ("low", "medium", "high"):
        print("enter a valid urgency")
        return
    if urgency == "high" and affected_user >= 10:
        priority = ("critical")
    elif urgency == "high" or affected_user >= 10:
        priority = ("high")
    elif urgency == "medium" or affected_user >= 3:
        priority = ("medium")
    else:
        priority = ("low")
    print (f"priority: {priority}")
    print("ticket created sucessfully")
create_ticket()