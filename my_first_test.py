from seleniumbase import BaseCase

class MyTestClass(BaseCase):

    def test_basics(self):
        self.open("https://seleniumbase.io/simple/login")
        self.type("#username", "demo_user")
        self.type("#password", "secret_pass")
        self.click('a:contains("Sign in")')
        self.assert_exact_text("Welcome!", "h1")
        self.assert_element("img#image1")
        self.highlight("#image1")
        self.click_link("Sign out")
        self.assert_text("signed out", "#top_message")
        self.wait(5)

