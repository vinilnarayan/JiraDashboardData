# JiraDashboardData
Analyzing data from Jira and creating a csv report file.
This will fetch reported issues (based on the reporter mentioned in 'ConfigFile.properties') with mentioned months and criterias in 'ConfigFile.properties'.
Then will process the fetched data and create 2 types of files for each month of data.
  1. PriorityCounts (Count of issues based on the current priority)
  2. StatusCounts (Count of issues based on the current status)
No file will generate if no issues reported in the mentioned month.
eg : jira.months=01-OCT-21
     This will consider like an issue reported from 01-OCT-2021 to 31-OCT-2021. (It automatically fetching start date and end date of given months)

#### Requirements
☛ Python
☛ Pip

#### Downloads

1. [Python](https://www.python.org/)
2. [Pip](https://pypi.org/project/pip/)

## Usage
➤ Clone this repository 
```
git clone https://github.com/vinilnarayan/JiraDashboardData.git
```
➤ Navigate to 'JiraDashboardData'
```
cd JiraDashboardData
```
➤ Run below code to install required packages
```
pip install -r requirements.txt
```
➤ Change the required data in 'ConfigFile.properties'
##### Sample data
```
[JiraSection]
jira.url=https://jira.demo.com/jira/
jira.username=Vinil
jira.password=Vinil@Password
jira.reporters=Vinil, Jabir, Ramdas
jira.months=01-OCT-21, 01-NOV-21, 01-DEC-21, 01-JAN-22, 01-FEB-22
jira.typeOfTesting=Security Testing
```
➤ Run scripts with 
```
python runner.py
```
or
```
python3 runner.py
```
