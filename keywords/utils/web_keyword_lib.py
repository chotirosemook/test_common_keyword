
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.remote.webelement import WebElement
from SeleniumLibrary.base import LibraryComponent, keyword
# from SeleniumLibrary.errors import ElementNotFound
# from selenium.webdriver.support.ui import Select
# from selenium.common.exceptions import NoSuchElementException
import random, string
from SeleniumLibrary import SeleniumLibrary

# keywords = SeleniumLibrary().get_keyword_names()
##### for log ####
# print({length})
# BuiltIn().log_to_console(rand_letters)

class web_keyword_lib():
    def get_driver_instance(self):
        return BuiltIn().get_library_instance('SeleniumLibrary')

    @keyword
    def click_visible_element(self,locator):
        driver = self.get_driver_instance()
        BuiltIn().log_to_console(locator)
        button_element = driver.find_element(By.XPATH, {locator})
        print("Hello, world!")
        # button_element = driver.find_element_by_xpath("//a[@id='CRO-Hero-Button']")
        button_element.click()  
    
    @keyword
    def generate_random_number(self,length:int):
        number = '0123456789'
        rand_num = ''.join(random.choice(number) for i in range(length))
        return rand_num
    
    @keyword
    def generate_random_string(self,length:int):
        letters = string.ascii_lowercase
        rand_letters = ''.join(random.choice(letters) for i in range(length))
        return rand_letters

    def verify_two_numbers_equal_by_py(self,number1:int, number2:int):
        if number1 == number2:
            print(f"{number1} equal {number2}")
        else:
            raise AssertionError(f"{number1} not equal {number2}")
    
if __name__ == "__main__":
    # webKeyword.lib_click_visible_element('id="CRO-Hero-Button"')
    print("__main__")
    # print(f"{keywords}")
    # print(f"{keywords.Get WebElement()}")

# *** Keywords ***
# Click visible element
#     [Documentation]    click when element visible
#     [Arguments] ${locator}  ${timeout}=30s
#     SeleniumLibrary.Wait Until Element Is Visible ${locator} ${timeout}
#     SeleniumLibrary.Click Element ${locator}

# Input visible element
#     [Documentation]    input text when element visible
#     [Arguments]    ${locator}    ${value}    ${timeout}=30s
#     Wait Until Element Is Visible    ${locator}    ${timeout}
#     Input Text    ${locator}    ${value}

# Get text verify
#     [Documentation]    Get text from element
#     [Arguments] ${locator} ${timeout}=30s
#     Wait Until Element Is Visible ${locator}
#     ${textValue} = Get Text ${locator}
#     RETURN    ${textValue}

# Generate Random Number
#     [Documentation]    generate random number
#     [Arguments]    ${length}
    
#     ${result}    Generate Random String    length=${length}    chars=[NUMBERS]

#     RETURN    ${result}

# Click element when ready
#     [Documentation]     Keyword to wait for element to be visible before clicking.
#     ...     \n default retry clicking is 3 times
#     ...     \n can also wait for only page is CONTAINS element instead of visible
#     [Arguments]     ${locator}  ${retry}=4      ${only_contains}=${FALSE}       ${timeout}=${GLOBAL_TIMEOUT}

#     FOR     ${i}    IN RANGE    1   ${retry}
#         IF  ${only_contains}
#             SeleniumLibrary.Wait until page contains element   ${locator}   ${timeout}
#         ELSE
#             SeleniumLibrary.Wait until element is enabled    ${locator}     ${timeout}
#             SeleniumLibrary.Wait until element is visible   ${locator}      ${timeout}
#         END
#         ${is_success}=          Run keyword and ignore error   SeleniumLibrary.Click element   ${locator}
#         ${err_msg}=             Convert To String       ${is_success[1]}
#         ${is_obsecure}=         Run keyword and return status    Should not contain     ${err_msg}       Other element would receive the click
#         ${is_not_stale}=        Run keyword and return status    Should not contain     ${err_msg}       element is not attached to the page document
#         ${is_no_err}=           Run keyword and return status    Should be true        '${err_msg}' == '${NONE}'
#         ${result}=              Evaluate    ${is_success} and ${is_obsecure} and ${is_obsecure} and ${is_not_stale} and ${is_no_err}
#         Exit for loop if        ${result}
#         Log     'retry clicking element for ${i} time with error: ${err_msg}'   level=WARN
#     END
#     Should be true  ${result}   msg="Failed to click element after ${retry} retry"

# Default test teardown
#     [Documentation]    Capture screenshot for every test case 
#     ...     \n all failed case always logs and returns the HTML source of the current page or frame.
#     Run Keyword And Ignore Error    SeleniumLibrary.Capture Page Screenshot
#     Run Keyword If Test Failed      Run Keyword And Ignore Error    SeleniumLibrary.Log Source
#     SeleniumLibrary.Close all browsers

