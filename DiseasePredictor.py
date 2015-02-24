# CSCI 3202: Assignment 4
# DiseasePredictor.py
# Kara James, Joshua Weaver

# Joint of capital letters doesn't work

import node
import getopt
import sys

"""
Conditional probability
"""
def ConditionalProb(arg):
    #for setting our own order of arguments
    flip = False
    arg2 = ''
    # check for leading c,x,d; add to arg2
    if '~c' in arg[:2]:
        flip = True
        arg2+='c|'
    elif arg[:1] is 'c':
        arg2+='c|'
    elif '~x' in arg[:2]:
        flip = True
        print "Made it!"
        arg2+='x|'
    elif arg[:1] is 'x':
        arg2+='x|'
    elif '~d' in arg[:2]:
        flip = True
        arg2+='d|'
    elif arg[:1] is 'd':
        arg2+='d|'
    #x,d are left out, if we determine that they could be options we need to add here
    if '~s' in arg:
        arg2+='~s'
    elif 's' in arg:
        arg2+='s'
    if '~p' in arg:
        arg2+='~p'
    elif 'p' in arg:
        arg2+='p'
    if '~c' in arg and not(arg[:1] is 'c'):
        arg2+='~c'
    elif 'c' in arg and not(arg[:1] is 'c'):
        arg2+='c'
    if '~d' in arg and not(arg[:1] is 'd'):
        arg2+='~d'
    elif 'd' in arg and not(arg[:1] is 'd'):
        arg2+='d'
    if '~x' in arg and not(arg[:1] is 'x'):
        arg2+='~x'
    elif 'x' in arg and not(arg[:1] is 'x'):
        arg2+='x'
    print 'Arg2', arg2
    results = { 'c|s' : (table[0][0]+table[0][1]+table[0][2]+table[0][3]+table[2][0]+table[2][1]+table[2][2]+table[2][3])/(Smoker.probabilities),
                'c|sp' : Cancer.probabilities['LT'],
                'c|s~p' : Cancer.probabilities['HT'],
                'c|~s' : (table[1][0]+table[1][1]+table[1][2]+table[1][3]+table[3][0]+table[3][1]+table[3][2]+table[3][3])/(1-Smoker.probabilities),
                'c|~sp' : Cancer.probabilities['LF'],
                'c|~s~p' : Cancer.probabilities['HF'],
                'c|p' : (table[0][0]+table[1][0]+table[2][0]+table[3][0]+table[0][2]+table[1][2]+table[2][2]+table[3][2])/(Pollution.probabilities),
                'c|~p' : (table[0][1]+table[1][1]+table[2][1]+table[3][1]+table[0][3]+table[1][3]+table[2][3]+table[3][3])/(1-Pollution.probabilities),
                'c|d' : 0,
                'c|dx' : 0,
                'c|~d' : 0,
                'c|~dx' : 0,
                'c|x' : 0,
                'c|~x' : 0,
                'c|sd' : 0,
                'c|spd' : 0,
                'c|s~pd' : 0,
                'c|~sd' : 0,
                'c|~spd' : 0,
                'c|~s~pd' : 0,
                'c|pd' : 0,
                'c|~pd' : 0,
                'c|s~d' : 0,
                'c|sp~d' : 0,
                'c|s~p~d' : 0,
                'c|~s~d' : 0,
                'c|~sp~d' : 0,
                'c|~s~p~d' : 0,
                'c|p~d' : 0,
                'c|~p~d' : 0,
                'c|sx' : 0,
                'c|spx' : 0,
                'c|s~px' : 0,
                'c|~sx' : 0,
                'c|~spx' : 0,
                'c|~s~px' : 0,
                'c|px' : 0,
                'c|~px' : 0,
                'c|s~x' : 0,
                'c|sp~x' : 0,
                'c|s~p~x' : 0,
                'c|~s~x' : 0,
                'c|~sp~x' : 0,
                'c|~s~p~x' : 0,
                'c|p~x' : 0,
                'c|~p~x' : 0,
                'x|s' : (table[0][0]+table[0][1]+table[0][2]+table[0][3]+table[0][4]+table[0][5]+table[0][6]+table[0][7])/(Smoker.probabilities),
                'x|~s' : (table[1][0]+table[1][1]+table[1][2]+table[1][3]+table[1][4]+table[1][5]+table[1][6]+table[1][7])/(1-Smoker.probabilities),
                'x|sp' : (table[0][0]+table[0][2]+table[0][4]+table[0][6])/(table[0][0]+table[0][2]+table[0][4]+table[0][6]+table[2][0]+table[2][2]+table[2][4]+table[2][6]),
                'x|s~p' : (table[0][1]+table[0][3]+table[0][5]+table[0][7])/(table[0][1]+table[0][3]+table[0][5]+table[0][7]+table[2][1]+table[2][3]+table[2][5]+table[2][7]),
                'x|~sp' : (table[1][0]+table[1][2]+table[1][4]+table[1][6])/(table[1][0]+table[1][2]+table[1][4]+table[1][6]+table[3][0]+table[3][2]+table[3][4]+table[3][6]),
                'x|~s~p' : (table[1][1]+table[1][3]+table[1][5]+table[1][7])/(table[1][1]+table[1][3]+table[1][5]+table[1][7]+table[3][1]+table[3][3]+table[3][5]+table[3][7]),
                'x|sc' : Xray.probabilities['True'],
                'x|s~c' : Xray.probabilities['False'],
                'x|~sc' : Xray.probabilities['True'],
                'x|~s~c' : (table[1][4]+table[1][5]+table[1][6]+table[1][7])/(table[1][4]+table[1][5]+table[1][6]+table[1][7]+table[3][4]+table[3][5]+table[3][6]+table[3][7]),
                'x|spc' : Xray.probabilities['True'],
                'x|sp~c' : Xray.probabilities['False'],
                'x|s~pc' : Xray.probabilities['True'],
                'x|~spc' : Xray.probabilities['True'],
                'x|~s~pc' : Xray.probabilities['True'],
                'x|~sp~c' : Xray.probabilities['False'],
                'x|s~p~c' : Xray.probabilities['False'],
                'x|~s~p~c' : Xray.probabilities['False'],
                'x|p' : (table[0][0]+table[1][0]+table[0][2]+table[1][2]+table[0][4]+table[1][4]+table[0][6]+table[1][6])/(Pollution.probabilities),
                'x|~p' : (table[0][1]+table[1][1]+table[0][3]+table[1][3]+table[0][5]+table[1][5]+table[0][7]+table[1][7])/(1-Pollution.probabilities),
                'x|pc' : Xray.probabilities['True'],
                'x|~pc' : Xray.probabilities['True'],
                'x|p~c' : Xray.probabilities['False'],
                'x|~p~c' : Xray.probabilities['False'],
                'x|c' : Xray.probabilities['True'],
                'x|~c' : Xray.probabilities['False'],
                #BELOW IS INCORRECT
                'x|sd' : (table[0][0]+table[0][1]+table[0][2]+table[0][3]+table[0][4]+table[0][5]+table[0][6]+table[0][7])/(Smoker.probabilities),
                'x|~sd' : (table[1][0]+table[1][1]+table[1][2]+table[1][3]+table[1][4]+table[1][5]+table[1][6]+table[1][7])/(1-Smoker.probabilities),
                'x|spd' : (table[0][0]+table[0][2]+table[0][4]+table[0][6])/(table[0][0]+table[0][2]+table[0][4]+table[0][6]+table[2][0]+table[2][2]+table[2][4]+table[2][6]),
                'x|s~pd' : (table[0][1]+table[0][3]+table[0][5]+table[0][7])/(table[0][1]+table[0][3]+table[0][5]+table[0][7]+table[2][1]+table[2][3]+table[2][5]+table[2][7]),
                'x|~spd' : (table[1][0]+table[1][2]+table[1][4]+table[1][6])/(table[1][0]+table[1][2]+table[1][4]+table[1][6]+table[3][0]+table[3][2]+table[3][4]+table[3][6]),
                'x|~s~pd' : (table[1][1]+table[1][3]+table[1][5]+table[1][7])/(table[1][1]+table[1][3]+table[1][5]+table[1][7]+table[3][1]+table[3][3]+table[3][5]+table[3][7]),
                'x|scd' : Xray.probabilities['True'],
                'x|s~cd' : Xray.probabilities['False'],
                'x|~scd' : Xray.probabilities['True'],
                'x|~s~cd' : (table[1][4]+table[1][5]+table[1][6]+table[1][7])/(table[1][4]+table[1][5]+table[1][6]+table[1][7]+table[3][4]+table[3][5]+table[3][6]+table[3][7]),
                'x|spcd' : Xray.probabilities['True'],
                'x|sp~cd' : Xray.probabilities['False'],
                'x|s~pcd' : Xray.probabilities['True'],
                'x|~spcd' : Xray.probabilities['True'],
                'x|~s~pcd' : Xray.probabilities['True'],
                'x|~sp~cd' : Xray.probabilities['False'],
                'x|s~p~cd' : Xray.probabilities['False'],
                'x|~s~p~cd' : Xray.probabilities['False'],
                'x|pd' : (table[0][0]+table[1][0]+table[0][2]+table[1][2]+table[0][4]+table[1][4]+table[0][6]+table[1][6])/(Pollution.probabilities),
                'x|~pd' : (table[0][1]+table[1][1]+table[0][3]+table[1][3]+table[0][5]+table[1][5]+table[0][7]+table[1][7])/(1-Pollution.probabilities),
                'x|pcd' : Xray.probabilities['True'],
                'x|~pcd' : Xray.probabilities['True'],
                'x|p~cd' : Xray.probabilities['False'],
                'x|~p~cd' : Xray.probabilities['False'],
                'x|cd' : Xray.probabilities['True'],
                'x|~cd' : Xray.probabilities['False'],
                'x|s~d' : (table[0][0]+table[0][1]+table[0][2]+table[0][3]+table[0][4]+table[0][5]+table[0][6]+table[0][7])/(Smoker.probabilities),
                'x|~s~d' : (table[1][0]+table[1][1]+table[1][2]+table[1][3]+table[1][4]+table[1][5]+table[1][6]+table[1][7])/(1-Smoker.probabilities),
                'x|sp~d' : (table[0][0]+table[0][2]+table[0][4]+table[0][6])/(table[0][0]+table[0][2]+table[0][4]+table[0][6]+table[2][0]+table[2][2]+table[2][4]+table[2][6]),
                'x|s~p~d' : (table[0][1]+table[0][3]+table[0][5]+table[0][7])/(table[0][1]+table[0][3]+table[0][5]+table[0][7]+table[2][1]+table[2][3]+table[2][5]+table[2][7]),
                'x|~sp~d' : (table[1][0]+table[1][2]+table[1][4]+table[1][6])/(table[1][0]+table[1][2]+table[1][4]+table[1][6]+table[3][0]+table[3][2]+table[3][4]+table[3][6]),
                'x|~s~p~d' : (table[1][1]+table[1][3]+table[1][5]+table[1][7])/(table[1][1]+table[1][3]+table[1][5]+table[1][7]+table[3][1]+table[3][3]+table[3][5]+table[3][7]),
                'x|sc~d' : Xray.probabilities['True'],
                'x|s~c~d' : Xray.probabilities['False'],
                'x|~sc~d' : Xray.probabilities['True'],
                'x|~s~c~d' : (table[1][4]+table[1][5]+table[1][6]+table[1][7])/(table[1][4]+table[1][5]+table[1][6]+table[1][7]+table[3][4]+table[3][5]+table[3][6]+table[3][7]),
                'x|spc~d' : Xray.probabilities['True'],
                'x|sp~c~d' : Xray.probabilities['False'],
                'x|s~pc~d' : Xray.probabilities['True'],
                'x|~spc~d' : Xray.probabilities['True'],
                'x|~s~pc~d' : Xray.probabilities['True'],
                'x|~sp~c~d' : Xray.probabilities['False'],
                'x|s~p~c~d' : Xray.probabilities['False'],
                'x|~s~p~c~d' : Xray.probabilities['False'],
                'x|p~d' : (table[0][0]+table[1][0]+table[0][2]+table[1][2]+table[0][4]+table[1][4]+table[0][6]+table[1][6])/(Pollution.probabilities),
                'x|~p~d' : (table[0][1]+table[1][1]+table[0][3]+table[1][3]+table[0][5]+table[1][5]+table[0][7]+table[1][7])/(1-Pollution.probabilities),
                'x|pc~d' : Xray.probabilities['True'],
                'x|~pc~d' : Xray.probabilities['True'],
                'x|p~c~d' : Xray.probabilities['False'],
                'x|~p~c~d' : Xray.probabilities['False'],
                'x|c~d' : Xray.probabilities['True'],
                'x|~c~d' : Xray.probabilities['False'],
                #BELOW IS CORRECT
                'd|s' : (table[0][0]+table[0][1]+table[0][4]+table[0][5]+table[2][0]+table[2][1]+table[2][4]+table[2][5])/(Smoker.probabilities),
                'd|~s' : (table[1][0]+table[1][1]+table[1][4]+table[1][5]+table[3][0]+table[3][1]+table[3][4]+table[3][5])/(1-Smoker.probabilities),
                'd|sp' : (table[0][0]+table[0][4]+table[2][0]+table[2][4])/(table[0][0]+table[0][2]+table[0][4]+table[0][6]+table[2][0]+table[2][2]+table[2][4]+table[2][6]),
                'd|s~p' : (table[0][1]+table[0][5]+table[2][1]+table[2][5])/(table[0][1]+table[0][3]+table[0][5]+table[0][7]+table[2][1]+table[2][3]+table[2][5]+table[2][7]),
                'd|~sp' : (table[1][0]+table[1][4]+table[3][0]+table[3][4])/(table[1][0]+table[1][2]+table[1][4]+table[1][6]+table[3][0]+table[3][2]+table[3][4]+table[3][6]),
                'd|~s~p' : (table[1][1]+table[1][5]+table[3][1]+table[3][5])/(table[1][1]+table[1][3]+table[1][5]+table[1][7]+table[3][1]+table[3][3]+table[3][5]+table[3][7]),
                'd|sc' : Dyspnoea.probabilities['True'],
                'd|s~c' : Dyspnoea.probabilities['False'],
                'd|~sc' : Dyspnoea.probabilities['True'],
                'd|~s~c' : Dyspnoea.probabilities['False'],
                'd|spc' : Dyspnoea.probabilities['True'],
                'd|sp~c' : Dyspnoea.probabilities['False'],
                'd|s~pc' : Dyspnoea.probabilities['True'],
                'd|~spc' : Dyspnoea.probabilities['True'],
                'd|~s~pc' : Dyspnoea.probabilities['True'],
                'd|~sp~c' : Dyspnoea.probabilities['False'],
                'd|s~p~c' : Dyspnoea.probabilities['False'],
                'd|~s~p~c' : Dyspnoea.probabilities['False'],
                'd|p' : (table[0][0]+table[1][0]+table[2][0]+table[3][0]+table[0][4]+table[1][4]+table[2][4]+table[3][4])/(Pollution.probabilities),
                'd|~p' : (table[0][1]+table[1][1]+table[2][1]+table[3][1]+table[0][5]+table[1][5]+table[2][5]+table[3][5])/(1-Pollution.probabilities),
                'd|pc' : Dyspnoea.probabilities['True'],
                'd|~pc' : Dyspnoea.probabilities['True'],
                'd|p~c' : Dyspnoea.probabilities['False'],
                'd|~p~c' : Dyspnoea.probabilities['False'],
                'd|c' : Dyspnoea.probabilities['True'],
                'd|~c' : Dyspnoea.probabilities['False'],
                #BELOW IS INCORRECT
                'd|sx' : (table[0][0]+table[0][1]+table[0][4]+table[0][5]+table[2][0]+table[2][1]+table[2][4]+table[2][5])/(Smoker.probabilities),
                'd|~sx' : (table[1][0]+table[1][1]+table[1][4]+table[1][5]+table[3][0]+table[3][1]+table[3][4]+table[3][5])/(1-Smoker.probabilities),
                'd|spx' : (table[0][0]+table[0][4]+table[2][0]+table[2][4])/(table[0][0]+table[0][2]+table[0][4]+table[0][6]+table[2][0]+table[2][2]+table[2][4]+table[2][6]),
                'd|s~px' : (table[0][1]+table[0][5]+table[2][1]+table[2][5])/(table[0][1]+table[0][3]+table[0][5]+table[0][7]+table[2][1]+table[2][3]+table[2][5]+table[2][7]),
                'd|~spx' : (table[1][0]+table[1][4]+table[3][0]+table[3][4])/(table[1][0]+table[1][2]+table[1][4]+table[1][6]+table[3][0]+table[3][2]+table[3][4]+table[3][6]),
                'd|~s~px' : (table[1][1]+table[1][5]+table[3][1]+table[3][5])/(table[1][1]+table[1][3]+table[1][5]+table[1][7]+table[3][1]+table[3][3]+table[3][5]+table[3][7]),
                'd|scx' : Dyspnoea.probabilities['True'],
                'd|s~cx' : Dyspnoea.probabilities['False'],
                'd|~scx' : Dyspnoea.probabilities['True'],
                'd|~s~cx' : Dyspnoea.probabilities['False'],
                'd|spcx' : Dyspnoea.probabilities['True'],
                'd|sp~cx' : Dyspnoea.probabilities['False'],
                'd|s~pcx' : Dyspnoea.probabilities['True'],
                'd|~spcx' : Dyspnoea.probabilities['True'],
                'd|~s~pcx' : Dyspnoea.probabilities['True'],
                'd|~sp~cx' : Dyspnoea.probabilities['False'],
                'd|s~p~cx' : Dyspnoea.probabilities['False'],
                'd|~s~p~cx' : Dyspnoea.probabilities['False'],
                'd|px' : (table[0][0]+table[1][0]+table[2][0]+table[3][0]+table[0][4]+table[1][4]+table[2][4]+table[3][4])/(Pollution.probabilities),
                'd|~px' : (table[0][1]+table[1][1]+table[2][1]+table[3][1]+table[0][5]+table[1][5]+table[2][5]+table[3][5])/(1-Pollution.probabilities),
                'd|pcx' : Dyspnoea.probabilities['True'],
                'd|~pcx' : Dyspnoea.probabilities['True'],
                'd|p~cx' : Dyspnoea.probabilities['False'],
                'd|~p~cx' : Dyspnoea.probabilities['False'],
                'd|cx' : Dyspnoea.probabilities['True'],
                'd|~cx' : Dyspnoea.probabilities['False'],
                'd|s~x' : (table[0][0]+table[0][1]+table[0][4]+table[0][5]+table[2][0]+table[2][1]+table[2][4]+table[2][5])/(Smoker.probabilities),
                'd|~s~x' : (table[1][0]+table[1][1]+table[1][4]+table[1][5]+table[3][0]+table[3][1]+table[3][4]+table[3][5])/(1-Smoker.probabilities),
                'd|sp~x' : (table[0][0]+table[0][4]+table[2][0]+table[2][4])/(table[0][0]+table[0][2]+table[0][4]+table[0][6]+table[2][0]+table[2][2]+table[2][4]+table[2][6]),
                'd|s~p~x' : (table[0][1]+table[0][5]+table[2][1]+table[2][5])/(table[0][1]+table[0][3]+table[0][5]+table[0][7]+table[2][1]+table[2][3]+table[2][5]+table[2][7]),
                'd|~sp~x' : (table[1][0]+table[1][4]+table[3][0]+table[3][4])/(table[1][0]+table[1][2]+table[1][4]+table[1][6]+table[3][0]+table[3][2]+table[3][4]+table[3][6]),
                'd|~s~p~x' : (table[1][1]+table[1][5]+table[3][1]+table[3][5])/(table[1][1]+table[1][3]+table[1][5]+table[1][7]+table[3][1]+table[3][3]+table[3][5]+table[3][7]),
                'd|sc~x' : Dyspnoea.probabilities['True'],
                'd|s~c~x' : Dyspnoea.probabilities['False'],
                'd|~sc~x' : Dyspnoea.probabilities['True'],
                'd|~s~c~x' : Dyspnoea.probabilities['False'],
                'd|spc~x' : Dyspnoea.probabilities['True'],
                'd|sp~c~x' : Dyspnoea.probabilities['False'],
                'd|s~pc~x' : Dyspnoea.probabilities['True'],
                'd|~spc~x' : Dyspnoea.probabilities['True'],
                'd|~s~pc~x' : Dyspnoea.probabilities['True'],
                'd|~sp~c~x' : Dyspnoea.probabilities['False'],
                'd|s~p~c~x' : Dyspnoea.probabilities['False'],
                'd|~s~p~c~x' : Dyspnoea.probabilities['False'],
                'd|p~x' : (table[0][0]+table[1][0]+table[2][0]+table[3][0]+table[0][4]+table[1][4]+table[2][4]+table[3][4])/(Pollution.probabilities),
                'd|~p~x' : (table[0][1]+table[1][1]+table[2][1]+table[3][1]+table[0][5]+table[1][5]+table[2][5]+table[3][5])/(1-Pollution.probabilities),
                'd|pc~x' : Dyspnoea.probabilities['True'],
                'd|~pc~x' : Dyspnoea.probabilities['True'],
                'd|p~c~x' : Dyspnoea.probabilities['False'],
                'd|~p~c~x' : Dyspnoea.probabilities['False'],
                'd|c~x' : Dyspnoea.probabilities['True'],
                'd|~c~x' : Dyspnoea.probabilities['False'],
    }
    if flip==True:
        result = 1-results[arg2]
    else:
        result = results[arg2]
    print result

