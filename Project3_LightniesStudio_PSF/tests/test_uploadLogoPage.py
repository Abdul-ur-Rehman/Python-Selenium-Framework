from Project3_LightniesStudio_PSF.pageObjects.HomePage import HomePage
from Project3_LightniesStudio_PSF.utilities.BaseClass import BaseClass


class Test_UploadLogo(BaseClass):

    def setup_method(self):
        self.home = HomePage(self.driver)
        self.uploadLogo = self.home.click_UploadLogo_Button()

    def test_form_submission(self):

        self.uploadLogo.enter_fullName("Abdur Rehman")
        self.uploadLogo.enter_email("test@gmail.com")
        self.uploadLogo.countryFlag()
        self.uploadLogo.enter_phone("090078601")
        self.uploadLogo.select_budget()








