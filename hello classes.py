class User:

  def __init__(self , full_name , birthday ):
   
    self.username = full_name
    self.userbirthday = birthday


  def create_greeting(self, salutation):
      greetmsg =  salutation + " " + self.username + " wishing you happy birthday today " +  self.userbirthday
      print(greetmsg)


  def sum(self, a , b):        
       print(10*(a + b))

  def sumandreturn(self, a , b):        
       return a + b


usr = User("Nishu" , "03-May-2000")
# x =  usr.create_greeting("hola")
# print(x)


# x =  usr.create_greeting("namaste")
# print(x)

c = 10

x =  usr.sumandreturn(300 , 400)
print(int(c) * x)

usr.sum (300 , 400)




#class point: 
   
  #  x =0 
   # y= 0
    #def movepoint(self, newX , newY):
     #   self.x = newX
     #     self.y = newY
     #def printpoint(self):
     #   print("x= " + str(self.x))
      #  print("y = " + str(self.y))


#origin = point()
#mypoint = point()
#mypoint.movepoint(input(),input())
#mypoint.printpoint()
#origin.printpoint()

       