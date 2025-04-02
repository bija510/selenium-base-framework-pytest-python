from boilerplates.base_test import BaseTestCase
from pages.optional_field_page import OptionalFieldPage as OptPage

# chrome is the default browser if not specified.
class OptionalFieldTest(BaseTestCase):

	def test_verify_toggle_swt(self):
		self.click(OptPage.mnu_pim)
		self.click(OptPage.pim_config_btn)
		self.click(OptPage.config_optional_optn)

		self.click(OptPage.tgl_swt_show_nick_name )
		self.wait(5)
