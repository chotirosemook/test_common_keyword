*** Settings ***
Resource    ${CURDIR}/../imports.resource
Library        AscendQaCommonLibrary
*** Variables ***
${lo_btn}    xpath=//a[@id='CRO-Hero-Button']

*** Test Cases ***
# Log To console    ${CURDIR}
# Test to Pass
#     webKeywordlib.Verify two numbers equal by py            10    10
    # Verify two numbers equal by resource      10    10

# Test to Fail 
#     Verify two numbers equal by py            5    10

Verify keywords to libs : random number
    # SeleniumLibrary.Open Browser    https://www.testim.io/    chrome
    # common_keyword.Click visible element    ${lo_btn}

    ${ran_num}=    common_keyword.Generate random number    10
    Log To Console    ran_num : ${ran_num}

Verify keywords to libs : random string
    ${ran_str}=    AscendQaCommonLibrary.Generate random string    5
    Log To Console    ran_str : ${ran_str}

# Verify keywords to libs : get thai year
#     ${thai_year}=    common_keyword.Get thai year    1993
#     Log To Console    thai_year : ${thai_year}

# Verify keywords to libs : get day of week in thai
#     ${Sunday}=    common_keyword.Get day of week in thai    Sunday
#     Log To Console    Sunday : ${Sunday}

#     ${Monday}=    common_keyword.Get day of week in thai    Monday
#     Log To Console    Monday : ${Monday}

#     ${Tuesday}=    common_keyword.Get day of week in thai    Tuesday
#     Log To Console    Tuesday : ${Tuesday}

#     ${Wednesday}=    common_keyword.Get day of week in thai    Wednesday
#     Log To Console    Wednesday : ${Wednesday}

#     ${Thursday}=    common_keyword.Get day of week in thai    Thursday
#     Log To Console    Thursday : ${Thursday}

#     ${Friday}=    common_keyword.Get day of week in thai    Friday
#     Log To Console    Sunday : ${Friday}

#     ${Saturday}=    common_keyword.Get day of week in thai    Saturday
#     Log To Console    Saturday : ${Saturday}

# Verify keywords to libs : random thai mobile number
#     ${mobile_number}=    common_keyword.Random thai mobile number
#     Log To Console    mobile_number : ${mobile_number}

# Verify keywords to libs : Get number of days in month
#     ${number_of_days_in_month}=    DateUtils.Get number of days in month
#     Log To Console    number_of_days_in_month : ${number_of_days_in_month}

# Verify keywords to libs : Get days remaining in current month
#     ${number_of_days_left_in_month}=     DateUtils.Get days remaining in current month
#     Log To Console    number_of_days_left_in_month : ${number_of_days_left_in_month}

# # Verify keywords to libs : Get current date and short month in thai
# #     ${current_date_and_short_month_in_thai}=    DateUtils.Get current date and short month in thai
# #     Log To Console    current_date_and_short_month_in_thai : ${current_date_and_short_month_in_thai}

# Verify keywords to libs : Random thai citizen id
#     ${random_thai_citizen_id}=     common_keyword.Random thai citizen id
#     Log To Console    random_thai_citizen_id : ${random_thai_citizen_id}

# Verify keywords to libs : Get os platform
#     ${get_os_platform}=     common_keyword.Get os platform
#     Log To Console    get_os_platform : ${get_os_platform}

# Verify keywords to libs : Get normalize path
#     ${get_normalize_path}=     common_keyword.Get normalize path    /home//user/Documents
#     Log To Console    get_normalize_path : ${get_normalize_path}

# Verify keywords to libs : PDF should contain
#     ${pdf_should_contain}=     common_keyword.PDF should contain    test_pdf.pdf   'Common T ypes of Cyber Attacks Cyber attacks are increasingly common,and some of the more advanced attacks can be launched without human intervention with the advent of network-based ransomware worms. What is a Cyber Attack? Definition of Cyber Attack: A cyber attack is when there is a deliberate and malicious attempt to breach the information system of an individual or organization. While there is usually an economic goal, some recent attacks show the destruction of data as a goal. Malicious actors often look for ransom or other kinds of economic gain, but attacks can be perpetrated with an array of motives, including political activism purposes.'
#     Log To Console    pdf_should_contain : ${pdf_should_contain}

# Verify keywords to libs : Image should be visible on screen
#     ${image_should_be_visible_on_screen}=     common_keyword.Image should be visible on screen    /home/user/Documents    0.8
#     Log To Console    image_should_be_visible_on_screen : ${image_should_be_visible_on_screen}

# Verify keywords to libs : Wait until download is completed
#     ${wait_until_download_is_completed}=     common_keyword.Wait until download is completed    /home/user/Documents
#     Log To Console    wait_until_download_is_completed : ${wait_until_download_is_completed}