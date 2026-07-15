class Employee:
    """Represents an employee who can exist independently."""
 
    def __init__(self, name, role):
        self.name = name
        self.role = role
 
    def introduce(self):
        print(f"Employee: {self.name} - {self.role}")
 
    def work_on(self, project):
        print(f"{self.name} is working on {project.title}.")
 
 
class Project:
    """Represents a project that can be associated with an employee."""
 
    def __init__(self, title):
        self.title = title
        self.project_lead = None
 
    def assign_lead(self, employee):
        self.project_lead = employee
        print(f"{employee.name} is now the lead for {self.title}.")
 
    def remove_lead(self):
        if self.project_lead is not None:
            print(f"Removing {self.project_lead.name} as lead of {self.title}.")
            self.project_lead = None
        else:
            print(f"{self.title} does not currently have a project lead.")
 
    def show_status(self):
        if self.project_lead is None:
            print(f"Project: {self.title} - No lead assigned")
        else:
            print(f"Project: {self.title} - Lead: {self.project_lead.name}")
 
 
# Independent objects are created separately.
employee_one = Employee("Jared", "Systems Analyst")
employee_two = Employee("Taylor", "Software Developer")
project = Project("Student Scheduling System")
 
print("Independent objects before association:")
employee_one.introduce()
employee_two.introduce()
project.show_status()
 
print("\nEstablishing the association:")
project.assign_lead(employee_one)
project.show_status()
employee_one.work_on(project)
 
print("\nReplacing the association:")
project.assign_lead(employee_two)
project.show_status()
 
print("\nRemoving the association:")
project.remove_lead()
project.show_status()
 
print("\nObjects still work after the association is removed:")
employee_one.introduce()
employee_two.introduce()
print(f"The project still exists: {project.title}")
