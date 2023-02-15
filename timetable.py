import random

from numpy import Infinity

sections = ["BioMaths-Tamil","BioMaths-English","Computer Science","Agri"]
days = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
nPeriods = 8

subjects = {"Math":7,
            "Tamil":4,
            "English":4,
            "Zoology":4,
            "Botany":4,
            "Physics":5,
            "Chemistry":5,
            "Computer Science":5,
            "Agri":7,
            "CT": 5,
            
            }

coreSubjects = ["Math","Physics","Chemistry","Computer Science","Zoology","Botany","Agri","CT"]

otherSubjects = ["Tamil","English"]

labs = {"Physics Lab":2,
        "Chemistry Lab":2,
        "CT":2,
        "Computer Science Lab":2,
        "Agri Lab":7,
        "PET":2,
        "Biology Lab": 2
        }

periods = {
    "BioMaths-Tamil": ["Tamil","English","Math","Physics","Chemistry","Zoology","Botany"],
    "BioMaths-English": ["Tamil","English","Math","Physics","Chemistry","Zoology","Botany"],
    "Computer Science": ["Tamil","English","Math","Physics","Chemistry","Computer Science"],
    "Agri": ["Tamil","English","Zoology","Botany","CT","Agri"],
}

labPeriods = {
    "BioMaths-Tamil": ["Physics Lab","Chemistry Lab","PET"],
    "BioMaths-English": ["Physics Lab","Chemistry Lab","PET"],
    "Computer Science": ["Computer Science Lab","Physics Lab","Chemistry Lab","PET"],
    "Agri": ["CT","Agri Lab","PET"],
}

classTeacher = {
    "BioMaths-Tamil": "English",
    "BioMaths-English": "English",
    "Computer Science": "Computer Science",
    "Agri": "Agri",
}
assistantTeacher = {
    "BioMaths-Tamil": "Tamil",
    "BioMaths-English": "Tamil",
    "Computer Science": "Computer Science",
    "Agri": "Agri",
}

def createTimeTables(sections,days,no_of_periods):
    timeTables = dict()
    for sec in sections:
        section = dict()

        for day in days:
            periods = []

            for _ in range(no_of_periods):
                periods.append("")

            section[day] = periods

        timeTables[sec] = section
    return timeTables


def displayTimeTables(timeTables):
    for sec,timetable in timeTables.items():
        print(sec)
        for day,periods in timetable.items():
            print(day,periods)

        print('-'*50)


def fillFirstPeriod(timetable,periods,section,classTeacher):
    for day,slots in timetable.items():
        if slots[0] == "" and periods[section][classTeacher[section]] > 0:
            slots[0] = classTeacher[section]
            periods[section][classTeacher[section]] -= 1


def fillSlots(timetable,periods,positions,subject,day,section):
    position = random.choice(positions)

    slot = timetable[section][day][position-1]
    if subject in periods[section].keys():
        flag = True
        for sections in periods.keys():
            if timetable[sections][day][position-1] == subject:
                flag = False


        if flag and slot == "" and periods[section][subject] > 0:
            timetable[section][day][position-1] = subject
            periods[section][subject] -= 1

            

def fillDuplicateSlots(timetable,periods,duplicateSections,positions,subject,day,section):
    position = random.choice(positions)

    slot = timetable[section][day][position-1]
    if section not in duplicateSections:
        if subject in periods[section].keys():
            flag = True
            for sections in periods.keys():
                if timetable[sections][day][position-1] == subject:
                    flag = False


            if flag and slot == "" and periods[section][subject] > 0:
                timetable[section][day][position-1] = subject
                periods[section][subject] -= 1

    else:


        if subject in periods[section].keys():
            flag = True
            for sections in periods.keys():
                if timetable[sections][day][position-1] == subject:
                    flag = False
            for sections in duplicateSections:

                if timetable[sections][day][position-1] != "":
                    flag = False

            for sections in duplicateSections:
                if subject in periods[sections].keys():
                    if flag and slot == "" and periods[sections][subject] > 0:

                        timetable[sections][day][position-1] = subject
                        periods[sections][subject] -= 1
            





