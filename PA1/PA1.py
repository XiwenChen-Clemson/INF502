#!/usr/bin/env python
# coding: utf-8

# # PA1: DNA Similarity
# ## Xiwen Chen xc53@nau.edu
# - This program provides two algorithm to compare seqences: Number Of Matchand MAXIMUM CONTIGUOUS CHAIN.
# - `PA1.py` is also provided in the folder for running directly.
# 

# ### Sequence Input 
# - Exception is `FileNotFoundError` for file input.
# - This function also check the sequence availablity: valied character, same length.

# In[5]:


def SequenceInput():
    Flag = 0
    Flag1 = 0
    Flag2 = 0
    while Flag == 0:
        while 1:
            try:
                FileNameA = input("Enter a sequence A file name:")
                fA = open('./'+FileNameA,"r")
            except FileNotFoundError:
                print("File A is not existed")
            else:
                try:
                    FileNameB = input("Enter a sequence B file name:")
                    fB = open('./'+FileNameB,"r")
                except FileNotFoundError:
                    print("File B is not existed")

                else:
                    SequenceA = fA.readline()
                    SequenceA.strip("\n")
                    fA.close()
                    SequenceB = fB.readline()
                    SequenceB.strip("\n")
                    fB.close()
                    break
                    
        for Char in SequenceA:
            if Char != 'A' and Char != 'G' and Char != 'C' and Char != 'T':
                print("Your sequence A has unavilable character! Please input again\n")
                Flag1 = 1
                break
                     
        for Char in SequenceB:
            if Char != 'A' and Char != 'G' and Char != 'C' and Char != 'T':
                print("Your sequence B has unavilable character! Please input again\n")
                Flag2 = 1
                break
                                          
        if len(SequenceA)==len(SequenceB) and Flag1 == 0 and Flag2 == 0:
            Flag = 1
            return SequenceA,SequenceB
        elif len(SequenceA)!=len(SequenceB):
            
            print("The sequences must have the same length! Please input again\n")
                


    


# ### Max Shift Bit input function
# - Input max shift bit. The exception is `MaxBit` not a non-negative integer. 

# In[6]:


def MaxShiftBitInput():
    while 1:
        try:
            print("We suggest that the number of your maximum shifted bits is no more than the greatest length of your sequence.\n ")
            MaxBit = input("please give a non-negative integer of the maximum shift bit:")
            MaxBit = int(MaxBit)
            if MaxBit<0:
                raise ValueError
        except ValueError:
            print("Please input a non-negative integer")
        else:
            break
    return MaxBit
    


# ### Shifting function
# - `-` before the string denotes the shifting operation. How many '-' means how many bits you shift.
# - e.g. `Shifting('ACGTTTA',3)` outputs `'---ACGTTTA'`

# In[7]:


def Shifting(Sequence,ShiftBits):
    NewSequence =list()
    for i in range(ShiftBits):
        NewSequence.append('-')
    for i in range(len(Sequence)):        
        NewSequence.append(Sequence[i])
    
    return ''.join(NewSequence)
    


# #### Testing for this function 

# In[8]:


Shifting('ACGTTTA',3)


# ### DNA NumberOfMatch Similarity 
# - We have two shifting scenories: shift A or shift B. **Ideally**, if we want to shift A, the maximum shift bis is `len(B)`; while shifting B, the  maximum shift bis is `len(A)`
# - Use `enumerate()` to return all indexes with maximu score
# - The function returns the max score, and two sequence after shifting processing. If one shifted sequence has more than one list return, it means all of them are optimal solutions. e.g. `NumberOfMatch('1AA','AAA',3)` The output is `(2, '1AA', ['AAA', '-AAA'])`, meaning that the max score is `2`, sequence A is not shifted, seqeucene to shifted by 0 or 1 can both achieve the best performance (which is 2). 
# - This function can compare different length sequence by setting up `MaxShiftBits_1` and `MaxShiftBits_2`.

# In[9]:


def NumberOfMatch(SequenceA,SequenceB,MaxShiftBits):
    
    ##MaxShiftBits_1 = len(SequenceB)+1
    ##MaxShiftBits_2 = len(SequenceA)+1
    Score_1 = list()
    Score_2 = list()
    
    for i in range(MaxShiftBits+1):
        Score_1.append(0)
        ShiftedA = Shifting(SequenceA,i)
        for j in range(min(len(ShiftedA),len(SequenceB))):            
            if ShiftedA[j]==SequenceB[j]:
                    Score_1[i]=Score_1[i]+1
    # Get the shifted string with max score by only shifting A
    index = [i for i,j in enumerate(Score_1) if j==max(Score_1)]
    ShiftedA = list()
    for i in index:
        ShiftedA.append(Shifting(SequenceA,i))
    
    #ShiftedA = Shifting(SequenceA,Score_1.index(max(Score_1)))               
                
                
    for i in range(MaxShiftBits+1):
        Score_2.append(0)
        ShiftedB = Shifting(SequenceB,i)
        for j in range(min(len(ShiftedB),len(SequenceA))):            
            if ShiftedB[j]==SequenceA[j]:
                    Score_2[i]=Score_2[i]+1
    # Get the shifted string with max score by only shifting A
    # Find the location of max score_2
    index = [i for i,j in enumerate(Score_2) if j==max(Score_2)]
    ShiftedB = list()
    for i in index:
        ShiftedB.append(Shifting(SequenceB,i))
    
    #ShiftedB = Shifting(SequenceB,Score_2.index(max(Score_2)))   
    
    
    if max(Score_1)>max(Score_2):
        ShiftedA = ShiftedA
        ShiftedB = []
        ShiftedB.append(SequenceB)
    else:
        ShiftedA = []
        ShiftedA.append(SequenceA)
        ShiftedB = ShiftedB
                    
                    
    Score = max(max(Score_1),max(Score_2))
    
    return Score, ShiftedA, ShiftedB
    
    
                
        
    


