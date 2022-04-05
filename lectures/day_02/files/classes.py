

class Instructor:

    def __init__(self, instructor_data):
        self.name = instructor_data['name']
        self.qualified = instructor_data['qualified']


class Dojo:

    motto = "strength through struggle!!"
    
    def __init__(self, location, instructor_data):
        self.location = location
        self.ninjas = []
        self.instructor = Instructor(instructor_data)

    def register_ninja(self, ninja):
        self.ninjas.append(ninja)

    @classmethod
    def display_motto(cls):
        print(cls.motto)

    @classmethod
    def update_motto(cls):
        cls.motto = "strenght through 20 minutes of struggle!!"

    @staticmethod
    def validate_ninja(ninja):
        is_valid = True
        if ninja.age <= 18:
            is_valid = False
        return is_valid


class Ninja:
  
    def __init__(self, name, age):
        self.name = name
        self.age = age

tyler = {'name': 'Tyler', 'qualified': False}
ed = {'name': 'Ed', 'qualified': True}

dojo1 = Dojo('Burbank', tyler)
dojo2 = Dojo('San Jose', ed)

ninja1 = Ninja('Cam', 24)
ninja2 = Ninja('Ben', 26)
ninja3 = Ninja('Aaron', 23)
ninja4 = Ninja('Junior', 16)

if not Dojo.validate_ninja(ninja4):
    print("Sorry, too young")
else:
    dojo1.register_ninja(ninja4)

dojo1.register_ninja(ninja1)
print(dojo1.ninjas)

Dojo.display_motto()

print(dojo1.motto)

Dojo.update_motto()
Dojo.display_motto()

print(dojo1.motto)