def fillLabSlots(timetable,labPeriods,positions,subject,day,section):
    position = random.choice(positions)

    slot = timetable[section][day][position-1]
    if position == 8:
        nextslot = "END"

    else:
        nextslot = timetable[section][day][position]

    if subject in labPeriods[section].keys():
        flag = True
        for sections in labPeriods.keys():
            if timetable[sections][day][position-1] == subject or timetable[sections][day][position-1] == subject.replace(" Lab",""):
                flag = False



        if flag and slot == "" and nextslot == "" and position != 4 and labPeriods[section][subject] > 0:
            timetable[section][day][position-1] = subject
            timetable[section][day][position] = subject

            labPeriods[section][subject] -= 2

def fillDuplicateLabSlots(timetable,duplicateSections,labPeriods,positions,subject,day,section):
    position = random.choice(positions)

    slot = timetable[section][day][position-1]
    if section not in duplicateSections:
        if position == 8:
            nextslot = "END"

        else:
            nextslot = timetable[section][day][position]

        if subject in labPeriods[section].keys():
            flag = True
            for sections in labPeriods.keys():
                if timetable[sections][day][position-1] == subject or timetable[sections][day][position-1] == subject.replace(" Lab",""):
                    flag = False



            if flag and slot == "" and nextslot == "" and position != 4 and labPeriods[section][subject] > 0:
                timetable[section][day][position-1] = subject
                timetable[section][day][position] = subject

                labPeriods[section][subject] -= 2
                
    else:
        if position == 8:
            nextslot = "END"

        else:
            nextslot = timetable[section][day][position]

        if subject in labPeriods[section].keys():
            flag = True
            for sections in labPeriods.keys():
                if timetable[sections][day][position-1] == subject or timetable[sections][day][position-1] == subject.replace(" Lab",""):
                    flag = False

            for sections in duplicateSections:
                if timetable[sections][day][position-1] != "":
                    flag = False

                if subject in labPeriods[sections].keys():

                    if flag and slot == "" and nextslot == "" and position != 4 and labPeriods[sections][subject] > 0:
                        timetable[sections][day][position-1] = subject
                        timetable[sections][day][position] = subject

                        labPeriods[sections][subject] -= 2




def fillCoreSubjects(timetable,periods,coreSubjects):
    x = 0
    while x < 1000:

        for subject in coreSubjects:

            for section,tymtable in timetable.items():
                for day, period in tymtable.items():
                    fillDuplicateSlots(timetable,periods,["BioMaths-Tamil","Computer Science"],[1,2,3,4],subject,day,section)


                    

            x +=1

        
def fillOtherSubjects(timetable,periods,otherSubjects):
    x= 0
    while x < 200:

        for subject in coreSubjects:

            for section,tymtable in timetable.items():
                for day, period in tymtable.items():

                    fillDuplicateSlots(timetable,periods,["BioMaths-Tamil","Computer Science"],[1,2,3,4,5,6,7,8],subject,day,section)
            x +=1

    x= 0
    while x < 1000:

        for subject in otherSubjects:

            for section,tymtable in timetable.items():
                for day, period in tymtable.items():

                    fillDuplicateSlots(timetable,periods,["BioMaths-Tamil","BioMaths-English"],[1,2,3,4,5,6,7,8],subject,day,section)
            x +=1


def fillExtraSubjects(timetable,periods,positions,subject,day,section):
    score = 0
    for position in positions:
        slot = timetable[section][day][position-1]
        if subject in periods[section].keys():
            flag = True
            for sections in periods.keys():
                if timetable[sections][day][position-1] == subject:
                    flag = False

        
            
            if flag and slot == "" and periods[section][subject] > 0:
                timetable[section][day][position-1] = subject
                periods[section][subject] -= 1

                score += 1

    return score

            
