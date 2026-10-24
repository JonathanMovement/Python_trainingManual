## -------------------------------------What is a Class?--------------------------------------



### A class is a blueprint for creating objects.



##### \- A ***class*** defines what an object is and what it can do

##### \- An ***object*** is an instance of a class



#### **Key Concepts:**



###### **- Class:** A template or blueprint that defines the properties and behaviors common to all objects of a certain type.

###### **- Object(Instance):** A specific realization of a class, with its own unique set of data.

###### **- Attribute:** Variables within a class that store data; instance attributes are unique to each object, while class attributes are shared by all instances.

###### **- Method:** Functions defined within a class that describe the behaviors or actions an object can perform.

###### **- SELF:** By convention, methods must have an explicit first argument, usually named ***self,*** which refers to the specific instance of the object when the method is called

------

##### **> Defining a Class**



###### class **Person:**

######     pass

###### 

###### **Person** - is the class name(usually written in CamelCase)

###### **pass** - means "do nothing for now"

------

##### **> Creating an Object(Instance)**



###### p1 = Person()

###### print(p1)

###### 

###### **- p1** is an object(instance) of the Person class

###### \- you can create many **objects** from one class



###### ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



###### **The \_\_init\_\_ Method (Constructor)**

###### 

###### class **Person:** -> defining the class name (Person)

    def \_\_init\_\_(*self*, name, age): -> **\_\_init\_\_** is called the constructor, ***self*** refers to the current object, self.name and self.age are attributes(variables)

######  	self.name = name

######  	self.age = age

