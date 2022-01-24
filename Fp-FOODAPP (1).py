#!/usr/bin/env python
# coding: utf-8

# In[1]:


user_database = {}
order_history = {}
menu_list = []
menu_d = {} 


# In[2]:


def main_display():
    print ("-"*5, end=" ")
    print("WELCOME! TO My Food Odering APP", end=" ")
    print( "-"*5) 
    print("For Admin Access ->  username = admin , passsword = admin")


# In[3]:




class Fstorage:
    
    def __init__(self, name, stock , price, discount):
        self.name = name
        self.stock = int(stock)
        self.price = int(price) - (int(price) * int(discount)/100)
        self.discount = int(discount)


    def info(self):
        info = ("%s , stock Available - %s , Price - %s INR")%(self.name, self.stock, self.price)
        print(info)
    
    # def __str__(self):
    #     return self.name
    #     pass

    def __repr__(self):
        return "%s INR %s" %(self.name, self.price)
# ADMIN FUNCTIONS 

    
     #function 1 add new items in menu
    def add_new_item():
        try:
            name = input('Enter the name : ex- Cake (1 piece)  ')
            stock = int(input("Enter total Stock : "))
            price = int(input("Enter the Price in INR : "))
            discount = int(input("Enter discount % : "))

            name = Fstorage(name, stock, price, discount)
            menu_list.append(name)
            print("--%s Added to Menu!--" %name)
            for i,j in enumerate(menu_list):
                menu_d[i]= j
        except:
            print("Wrong Input Type , Please try again.")


    def remove_item():
        pass
        # menu_d.pop()
    #Function 2 - > edit current items in menu
    def edit(self):
        try:
            print(self.name)
            print(" 1- Edit Price \n 2- Edit Available Stock \n 3- Edit Name (per serve quantity)")
            x = int(input("Select an Option : "))
            if x == 1:
                y = input("Enter The New Price : ")
                self.price = int(y)
                print ("Price for %s updated"   % self.name)
            if x == 2:
                y = input("Enter Available Stock : ") 
                self.stock = int(y)
                print ("Available Stock for %s Updated"  %self.name)
            if x == 3:
                self.name = input("Enter Name (per serve quantity) : ")
                print ("Name(per serve quantity) for %s  updated"   % self.name)
        except:
            print("Wrong Input Type , Please try again.")

    def order_item(self, x):
        if self.stock < x:
            print ("Sorry %s is Out Of Stock , Only %s In stock." %(self.name, self.stock))
        else: 
            self.stock -= x
            y = ("Order Recieved for %s x %s , Your total bill is INR %s" %(self.name, x, self.price*x))
            print(y)
            
        


# In[4]:


food1 = Fstorage("Chicken Tandoori (4 Pieces)", 100, 240, 0)
food2 = Fstorage("Vegan Burgen (1 Piece)", 100, 320, 0)
food3 = Fstorage("Truffle Cake (500gm)", 100, 900, 0)
menu_list.append(food1)
menu_list.append(food2)
menu_list.append(food3)
for i,j in enumerate(menu_list):
                menu_d[i]= j


# In[5]:


class User:
    def __init__(self, userid, password, address , email , phone,  admin = False ):
        self.userid = userid
        self.password = password
        self.admin = admin
        self.address = address
        self.email = email
        self.phone = phone
        

    def profile(self):
        self.address = input("Enter address : ")
        self.email = input("Enter email id : ")
        self.phone = input("enter phone number : ")

    def info(self):
        print("\n Hello %s\n"  % (self.userid) )
        if self.address :
            print("Address -> %s\n" % (self.address) )
        else:
            print("Address ->  Please Update Address\n")
        if self.email:
            print("Email - > %s\n" % (self.email))
        else:
            print("Email - >  Please Update Email Id\n")
        if self.phone:
            print("Phone -> %s \n" % (self.phone))
        else:
            print("Phone ->  Please Update Phone Number\n")

    def add_new_user():
        userid = input("Enter Username : ")
        password = input("Enter Password : ")
        addressx = input("Enter Location : ")
        emailx = input("Enter Email Id : ")
        phonex = input("Enter Mobile Number : ")
        userx = User(userid, password, addressx ,emailx, phonex, False, )
        user_database[userid] = userx
        print ("\n -- User Created -- \n -- Please-Login! -- \n")