"""
Joint Probability
"""
def JointProb(arg):
    product = 1
    p = 'N'
    s = 'N'
    c = 'N'
    if '~p' in arg:
        p = 'H'
        product *= 1 - Pollution.probabilities
    elif 'p' in arg:
        p = 'L'
        product *= Pollution.probabilities
    if '~s' in arg:
        s = 'F'
        product *= 1 - Smoker.probabilities
    elif 's' in arg:
        s = 'T'
        product *= Smoker.probabilities
    if '~c' in arg:
        c = 'F'
        if (p=='H' and s=='T'):
            product *= (1-Cancer.probabilities["HT"])
        elif (p=='H' and s=='F'):
            product *= (1-Cancer.probabilities["HF"])
        elif (p=='L' and s=='T'):
            product *= (1-Cancer.probabilities["LT"])
        elif (p=='L' and s=='F'):
            product *= (1-Cancer.probabilities["LF"])
        elif (p=='H' and s=='N'):
            product *= ((1-Cancer.probabilities["HT"]) + (1-Cancer.probabilities["HF"]))
        elif (p=='L' and s=='N'):
            product *= ((1-Cancer.probabilities["LT"]) + (1-Cancer.probabilities["LF"]))
        elif (p=='N' and s=='T'):
            product *= ((1-Cancer.probabilities["HT"]) + (1-Cancer.probabilities["LT"]))
        elif (p=='N' and s=='F'):
            product *= ((1-Cancer.probabilities["HF"]) + (1-Cancer.probabilities["LF"]))
        elif (p=='N' and s=='N'):
            product *= ((1-Cancer.probabilities["HF"]) + (1-Cancer.probabilities["LF"]) + (1-Cancer.probabilities["HT"]) + (1-Cancer.probabilities["LT"]))
    elif 'c' in arg:
        c = 'T'
        if (p=='H' and s=='T'):
            product *= Cancer.probabilities["HT"]
        elif (p=='H' and s=='F'):
            product *= Cancer.probabilities["HF"]
        elif (p=='L' and s=='T'):
            product *= Cancer.probabilities["LT"]
        elif (p=='L' and s=='F'):
            product *= Cancer.probabilities["LF"]
        elif (p=='H' and s=='N'):
            product *= (Cancer.probabilities["HT"]+Cancer.probabilities["HF"])
        elif (p=='L' and s=='N'):
            product *= (Cancer.probabilities["LT"]+Cancer.probabilities["LF"])
        elif (p=='N' and s=='T'):
            product *= (Cancer.probabilities["HT"]+Cancer.probabilities["LT"])
        elif (p=='N' and s=='F'):
            product *= (Cancer.probabilities["HF"]+Cancer.probabilities["LF"])
        elif (p=='N' and s=='N'):
            product *= (Cancer.probabilities["HF"]+Cancer.probabilities["LF"]+Cancer.probabilities["HT"]+Cancer.probabilities["LT"])
    if '~x' in arg:
        if c=='T':
            product *= (1-Xray.probabilities['True'])
        elif c=='F':
            product *= (1-Xray.probabilities['False'])
    elif 'x' in arg:
        if c=='T':
            product *= Xray.probabilities['True']
        elif c=='F':
            product *= Xray.probabilities['False']
    if '~d' in arg:
        if c=='T':
            product *= (1-Dyspnoea.probabilities['True'])
        elif c=='F':
            product *= (1-Dyspnoea.probabilities['False'])
    elif 'd' in arg:
        if c=='T':
            product *= Dyspnoea.probabilities['True']
        elif c=='F':
            product *= Dyspnoea.probabilities['False']
    if 'C' in arg or 'D' in arg or 'X' in arg or 'S' in arg or 'P' in arg:
        arg1 = ''
        if 'C' in arg:
            arg1+='c'
        if 'D' in arg:
            arg1+='d'
        if 'X' in arg:
            arg1+='x'
        if 'S' in arg:
            arg1+='s'
        if 'P' in arg:
            arg1+='p'
        print "Arg1:", arg1
        product = JointProb(arg1)
    return product

