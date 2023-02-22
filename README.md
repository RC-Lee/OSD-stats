## [OSD-stats](https://github.com/RC-Lee/OSD-stats/wiki)
Beginning of a project to centralize data for students participating in Hacktoberfest for OSD.

For basic stats go to the repo [wiki](https://github.com/RC-Lee/OSD-stats/wiki)

---

## Where does the data come from?
As written in [data.json](https://github.com/RC-Lee/OSD-stats/blob/main/data.json), all current basic data are gathered from parsing wiki data from previous OSD years.
1. [2018](https://raw.githubusercontent.com/wiki/humphd/hacktoberfest-at-seneca-2018/Student-Submissions.md)
2. [2019](https://raw.githubusercontent.com/wiki/RC-Lee/2019raw/raw.md), originally from [here](https://wiki.cdot.senecacollege.ca/wiki/OSD_%26_DPS909_Fall_2019_-_Release_0.2).
3. [2020](https://raw.githubusercontent.com/wiki/Seneca-CDOT/topics-in-open-source-2020/release-0.2.md)
4. [2021](https://raw.githubusercontent.com/wiki/Seneca-CDOT/topics-in-open-source-2021/release-0.2.md)
5. [2022](https://raw.githubusercontent.com/wiki/Seneca-CDOT/topics-in-open-source-2022/release-0.2.md)

---

## Setup
- Download Python3, which should come with sqlite3
- Run the following script
```script
py load.py
```
- Will create a `stats.db` database in the current working directory, and populate the database
- Create scripts to create `.md` files as needed, like in the [wiki](https://github.com/RC-Lee/OSD-stats/wiki)

---

## DB Tables
Current schema for the database tables is as below:
```db
users (
  id         INTEGER  PRIMARY KEY,
  username   TEXT     UNIQUE,
  full_name  TEXT,
  year       INTEGER
)

issues (
  id            INTEGER  PRIMARY KEY,
  url           TEXT     UNIQUE,
  org_name      TEXT,
  repo_name     TEXT,
  issue_number  INTEGER,
  year          INTEGER
)

prs (
  id         INTEGER  PRIMARY KEY,
  url        TEXT     UNIQUE,
  org_name   TEXT,
  repo_name  TEXT,
  pr_number  INTEGER,
  year       INTEGER
)
```
