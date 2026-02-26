from helper import file_handle,wordt_time,get_time_string
def add_content(filename):  
    print("\nEnter new content (press Enter twice to finish):")  
    lines = []  
    while True:  
        line = input()  
        if line == "":  
            break  
        lines.append(line)  
    new_content = "\n".join(lines)  
    old_text = file_handle(filename, "read")  
    combined = old_text + "\n" + new_content if old_text else new_content  
    file_handle(filename, "write", combined)  
    print("Content added successfully.")  
#definition add_content(filename)
# prompt user to enter new content (until blank line)
# read old document content (excluding word count/timestamp)
# add new content to old content
# write combined content back to file (without word count/timestamp)
# print confirmation message