"""
Marginal Probability
"""
def MarginalProb(arg):
    #Uppercase marginal: will return two numbers, 
        #one for y and one for ~y
    if 'S' in arg:
        #Sum for s
        sums = 0
        #First column
        sums+=table[0][0]+table[0][1]+table[0][2]+table[0][3]+table[0][4]+table[0][5]+table[0][6]+table[0][7]
        #Second column
        sums+=table[2][0]+table[2][1]+table[2][2]+table[2][3]+table[2][4]+table[2][5]+table[2][6]+table[2][7]
        #Sum for ~s
        sumns = 0
        #First column
        sumns+=table[1][0]+table[1][1]+table[1][2]+table[1][3]+table[1][4]+table[1][5]+table[1][6]+table[1][7]
        #Second column
        sumns+=table[3][0]+table[3][1]+table[3][2]+table[3][3]+table[3][4]+table[3][5]+table[3][6]+table[3][7]
        print "S P(s=S)"
        print "T", sums
        print "F", sumns
    if 'P' in arg:
        #Sum for p
        sump = 0
        #First two rows
        sump+=table[0][0]+table[1][0]+table[2][0]+table[3][0]
        sump+=table[0][2]+table[1][2]+table[2][2]+table[3][2]
        #Second two rows
        sump+=table[0][4]+table[1][4]+table[2][4]+table[3][4]
        sump+=table[0][6]+table[1][6]+table[2][6]+table[3][6]
        #Sum for ~p
        sumnp = 0
        #First two rows
        sumnp+=table[0][1]+table[1][1]+table[2][1]+table[3][1]
        sumnp+=table[0][3]+table[1][3]+table[2][3]+table[3][3]
        #Second two rows
        sumnp+=table[0][5]+table[1][5]+table[2][5]+table[3][5]
        sumnp+=table[0][7]+table[1][7]+table[2][7]+table[3][7]
        print "P P(p=P)"
        print "T", sump
        print "F", sumnp
    if 'C' in arg:
        #Sum for c
        sumc = 0
        #Four rows
        sumc+=table[0][0]+table[1][0]+table[2][0]+table[3][0]
        sumc+=table[0][1]+table[1][1]+table[2][1]+table[3][1]
        sumc+=table[0][2]+table[1][2]+table[2][2]+table[3][2]
        sumc+=table[0][3]+table[1][3]+table[2][3]+table[3][3]
        #Sum for ~c
        sumnc = 0
        #Four rows
        sumnc+=table[0][4]+table[1][4]+table[2][4]+table[3][4]
        sumnc+=table[0][5]+table[1][5]+table[2][5]+table[3][5]
        sumnc+=table[0][6]+table[1][6]+table[2][6]+table[3][6]
        sumnc+=table[0][7]+table[1][7]+table[2][7]+table[3][7]
        print "C P(c=C)"
        print "T", sumc
        print "F", sumnc
    if 'X' in arg:
        #Sum for x
        sumx = 0
        #First column
        sumx+=table[0][0]+table[0][1]+table[0][2]+table[0][3]+table[0][4]+table[0][5]+table[0][6]+table[0][7]
        #Second column
        sumx+=table[1][0]+table[1][1]+table[1][2]+table[1][3]+table[1][4]+table[1][5]+table[1][6]+table[1][7]
        #Sum for ~x
        sumnx = 0
        #First column
        sumnx+=table[2][0]+table[2][1]+table[2][2]+table[2][3]+table[2][4]+table[2][5]+table[2][6]+table[2][7]
        #Second column
        sumnx+=table[3][0]+table[3][1]+table[3][2]+table[3][3]+table[3][4]+table[3][5]+table[3][6]+table[3][7]
        print "X P(x=X)"
        print "T", sumx
        print "F", sumnx
    if 'D' in arg:
        #Sum for d
        sumd = 0
        #First two rows
        sumd+=table[0][0]+table[1][0]+table[2][0]+table[3][0]
        sumd+=table[0][1]+table[1][1]+table[2][1]+table[3][1]
        #Second two rows
        sumd+=table[0][4]+table[1][4]+table[2][4]+table[3][4]
        sumd+=table[0][5]+table[1][5]+table[2][5]+table[3][5]
        #Sum for ~d
        sumnd = 0
        #First two rows
        sumnd+=table[0][2]+table[1][2]+table[2][2]+table[3][2]
        sumnd+=table[0][3]+table[1][3]+table[2][3]+table[3][3]
        #Second two rows
        sumnd+=table[0][6]+table[1][6]+table[2][6]+table[3][6]
        sumnd+=table[0][7]+table[1][7]+table[2][7]+table[3][7]
        print "D P(d=D)"
        print "T", sumd
        print "F", sumnd
    #Lowercase marginal; will return a single number
    if '~s' in arg:
        #Sum for ~s
        sumns = 0
        #First column
        sumns+=table[1][0]+table[1][1]+table[1][2]+table[1][3]+table[1][4]+table[1][5]+table[1][6]+table[1][7]
        #Second column
        sumns+=table[3][0]+table[3][1]+table[3][2]+table[3][3]+table[3][4]+table[3][5]+table[3][6]+table[3][7]
        print "Marginal Probability for ~s:"
        print "~s=", sumns
    elif 's' in arg:
        #Sum for s
        sums = 0
        #First column
        sums+=table[0][0]+table[0][1]+table[0][2]+table[0][3]+table[0][4]+table[0][5]+table[0][6]+table[0][7]
        #Second column
        sums+=table[2][0]+table[2][1]+table[2][2]+table[2][3]+table[2][4]+table[2][5]+table[2][6]+table[2][7]
        print "Marginal Probability for s:"
        print "s=", sums
    if '~p' in arg:
        #Sum for ~p
        sumnp = 0
        #First two rows
        sumnp+=table[0][1]+table[1][1]+table[2][1]+table[3][1]
        sumnp+=table[0][3]+table[1][3]+table[2][3]+table[3][3]
        #Second two rows
        sumnp+=table[0][5]+table[1][5]+table[2][5]+table[3][5]
        sumnp+=table[0][7]+table[1][7]+table[2][7]+table[3][7]
        print "Marginal Probability for ~p:"
        print "~p=", sumnp
    elif 'p' in arg:
        #Sum for p
        sump = 0
        #First two rows
        sump+=table[0][0]+table[1][0]+table[2][0]+table[3][0]
        sump+=table[0][2]+table[1][2]+table[2][2]+table[3][2]
        #Second two rows
        sump+=table[0][4]+table[1][4]+table[2][4]+table[3][4]
        sump+=table[0][6]+table[1][6]+table[2][6]+table[3][6]
        print "Marginal Probability for p:"
        print "p=", sump
    if '~c' in arg:
        #Sum for ~c
        sumnc = 0
        #Four rows
        sumnc+=table[0][4]+table[1][4]+table[2][4]+table[3][4]
        sumnc+=table[0][5]+table[1][5]+table[2][5]+table[3][5]
        sumnc+=table[0][6]+table[1][6]+table[2][6]+table[3][6]
        sumnc+=table[0][7]+table[1][7]+table[2][7]+table[3][7]
        print "Marginal Probability for ~c:"
        print "~c=", sumnc
    elif 'c' in arg:
        #Sum for c
        sumc = 0
        #Four rows
        sumc+=table[0][0]+table[1][0]+table[2][0]+table[3][0]
        sumc+=table[0][1]+table[1][1]+table[2][1]+table[3][1]
        sumc+=table[0][2]+table[1][2]+table[2][2]+table[3][2]
        sumc+=table[0][3]+table[1][3]+table[2][3]+table[3][3]
        print "Marginal Probability for c:"
        print "c=", sumc
    if '~x' in arg:
        #Sum for ~x
        sumnx = 0
        #First column
        sumnx+=table[2][0]+table[2][1]+table[2][2]+table[2][3]+table[2][4]+table[2][5]+table[2][6]+table[2][7]
        #Second column
        sumnx+=table[3][0]+table[3][1]+table[3][2]+table[3][3]+table[3][4]+table[3][5]+table[3][6]+table[3][7]
        print "Marginal Probability for ~x:"
        print "~x=", sumnx
    elif 'x' in arg:
        #Sum for x
        sumx = 0
        #First column
        sumx+=table[0][0]+table[0][1]+table[0][2]+table[0][3]+table[0][4]+table[0][5]+table[0][6]+table[0][7]
        #Second column
        sumx+=table[1][0]+table[1][1]+table[1][2]+table[1][3]+table[1][4]+table[1][5]+table[1][6]+table[1][7]
        print "Marginal Probability for x:"
        print "x=", sumx
    if '~d' in arg:
        #Sum for ~d
        sumnd = 0
        #First two rows
        sumnd+=table[0][2]+table[1][2]+table[2][2]+table[3][2]
        sumnd+=table[0][3]+table[1][3]+table[2][3]+table[3][3]
        #Second two rows
        sumnd+=table[0][6]+table[1][6]+table[2][6]+table[3][6]
        sumnd+=table[0][7]+table[1][7]+table[2][7]+table[3][7]
        print "Marginal Probability for ~d:"
        print "~d=", sumnd
    elif 'd' in arg:
        #Sum for d
        sumd = 0
        #First two rows
        sumd+=table[0][0]+table[1][0]+table[2][0]+table[3][0]
        sumd+=table[0][1]+table[1][1]+table[2][1]+table[3][1]
        #Second two rows
        sumd+=table[0][4]+table[1][4]+table[2][4]+table[3][4]
        sumd+=table[0][5]+table[1][5]+table[2][5]+table[3][5]
        print "Marginal Probability for d:"
        print "d=", sumd

