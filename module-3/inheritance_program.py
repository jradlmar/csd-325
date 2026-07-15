class Animal:
    def __init__(self, name):
        self.name = name

    # Parent private method
    def __make_sound(self):
        return "Generic animal sound"

    # Public method
    def speak(self):
        print(f"{self.name} says: {self.__make_sound()}")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    # Child private method
    def __wag_tail(self):
        return "The dog is wagging its tail."

    # Override the public method
    def speak(self):
        print(f"{self.name} says: Woof!")
        print(self.__wag_tail())

    # Demonstrates that the child cannot directly access the parent's private method
    def try_parent_private(self):
        try:
            print(self.__make_sound())
        except AttributeError as e:
            print("Child cannot directly access parent's private method.")
            print(e)


dog = Dog("Buddy")

print("Public method:")
dog.speak()

print("\nAttempt from child:")
dog.try_parent_private()

print("\nAttempt from outside:")
try:
    dog.__wag_tail()
except AttributeError as e:
    print("Cannot access child private method directly.")
    print(e)

try:
    dog.__make_sound()
except AttributeError as e:
    print("Cannot access parent private method directly.")
    print(e)