import os
s=input('Enter a name for testing=')
if os.path.isfile(f'C:\Users\nidhi\OneDrive\Desktop\v\{s}'):
    print('Name exist in current directory')
'''elif os.path.isdir(f'C:\Users\nidhi\OneDrive\Desktop\v\{s}'):
    print('Its a directory')
'''
else:
    print('Not found')