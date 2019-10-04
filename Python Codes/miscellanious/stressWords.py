'''
The function should recognise if a subject line is stressful.
A stressful subject line means that all letters are in uppercase,
and/or ends by at least 3 exclamation marks, and/or contains at least one of the following “red” words:
"help", "asap", "urgent". Any of those "red" words can be spelled in different ways - "
HELP", "help", "HeLp", "H!E!L!P!", "H-E-L-P", even in a very loooong way "HHHEEEEEEEEELLP"
'''
def is_stressful(subj):
    red = ['help', 'asap', 'urgent']
    print("here")
    if subj == subj.upper():
        return True
    elif (subj.count('!') > 2):
        return True
    else:
        print("here agina")
        for i in red:
            if i in subj:
                return True
            else:
                print("else")
                #data = ''.join(list(dict.fromkeys(subj).keys()))
                #Cotinue https://py.checkio.org/mission/stressful-subject/solve/

                subj1 = [i for i in subj.lower() if i.isalpha()]
                print(subj1)
                subj1 = ''.join(subj1)
                for i in red:
                    index = subj1.find(i)
                    if index >= 0:
                        return True
                    else:
                        continue
                if index < 0:
                    return False

if __name__ == '__main__':
   #These "asserts" using only for self-checking and not necessary for auto-testing
   #assert is_stressful("asap help") == True, "First"
   #assert is_stressful("We need you A.S.A.P.!!") == True, "Second"
   ##assert is_stressful("yelp!!!!") == True, "Third"
   assert is_stressful("URGEEENNNTT here") == True, "Third"

   print('Done! Go Check it!')