def fillOtherExtraSlots(timetable,periods,positions,subject,day,section):
    score = 0
    for position in positions:
        slot = timetable[section][day][position-1]
        if subject in periods[section].keys():
            flag = True
            for sections in periods.keys():
                if timetable[sections][day][position-1] == subject:
                    flag = False            
            
            for secs in periods.keys():
                if subject in periods[secs].keys():
                    if flag and timetable[section][day][position-1] == "" and periods[secs][subject]>0:
                        timetable[section][day][position-1] = subject
                        periods[secs][subject] -= 1
                        score += 2

    return score
                        


def fillExtra(timetable,periods,subjects,labs):
    x = 0
    score = 0
    while x < 1000:

        for subject in subjects.keys():

            for section,tymtable in timetable.items():
                for day, period in tymtable.items():

                    score += fillExtraSubjects(timetable,periods,[1,2,3,4,5,6,7,8],subject,day,section)

            x +=1

        for subject in labs.keys():

            for section,tymtable in timetable.items():
                for day, period in tymtable.items():

                    score += fillExtraSubjects(timetable,periods,[1,2,3,4,5,6,7,8],subject,day,section)

            x +=1

    x = 0
    while x < 1000:

        for subject in subjects.keys():

            for section,tymtable in timetable.items():
                for day, period in tymtable.items():

                    score += fillOtherExtraSlots(timetable,periods,[1,2,3,4,5,6,7,8],subject,day,section)

            x +=1


    return score



def fillLabs(timetable,labPeriods,labs):
    x = 0
    while x < 1000:

        for subject in labs.keys():

            for section,tymtable in timetable.items():
                for day, period in tymtable.items():

                    fillDuplicateLabSlots(timetable,['BioMaths-Tamil','Computer Science'],labPeriods,[1,2,3,4,5,6,7,8],subject,day,section)

            x +=1


def main(sections,days,nPeriods,subjects,coreSubjects,otherSubjects,labs,periods,labPeriods,classTeacher):
    remainingSubs = 100
    while remainingSubs > 1:
        ideal = Infinity
    
        # Nesting periods and subjects
        newPeriodList = {}
        for section,periodList in periods.items():
            for idx,period in enumerate(periodList):
                newPeriodList[period] = subjects[period]

            periods[section] =  newPeriodList.copy()
            newPeriodList.clear()

        # Nesting periods and subjects
        newLabList = {}
        for section,periodList in labPeriods.items():
            for idx,period in enumerate(periodList):
                newLabList[period] = labs[period]

            labPeriods[section] =  newLabList.copy()
            newLabList.clear()



        timetable = createTimeTables(sections,days, nPeriods)

        for section, table in timetable.items():
            fillFirstPeriod(table,periods,section,classTeacher)

        for section, table in timetable.items():
            fillFirstPeriod(table,periods,section,assistantTeacher)


        fillCoreSubjects(timetable,periods,coreSubjects)
        fillLabs(timetable,labPeriods,labs)
        fillOtherSubjects(timetable,periods,otherSubjects)

        # exScore =fillExtra(timetable,periods,subjects,labs)
        exScore = 0


        emptyCount = 0

        for sec, table in timetable.items():
            for day, prds in table.items():
                for position,prd in enumerate(prds):
                    if prd == "":
                        timetable[sec][day][position] = "Value Education"
                        emptyCount += 1

        remainingSubs = 0
        for sec, perd in periods.items():
            for subs,count in perd.items():
                if count>0:
                    remainingSubs += count

        adjScore = 0

        for sec, timtable in timetable.items():
            for day, perdList in timtable.items():
                for idx in range(0, len(perdList)-1):
                    if perdList[idx] == perdList[idx+1]:

                        adjScore += 1


        overallScore = 100*remainingSubs
        overallScore += adjScore                    

        if overallScore < ideal:
            ideal = overallScore
            ideal_timetable = timetable
            ideal_emptyCount = emptyCount
            ideal_remainingSubs = remainingSubs

            ideal_periods = periods
            ideal_labPeriods = labPeriods


    displayTimeTables(ideal_timetable)


    print(ideal_emptyCount)
    print(ideal_remainingSubs)
    print(ideal_periods)
    print(ideal_labPeriods)

main(sections,days,nPeriods,subjects,coreSubjects,otherSubjects,labs,periods,labPeriods,classTeacher)