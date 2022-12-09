import csv 



with open('try_data.csv','r' ) as csv_file, open("vystup_7denni.csv", "w", encoding="utf-8", newline="") as csv_out_week,open("vystup_rok.csv", "w", encoding="utf-8", newline="") as csv_out_year:
    csv_reader=csv.reader(csv_file) # takhle to vytiskne jako list, ve kterim mužeš makat jako frajer 

    writer_week = csv.writer(csv_out_week)
    writer_year = csv.writer(csv_out_year)
    
    #Sumy prutků 
    total=0
    sum_year=0
    # počítaní dnů 
    counter=0
    year_counter=0
    rok=0
    first_day=None
    first_day_year=None
    prefix=None
    
    
    for line in csv_reader:
        print(counter)###
        
        if prefix is None:  #prefix zustava 
            prefix=line[0:2]
            
        
        if rok ==0:
            datum=line[2]
            rok=[int(datum.split('.')[2])]
            vystup_rok_iter=int(datum.split('.')[2])
            print(vystup_rok_iter)
            
        if first_day is None:
            datum=line[2]
            first_day=[int(datum.split('.')[0])]   
            month=[int(datum.split('.')[1])]
        
        if first_day_year is None:
            datum=line[2]
            first_day_year=[int(datum.split('.')[0])]
            
        # vypočet roku iterarace
        datum=line[2]
        vystup_rok_iter=[int(datum.split('.')[2])]
        
            
        if vystup_rok_iter != rok:
            rocni_flow=(sum_year/year_counter)
            print(rocni_flow)
            writer_week.writerow(prefix + first_day_year + month + [round(sum_year/year_counter, 4)])
            year_counter=0 
            datum=line[2]
            first_day_year=[int(datum.split('.')[0])] 
            rok=[int(datum.split('.')[2])]
            print("změna roku iterace") #koment 
            
        # týdení count 
        if counter==7:
            prumer=(total/counter)
            print(prumer)
            writer_week.writerow(prefix + first_day + month + [round(total/counter, 4)])
            counter=0
            total=0
            
            datum=line[2]
            first_day=int(datum.split('.')[0])   
            month=int(datum.split('.')[1])
            
            
            
        counter+=1
        year_counter+=1
        total+=float(line[3])
        sum_year+=float(line[3])

        
        
        #prutok=line(float[3])
    #print(total)
    #print(counter)
    #prumer=(total/counter)
    #print(prumer)

    
        
        
    
        
            

        
        





    
