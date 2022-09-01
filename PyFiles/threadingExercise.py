# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 07:51:58 2022

@author: Momin-PC
"""

#Threading Exercise ---
import datetime as dt
from datetime import datetime as dtClass
import threading as th
import csv as c
import statistics as s
import cProfile as cP
import pstats
import io
border = "-" * 175 + "\n"
logFile = open('E:\\python\\temperature.txt','a')

def traceTask(func):
    def calOperation(*args,**kargs):
        logFile.write("The Method Called is : {}\n".format(func.__name__))
        pr = cP.Profile()
        pr.enable()
        returned_value = func(*args,**kargs)
        pr.disable()
        data = io.StringIO()
        ps = pstats.Stats(pr, stream=data).sort_stats('tottime')
        ps.print_stats()
        result = "Operation Result: {}\n".format(returned_value)
        log = data.getvalue()
        logFile.write(result)
        logFile.write(log)
        logFile.write('Execution of the method is completed\n')
        logFile.write(border)
        return result
    return calOperation

#get Data
filePath = "E:\\python\\temperature-200423-032315.csv"
dataFile = open(filePath)
file = c.reader(dataFile)
#rm header
file.__next__()
tempList = []
lapseList = []
for record in file:
    tempList.append(float(record[1]))
    lapseList.append(record[0])
@traceTask    
def avg_Temperature(temps):
    return s.mean(temps)
@traceTask  
def avg_Lapse(lapses):
    length = lapses.__len__()
    lapseFirst = dtClass.strptime(lapses[0],"%H:%M:%S")
    lapseLast = dtClass.strptime(lapses[length - 1],"%H:%M:%S")
    lapseDifference = (lapseLast - lapseFirst).seconds
    return lapseDifference/length
@traceTask
def largest_Spike(temps):
    spikes = []
    for index,temperature in enumerate(temps):
        if(index == temps.__len__()-1):continue
        spikes.append((temperature - temps[index+1])/temps[index+1] )
    return max(spikes)
@traceTask
def deviation(temps):
    return s.pstdev(temps)


def non_threading():
    start_time = dtClass.now()
    logFile.write(border+"Without Threading >> Starting at : ")
    logFile.write(str(start_time))
    logFile.write("\n"+border)
    calculateAvg(tempList,lapseList)
    calculateSharpness(tempList)
    end_time = dtClass.now()
    logFile.write(border+"Without Threading >> Ending at : ")
    logFile.write(str(end_time))
    logFile.write("\n"+border)
    time = (start_time - end_time).seconds
    return time
    #logFile.write(border+"Without Threading >> Ending at : "+end_time+"\n"+border)
    
def calculateAvg(tempList,lapseList):
    print('Average Temperature: ',avg_Temperature(tempList))
    print("Average Lapse Duration: ",avg_Lapse(lapseList))
def calculateSharpness(tempList):
    print("Largest Spikes: ",largest_Spike(tempList))
    print("Deviation: ",deviation(tempList))
    
   
def threading():
    start_time = dtClass.now()
    logFile.write(border+"Threading >> Starting at : ")
    logFile.write(str(start_time))
    logFile.write("\n"+border)
    logFile.write("Creating Thread No.1 >>\n Functions:\nave_Temperature\navg_Lapse")
    t1 = th.Thread(target=calculateAvg,args=(tempList,lapseList))
    logFile.write("Creating Thread No.2 >>\n Functions:\nlargets_Spike\ndeviation")
    t2 = th.Thread(target=calculateSharpness,args=(tempList,))
    logFile.write("Starting {}".format(t1))
    t1.start()
    logFile.write("Starting {}".format(t2))
    t2.start()
    logFile.write("Waiting for {} to finish".format(t1))
    t1.join()
    logFile.write("Waiting for {} to finish".format(t2))
    t2.join()
    end_time = dtClass.now()
    logFile.write(border+"Threading >> Ending at : ")
    logFile.write(str(end_time))
    logFile.write("\n"+border)
    time = (start_time - end_time).microseconds
    return time
    #logFile.write(border+"Threading >> Ending at : "+end_time+"\n"+border)
#Threading:
def main():
    s1 = str(non_threading())
    s2 = str(threading())
    logFile.write("Summary : \nTime Taken By Non-Threading Process :"+s1+"\nTime Taken By Threading Process :"+s2)
    logFile.close()
    
main()    
    