# In[6]:


userid = "admin" #input("New id register / enter user id to login ")
password = "admin" #input("enter password")
email = "abc@gmail.com" #input("Enter email")
phone = "98545" #input("Enter phone number")
address = "mumbai" #input("enter address")
user1 = User(userid, password, address, email , phone, True )


# In[7]:


user_database[userid] = user1


# In[ ]:


while True:
    main_display()
    login_userid = input("Enter username :")

    if login_userid == "exit":
        break
    else:
        if login_userid in user_database.keys():        
            login_pass = input("Enter Password : ")
            if user_database[login_userid].password == login_pass:
                if user_database[login_userid].admin == True:
                    while True:
                        print("*" * 64)
                        print("*" * 64)
                        print("--Welcome Admin--")
                        print(" " *2 )
                        print("Please select an option  \n 1> Add New Item To Menu \n 2> Edit Current Menu Item \n 3> View Menu \n 4> Login Page")
                        admin_home_menu = input()
                        try:
                            if int(admin_home_menu) == 1:   #Add new Item
                                Fstorage.add_new_item()
                                print()
                                print()
                                print(menu_d)
                            if int(admin_home_menu) == 2:

                                if len(menu_d) == 0:
                                    print("\n Oops! There is Nothing to Edit! please add Items! \n")
                                else:
                                    print(menu_d)
                                    x = input("\nWhich Item Do you want to Edit - Please Select Number\n")
                                    menu_d[int(x)].edit()
                            if int(admin_home_menu) == 3:
                                if len(menu_d) ==0:
                                    print("Nothing here :( , Please Add Some Menu Items!") 
                                else:
                                    print("**MENU**") #View Menu
                                    print(menu_d)
                            if int(admin_home_menu) == 4:    #Exit
                                break
                        except ValueError as ve:
                            print("Invalid Input!, Please Try Again")


                else:   
                    while True:
                        print("*" * 64)
                        print("*" * 64)
                        print("--Welcome User--")
                        print(" " *2 )
                        print("Please Select \n 1-> Profile (View/Update) \n 2-> New Order \n 3-> Order History \n 4-> Back")
                        user_menu_home = input()
                        try:
                            if int(user_menu_home) == 1:
                                while True:
                                    user_database[login_userid].info()
                                    print("\n 1-> To edit, \n 2-> Go back")
                                    x = int(input("\nPlease Select\n"))
                                    if x == 1:
                                        user_database[login_userid].profile()
                                    else:
                                        break
                            if int(user_menu_home) == 2:
                                print("**MENU**")
                                print(menu_d)
                                new_order = []
                                x = input("Select An Item\n")
                                y = input("How many?\n")
                                menu_d[int(x)].order_item(int(y))
                                new_order.append([menu_d[int(x)], int(y)])

                                if login_userid in order_history.keys():
                                    order_history[login_userid].append(new_order)
                                else:
                                    order_history[login_userid] = new_order          

                            if int(user_menu_home) == 3:
                                print("\n-- ORDER HISTOY --  (Item name, Quantity Ordered")
                                if login_userid in order_history.keys():
                                    print(order_history[login_userid])
                                else:
                                    print("Please make your 1st order ^_^\n")
                            if int(user_menu_home) == 4:
                                break
                        except ValueError as ve:
                            print("Invalid Input!, Please Try Again\n")

            else: 
                print("Wrong Password")
        else: 
            print("User id Not Found Please make a new ID")
            User.add_new_user()

        

    
    
        



        


# In[ ]:


menu_list


# In[ ]:


menu_d


# In[ ]:


menu_list


# In[ ]:


user_database


# In[ ]:





# In[ ]:





# In[ ]:




