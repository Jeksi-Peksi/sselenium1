import logging

from testpage import OperationsHelper
import yaml, time

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
name = testdata["username"]
passwd = testdata["password"]
titl = testdata["title"]
cont = testdata["content"]
descript = testdata["description"]
mail = testdata["mail"]

def test_step1(browser):
    logging.info("Test 1 Start")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401"

def test_step2(browser):
    logging.info("Test 2 Start")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(name)
    testpage.enter_pass(passwd)
    testpage.click_login_button()
    assert testpage.get_user_text() == f"Hello, {name}"

def test_step3(browser):
    logging.info("Test 3 Start")
    testpage = OperationsHelper(browser)
    testpage.click_new_post_btn()
    testpage.enter_title(titl)
    testpage.enter_description(descript)
    testpage.enter_content(cont)
    testpage.click_save_post_btn()
    time.sleep(3)
    assert testpage.get_title_text() == "Just new post"

def test_step4(browser):
    logging.info("Test 4 Start")
    testpage = OperationsHelper(browser)
    testpage.click_contact_link()
    time.sleep(2)
    testpage.enter_contact_name(name)
    testpage.enter_contact_mail(mail)
    testpage.enter_contact_content("testactcontent")
    time.sleep(2)
    testpage.click_contact_send_btn()
    time.sleep(3)
    assert testpage.get_alert() == "Form successfully submitted"
