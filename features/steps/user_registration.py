from behave import given, when, then
from app.application import Application
from pages.registration_page import RegistrationPage


@given("Open the Registration page")
def open_registration_page(context):
    context.registration_page = RegistrationPage(context.driver)
    context.driver.get(context.registration_page.url)

@when("Enter test Information in the registration form")
def user_reg_form_fill(context):
    context.registration_page.fill_registration_form()

@then("Verify that the correct information is present")
def verify_user_reg_info(context):
    context.registration_page.verify_registration_form()





