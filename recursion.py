from utilities.file_utils import get_files

photo_folder = '/home/mike/Képek'



def call_myself(i):
    if i >= 10:
        print("i >= 10. exit.")
    else:
        print(f"I called myself {i} times.")
        call_myself(i+1)
    

files = get_files(photo_folder)
for i in files:
    print(i)



