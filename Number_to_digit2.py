ones={'0':"zero",'1':"one",'2':"two",'3':"three",'4':"four",'5':"five",'6':"six",'7':"seven",'8':"eight",'9':"nine"}
eleven_to_19={'11':"eleven",'12':"twelve",'13':"thirteen",'14':"fourteen",'15':"fifteen",'16':"s'ixteen",
    '17':"seventeen",'18':"eighteen",'19':"ninteen"}
tens={'10':"ten",'20':"twenty",'30':"thirty",'40':"forty",'50':"fifty",'60':"sixty",'70':"seventy",'80':"eighty",
    '90':"nintey"}
#------------------------------------------------------------------------------------------------------
def two_digits_to_words(a):
    word=[]
    if len(a)==1:
        word.append(ones[a[0]])
        return word
    if len(a)==2:
        num=str(int(a[0])*10+int(a[1]))
        if a==['0','0']:
            return None
        if num in eleven_to_19:
            word.append(eleven_to_19[num])
            return word
        if num in tens:
            word.append(tens[num])
            return word
        else:
            if a[0]!='0':
                word.append(tens[str(int(a[0])*10)])
            word.append(ones[a[1]])
            return word

def array_combiner(a):
    combine=""
    for i in a:
        if i==None:
            continue
        for j in range(len(i)):
            combine=combine+i[j]+" "
    return combine

def splitting_to_array(str):
    length=len(number)
    if length <=2:
        two_digi=list(number[-2:])
        hundred=""
        thousand=""
        lakh=""
        crore=""
    elif length==3:
        two_digi=list(number[-2:])
        hundred=list(number[-3:-2])
        thousand=""
        lakh=""
        crore=""
    elif length>3 and length<=5:
        two_digi=list(number[-2:])
        hundred=list(number[-3:-2])
        thousand=list(number[-5:-3])
        lakh=""
        crore=""
    elif length>5 and length<=7:
        two_digi=list(number[-2:])
        hundred=list(number[-3:-2])
        thousand=list(number[-5:-3])
        lakh=list(number[-7:-5])
        crore=""
    else:
        two_digi=list(number[-2:])
        hundred=list(number[-3:-2])
        thousand=list(number[-5:-3])
        lakh=list(number[-7:-5])
        crore=list(number[:-7])

    number_set=[]
    number_set.append(crore)
    number_set.append(lakh)
    number_set.append(thousand)
    number_set.append(hundred)
    number_set.append(two_digi)
    return number_set
#---------------------------------------------------------------------------------------------------------------------------------------
number=input("Input a number to convert to words according to indian system\n")
array=final=[]
if len(number)>9:
    print("Oops number too huge....:(")    
else:
    if number=='0':
        print("Zero")
    else:    
        array=splitting_to_array(number)
        for i in range(len(array)):
            if i==0 and len(array[i])!=0:
                words_array=two_digits_to_words(array[i])
                if words_array!=None:
                    if words_array!=['zero']:
                        final.append(words_array+["crore,"])
            elif i==1 and len(array[i])!=0:
                words_array=two_digits_to_words(array[i])
                if words_array!=None:
                    if words_array!=['zero']:
                        final.append(words_array+["lakh,"])
            elif i==2 and len(array[i])!=0:
                words_array=two_digits_to_words(array[i])
                if words_array!=None:
                    if words_array!=['zero']:
                        final.append(words_array+["thousand,"])
            elif i==3 and len(array[i])!=0:
                words_array=two_digits_to_words(array[i])
                if words_array!=['zero']:
                    final.append(words_array+["hundred,"])
            else:
                words_array=two_digits_to_words(array[i])
                final.append(words_array)
        finalmost=array_combiner(final)
        print(finalmost.title())
