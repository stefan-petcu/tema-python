class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):  #constructorul clasei
        self.name = name
        self.salary = salary
        self.tasks = {}		       #dictionar
        Employee.empCount += 1

    def display_emp_count(self):
        "Displays the number of employees"
        print(f"Total number of employee(s) is {Employee.empCount}")

    def display_employee(self):
        print("Name: ", self.name, ", Salary: ", self.salary)

    def __del__(self):
        Employee.empCount -= 1

    def update_salary(self, new_salary):
        self.salary = new_salary

    def modify_task(self, task_name, status="New"):
        self.tasks[task_name] = status

    def display_task(self, status):
        print(f"Taskuri cu statusul {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)


class Manager(Employee):   #clasa mostenita din Employee
    mgrCount = 0

    def __init__(self, name, salary, department):
        NUME_ECHIPA = "F22 "
        super().__init__(name, salary)  #folosim super()ca sa obtinem un obiect care face referire la clasa părinte a clasei curente 
        self.department = NUME_ECHIPA + department
        Manager.mgrCount += 1

    
    # x % 3 == 2, deci modific metoda ai sa afiseze doar departamentul
    def display_employee(self):
        print(f"Department: {self.department}")

    def __del__(self):
        Manager.mgrCount -= 1

if __name__ == "__main__":    #asigură că secțiunea de cod din interiorul acestei condiții va fi executată doar dacă scriptul este rulat direct

    # y / 3 == 4, deci creez 4 obiecte ale clasei Manager
    manager1 = Manager("Alexandru", 8600, "CySec") 
    manager2 = Manager("Anastasia", 3500, "Tester") 
    manager3 = Manager("Dorian", 5200, "HR") 
    manager4 = Manager("Iulia", 11300, "Management") 

    #apelez metoda display_employee pt fiecare in parte
    manager1.display_employee()
    manager2.display_employee()
    manager3.display_employee()
    manager4.display_employee()

    print(f"Numarul de manageri este: {Manager.mgrCount}")
    print(f"Numarul de angajati este: {Employee.empCount}")
