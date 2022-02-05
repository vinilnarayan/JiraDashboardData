from jira.client import JIRA
import pandas as pd 
import configparser
config = configparser.RawConfigParser()
config.read('ConfigFile.properties')
months = config.get('JiraSection', 'jira.months')
month=months.split(",")
jira = JIRA(config.get('JiraSection', 'jira.url'), basic_auth=(config.get('JiraSection', 'jira.username'), config.get('JiraSection', 'jira.password')))
print ("=====> Fetching data from Jira")
for mnt in month:
     curr_mnth=mnt.strip()
     start_date=str(pd.Period(curr_mnth,freq='M').start_time.date())
     end_date=str(pd.Period(curr_mnth,freq='M').end_time.date())    
     iTQSecIssuesJQL = "'Type of Testing' = '"+config.get('JiraSection', 'jira.typeOfTesting')+"' AND createdDate >= "+start_date+" AND createdDate <= "+end_date+" AND reporter in ("+config.get('JiraSection', 'jira.reporters')+")"
     data = jira.search_issues(iTQSecIssuesJQL,maxResults=500000)
     '''
     if len(data) == 0:
        print('No vulnerabilities reported')
     '''
     if data:
         file=open(curr_mnth+"_iTQSecIssues.csv","w") 
         for issue in data:
          file.write(str(issue.fields.project.name)+','+str(issue.key)+','+str(issue.fields.priority.name)+','+str(issue.fields.status)+'\n')
         file.close()
print ("=====> Data fetching completed")