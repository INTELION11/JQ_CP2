from helper import file_handle,wordt_time,get_time_string
def update_document(filename):  
    text = file_handle(filename, "read")  
    timestamp = get_time_string()  
    updated = wordt_time(text, timestamp)  
    file_handle(filename, "write", updated) 
    print(timestamp)
    print(f"Document updated.{updated} :time might be off, i dont know how:")  
#definition update_document(filename)
# read document content from file (excluding old word count/timestamp)
# get current time string
# create updated text with new word count and timestamp
# write updated text to file
# print confirmation message with new word count

