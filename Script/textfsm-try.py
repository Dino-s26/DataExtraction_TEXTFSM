import textfsm
import os, sys, glob, csv
import datetime

ddt = str(datetime.datetime.now().strftime("%d-%m-%y--%H-%M-%M"))
currentMonth = str(datetime.datetime.now().strftime('%B-%Y'))
output_files = "Extract_Data"+'-'+currentMonth+'_'+'Timestamp-'+ddt+'.csv'
name = str(output_files)
print("Extracted File Name : ", name)
print(currentMonth)

path = os.getcwd()
print ("File Path : ",path)

source_file = glob.glob(os.path.join(path,"*.txt"))
print ("Source File Name : ",source_file)

for file in source_file:
    files = open(file,encoding='utf-8')
    raw_text_data = files.read()
    files.close()

    template = open("show_memory_ios_xe.textfsm")
    re_table = textfsm.TextFSM(template)
    fsm_results = re_table.ParseText(raw_text_data)

    print(fsm_results)

    outfile_name = open(name, 'a')
    outfile = outfile_name

    print(re_table.header)
    for s in re_table.header:
        outfile.write("%s," % s)
    outfile.write("\n")

    counter = 0
    for row in fsm_results:
        print(row)
        for s in row:
            outfile.write("%s," % s)
        outfile.write("\n")
        counter += 1
    print("Write %d records" % counter)

#input_file = open("WSA2-LAN-D1.20191127.1209.txt", encoding='utf-8')
#raw_text_data = input_file.read()
#input_file.close()
