# class ParentClass:
#     def parent_method (self) :
#         print("This is the parent method1.")
# class ChildClass (ParentClass):
#     def parent_method(self) :
#      print ("Harry")
#      super().parent_method()
#     def child_method (self):
#         print( "This is the childmethod.2" )
#         super().parent_method( )
# child_object = ChildClass()
# child_object. child_method() 
# child_object.parent_method()        

class employee :
    def __init__(self,name,id) -> None:
       self.name = name 
       self.id =id

class programmer(employee):
    def __init__(self,name,id,lang) -> None:
        self.name = name
        self.id =id
        self.lang = lang

ashish = employee("Ashish thakur " , "181")
naveen = programmer("naveen  " , "142","python")

print(ashish.name)
print(naveen.lang)
print(ashish.id)