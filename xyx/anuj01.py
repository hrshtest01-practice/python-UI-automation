

youraccountBTN_Xpath = "//li[@class='MuiBreadcrumbs-li']/a[text()='YOUR ACCOUNT']"

#Personal Info
personalInfoTagline_xpath = "//div/div[text()='Personal Info']"
PersonalInfoEditBtn_Xpath = "//div[@id='esr-route-view']/div/div/div[@class='MuiBox-root css-1b6p7et']/div[1]/div[2]/div[2]/button"
firstname_cssSelector = "input[name='firstName']"
lastname_cssSelector= "input[name='lastName']"
mobileno_cssSelector= "input[name='mobileNumber']"
emailUpdate_Xpath= "//div/div[text()='Request email update']"
savechanges_xpath= "//button[@type='submit']"

# Edit your company info
companyInfotagline_xpath = "//div/div[text()='Company Info']"
companyname_cssSelector = "input[name='companyName']"
companyaddress_xpath="//input[@value='Florida 30A, Panama City, Florida, 55555']"
companyaddressEdit_Xpath ="//span[text()='Edit']"
companyphoneno_xpath="//input[@name='companyPhone']"
savechangesCompany_xpath= "//button[@type='submit']"

#Billing info
billingInfoTagline_xpath = "//div/div[text()='Billing Info']"
billingfirstname_xpath="//input[@name='firstName']"
billinglastname_xpath="//input[@name='lastName']"
billingphone_xpath= "//input[@name='phone']"
billingaddress_id="//input[@value='Florida 30A']"
billingaddressEdit_xpath = "//span[text()='Edit']"
billingemail_id="//input[@name='email']"
savechanges_billing = "//button[@type='submit']"

#Manage your team
ManageyourteamTagline_xpath = "//div/div[text()='Manage Your Team']"
teamEmaillist_xpath = "//div[text()='Manage Your Team']/../following-sibling::div[1]/div/div/div/div[2]"
addnewteammember_xpath="//button[text()='add new team member']"
teammemberemail_cssSelector="[name='email']"
addButtonnewteammember_xpath='//button[text()="Add"]'

#Your Job Sites
YourJobSitesTagline_xpath="//div/div[text()='Your Jobsites']"
jobsiteslist_xpath="//div/div[text()='Your Jobsites']/../../div[2]/div/div"
addnewjobsiteButton_xpath ="//button[text()='Add new jobsite']"
jobsitename_xpath="//input[@name='jobsiteName']"
jobsiteaddress_xpath="//div/div[2]/div[1]/div[2]/div/div/input[@type='search']"
jobsitecCity_xpath="//input[@name='city']"
jobsitestate_xpath="//input[@name='state']"
jobsitezipcode_xpath="//input[@name='zip']"
prefferdjobcheckbox_xpath="//input[@type='checkbox']"
addjobsiteButton_xpath="//button[@type='submit']"

#Notifications
Notificationtagline_xpath= "//div[text()='Notifications']"
NotificationEditbtn_xpath="//div[text()='Notifications']/../../div[2]/div[2]/button"
Emailcheckbox_xpath="//div[text()='Email']/../span/span/input[@type='checkbox']"
smscheckbox_xpath="//div[text()='SMS']/../span/span/input[@type='checkbox']"
