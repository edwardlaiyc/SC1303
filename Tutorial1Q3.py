#to test a number for palindrome ([::-1])
#to extract certain digits from an integer to test for palindrome (convert to string[])
#use .zfill to pad numbers to 6 digits

#test all cases from 0 - 999,999
for i in range (1000000):

    #convert number to string for easier manipulation, and pad w/ leading 0s to form 6 digits
    firstMile = str(i).zfill(6)
    #test last 4 digits, but not the last 5 digits form palindrome
    if firstMile[-4:] == firstMile[-4:][::-1] and firstMile[-5::] != firstMile[-5:][::-1]:

        #add one mile
        secondMile = str(i+1).zfill(6)
        #test last 5 digits form palindrome
        if secondMile[-5:] == secondMile[-5:][::-1]:

            #add one more mile (add 2 to original number)
            thirdMile = str(i+2).zfill(6)
            #test middle 4 digits form palindrome
            if thirdMile[1:5] == thirdMile[1:5][::-1]:

                #add one more mile
                fourthMile = str(i+3).zfill(6)
                #test all 6 digits are palindrome
                if fourthMile == fourthMile[::-1]:

                    #return number
                    print(i)

'''
abcdef --> c = f, d = e --> c = d = e = f
+1
abcde(f+1) --> b = f+1, c = e --> c = d = e, b = f+1
+1
abcde(f+2) --> b = e, c = d --> b unchanged, so e+1 from previous mile
--> f+1 = 9 --> f = 8 --> c=d=e=f=8
--> current number: abcd(e+1)0
--> original number: ab8888 -->(+1) a98889 -->(+1) a98890
+1
a98891 --> a = 1
--> Original number: 198888

Check: 198888 (+1) 198889 (+1) 198890 (+1) 198891
'''