from boilerplates.base_test_case import BaseTestCase
from Pages.LoginPage import LoginPage as page

# chrome is the default browser if not specified.
class LoginTest(BaseTestCase):

	def test_login(self):
		self.type(page.userName_txt, "Admin")
		self.type(page.password_txt, "admin123")
		self.click(page.login_btn)