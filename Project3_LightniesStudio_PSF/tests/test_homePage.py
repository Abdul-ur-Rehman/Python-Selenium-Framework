import time

import pytest

from Project3_LightniesStudio_PSF.pageObjects.HomePage import HomePage

@pytest.mark.usefixtures("setup")
class Test_HomePage:

    def test_logo_present(self):
        home = HomePage(self.driver)
        assert home.is_logo_displayed(), "Logo is not displayed."

    def test_navigation_links(self):
        home = HomePage(self.driver)
        links = home.get_navigation_links()
        newLinks = []
        for link in links:
            if link.text is not '':
                newLinks.append(link.text)
        print(newLinks)
        assert len(links) > 0, "No navigation links found"

    def test_hero_section_text(self):
        home = HomePage(self.driver)
        heroText = home.get_hero_section_text()
        print(heroText)

        assert "LIGHTNINES" in heroText, "Hero text does not contain site name"





