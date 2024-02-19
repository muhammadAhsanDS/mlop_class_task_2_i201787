import pytest
from main import StudentsInMLOps

def test_enrollStudents():
    mlops = StudentsInMLOps()
    mlops.enrollStudents(5)
    assert mlops.getTotalStrength() == 5

def test_dropStudents():
    mlops = StudentsInMLOps()
    mlops.enrollStudents(10)
    mlops.dropStudents(3)
    assert mlops.getTotalStrength() == 7

def test_getClassName():
    mlops = StudentsInMLOps()
    assert mlops.getClassName() == "MLOps"
