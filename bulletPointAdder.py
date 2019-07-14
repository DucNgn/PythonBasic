import pyperclip

text = pyperclip.paste()  #Receive the content in clipboard

#Adding bulletPoint
lines = text.split('\n')

print('What kind of character do you want to use as your bullet point ?')
bulletPoint = str(input())
for i in range(len(lines)):
    lines[i] = bulletPoint + ' ' + lines[i]
text = '\n'.join(lines)  #Rejoin the text

#Copy the edited content to clipboard
pyperclip.copy(text)
print('Done. You can paste your new paragraph with nice bullet points now!')

