*** Settings ***
Resource    ../globalVariable.robot 
Resource    ../imports.robot

***Keywords***
Open mobile application
    ${capability}       Create dictionary
        ...                 platformName=${platformName}
        ...                 automationName=${automation}
        ...                 platformVersion=${platformVersion}
        ...                 deviceName=${deviceName}
        ...                 udid=${udid}
        ...                 systemPort=${systemPort}
        ...                 noReset=${noReset}
		...					fullReset=${fullReset}
        ...                 newCommandTimeout=0
        ...                 uiautomator2ServerInstallTimeout=120000
        ...                 autoGrantPermissions=true
        ...                 language=${lang}
        ...                 locale=${lang.upper()}
        ...                 appPackage=${appPackage}
        ...                 appActivity=${appActivity}
        ...                 adbExecTimeout=${adbExecTimeout}

    IF  "${app}" != "None"
        Set To Dictionary    ${capability}
        ...                 app=${app}
    END
    AppiumLibrary.Set appium timeout    ${GLOBAL_TIMEOUT}
    AppiumLibrary.Open application    remote_url=${remoteUrl}    &{capability}

Close mobile application
    Run keyword and ignore error    AppiumLibrary.Capture page screenshot
    Run keyword if test failed      Run keyword and ignore error    AppiumLibrary.Log source
    AppiumLibrary.Close application
    
Generate Random String
    [Documentation]    generate random number
    [Arguments]    ${length}   
    ${result}    Generate Random String    length=${length}    chars=[LETTERS]
    RETURN    ${result}

Generate Random Number
    [Documentation]    generate random number
    [Arguments]    ${length}
    ${result}    Generate Random String    length=${length}    chars=[NUMBERS]
    RETURN    ${result}

Get text and verify value
    [Arguments]    ${element}    ${expect_value}    ${timeout}=${GLOBAL_TIMEOUT}
    AppiumLibrary.Wait Until Element Is Visible    ${element}    ${timeout}
    ${actual_value}=    Get Text    ${element}
    Should be Equal As Strings    ${actual_value}    ${expect_value}f

Format text
    [Arguments]    ${format_string}    &{key_value_pairs}
    ${key_value_pairs}=     Collections.Convert To Dictionary    ${key_value_pairs}
    ${result_text}    Evaluate    unicode($format_string).format(**$key_value_pairs) if sys.version_info.major==2 else str($format_string).format(**$key_value_pairs)    modules=sys
    [Return]    ${result_text}

Wait until element is visible except stale
    [Documentation]         Wait until element is visible except stale
    [Arguments]    ${locator}        ${timeout}=${GLOBAL_TIMEOUT}
    FOR     ${i}    IN RANGE    1       5
        ${is_visible}       Run keyword and ignore error    AppiumLibrary.Wait until element is visible       ${locator}         ${timeout}
        ${err_msg}=         Convert to string       ${is_visible[1]}
        ${is_not_stale}=    Run keyword and return status    Should not contain    ${err_msg}      StaleElementReferenceException
        ${no_err_msg}       Run keyword and return status    Should be equal       ${is_visible[0]}      PASS       msg=${err_msg}
        ${result}=          Evaluate    ${is_not_stale} and ${no_err_msg}
        Exit for loop if        ${result}
    END
    Should be true      ${result}       msg="element either in stale mode or not visible, error message is ${err_msg}"

Push image file to emulator 
    [Arguments]     ${emulator_destination_path}    ${to_push_image_path}
    AppiumUtils.Push image file to emulator     ${emulator_destination_path}    ${to_push_image_path}

Find element by swiping down
    [Documentation]     Find element by swiping down
    [Arguments]         ${target_element}
                ...     ${scroll_panel}
                ...     ${default_scroll_view}=${NONE}
                ...     ${moveto}=Top
                ...     ${percent}=0.3
                ...     ${number_of_scroll}=10
                ...     ${timeout}=${GLOBAL_TIMEOUT}
    ${element_status}=      Run keyword and return status    mobileKeyword.Wait until element is visible except stale      ${target_element}      ${timeout}
    IF  '${element_status}'=='False'
        Set resolution      ${scroll_panel}    ${percent}
        FOR    ${i}    IN RANGE    ${number_of_scroll}
            Move to    ${moveto}
            ${element_status}=      Run keyword and return status    mobileKeyword.Wait until element is visible except stale      ${target_element}      ${timeout}
            Exit for loop if    ${element_status}
        END
        Should be true      ${element_status}   msg='Element is not visible after ${number_of_scroll} scroll'
    END
    Should be true      ${element_status}

