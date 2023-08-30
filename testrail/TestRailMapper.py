import sys
sys.path.append('./resources/etc/')

from TestRailConfig import *

def get_runid(project_id,milestone_id,runid_list = []):
    url = API_GET_RUNS.format(projectId=project_id,milestoneId=milestone_id)
    resp = requests.get(url,
                        auth=(TESTRAIL_USERNAME,TESTRAIL_PASSWORD),
                        headers=header,
                        timeout=60)
    if resp.status_code == 200:
        for run in resp.json()['runs']:
            runid_list.append(run['id'])
        return runid_list
    else:
        return []
    
def get_mapping_testid_and_automationid(runid_list):
    mapping = {}
    for runid in runid_list:
        url = API_GET_TESTS.format(runId=runid)
        
        while url:
            print("Full URL:", url)
            resp = requests.get(url,
                                auth=(TESTRAIL_USERNAME, TESTRAIL_PASSWORD),
                                headers=header,
                                timeout=60)
            if resp.status_code == 200:
                res = resp.json()
                _links = res['_links']
                responseNext = _links.get('next')
                
                for test in res['tests']:
                    automation_id = test.get('custom_automation_id')
                    test_id = test['id']
                    case_id = test['case_id']
                    
                    if automation_id:
                        mapping[automation_id] = test_id
                    else:
                        mapping[f"C{case_id}"] = test_id

                if responseNext:
                    url = API_GET_TESTS_OFFSET.format(resNext=responseNext)
                else:
                    url = None
            else:
                print("Error:", resp.status_code)

    return mapping

def get_planid(project_id,milestone_id):
    url = API_GET_PLANS.format(projectId=project_id,milestoneId=milestone_id)
    resp = requests.get(url,
                        auth=(TESTRAIL_USERNAME,TESTRAIL_PASSWORD),
                        headers=header,
                        timeout=60)
    planid_list = []
    if resp.status_code == 200:
        for plan in resp.json()['plans']:
            planid_list.append(plan['id'])
        return planid_list
    else:
        return []

def get_runid_from_plan(planid_list,runid_list = []):
    for planid in planid_list:
        url = API_GET_PLAN.format(planId=planid)
        resp = requests.get(url,
                            auth=(TESTRAIL_USERNAME,TESTRAIL_PASSWORD),
                            headers=header,
                            timeout=60)
        if resp.status_code == 200:
            for entry in resp.json()['entries']:
                for run in entry['runs']:
                    runid_list.append(run['id'])
    return runid_list

def create_mapping_file(mapping):
    with open(mapping_file_path, "w") as outfile:
        json.dump(mapping, outfile)

if __name__ == '__main__':
    runid_list = get_runid(PROJECT_ID,MILESTONE_ID)
    planid_list = get_planid(PROJECT_ID,MILESTONE_ID)
    runid_list = get_runid_from_plan(planid_list,runid_list)
    print(runid_list)
    mapping = get_mapping_testid_and_automationid(runid_list)
    print(mapping)
    create_mapping_file(mapping)