"""
Create the nodes in the Bayes Net
"""
Pollution = node.make_node("N", .9)

Smoker = node.make_node("N", .3)

dictc = {'HT': .05, 'HF': .02, 'LT': .03, 'LF': .001}
Cancer = node.make_node(("P","S"), dictc)

dictx = {'True': .9, 'False': .2}
Xray = node.make_node("C", dictx)

dictd = {'True': .65, 'False': .3}
Dyspnoea = node.make_node("C", dictd)

"""
Table Creation
"""
table = [[0 for x in xrange(8)] for x in xrange(4)]
 
table[0][0] = JointProb("spdxc")
table[1][0] = JointProb("~spdxc")
table[2][0] = JointProb("spd~xc")
table[3][0] = JointProb("~spd~xc")

table[0][1] = JointProb("s~pdxc")
table[1][1] = JointProb("~s~pdxc")
table[2][1] = JointProb("s~pd~xc")
table[3][1] = JointProb("~s~pd~xc")

table[0][2] = JointProb("sp~dxc")
table[1][2] = JointProb("~sp~dxc")
table[2][2] = JointProb("sp~d~xc")
table[3][2] = JointProb("~sp~d~xc")

table[0][3] = JointProb("s~p~dxc")
table[1][3] = JointProb("~s~p~dxc")
table[2][3] = JointProb("s~p~d~xc")
table[3][3] = JointProb("~s~p~d~xc")

