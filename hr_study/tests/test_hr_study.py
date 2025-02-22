# Copyright 2023 Tecnativa - Víctor Martínez
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import Form, new_test_user
from odoo.tests.common import users

from odoo.addons.base.tests.common import BaseCommon


class TestHrStudy(BaseCommon):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.study = cls.env["hr.study"].create({"name": "Test study"})
        cls.employee = cls.env["hr.employee"].create({"name": "Test employee"})
        new_test_user(
            cls.env,
            login="test-hr_user",
            groups="hr.group_hr_user",
        )

    @users("test-hr_user")
    def test_employee_onchange(self):
        self.assertFalse(self.employee.study_field)
        employee_form = Form(self.employee)
        employee_form.study_id = self.study
        employee_form.save()
        self.assertEqual(self.employee.study_field, "Test study")
