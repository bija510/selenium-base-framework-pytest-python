from seleniumbase import BaseCase
from pages.login_page import LoginPage as page

class BaseTestCase(BaseCase):

    def setUp(self):
        super().setUp()
        # <<< Run custom code AFTER the super() line >>>
        self.open("https://opensource-demo.orangehrmlive.com/")
        self.maximize_window()
        self.login()


    def tearDown(self):
        self.save_teardown_screenshot()
        if self.has_exception():
            # <<< Run custom code if the test failed. >>>
            pass
        else:
            # <<< Run custom code if the test passed. >>>
            pass
        # (Wrap unreliable code in a try/except block.)
        # <<< Run custom code BEFORE the super() line >>>
        super().tearDown()


    def login(self):
        # <<< Placeholder. Add your code here. >>>
        self.type(page.userName_txt, "Admin")
        self.type(page.password_txt, "admin123")
        self.click(page.login_btn)
        print("------Login test executed-------")

        pass

    def example_method(self):
        # <<< Placeholder. Add your code here. >>>

        pass
