from behave import *
from selenium import webdriver


@when('点击"Explore"标识')
def step_impl(context):
    context.ele_item = context.browser.find_element_by_link_text("Explore")
    context.ele_item.click()


@then('进入GitHub社区首页')
def step_impl(context):
    assert 'Explore' in context.browser.title


@when('点击"Discover repositories"标签')
def step_impl(context):
    context.ele_tab = context.browser.find_element_by_link_text(
        "Discover repositories")
    context.ele_tab.click()


@then('进入相关项目列表页')
def step_impl(context):
    assert 'Discover Repositories' in context.browser.title