# Input text to element when ready
#     [Documentation]     Wait for element to be visible first before input text. Retry 4 times
#     [Arguments]     ${locator}     ${text}     ${clear}=${TRUE}     ${timeout}=${GLOBAL_TIMEOUT}
#     SeleniumLibrary.Wait until element is visible    ${locator}     ${timeout}
#     SeleniumLibrary.Wait until element is enabled    ${locator}     ${timeout}
#     FOR    ${index}    IN RANGE    1    4
#         ${result_msg}=      Run Keyword And Ignore Error    SeleniumLibrary.Input Text      ${locator}     ${text}     clear=${clear}
#         ${err_msg}=         Convert To String       ${result_msg[1]}
#         ${is_success}=                  Run Keyword And Return Status    Should Be Equal        ${err_msg}      None
#         ${is_not_loading_error}=        Run Keyword And Return Status    Should Not Contain     ${err_msg}      invalid element state
#         Exit For Loop If        ${is_success} or ${is_not_loading_error}
#     END
#     Should Be True      ${is_success}   msg=Unable to input text to element after 4 retry

# Select option by label when ready
#     [Documentation]     Wait until element is visible first before select from list by label
#     [Arguments]     ${locator}     ${label}     ${timeout}=${GLOBAL_TIMEOUT}
#     SeleniumLibrary.Wait until element is visible    ${locator}     ${timeout}
#     FOR    ${index}    IN RANGE    1    10
#         ${result_msg}=      Run Keyword And Ignore Error    Select From List By Label      ${locator}     ${label}
#         ${err_msg}=         Convert To String       ${result_msg[1]}
#         ${is_success}=                  Run Keyword And Return Status    Should Be Equal        ${err_msg}      None
#         ${is_not_loading_error}=        Run Keyword And Return Status    Should Not Contain     ${err_msg}      invalid element state
#         Exit For Loop If        ${is_success} or ${is_not_loading_error}
#     END
#     Should Be True      ${is_success}   msg=Unable to select option dropdownlist after 10 retry


# Get text from element when ready
#     [Documentation]     Wait until element is visible first before get text from element. 
#                         ...     \n default timeout is same as ${GLOBAL_TIMEOUT}
#     [Arguments]     ${locator}      ${timeout}=${GLOBAL_TIMEOUT}
#     SeleniumLibrary.Wait until element is visible    ${locator}     ${timeout}
#     ${text}=    SeleniumLibrary.Get text    ${locator}
#     [Return]    ${text}

# Get element count when ready
#     [Documentation]     Wait until element is visible first before get element count
#                         ...     \n default timeout is same as ${GLOBAL_TIMEOUT}
#     [Arguments]     ${locator}   ${timeout}=${GLOBAL_TIMEOUT}
#     SeleniumLibrary.Wait until element is visible       ${locator}      ${timeout}
#     ${count}=   SeleniumLibrary.Get Element Count       ${locator}
#     [Return]    ${count}

# Get element attribute when ready
#     [Documentation]     Wait until element is visible first before get element attribute
#     ...     \n default timeout is same as ${GLOBAL_TIMEOUT}
#     [Arguments]     ${locator}      ${attribute}    ${only_contain}=${FALSE}    ${timeout}=${GLOBAL_TIMEOUT}
#     IF  ${only_contain}
#         Wait until keyword succeeds    5x    2s     SeleniumLibrary.Wait until page contains element    ${locator}      ${timeout}
#     ELSE IF     ${only_contain} == ${FALSE}
#         Wait until keyword succeeds    5x    2s     SeleniumLibrary.Wait until element is visible       ${locator}      ${timeout}
#     END
#     ${att}=   SeleniumLibrary.Get element attribute     ${locator}  ${attribute}
#     [Return]    ${att}

# Scroll element into view when ready
#     [Documentation]     Wait until page contains element then scroll the element into view
#     ...     \n default timeout is same as ${GLOBAL_TIMEOUT}
#     [Arguments]     ${locator}      ${retry}=4      ${timeout}=${GLOBAL_TIMEOUT}
#     FOR     ${i}    IN RANGE   0    ${retry}
#         SeleniumLibrary.Wait until page contains element    ${locator}      ${timeout}
#         SeleniumLibrary.Scroll element into view            ${locator}
#         ${is_visible}=  Run keyword and return status   SeleniumLibrary.Wait until element is visible       ${locator}      ${timeout}
#         Exit for loop if    ${is_visible}
#     END

# Browse file when ready
#     [Documentation]     Wait until page contains element then choose file from file path
#     ...     \n default timeout is same as ${GLOBAL_TIMEOUT}
#     [Arguments]     ${locator}      ${file_path}    ${timeout}=${GLOBAL_TIMEOUT}
#     SeleniumLibrary.Wait until Page contains element   ${locator}       ${timeout}
#     SeleniumLibrary.Choose File     ${locator}  ${file_path}


