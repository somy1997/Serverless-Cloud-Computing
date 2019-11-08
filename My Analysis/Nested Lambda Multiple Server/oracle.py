#!/usr/bin/env python3
# coding: utf-8

import requests
import statistics
import random
import names
import argparse # for parsing arguments https://docs.python.org/2/howto/argparse.html, https://docs.python.org/2/library/argparse.html
import string
import time
from datetime import datetime as dt
#import itertools #default zip() which doesn't require any imports behaves like itertools.izip() did in py2 so just use zip(), also, no module in itertools called izip in py3

# Generate data for n entries in the table in the file filename
# Email ID has a pattern
# First name and Last name are random
def gendata(filename,n,seed) :
    print('Generating',n,'data values in',filename)
    if verbose :
        print()
    f = open(filename, 'w')
    random.seed(seed)
    for i in range(n):
        #firstname = ''.join(random.choices(string.ascii_uppercase, k=random.randrange(2,18)))
        #lastname = ''.join(random.choices(string.ascii_uppercase, k=random.randrange(2,18)))
        firstname = names.get_first_name()
        lastname = names.get_last_name()
        line = "custid%03d@iitkgp.ac.in,%s,%s\n"%(i, firstname, lastname)
        if verbose :
            print(line.strip())
        f.write(line)
    if verbose :
        print()
    f.close()

def loaddata(filename,n) :
    print('Loading',n,'data values from',filename)
    if verbose :
        print()
    f = open(filename, 'r')
    datalist = []
    i = 0
    for line in f:
        if verbose :
            print(line.strip())
        datalist += [tuple(line.strip().split(','))]
        #print(datalist[-1])
        i += 1
        if i == n:
            break
    f.close()
    if verbose :
        print()
    return datalist

def collectstats(datalist,baseurl,location):
    print('Collecting stats by making post requests to',baseurl)
    if verbose :
        print()
    statslist = []
    i = 1
    for item in datalist :
        payload = {'Location':location}
        now = dt.now()
        start = time.time()
        response=requests.post(baseurl,json=payload)
        end = time.time()
        t = end-start
        t = round(t*1000)
        if verbose :
            print('%03d'%(i)+'. ',now,'Time Taken :',str(t)+'ms Response :',response.text)
        statslist += [(now,t,int(response.text))]
        i += 1
    if verbose :
        print()
    return statslist # its a list of tuple

def collectstatspostdb(datalist,baseurl,location):
    print('Collecting stats by making post requests to',baseurl)
    if verbose :
        print()
    statslist = []
    i = 1
    for item in datalist :
        payload = {'EmailID':item[0], 'FirstName':item[1], 'LastName':item[2], 'Location':location, 'DB':'true'}
        now = dt.now()
        start = time.time()
        response=requests.post(baseurl,json=payload)
        end = time.time()
        t = end-start
        t = round(t*1000)
        if verbose :
            print('%03d'%(i)+'. ',now,'Time Taken :',str(t)+'ms Response :',response.text,'for',item)
        response = response.text.split('$')
        statslist += [(now,t,int(response[0]),int(response[1]))]
        i += 1
    if verbose :
        print()
    return statslist # its a list of tuple

def collectstatsget(datalist,baseurl):
    print('Collecting stats by making get requests to',baseurl)
    if verbose :
        print()
    statslist = []
    i = 1
    for item in datalist :
        start = time.time()
        response=requests.get(baseurl+'?EmailID='+item[0])
        end = time.time()
        if verbose :
            print('%03d'%(i)+'. ','Time Taken :',str(end-start)+'s Response :',response.text)
        statslist += [int(response.text.split('$')[-1])]
        i += 1
    if verbose :
        print()
    return statslist

