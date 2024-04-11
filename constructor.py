class person: 

    def __init__(self,n,o):

     self.name = n
     self.occ = o
    def info(self):
        print(f"{self.name} is a {self.occ}")
 

a=person("Rahul","Coder")
b=person("Arpan","HR")

a.info()
b.info()