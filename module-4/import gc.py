import gc
import weakref
 
 
class Lesson:
    """Represents one lesson inside a course module."""
 
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
 
    def display_lesson(self, lesson_number):
        print(f"Lesson {lesson_number}: {self.title} ({self.duration} minutes)")
 
 
class CourseModule:
    """Owns and manages the lessons that make up a course module."""
 
    def __init__(self, module_name):
        self.module_name = module_name
        self.__lessons = []
 
    def add_lesson(self, title, duration):
        # The CourseModule creates and owns each Lesson object.
        lesson = Lesson(title, duration)
        self.__lessons.append(lesson)
 
    def display_module(self):
        print(f"Course Module: {self.module_name}")
        print("-" * 45)
 
        for number, lesson in enumerate(self.__lessons, start=1):
            lesson.display_lesson(number)
 
        print(f"Total lessons: {len(self.__lessons)}")
 
    def get_lesson_reference(self, lesson_index):
        # A weak reference observes the lesson without owning it.
        return weakref.ref(self.__lessons[lesson_index])
 
 
course_module = CourseModule("Introduction to Python")
 
course_module.add_lesson("Python Variables and Data Types", 25)
course_module.add_lesson("Conditional Statements", 30)
course_module.add_lesson("Loops and Repetition", 35)
 
course_module.display_module()
 
lesson_reference = course_module.get_lesson_reference(0)
 
print("\nBefore deleting the course module:")
print("Does the first lesson exist?", lesson_reference() is not None)
 
del course_module
gc.collect()
 
print("\nAfter deleting the course module:")
print("Does the first lesson exist?", lesson_reference() is not None)
print("The lesson was removed because it was owned by the course module.")