def getbilledstats(filename):
    print('Loading billed stats from',filename)
    if verbose :
        print()
    f = open(filename, 'r')
    statslist = []
    for line in f:
        if verbose :
            print(line.strip())
        line = line.split()
        #print(line)
        statslist += [round(float(line[4]))] 
        #round function returns type as int by default (decimal places to keep is 0) otherwise float
    f.close()
    if verbose :
        print()
    return statslist 

def getactualstats(filename):
    print('Loading actual stats from',filename)
    if verbose :
        print()
    f = open(filename, 'r')
    statslist = []
    for line in f:
        if verbose :
            print(line.strip())
        #print(line)
        line = line.split(',')
        statslist += [(int(line[0]),int(line[1]))] 
        #round function returns type as int by default (decimal places to keep is 0) otherwise float
    f.close()
    if verbose :
        print()
    return statslist    

def getactualstatsdb(filename):
    print('Loading actual stats from',filename)
    if verbose :
        print()
    f = open(filename, 'r')
    statslist = []
    for line in f:
        if verbose :
            print(line.strip())
        #print(line)
        line = line.split(',')
        statslist += [(int(line[0]),int(line[1]),int(line[2]))] 
        #round function returns type as int by default (decimal places to keep is 0) otherwise float
    f.close()
    if verbose :
        print()
    return statslist   

def savestats(filename, actualstats, outerbilledstats, innerbilledstats) :
    print('Saving actual stats and billed stats in',filename)
    f = open(filename, 'w')
    f.write('Time at which request was sent,Total Time taken (Kharagpur) (ms),Billed Time for outerFunction(ms),Actual Time for innerFunction(ms),Billed Time for innerFunction(ms)\n')
    for (actualstat, outerbilledtime, innerbilledtime) in zip(actualstats,outerbilledstats,innerbilledstats):
        f.write("%s,%d,%d,%d,%d\n"%(actualstat[0],actualstat[1],outerbilledtime,actualstat[2],innerbilledtime))
    if verbose :
        print()
    f.close()

def savestatsdb(filename, actualstats, outerbilledstats, innerbilledstats) :
    print('Saving actual stats and billed stats in',filename)
    f = open(filename, 'w')
    f.write('Time at which request was sent,Total Time taken (Kharagpur) (ms),Billed Time for outerFunction(ms),Actual Time for innerFunction(ms),Billed Time for innerFunction(ms),Actual Time for DB Call(ms)\n')
    for (actualstat, outerbilledtime, innerbilledtime) in zip(actualstats,outerbilledstats,innerbilledstats):
        f.write("%s,%d,%d,%d,%d,%d\n"%(actualstat[0],actualstat[1],outerbilledtime,actualstat[2],innerbilledtime,actualstat[3]))
    if verbose :
        print()
    f.close()

def saveactualstats(filename, actualstats) :
    print('Saving actual stats in',filename)
    f = open(filename, 'w')
    #f.write('Actual Time (ms)\n')
    for stat in actualstats:
        f.write("%d,%d\n"%(stat[0],stat[1]))
    if verbose :
        print()
    f.close()

def saveactualstatsdb(filename, actualstats) :
    print('Saving actual stats in',filename)
    f = open(filename, 'w')
    #f.write('Actual Time (ms)\n')
    for stat in actualstats:
        f.write("%d,%d,%d\n"%(stat[0],stat[1],stat[2]))
    if verbose :
        print()
    f.close()

# gendata(101, "data.txt")

# datalist = loaddata("data.txt")

# baseurlpost = 'https://7yx9o87rrh.execute-api.ap-south-1.amazonaws.com/test/postcustomerdetails'
# actualstatslistpost = collectstatspost(datalist,baseurlpost)

# # ## Note : Copy cloud watch logs in the following file before running this cell
# billedlogsfilepost = 'cwlogs/mumbai_post.txt'
# billedstatslistpost = getbilledstats(billedlogsfilepost)
# savestatsfilepost = 'stats/mumbai_post.csv'
# savestats(savestatsfilepost,actualstatslistpost,billedstatslistpost)


