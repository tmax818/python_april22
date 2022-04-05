instructors = [
    {'name': 'Tyler', 'years_exp': 2},
    {'name': 'Ed', 'years_exp': 7}
]

# instructor_data = {'name': 'Tyler', 'years_exp': 2}
# print(instructor_data['name'], instructor_data['years_exp'])


class Instructor:

    def __init__(self, instructor_data):
        self.name = instructor_data['name']
        self.experience = instructor_data['years_exp']

class Dojo:
    # class attribute
    motto = "strength through struggle!!"
    
    def __init__(self, location,instructor_data):
        self.location = location
        self.capacity = 35
        self.ninjas = []
        self.instructor = Instructor(instructor_data)


    def register_ninja(self, ninja):
        self.ninjas.append(ninja)

    # def display_motto(self):

    
    @classmethod
    def display_motto(cls):
        print(cls.motto)

    @classmethod 
    def change_motto(cls, new_motto):
        cls.motto = new_motto

    

        
class Ninja:
  
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def kick(self):
        if self.age > 60:
            print("I'm too old for this..")
        else:
            print("I am kicking you in the face...")
    
    @staticmethod
    def validate_ninja(ninja):
        if ninja.age < 18:
            return False
        return True

burbank = Dojo("Burbank", instructors[1])
# san_jose = Dojo("San Jose")


ryan = Ninja("Ryan", 16)
kevin = Ninja("Kevin", 25)
brian = Ninja("Brian", 24)
tyler = Ninja("Tyler", 66)



















# if not Ninja.validate_ninja(ryan):
#     print("Sorry, too young")
# else:
#     burbank.register_ninja(ryan)

# print(burbank.ninjas)

# Dojo.display_motto()
# Dojo.change_motto("Strength through 20 minutes of struggle.")
# Dojo.display_motto()