Tap element when ready
    [Documentation]     Keyword to wait for element to be visible before clicking.
    ...    \n default retry clicking is 3 times
    ...    \n can also wait for only page is CONTAINS element instead of visible
    ...    \n default timeout is same as ${GLOBAL_TIMEOUT}
    [Arguments]     ${locator}      ${only_contain}=${FALSE}    ${timeout}=${GLOBAL_TIMEOUT}
    FOR     ${i}    IN RANGE    1   4
        IF  ${only_contain}
            ${wait_status}=             Run keyword and ignore error   AppiumLibrary.Wait until page contains element     ${locator}    ${timeout}
            ${err_msg_wait}=            Convert to string       ${wait_status[1]}
            ${is_not_stale_wait}=       Run keyword and return status    Should not contain     ${err_msg_wait}      StaleElementReferenceException
        ELSE
            ${wait_status}=             Run keyword and ignore error   AppiumLibrary.Wait until element is visible     ${locator}   ${timeout}
            ${err_msg_wait}=            Convert to string       ${wait_status[1]}
            ${is_not_stale_wait}=       Run keyword and return status    Should not contain     ${err_msg_wait}      StaleElementReferenceException
        END

        ${tap_status}=              Run keyword and ignore error   AppiumLibrary.Tap         ${locator}
        ${err_msg_tab}=             Convert to string       ${tap_status[1]}
        ${is_not_stale_tap}=        Run keyword and return status    Should not contain     ${err_msg_tab}      StaleElementReferenceException
        ${is_empty}=                Run keyword and return status    Should be true    '${err_msg_tab}'  == '${NONE}'
        ${is_empty_wait}=           Run keyword and return status    Should be true    '${err_msg_wait}' == '${NONE}'

        ${result}=                  Evaluate    ${is_not_stale_wait} and ${is_not_stale_tap} and ${is_empty} and ${is_empty_wait}
        Exit for loop if            ${result}
    END
    Should be true  ${result}   msg='Failed to click element after 10 retry, with error ${err_msg_tab}, ${err_msg_wait},'

Long press when ready
    [Documentation]     Keyword to wait for element to be visible before long press
    ...    \n default timeout is same as ${GLOBAL_TIMEOUT}
    [Arguments]     ${locator}      ${duration}=1000    ${timeout}=${GLOBAL_TIMEOUT}
    mobileKeyword.Wait until element is visible except stale     ${locator}    ${timeout}
    AppiumLibrary.Long press         ${locator}       duration=${duration}

Input text to element when ready
    [Documentation]     Keyword to wait for element to be visible before input text
    ...    \n default timeout is same as ${GLOBAL_TIMEOUT}
    [Arguments]     ${locator}      ${text}    ${clear}=${TRUE}     ${timeout}=${GLOBAL_TIMEOUT}
    mobileKeyword.Wait until element is visible except stale    ${locator}     ${timeout}
    mobileKeyword.Tap element when ready   ${locator}     ${timeout}
    IF  ${clear}
        AppiumLibrary.Clear text      ${locator}
    END
    AppiumLibrary.Input text      ${locator}          ${text}

Get text from element when ready
    [Documentation]     Wait until element is visible then get text
    ...    \n default timeout is same as ${GLOBAL_TIMEOUT}
    [Arguments]     ${locator}      ${timeout}=${GLOBAL_TIMEOUT}
    mobileKeyword.Wait until element is visible except stale   ${locator}    ${timeout}
    ${text}=    AppiumLibrary.Get text    ${locator}
    [Return]    ${text}

Swipe up
    [Documentation]     Swiping up by percent
    ...     \n ``start_x`` starting at 50% of width of the screen
    ...     \n ``start_y`` starting at 80% of hight of the screen, button of the screen
    ...     \n ``end_x``   ending at 50% of width of the screen, same horizontally as start
    ...     \n ``end_y``   ending at 20% of hight of the screen, moving up 
    [Arguments]         ${start_x}=50
                ...     ${start_y}=80
                ...     ${end_x}=50
                ...     ${end_y}=20
                ...     ${duration}=1000
    AppiumLibrary.Swipe by percent    ${start_x}  ${start_y}  ${end_x}  ${end_y}    duration=${duration}

Swipe down
    [Documentation]     Swiping down by percent
    ...     \n ``start_x`` starting at 50% of width of the screen
    ...     \n ``start_y`` starting at 20% of hight of the screen, top of the screen
    ...     \n ``end_x``   ending at 50% of width of the screen, same horizontally as start
    ...     \n ``end_y``   ending at 80% of hight of the screen, moving down 
    [Arguments]         ${start_x}=50
                ...     ${start_y}=20
                ...     ${end_x}=50
                ...     ${end_y}=80
                ...     ${duration}=1000
    AppiumLibrary.Swipe by percent    ${start_x}  ${start_y}  ${end_x}  ${end_y}    duration=${duration}

Move to
    [Documentation]  Move to used this keyword with set resolution
    [Arguments]    ${moveto}
    IF  "${moveto}"=="Left"
        Swipe    ${center_x}        ${center_y}    ${newx}          ${center_y}         1500
    ELSE IF     "${moveto}"=="Right"
        Swipe    ${newx}            ${center_y}    ${center_x}       ${center_y}        1500
    ELSE IF     "${moveto}"=="Top"
        Swipe    ${center_x}        ${center_y}    ${center_x}       ${newY}            2500
    ELSE IF     "${moveto}"=="Bottom"
        Swipe    ${center_x}        ${newY}        ${center_x}       ${center_y}        2500
    END
