from helper import file_handle,wordt_time,get_time_string

def view_document(filename):  
    text = file_handle(filename, "read")  
    print("\nDocument content:")  
    print(text)  
  #definition view_document(filename)
# read document content from file (excluding old word count/timestamp)
# print the document content