# Get value from element when ready
#     [Documentation]    Wait until element is visible first before get element attribute value
#     ...     \n default timeout is same as ${GLOBAL_TIMEOUT}
#     [Arguments]     ${locator}  ${only_contain}=${FALSE}    ${timeout}=${GLOBAL_TIMEOUT}
#     IF  ${only_contain}
#         SeleniumLibrary.Wait until page contains element    ${locator}      ${timeout}
#     ELSE IF     ${only_contain} == ${FALSE}
#         SeleniumLibrary.Wait until element is visible       ${locator}      ${timeout}
#     END
#     ${value}=   SeleniumLibrary.Get value     ${locator}
#     [Return]    ${value}


# Manually clear input from textbox
#     [Documentation]  sometime selenium cannot clear text box easily
#     ...     \n this keyword will get length of text in text box then press BACKSPACE key n number
#     ...     \n equal to that amount     
#     [Arguments]     ${locator}      ${timeout}=${GLOBAL_TIMEOUT}
#     ${current_value}=   DobbyWebCommon.Get value from element when ready    ${locator}      ${timeout}
#     ${word_length}=     Get length      ${current_value}
#     FOR     ${i}    IN RANGE   ${word_length}
#         Press keys     ${locator}       BACKSPACE
#     END

# Wait until element is visible except stale
#     [Documentation]  Wait until element is visible except stale
#     ...     \n default timeout is same as ${GLOBAL_TIMEOUT}
#     [Arguments]    ${locator}       ${timeout}=${GLOBAL_TIMEOUT}
#     FOR     ${i}    IN RANGE    1       15
#         ${status}           Run keyword and ignore error   SeleniumLibrary.Wait until element is visible    ${locator}      ${timeout}
#         ${err_msg}=         Convert To String       ${status[1]}
#         ${is_not_stale}=    Run keyword and return status    Should not contain     ${err_msg}      StaleElementReferenceException
#         Exit For Loop If        ${is_not_stale}
#     END
#     SeleniumLibrary.Wait until element is visible    ${locator}      ${timeout}
#     BuiltIn.Should Be True  ${is_not_stale}     msg='element is not visible and still in stale stage'

# Get WebElement when ready
#     [Documentation]     Returns the first WebElement matching the given locator when ready
#     [Arguments]     ${locator}      ${timeout}=${GLOBAL_TIMEOUT}
#     SeleniumLibrary.Wait until element is visible    ${locator}     ${timeout}
#     ${element}=     SeleniumLibrary.Get WebElement      ${locator}
#     [Return]    ${element}

# Get WebElements when ready
#     [Documentation]     Returns a list of WebElement objects matching the locator when ready
#     [Arguments]     ${locator}      ${timeout}=${GLOBAL_TIMEOUT}
#     SeleniumLibrary.Wait until element is visible    ${locator}     ${timeout}
#     ${elements}=     SeleniumLibrary.Get WebElements      ${locator}
#     [Return]    ${elements}

# Mouse over when ready
#     [Documentation]     Simulates hovering the mouse over the element locator when ready
#     [Arguments]     ${locator}
#     SeleniumLibrary.Wait until element is visible       ${locator}
#     SeleniumLibrary.Mouse over      ${locator}

# Verify element text when ready
#     [Documentation]     Verifies that element locator contains exact the text expected when ready 
#     ...    \n if you want to match the exact text, not a substring
#     [Arguments]     ${locator}      ${expected}     ${override_error_msg}=${None}    ${ignore_case}=${False}       ${timeout}=${GLOBAL_TIMEOUT}
#     SeleniumLibrary.Wait until element is visible       ${locator}      ${timeout}
#     SeleniumLibrary.Element text should be      ${locator}      ${expected}     ${override_error_msg}    ${ignore_case}

# Verify element should contains text when ready
#     [Documentation]     Verifies that element locator contains text expected when ready if a substring match is desired
#     [Arguments]     ${locator}      ${expected}     ${override_error_msg}=${None}    ${ignore_case}=${False}       ${timeout}=${GLOBAL_TIMEOUT}
#     SeleniumLibrary.Wait until element is visible       ${locator}      ${timeout}
#     SeleniumLibrary.Element should contain      ${locator}      ${expected}     ${override_error_msg}    ${ignore_case}

# Open and switch to new tab 
#     [Documentation]     Open a new tab in the same browser session and switch to it
#     ...     \n accept url if you want to open a newtab to a url. default is blank.
#     [Arguments]     ${url}=${EMPTY}
#     Execute Javascript    window.open('${url}');
#     ${headles}    SeleniumLibrary.Get window handles
#     SeleniumLibrary.Switch Window    ${headles}[1]

