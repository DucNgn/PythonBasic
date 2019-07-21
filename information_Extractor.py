#!/usr/bin/env python3
'''
FIND PERSONAL INFORMATION ON THE CLIPBOARD 
(PHONE NUMBER, EMAIL ADDRESS, POSTAL CODE)
                  ---Demo Output:--- 
--copy on clipboard:

My phone number is (+1) (514)-890-2380, call me later. 
My email address is niceGuy2341@gmail.ca,
my postal code is H3A 5B2. visit me!!!

--Run

--Output on clipboard:

 - Phone Numbers:
(+1) (514)-890-2380
- Email Address:
niceGuy2341@gmail.ca
- Postal Code:
H3A 5B2

'''


import re, pyperclip

'''
REGEX TO MATCH:
  + PHONE NUMBER
  + EMAIL ADDRESS
  + POSTAL CODE
'''
phone_Regex = re.compile(r'''(
    (\+\d|\(\+\d\)|\d)?               #Country code
    (\s|-|\.)?                        #separator
    (\d{3}|\(\d{3}\))                 #first 3 digits (AREA code)
    (\s|-|\.)?                        #separator
    (\d{3})                           #first 3 digits
    (\s|-|\.)?                        #separator
    (\d{4})                           #last 4 digits 
    (\s*(ext|x|ext.)\s*(\d{2, 5}))?   #extension
)''', re.VERBOSE)

email_Regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+                 #userName
    @                                 #@ character
    [a-zA-Z0-9.-]+                    #Domain
    (\.[a-zA-Z]{2,4})                 #dot ...
)''', re.VERBOSE | re.IGNORECASE)

postal_Regex = re.compile(r'''(
    (\w\d\w)                          #First 3 characters     
    (\s)?                             #separator
    (\d\w\d)                          #Last 3 characters
)''', re.VERBOSE | re.IGNORECASE)

#Receive content inside clipboard
text = str(pyperclip.paste())

phone_Result = []
for groups in phone_Regex.findall(text):
    phoneNum = '-'.join([groups[3], groups[5], groups[7]])
    if groups[1] != '':
        phoneNum = groups[1] + ' ' + phoneNum
    if groups[10] != '':
        phoneNum += ' x' + groups[8]
    phone_Result.append(phoneNum)

email_Result = []
for groups in email_Regex.findall(text):
    email_Result.append(groups[0])

postal_Result = []
for groups in postal_Regex.findall(text):
    postal_Result.append(groups[0])

result = ' '

if len(phone_Result) != 0:
    print('Found ' + str(len(phone_Result)) + ' phone numbers')
    result += str('- Phone Numbers:\n')
    result += str('\n'.join(phone_Result))
    result += '\n'
else:
    print('No phone number found')
    result += 'No phone number found\n'

if len(email_Result) != 0:
    print('Found ' + str(len(email_Result)) + ' email address(es)')
    result += str('- Email Address:\n')
    result += str('\n'.join(email_Result))
    result += '\n'
else:
    print('No email found')
    result += 'No email found\n'

if len(postal_Result) != 0:
    print('Found ' + str(len(postal_Result)) + ' postal code(s)')
    result += str('- Postal Code:\n')
    result += str('\n'.join(postal_Result))
    result += '\n'
else:
    print('No postal code found')
    result += 'No postal code found\n'


pyperclip.copy(result)
print('Copied result to the clipboard')









