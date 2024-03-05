import datetime
import unittest
from employee import Employee
from employee_manager import EmployeeManager
from relations_manager import RelationsManager


class TestEmployeeRelationsManager(unittest.TestCase):
    def setUp(self):
        self.relations_manager = RelationsManager()
        self.employee_manager = EmployeeManager(self.relations_manager)
        self.john_doe = Employee(id=1, first_name="John", last_name="Doe",
                                 base_salary=3000, birth_date=datetime.date(1970, 1, 31),
                                 hire_date=datetime.date(1990, 10, 1))
        self.gretchen_walford = Employee(id=4, first_name="Gretchen", last_name="Walford", base_salary=4000,
                                         birth_date=datetime.date(1960, 1, 1),
                                         hire_date=datetime.date(1990, 1, 1))

    def test_team_leader_john_doe(self):
        employees = self.relations_manager.get_all_employees()

        john_doe_leader = any(employee.first_name == "John" and employee.last_name == "Doe"
                              and employee.birth_date == datetime.date(1970, 1, 31)
                              and self.relations_manager.is_leader(employee)
                              for employee in employees)

        self.assertTrue(john_doe_leader, "John Doe is not the team leader!")

    def test_john_doe_team_memebers(self):
        john_doe_team_members = self.relations_manager.get_team_members(self.john_doe)
        expected_team_members = [2, 3]
        actual_team_members = john_doe_team_members
        self.assertListEqual(actual_team_members, expected_team_members, "John Doe's team members are not as expected!")

    def test_tomas_andre_not_in_john_doe_team(self):
        john_doe_team_members = self.relations_manager.get_team_members(self.john_doe)
        self.assertNotIn(5, john_doe_team_members, "Tomas Andre should not be in John Doe's team!")

    def test_gretchen_walford_base_salary(self):
        gretchen_walford_base_salary = self.gretchen_walford.base_salary
        expected_base_salary = 4000
        self.assertEqual(gretchen_walford_base_salary, expected_base_salary, "Gretchen Walford's salary is not $4000!")


if __name__ == '__main__':
    unittest.main()
