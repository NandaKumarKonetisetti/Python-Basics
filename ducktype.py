class nanda:
    def name(self):
        print("In Nanda")
class kumar:
    def name(self):
        print("In Kumar")
    
class execution:
     def execute(self,obj):
         obj.name()


nan = nanda()
kum = kumar()
ex = execution()
ex.execute(kum)
         