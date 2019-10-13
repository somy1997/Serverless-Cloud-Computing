import sys

if __name__ == "__main__":
    
    f = open('cwlogsactualcall.txt','r')
    actual = []
    for line in f :
        actual += [int(line.split()[3])]
    f.close()
    
    f = open('cwlogsbilledinner.txt','r')
    billedinner = []
    for line in f :
        billedinner += [round(float(line.split()[4]))]
    f.close()

    f = open('cwlogsbilledouter.txt','r')
    billedouter = []
    for line in f :
        billedouter += [round(float(line.split()[4]))]
    f.close()

    f = open('nested.csv','w')
    f.write('Inner Function Billed (ms), Function call (ms), Outer Function Billed (ms)\n')
    for i in range(len(actual)) :
        f.write('%d,%d,%d\n'%(billedinner[i],actual[i],billedouter[i]))
    f.close()