# #### Testing for the function

# In[10]:


NumberOfMatch('1AA','AAA',3)


# ### MaxChain
# - Similarly to algorithm `NumberOfMatch`, we have two shifting operations, for two sequence respectively.
# - To calculate max contiguous, we first label the each mathced bits, and store the signal into list `SubIndex`:`1` denotes matached, `''`denotes no matched. Then deploy `itertools.groupby()` to divide the list into group-level. Here each element of each group is adjacent and equal. Then the biggest length in all valied group can represent the max contiguous score.
# - Example is shown below. Also, like early mention, if the return of one sequence has more than one sequence, it means all these seuqneces are optimal solutions.

# In[11]:


import itertools


def MaxChain(SequenceA,SequenceB,MaxShiftBits):
    
    ##MaxShiftBits_1 = len(SequenceB)+1
    ##MaxShiftBits_2 = len(SequenceA)+1
    Score_1 = list()
    Score_2 = list()
    
    for i in range(MaxShiftBits+1):
        
        ShiftedA = Shifting(SequenceA,i)
        SubIndex = list()
        for j in range(min(len(ShiftedA),len(SequenceB))):            
            if ShiftedA[j]==SequenceB[j]:
                SubIndex.append(1)
            else:
                SubIndex.append('')
        SubScore = [0]
        for k,v in itertools.groupby(SubIndex):
            if k!='':
                SubScore.append(len(list(v)))
        Score_1.append(max(SubScore))
            
                
        
                    
                    
    # Get the shifted string with max score by only shifting A
    index = [i for i,j in enumerate(Score_1) if j==max(Score_1)]
    ShiftedA = list()
    for i in index:
        ShiftedA.append(Shifting(SequenceA,i))
        
                
                
                
    for i in range(MaxShiftBits+1):
        
        ShiftedB = Shifting(SequenceB,i)
        SubIndex = list()
        for j in range(min(len(ShiftedB),len(SequenceA))):            
            if ShiftedB[j]==SequenceA[j]:
                SubIndex.append(1)
            else:
                SubIndex.append('')
        SubScore = [0]
        for k,v in itertools.groupby(SubIndex):
            if k!='':
                SubScore.append(len(list(v)))
        Score_2.append(max(SubScore))
                    
                    
    # Get the shifted string with max score by only shifting A
    # Find the location of max score_2
    index = [i for i,j in enumerate(Score_2) if j==max(Score_2)]
    ShiftedB = list()
    for i in index:
        ShiftedB.append(Shifting(SequenceB,i))
    
    #ShiftedB = Shifting(SequenceB,Score_2.index(max(Score_2)))   
    
    
    if max(Score_1)>max(Score_2):
        ShiftedA = ShiftedA
        ShiftedB = []
        ShiftedB.append(SequenceB)
    else:
        ShiftedA = []
        ShiftedA.append(SequenceA)
        ShiftedB = ShiftedB
                    
                    
    Score = max(max(Score_1),max(Score_2))
    
    return Score, ShiftedA, ShiftedB
    


# In[12]:


a='ACTTTTCAC'
b='TTATCTCGA'
MaxChain(a,b,8)


# ### main function
# - `Option`--->`SequenceInput()`--->`MaxShiftBitInput()`--->`NumberOfMatch`or`MaxChain`
# - Exception is  `ValueError`from `Option` input. We also manually raise the error if `Option` is not equal to 1,2 or 3.
# - Option 3 is for exiting the program.

# In[13]:


def main():       
    while 1:
        flag = 0
        while flag == 0:
            try:
                Option = int(input("Please select you algorithm to compare the sequence\n                                 1 : Number of match\n                                 2 : Maximum contiguous chain \n                                 3 ：Exit the program \n                                 Your Select is:"))
                if Option!=1 and Option!=2 and Option!=3:
                    raise ValueError
            except ValueError:
                print("Please input 1,2 or 3\n")
            else:
                flag = 1
                if   Option == 1:
                    print("You selected **Number of match**\n")
                elif Option == 2:
                    print("You selected **Maximum contiguous chain**\n")
                else:
                    return

        SequenceA,SequenceB=SequenceInput()
        print("The sequence A you choose is:\n",SequenceA)
        print("The sequence B you choose is:\n",SequenceB)


        MaxShiftBits=MaxShiftBitInput()
        print("The Max Shift Bits you choose is:%d\n"%MaxShiftBits)
        

        if Option == 1:
            Score, ShiftedA, ShiftedB = NumberOfMatch(SequenceA,SequenceB,MaxShiftBits)
            print("The number of match of the two sequence is %d\n"%Score)
            print("The processed sequence A is:\n",ShiftedA)
            print("The processed sequence B is:\n",ShiftedB)
            print("*-*denotes the bit shifting")

        else:
            Score, ShiftedA, ShiftedB = MaxChain(SequenceA,SequenceB,MaxShiftBits)
            print("The max contiguous of the two sequence is %d\n"%Score)
            print("The processed sequence A is:\n",ShiftedA)
            print("The processed sequence B is:\n",ShiftedB)
            print("*-*denotes the bit shifting")
                
        
    


# ### To convert .py file

# In[15]:


if __name__ == '__main__':
    main()

