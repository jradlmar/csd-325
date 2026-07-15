"""student.py

Attempts to instantiate an abstract Student class directly.
Running this file demonstrates the TypeError raised by Python.
"""

from abc import ABC, abstractmethod


class Student(ABC):
    """Abstract base class for students who must take a test."""

    @abstractmethod
    def take_test(self) -> None:
        """Require every concrete student subclass to implement a test."""
        pass


student = Student()
student.take_test()