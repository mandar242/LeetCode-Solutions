"""
In this problem we are given a list containing logs.
eg. - ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

There are two varieties of logs letter-logs which start which contain letters and 
digit-logs which contains only digits.  
we have to Reorder the logs so that all of the letter-logs come before any digit-log.  
The letter-logs are ordered lexicographically.j

This can be done using basic list and string operations. 

Time - O ( n log n ) :  N for iterating over lines and Log N for sorting the logs

"""

def reorderLogFiles(logs):
    
    #create two different lists to store digit logs and letter logs
    letterlogs = []
    digitlogs = []
    
    #for each log in logs split the log and check if the 1st(indexwise) item is digit or alphabet
    #and then add to digitLog or letterLog
    for log in logs:
        if (log.split()[1]).isdigit():
            digitlogs.append(log)
        else:
            letterlogs.append(log.split())
    
    # while adding to list we need to split the logs into list of words because 
    # we cannot sort the string directly
            
    # sort letter logs based on 1st(indexwise) string log
    letterlogs = sorted(letterlogs,key = lambda x:x[0])
    #sort letter logs based on 2nd(indexwise) string in the log
    letterlogs = sorted(letterlogs,key = lambda x:x[1:])
    
    for i in range(len(letterlogs)):
        letterlogs[i] = (" ".join(letterlogs[i])) #re-creating log from list items
        
    letterlogs.extend(digitlogs) #combining letterLogs and digitLogs
    return letterlogs


logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
print(reorderLogFiles(logs))