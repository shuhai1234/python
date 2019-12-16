from behave import *
import time

@when(u'go to create post page')
def step_impl(context):
    context.dr.get('http://localhost/wordpress/wp-admin/post-new.php')

@when(u'create a post')
def step_impl(context):
    context.title = 'This is my post for py se 10 %s' %(time.time())
    content = 'post body'
    context.dr.find_element_by_id('title').send_keys(context.title)
    js = 'document.getElementById("content_ifr").contentWindow.document.body.innerHTML="%s"' %(content)
    context.dr.execute_script(js)
    context.dr.find_element_by_id('publish').click()


@then(u'verify post title')
def step_impl(context):
    context.dr.get('http://localhost/wordpress/wp-admin/edit.php')
    assert context.dr.find_element_by_css_selector('.row-title').text == context.title
