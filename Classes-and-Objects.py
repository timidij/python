
class Student:
    # [assignment] Skeleton class. Add your code here

    # Assigning variables
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

        # New Methods
    def change_name(self, change_name):
        self.name = change_name
        return str(self.name)

    def change_age(self, change_age):
        self.age = change_age
        return int(self.age)

    def add_track(self, add_track):
        self.tracks = add_track
        return self.tracks

    def get_score(self, get_score):
        self.score = get_score
        return float(self.score)



Bob = Student(name="Bob", age=26, tracks=["FE" ,"BE"] ,score=20.90)

# Expected methods
print(Bob.change_name("Peter"))
print(Bob.change_age(34))
print(Bob.add_track("UI/UX"))
print(Bob.get_score(65.3))


User2 = Student(name="User2", age=30, tracks=["UI/UX"] ,score=20)

print(User2.change_name("mark"))
print(User2.change_age(40))
print(User2.add_track(["FE","BE"]))
print(User2.get_score(45))


