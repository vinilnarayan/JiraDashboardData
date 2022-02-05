import glob
import csv
files = []
files = glob.glob("*.csv")
print ("=====> Analyzing data")
for file in files:
    #print(str(file))
    countFileName = str(file).split(".")[0]
    statusCountFile = open(str(countFileName)+"_StatusCounts.csv","w")
    statusCountFile.write('Open,Fixed,Wont Fix\n')
    priorityCountFile = open(str(countFileName)+"_PriorityCounts.csv","w")
    priorityCountFile.write('Critical,Major,Minor,Trivial\n')
    '''
    projectPriorityCountFile = open(str(countFileName)+"_ProjectPriorityCounts.csv","w")
    projectPriorityCountFile.write('Project,Critical,Major,Minor,Trivial\n')
    projectStatusCountFile = open(str(countFileName)+"_ProjectStatusCounts.csv","w")
    projectStatusCountFile.write('Project,Open,Fixed,Wont Fix\n')
    '''
    #projects = []
    openIssues = 0
    verifiedIssues = 0
    wontFixIssues = 0
    CriticalIssues = 0
    MajorIssues = 0
    MinorIssues = 0
    TrivialIssues = 0
    with open(file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for csvdata in reader:
            #print(csvdata[2])
            #if csvdata[0] not in projects:
            #    projects.append(csvdata[0])
            if csvdata[3] in ('Verified', 'Closed'):
                verifiedIssues = verifiedIssues+1
            if csvdata[3] in ('Deferred'):
                wontFixIssues = wontFixIssues+1
            if csvdata[3] in ('Open', 'Resolved', 'Assigned', 'Released for Testing'):
                openIssues = openIssues+1
            if csvdata[2] in ('Critical'):
                CriticalIssues = CriticalIssues+1
            if csvdata[2] in ('Major'):
                MajorIssues = MajorIssues+1
            if csvdata[2] in ('Minor'):
                MinorIssues = MinorIssues+1
            if csvdata[2] in ('Trivial'):
                TrivialIssues = TrivialIssues+1
                
    #print("Verified Issues = "+str(verifiedIssues))
    #print("Won't Fix Issues = "+str(wontFixIssues))
    #print("Open Issues = "+str(openIssues))
    #print (projects)
    statusCountFile.write(str(openIssues)+','+str(verifiedIssues)+','+str(wontFixIssues)+'\n')
    statusCountFile.close()
    priorityCountFile.write(str(CriticalIssues)+','+str(MajorIssues)+','+str(MinorIssues)+','+str(TrivialIssues)+'\n')
    priorityCountFile.close()
print ("=====> Data analysis completed")