*** Settings ***
Library        AppiumLibrary
Library        SeleniumLibrary
Library        ExcelLibrary
Library        OperatingSystem
Library        Pdf2TextLibrary
Library        Collections
Library        DateTime
Library        String
Library        ImapLibrary2
Library        BrowserMobProxyLibrary
Library        JSONLibrary
Library        AscendQaCommonLibrary
# for submodule
Library        ${CURDIR}/keywords/utils/AppiumUtils.py
Library        ${CURDIR}/keywords/utils/DateUtils.py
Library        ${CURDIR}/keywords/utils/ImageUtils.py
Library        ${CURDIR}/keywords/utils/JsonUtils.py
Library        ${CURDIR}/keywords/utils/GeneralUtils.py
Library        ${CURDIR}/keywords/utils/AdbUtils.py
Library        ${CURDIR}/keywords/utils/AppiumUtils.py