# baseurlget = 'https://7yx9o87rrh.execute-api.ap-south-1.amazonaws.com/test/getcustomerdetails'
# actualstatslistget = collectstatsget(datalist,baseurlget)


# # ## Note : Copy cloud watch logs in the following file before running this cell

# billedlogsfileget = 'cwlogs/mumbai_get.txt'
# billedstatslistget = getbilledstats(billedlogsfileget)
# savestatsfileget = 'stats/mumbai_get.csv'
# savestats(savestatsfileget,actualstatslistget,billedstatslistget)

verbose = 1

if __name__ == "__main__":
    locas = ['ap-northeast-1', 'ap-south-1', 'us-west-1', 'sa-east-1', 'ap-southeast-2', 'eu-west-2']
    locanames = ['Tokyo', 'Mumbai', 'Northern California', 'Sau Paulo', 'Sidney', 'London']
    links = ['https://v8ayvr7yna.execute-api.ap-northeast-1.amazonaws.com/test/test', 'https://aw3yar6j4j.execute-api.ap-south-1.amazonaws.com/test/test', 'https://fwcump7jo7.execute-api.us-west-1.amazonaws.com/test/test', 'https://3zvlb57rq1.execute-api.sa-east-1.amazonaws.com/test/test', 'https://ogkp9x3x69.execute-api.ap-southeast-2.amazonaws.com/test/test', 'https://cfz54bjgwb.execute-api.eu-west-2.amazonaws.com/test/test']
    print('Enter filename for datalist')
    datafile = input().strip()
    print('Enter number of vals to be generated')
    nval = int(input())
    for (i, link) in enumerate(links) :
        for (j,loca) in enumerate(locas) :
            if(j == 0) :
                continue
            print()
            print('Outer Function location :',locanames[i])
            print('Inner Function location :',locanames[j])
            print()
            print('Enter seed value for generating data')
            seed = int(input().strip())
            print('Generating data')
            gendata(datafile, nval, seed)
            datalist = loaddata(datafile, nval)
            
            # print('Taking stats without DB call')
            # print('Press Enter to Continue')
            # input()
            # dblessstats = collectstats(datalist, link, loca)
            # print('Please copy the latest cloudwatch logs for outerFunction from location',locanames[i],'to a local file by selecting logs in raw format and filtering it using keyword "REPORT"')
            # print('Please enter the name of this file')
            # outerbilledfile = input().strip()
            # outerbilledstats = getbilledstats(outerbilledfile)
            # print('Please copy the latest cloudwatch logs for innerFunction from location',locanames[j],'to a local file by selecting logs in raw format and filtering it using keyword "REPORT"')
            # print('Please enter the name of this file')
            # innerbilledfile = input().strip()
            # innerbilledstats = getbilledstats(innerbilledfile)
            # print('Please enter the name of the file to save the stats')
            # savefilename = input().strip()
            # savestats(savefilename, dblessstats, outerbilledstats, innerbilledstats)

            print('Taking stats with DB call')
            print('Press Enter to Continue')
            input()
            dbfullstats = collectstatspostdb(datalist, link, loca)
            print('Please copy the latest cloudwatch logs for outerFunction from location',locanames[i],'to a local file by selecting logs in raw format and filtering it using keyword "REPORT"')
            print('Please enter the name of this file')
            outerbilledfile = input().strip()
            outerbilledstats = getbilledstats(outerbilledfile)
            print('Please copy the latest cloudwatch logs for innerFunctionDB from location',locanames[j],'to a local file by selecting logs in raw format and filtering it using keyword "REPORT"')
            print('Please enter the name of this file')
            innerbilledfile = input().strip()
            innerbilledstats = getbilledstats(innerbilledfile)
            print('Please enter the name of the file to save the stats')
            savefilename = input().strip()
            savestatsdb(savefilename, dbfullstats, outerbilledstats, innerbilledstats)