from ssm import get_ssm_value
from chrome import KabuChrome


class NomuraChrome(KabuChrome):
    login_page = "https://hometrade.nomura.co.jp/web/rmfCmnCauSysLgiAction.do"
    ipo_list_page = "https://hometrade.nomura.co.jp/web/rmfTrdStkIpoLstAction.do"

    def login(self):
        self.get(NomuraChrome.login_page)
        self.find_element_by_xpath(
            "//input[@id='branchNo']").send_keys(get_ssm_value('NOMURA_BRANCH_NUMBER'))
        self.find_element_by_xpath(
            "//input[@id='accountNo']").send_keys(get_ssm_value('NOMURA_ACCOUNT_NUMBER'))
        self.find_element_by_xpath(
            "//input[@id='passwd1']").send_keys(get_ssm_value('NOMURA_PASSWORD'))
        self.find_element_by_xpath(
            "//button[@name='buttonLogin']").click()

    def test_login(self):
        assert 'トップ' in self.title
        return self.title

    def get_current_asset(self):
        self.get("https://hometrade.nomura.co.jp/web/rmfCmnEtcInvTopAction.do")
        elms = self.xpaths("//table[@class='asset-summary-data']//tr/td")
        return [e.text for e in elms]

    def test_get_current_asset(self):
        result = self.get_current_asset()  # ['11,832', '+600円']
        assert len(result) == 2
        asset, change = result
        assert '円' in asset
        assert '円' in change
        return result


if __name__ == '__main__':
    print(NomuraChrome().test())
