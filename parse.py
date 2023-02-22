import re
import db

def parse_line(line, year=0):
    db.init()

    # regular expression pattern
    patternUser1 = r"https://github.com/([\w\d-]+)[^/?] - (.*)"
    patternUser2 = r"https://github.com/([\w\d-]+)[\s^/?].* - ([^=]+)==="
    patternIssue = r"(https://github.com/[^/]+/[^/]+/issues/\d+)[\s\/<]?"
    patternPr = r"(https://github.com/[^/]+/[^/]+/pull"
    
    # user
    matchUser = re.search(patternUser1, line)
    if not matchUser:
        matchUser = re.search(patternUser2, line)

    if matchUser:
        user = {}
        user['username'] = matchUser.group(1)
        user['full_name'] = matchUser.group(2)
        user['year'] = year

        if user['username'] != "GitHubUserName":
            db.add_user(user)
    
    #issue
    matchIssue = re.findall(patternIssue, line)
    for match in matchIssue:
        issue = {}
        issue['url'] = match
        parseIssue = r"https://github.com/([^/]+)/([^/]+)/issues/(\d+)"
        parse = re.search(parseIssue, match)
        issue['org_name'] = parse.group(1)
        issue['repo_name'] = parse.group(2)
        issue['issue_number'] = parse.group(3)
        issue['year'] = year

        if "example" not in match:
            db.add_issue(issue)

    #pr
    matchPr = re.findall(patternPr, line)
    for match in matchPr:
        pr = {}
        pr['url'] = match
        parsePr = r"https://github.com/([^/]+)/([^/]+)/pull/(\d+)"
        parse = re.search(parsePr, match)
        pr['org_name'] = parse.group(1)
        pr['repo_name'] = parse.group(2)
        pr['pr_number'] = parse.group(3)
        pr['year'] = year
        db.add_pr(pr)
