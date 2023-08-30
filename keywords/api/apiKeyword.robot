*** Settings ***
Resource    ../globalVariable.robot 
Resource    ../imports.robot

*** Keywords ***
Get access token

Generate random string
    ${randomString} = Generate Random String    8 [LETTERS]
    RETURN    ${randomString}

Generate random number
    ${randomNumber} = Generate Ramdom String    7 [NUMBERS]
    RETURN    ${randomNumber}

Generate authorization key
    [Arguments]    ${username}    ${password}
    ${text}=    BuiltIn.Catenate        ${username}:${password}
    ${encode_string}=    Evaluate    base64.urlsafe_b64encode($text.encode('UTF-8'))    modules=base64
    ${return_string}=    Get Line    ${encode_string}    0
    [Return]    ${return_string}