table[0][4] = JointProb("spdx~c")
table[1][4] = JointProb("~spdx~c")
table[2][4] = JointProb("spd~x~c")
table[3][4] = JointProb("~spd~x~c")

table[0][5] = JointProb("s~pdx~c")
table[1][5] = JointProb("~s~pdx~c")
table[2][5] = JointProb("s~pd~x~c")
table[3][5] = JointProb("~s~pd~x~c")

table[0][6] = JointProb("sp~dx~c")
table[1][6] = JointProb("~sp~dx~c")
table[2][6] = JointProb("sp~d~x~c")
table[3][6] = JointProb("~sp~d~x~c")

table[0][7] = JointProb("s~p~dx~c")
table[1][7] = JointProb("~s~p~dx~c")
table[2][7] = JointProb("s~p~d~x~c")
table[3][7] = JointProb("~s~p~d~x~c")

#debug only, REMOVE for deployment
#for i in range(8):
#    for j in range(4):
#        sys.stdout.write(str(table[j][i]))
#        sys.stdout.write(" ")
#    print " "

option = ''
#print 'ARGV      :', sys.argv[1:] #debug only, REMOVE for deployment

options, remainder = getopt.getopt(sys.argv[1:], 'g:j:m:', 
                                                ['conditional',
                                                 'joint',
                                                 'marginal'])
#print 'OPTIONS   :', options #debug only, REMOVE for deployment

for opt, arg in options:
    if opt in ('-g'):
        option = arg
        ConditionalProb(arg)
        #print "Val: ", ConditionalProb(arg)  #text is for debug only, REMOVE for deployment
    elif opt in ('-j'):
        option = arg
        print JointProb(arg) #text is for debug only, REMOVE for deployment
    elif opt in ('-m'):
        option = arg
        MarginalProb(arg)

#debug only, REMOVE for deployment
#print 'REMAINING :', remainder #everything else/unexpected 
#print 'OPTION    :', option #options to the flag


