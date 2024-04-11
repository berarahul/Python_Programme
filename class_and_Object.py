class person:
    name = "Rahul"
    occupation="Software Engineer"
    networth=10
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a=person()
b=person()

a.name="Arpan"
a.occupation="Coder"

b.name="Tusar"
b.occupation="Desginer"
a.info()
b.info()