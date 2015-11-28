import requests
import lxml.html


search_url = 'http://acm.cs.nthu.edu.tw/status/'
login_url = 'http://acm.cs.nthu.edu.tw/users/login/'
view_code_url = 'http://acm.cs.nthu.edu.tw/status/view_code/{}'
problem_url = 'http://acm.cs.nthu.edu.tw/problem/{}/'


class LoginFailed(Exception):
    pass


class YouNoAc(Exception):
    pass


class QueryFailed(Exception):
    pass


class Problem404(Exception):
    pass


def verify_ac(username, problem_id):
    response = requests.get(search_url,
        params={
            'username': username,
            'pid': problem_id,
            'status': 'AC'
        })
    if 'No submissions found for the given query!' in response.text:
        return None
    elif 'Please check filter constraints again!' in response.text:
        raise QueryFailed(username, problem_id)
    else:
        document = lxml.html.fromstring(response.content)
        return int(document.xpath('//tr[@class="success"]/td[1]')[0].text.strip())


def login_session(username, password):
    session = requests.Session()
    response = session.get(login_url)
    document = lxml.html.fromstring(response.content)
    target = document.xpath('//input[@name="csrfmiddlewaretoken"]')[0]
    response = session.post(
        login_url,
        data={
            'username': username,
            'password': password,
            'csrfmiddlewaretoken': target.attrib['value']
        }
    )
    if 'Please enter a correct username and password. Note that both fields may be case-sensitive.' in response.text:
        raise LoginFailed
    return session


def fetch_ac_code(username, password, problem_id):
    session = login_session(username, password)
    submission_id = verify_ac(username, problem_id)
    if submission_id is None:
        raise YouNoAc(username, problem_id)
    url = view_code_url.format(submission_id)
    response = session.get(url)
    document = lxml.html.fromstring(response.content)
    target = document.xpath('//textarea[@id="code_editor"]')
    # print(target[0].text)
    return target[0].text


def test_problem_existence(problem_id):
    return requests.get(problem_url.format(problem_id)).status_code == 200
