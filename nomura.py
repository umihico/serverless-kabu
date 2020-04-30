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
