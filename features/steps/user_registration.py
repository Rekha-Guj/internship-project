from behave import given, when, then
from app.application import Application
from pages.registration_page import RegistrationPage


@given("Open the Registration page")
def step_open_registration_page(context):
    context.registration_page = RegistrationPage(context.driver)
    context.registration_page.open()
    #context.driver.get(context.registration_page.url)
    print("Registration page opened")

@when("Enter test Information in the registration form")
def step_user_reg_form_fill(context):
    context.registration_page.fill_registration_form()
    print("Registration form filled")

@then("Verify that the correct information is present")
def step_verify_user_reg_info(context):
    context.registration_page.verify_registration_form()
    print("Registration form verified")





