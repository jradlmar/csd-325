"""Morris_assign5.py

Demonstrates an abstract base class and a concrete subclass.
The program creates an instance of each class and displays the
concrete class name and its base class name.
"""

from abc import ABC


class CourseMember(ABC):
    """Abstract base class representing a member of a course."""

    def role_description(self) -> str:
        return "General course member"


class Student(CourseMember):
    """Concrete class derived from CourseMember."""

    def role_description(self) -> str:
        return "Student enrolled in the course"


def main() -> None:
    """Create the required instances and display class information."""
    base_instance = CourseMember()
    concrete_instance = Student()

    print(f"Abstract base class instance: {base_instance.__class__.__name__}")
    print(f"Concrete class instance: {concrete_instance.__class__.__name__}")
    print(f"Base class of {concrete_instance.__class__.__name__}: "
          f"{concrete_instance.__class__.__bases__[0].__name__}")


if __name__ == "__main__":
    main()