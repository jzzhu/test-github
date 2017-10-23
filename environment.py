from behave import *
from selenium import webdriver


def before_all(context):
    # 完成登录
    context.browser = webdriver.Firefox()
    context.browser.get("https://github.com")
    context.ele_btn = context.browser.find_element_by_link_text("Sign in")
    context.ele_btn.click()
    context.ele_text = context.browser.find_element_by_id("login_field")
    context.ele_text.send_keys("jzzhu")
    context.ele_text = context.browser.find_element_by_id("password")
    context.ele_text.send_keys("621108zjz")
    context.ele_btn = context.browser.find_element_by_name("commit")
    context.ele_btn.click()


def after_all(context):
    context.browser.close()


def before_feature(context, feature):
    pass


def after_feature(context, feature):
    pass


def before_scenario(context, scenario):
        # 转首页
    context.browser.get("https://github.com")


def after_scenario(context, scenario):
    pass
