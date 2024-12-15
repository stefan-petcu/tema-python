import pytest
from ex1 import Employee, Manager    # Importam clasele Employee si Manager din fisierul ex1.py pentru a le testa

def test_create_employee():
    # Testam crearea unui obiect de tip Employee
    emp = Employee("Ionel", 4000)  		# Cream un angajat cu numele "Ionel" si salariul 4000
    assert emp.name == "Ionel"  		# Verificam daca numele angajatului este setat corect
    assert emp.salary == 4000  			# Verificam daca salariul angajatului este setat corect
    assert Employee.empCount == 1  		# Verificam daca numarul total de angajati a fost incrementat corect
    del emp  					# Stergem obiectul pentru a elibera memoria si a scadea contorul angajatilor

def test_create_manager():
    # Testam crearea unui obiect de tip Manager
    mgr = Manager("Denisa", 5500, "HR")  	# Cream un manager cu numele "Denisa", salariul 5500 si departamentul "HR"
    assert mgr.department == "F22 HR"  		# Verificam daca departamentul este format corect cu prefixul "F22"
    assert Manager.mgrCount == 1  		# Verificam daca numarul total de manageri a fost incrementat corect
    del mgr 					# Stergem obiectul pentru a elibera memoria si a scadea contorul managerilor

if __name__ == "__main__":
    pytest.main()  				# Daca fisierul este rulat direct, executam toate testele definite in acest script
