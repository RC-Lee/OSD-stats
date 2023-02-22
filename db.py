import sqlite3

dbName = "stats.db"

def init():
    print("Initializing DataBase")
    try:
        conn = sqlite3.connect(dbName)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE,
                full_name TEXT,
                year INTEGER
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS issues (
                id INTEGER PRIMARY KEY,
                url TEXT UNIQUE,
                org_name TEXT,
                repo_name TEXT,
                issue_number INTEGER,
                year INTEGER
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS prs (
                id INTEGER PRIMARY KEY,
                url TEXT UNIQUE,
                org_name TEXT,
                repo_name TEXT,
                pr_number INTEGER,
                year INTEGER
            )
        ''')
        conn.commit()
        conn.close()

    except Exception as e:
        print("type error: " + str(e))

def add_user(user):
    try:
        conn = sqlite3.connect(dbName)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT OR IGNORE INTO users (username, full_name, year)
            VALUES (?, ?, ?)
        ''', (user['username'], user['full_name'], user['year']))
        conn.commit()
        conn.close()
    except Exception as e:
        print("type error: " + str(e))

def add_issue(issue):
    try: 
        conn = sqlite3.connect(dbName)
        cursor = conn.cursor()
        cursor.execute(('''
            INSERT OR IGNORE INTO issues (url, org_name, repo_name, issue_number, year)
            VALUES (?, ?, ?, ?, ?)
        '''), (issue['url'], issue['org_name'], issue['repo_name'], issue['issue_number'], issue['year']))
        conn.commit()
        conn.close()
    except Exception as e:
        print("type error: " + str(e))

def add_pr(pr):
    try: 
        conn = sqlite3.connect(dbName)
        cursor = conn.cursor()
        cursor.execute(('''
            INSERT OR IGNORE INTO prs (url, org_name, repo_name, pr_number, year)
            VALUES (?, ?, ?, ?, ?)
        '''), (pr['url'], pr['org_name'], pr['repo_name'], pr['pr_number'], pr['year']))
        conn.commit()
        conn.close()
    except Exception as e:
        print("type error: " + str(e))

