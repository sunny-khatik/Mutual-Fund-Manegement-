from selenium import webdriver as wd
import time

browser=wd.Firefox(executable_path="C:\\Users\\acer\\Desktop\\temper\\se_term_project\\se_term_work_prototype\\geckodriver")


browser.get("file:///C:/Users/acer/Desktop/temper/se_term_project/se_term_work_prototype/index.html")

browser.maximize_window()
time.sleep(3)

#First of all moving to Index page
##working with link
 
browser.find_element_by_link_text("Create Account").click()
time.sleep(4)

#We will enter the data in the form for the registration

browser.find_element_by_name("name").send_keys("Khunt Brijesh")
time.sleep(2)
browser.find_element_by_name("number").send_keys("9712766567")
time.sleep(2)
browser.find_element_by_name("password").send_keys("Brijesh@123")
time.sleep(2)
browser.find_element_by_name("email").send_keys("bjkhuntkanbi@gmail.com")
time.sleep(2)

# for submit button
browser.find_element_by_xpath("//input[@type='submit']").click()
time.sleep(4)

#after execution of above statement it would go to Banking page
#entering data for the next page

browser.find_element_by_name("pan").send_keys("IZAFG0550W")
time.sleep(2)
browser.find_element_by_name("bdate").send_keys("29/03/2001")
time.sleep(2)
browser.find_element_by_name("acno").send_keys("25691591035")
time.sleep(2)
browser.find_element_by_name("ifscno").send_keys("SBIN00045894")
time.sleep(2)
browser.find_element_by_name("bname").send_keys("Vaniyavad Branch")
time.sleep(2)
browser.find_element_by_xpath("//input[@type='submit']").click()
time.sleep(4)

#after exceution of the above statement it would go on home.html page

browser.find_element_by_xpath("//select[@id='AMC']/option[text()='HDFC Mutual Funds']").click()
time.sleep(2)
browser.find_element_by_xpath("//select[@id='catagories']/option[text()='Small Cap']").click()
time.sleep(2)
browser.find_element_by_xpath("//input[@type='submit']").click()
time.sleep(4)

#after exceution of the above statement it would go on info.html page

browser.find_element_by_xpath("//select[@id='lump-sip']/option[text()='SIP(monthly)']").click()
time.sleep(2.5)
browser.find_element_by_name("amt").send_keys("1000")
time.sleep(2.5)
browser.find_element_by_xpath("//input[@type='submit']").click()
time.sleep(4)

browser.close()

