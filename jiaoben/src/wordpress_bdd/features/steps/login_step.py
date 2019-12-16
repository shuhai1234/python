from behave import *
from pages import login_page

@given(u'go to login page')
def step_impl(context):
	context.login_page = login_page.LoginPage(context.dr)
	context.login_page.url = context.login_page.domain + 'wp-login.php'
	context.login_page.navigate()

@when(u'login with {user_name} {password}')
def step_impl(context, user_name, password):
	context.dashboard_page = context.login_page.login(user_name, password)

@then(u'redirect to dashboard page')
def step_impl(context):
	assert 'wp-admin' in context.dr.current_url

@then(u'display hello {user_name}')
def step_impl(context, user_name):
	greeking_link = context.dashboard_page.greeking_link
	assert user_name in greeking_link.text
