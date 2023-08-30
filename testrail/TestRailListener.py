import sys
sys.path.append('./resources/etc/')

from TestRailConfig import *
import re
ROBOT_LISTENER_API_VERSION = 3

def end_test(name, attrs):
    mapping = json.load(open(mapping_file_path))
    status_id = get_testrail_status(attrs.status)
    tags = extract_testrail_automation_id(attrs)
    elapsed = int(attrs.elapsedtime / 1000)
    comment = BuiltIn().get_variable_value('${TEST_MESSAGE}')
    output_dir = BuiltIn().get_variable_value('${OUTPUT_DIR}')
    if elapsed > 0:
        elapsed = str(int(attrs.elapsedtime / 1000)) + "s"
    print(elapsed)
    for tag in tags:
        test_id = mapping[tag]
        result_id = add_test_result(test_id, status_id, elapsed, comment)
        if result_id != 0:
            if status_id == TESTRAIL_TEST_STATUS_ID_FAILED:
                filepath = get_screenshot_path(output_dir, name)
                print("test_id = {} and result_id = {} and screenshot path = {}".format(test_id, result_id, filepath))
                add_attachment(result_id, filepath)
            else:
                print("test_id = {} and result_id = {}".format(test_id, result_id))
        else:
            print("result_id + {}".format(result_id))

def extract_testrail_automation_id(attrs):
    tags = []
    for tag in attrs.tags:
        if eval(TESTTAG_FILTER_LOGIC) :
            tags.append(tag)
    return tags

def add_test_result(test_id, status_id, elapsed, comment):
    url = API_ADD_RESULT.format(testId=test_id)
    payload = {"status_id": status_id,
               "elapsed": elapsed,
               "comment": comment}
    resp = requests.post(url,
                        json=payload,
                        auth=(TESTRAIL_USERNAME,TESTRAIL_PASSWORD),
                        headers=header,
                        timeout=60)
    if resp.status_code == 200:
        return resp.json()['id']
    else:
        print(resp.json())
        print(payload)
        print("Status code = {}. Cannot update test result for test_id = {} ".format(resp.status_code, test_id))
        return 0
    
def get_testrail_status(robot_status):
    if robot_status == 'PASS':
        return TESTRAIL_TEST_STATUS_ID_PASSED
    elif robot_status == 'FAIL':
        return TESTRAIL_TEST_STATUS_ID_FAILED
    else:
        return TESTRAIL_TEST_STATUS_ID_UNTESTED
    
def get_screenshot_path(output_dir, name):
    filepath = os.path.join(output_dir, str(name) + '.png')
    return filepath

def add_attachment(result_id, filepath):
    url = API_ADD_ATTACHMENT.format(resultId=result_id)
    files = {'attachment': (open(filepath, 'rb'))}
    resp = requests.post(url,
                    auth=(TESTRAIL_USERNAME,TESTRAIL_PASSWORD),
                    files=files)
    files['attachment'].close()
    print(url)
    print(resp.jsopn())
    if resp.status_code != 200:
        print("Status code = {}. Cannot add aattachment for result_id = {}".format(resp.status_code, result_id))