*** Settings ***
Library    SeleniumLibrary
Library    BuiltIn
Library    String
Resource    keywords/web/webKeyword.robot
# Suite Teardown     Close Browser
Resource    ${CURDIR}/../imports.resource

*** Variable ***
${url_facebook}        https://www.facebook.com
${title_facebook}      Facebook - เข้าสู่ระบบหรือสมัครใช้งาน
${input_user}          //*[@id="email"]
${input_pass}          //*[@id="pass"]
${btn_login}           //*[@class="uiButton uiButtonConfirm"]
${txt_not_me}          //*[@id="not_me_link"]
${txt_message}         //div//textarea[@name="xhpc_message"]
${username_fail}            xxxxx@xxxxx.com
${password_fail}            12345678
${username_success}            iamgique@iamgique.com
${password_success}            iamgique@iamgique.com

*** Test Cases ***
facebook
    [tags]    fail
    Open Browser    about:blank    chrome
    Go To           ${url_facebook}
    ${random_no}    Generate Random Number    length=4
    Input text to element when ready    ${input_user}     ${random_no}