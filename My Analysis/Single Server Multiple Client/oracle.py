#!/usr/bin/env python3
# coding: utf-8

import requests
import statistics
import random
import names
import argparse # for parsing arguments https://docs.python.org/2/howto/argparse.html, https://docs.python.org/2/library/argparse.html
import string
import time
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

def collectstatspost(datalist,baseurl):
    print('Collecting stats by making post requests to',baseurl)
    if verbose :
        print()
    statslist = []
    i = 1
    for item in datalist :
        payload = {'EmailID':item[0], 'FirstName':item[1], 'LastName':item[2]}
        start = time.time()
        response=requests.post(baseurl,json=payload)
        end = time.time()
        if verbose :
            print('%03d'%(i)+'. ','Time Taken :',str(end-start)+'s Response :',response.text,'for',item)
        statslist += [int(response.text.split('$')[-1])]
        i += 1
    if verbose :
        print()
    return statslist

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
        statslist += [int(line)] 
        #round function returns type as int by default (decimal places to keep is 0) otherwise float
    f.close()
    if verbose :
        print()
    return statslist    

def savestats(filename, actualstats, billedstats) :
    print('Saving actual stats and billed stats in',filename)
    f = open(filename, 'w')
    f.write('Actual Time (ms),Billed Time (ms)\n')
    for (actualtime, billedtime) in zip(actualstats,billedstats):
        f.write("%d,%d\n"%(actualtime,billedtime))
    if verbose :
        print()
    f.close()

def saveactualstats(filename, actualstats) :
    print('Saving actual stats in',filename)
    f = open(filename, 'w')
    #f.write('Actual Time (ms)\n')
    for actualtime in actualstats:
        f.write("%d\n"%(actualtime))
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

if __name__ == "__main__":
    # Following options :
    # gen data : filename // where it is to be put, automatically calls loaddata
    # load data : filename // same as above but only loading data
    # make post calls : baseurlpost and filename where to put stats // for making post calls
    # parse post stats : filename of ^^ stats, filename for parsing cloudwatch logs
    # make get calls : baseurlget and filename where to put stats // for making get calls
    # parse get stats : filename of ^^ stats, filename for parsing cloudwatch logs
    parser = argparse.ArgumentParser(description='Oracle for doing everything')
    # argument for datafile
    parser.add_argument('datafile', type=str, help='File for loading or generating our dummy data')
    parser.add_argument('numvals', type=int, help='Number of values to be generated/loaded')
    parser.add_argument('-g', '--generate', type=int, help='To generate data, argument : random seed to generate data')
    parser.add_argument('-v', '--verbose', help='Increase output verbosity', action='store_true')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-mp', '--makepost', nargs=2, help='Make post calls, arguments : Filename for storing stats and URL for Post')
    group.add_argument('-pp', '--parsepost', nargs=2, help='Parse Post stats from Cloudwatch logs and output the stats, arguments : File from which to read URL response stats and File from which to read Cloudwatch logs (The cloudwatch logs must be copied to this file first). The new stats would be copied to the 1st file in the argument.')
    group.add_argument('-mg', '--makeget', nargs=2, help='Make get calls, arguments : Filename for storing stats and URL for Get')
    group.add_argument('-pg', '--parseget', nargs=2, help='Parse Get stats from Cloudwatch logs and output the stats, arguments : File from which to read URL response stats and File from which to read Cloudwatch logs (The cloudwatch logs must be copied to this file first). The new stats would be copied to the 1st file in the argument.')
    args = parser.parse_args()
    
    global verbose
    verbose = args.verbose
    
    if args.generate :
        gendata(args.datafile, args.numvals, args.generate)
    
    global datalist
    datalist = loaddata(args.datafile, args.numvals)
    
    if args.makepost :
        baseurlpost = args.makepost[1]
        actualstatslistpost = collectstatspost(datalist, baseurlpost)
        actualstatsfilepost = args.makepost[0]
        saveactualstats(actualstatsfilepost, actualstatslistpost)
        print('Actual stats saved successfully in',actualstatsfilepost)
    
    if args.parsepost :
        actualstatsfilepost = args.parsepost[0]
        actualstatslistpost = getactualstats(actualstatsfilepost)
        billedlogsfilepost = args.parsepost[1]
        billedstatslistpost = getbilledstats(billedlogsfilepost)
        savestatsfilepost = actualstatsfilepost
        savestats(savestatsfilepost,actualstatslistpost,billedstatslistpost)
        print('All stats saved successfully in',savestatsfilepost)

    if args.makeget :
        baseurlget = args.makeget[1]
        actualstatslistget = collectstatsget(datalist, baseurlget)
        actualstatsfileget = args.makeget[0]
        saveactualstats(actualstatsfileget, actualstatslistget)
        print('Actual stats saved successfully in',actualstatsfileget)
    
    if args.parseget :
        actualstatsfileget = args.parseget[0]
        actualstatslistget = getactualstats(actualstatsfileget)
        billedlogsfileget = args.parseget[1]
        billedstatslistget = getbilledstats(billedlogsfileget)
        savestatsfileget = actualstatsfileget
        savestats(savestatsfileget,actualstatslistget,billedstatslistget)
        print('All stats saved successfully in',savestatsfileget)
    

