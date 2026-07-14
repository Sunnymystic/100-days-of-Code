#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

def read_name_from_file():
    with open(r"Mail_Merge_Project_Start\Input\Names\invited_names.txt") as file:
        names = file.readlines()
        return names
        

def read_mail_content(name):
    with open(r"Mail_Merge_Project_Start\Input\Letters\starting_letter.txt") as file:
        records = file.readlines()
        records[0] = records[0].replace("[name]",name)
        return records
        
def write_letter(name,records):
        with open(f"Mail_Merge_Project_Start/Output/ReadyToSend/Letter_for_{name}.txt","w") as file: 
            file.writelines(records) 
            

for name in read_name_from_file():
    if name.strip() != "Aang":
        records = read_mail_content(name.strip())
        write_letter(name.strip(),records)



    
        
            