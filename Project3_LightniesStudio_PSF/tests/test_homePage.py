from Project3_LightniesStudio_PSF.pageObjects.HomePage import HomePage
from Project3_LightniesStudio_PSF.utilities.BaseClass import BaseClass




class Test_HomePage(BaseClass):

    def setup_method(self):
        self.home = HomePage(self.driver)

    def test_logo_present(self):

        assert self.home.is_logo_displayed(), "Logo is not displayed."

    def test_navigation_links(self):

        links = self.home.get_navigation_links()
        newLinks = []
        for link in links:
            if link.text != '':
                newLinks.append(link.text)
        print(newLinks)
        assert len(links) > 0, "No navigation links found"

    def test_hero_section_text(self):

        heroText = self.home.get_hero_section_text()
        print(heroText)

        assert "LIGHTNINES" in heroText, "Hero text does not contain site name."

    def test_upload_button(self):

        uploadButton = self.home.upload_logo_Button()
        assert uploadButton.is_enabled() and uploadButton.is_displayed(), "Upload logo button is not clickable."

    def test_create_Sign_button(self):
        createSignButton = self.home.create_Sign_Button()
        assert createSignButton.is_enabled() and createSignButton.is_displayed(), "Create sign button is not clickable."



