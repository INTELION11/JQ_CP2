def file_handle(filename, mode, content=""):  
    if mode == "read":  
        try:  
            f = open(filename, "r")  
            lines = f.readlines()  
            f.close()  
            clean = []  
            for line in lines:  
                if not (line.startswith("Word Count:") or line.startswith("Last Updated:")):  
                    clean.append(line.rstrip())  
            return "\n".join(clean).strip()  
        except:  
            print("File not found.")  
            return ""  
    elif mode == "write":  
        f = open(filename, "w")  
        f.write(content)  
        f.close()  
    elif mode == "append":  
        f = open(filename, "a")  
        f.write(content)  
        f.close()  
  
def wordt_time(text, timestamp):  
    words = len(text.split())  
    return text + "\n\nWord Count: " + str(words) + "\nLast Updated: " + timestamp + "\n"  
  
def get_time_string():  
    import time  
    t = time.localtime()  
    return str(t.tm_year) + "-" + str(t.tm_mon).zfill(2) + "-" + str(t.tm_mday).zfill(2) + " " + str(t.tm_hour).zfill(2) + ":" + str(t.tm_min).zfill(2) + ":" + str(t.tm_sec).zfill(2) 
# define file_handle(filename, mode, content="")
# if mode is "read"
# try to open file for reading
# read all lines from file
# remove any lines that start with "Word Count:" or "Last Updated:"
# return cleaned text
# if file not found
# print file not found
# return empty string
# if mode is "write"
# open file for writing
# write content to file
# if mode is "append"
# open file for appending
# write content to file

#define wordt_time(text, timestamp)
# count number of words in text
# return text with "\n\nWord Count: X\nLast Updated: timestamp\n" appended

#define get_time_string()
# get current local time
# format as "YYYY-MM-DD HH:MM:SS"
# return formatted string