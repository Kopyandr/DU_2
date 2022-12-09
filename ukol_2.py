import csv 



with open('try_data.csv','r' ) as csv_file:
    csv_reader=csv.reader(csv_file) # takhle to vytiskne jako list, ve kterim mužeš makat jako frajer 

    total=0
    counter=0
    year_counter=0
    rok=0
    first_day=None
    
    
    for line in csv_reader:
        print(counter)
        if rok ==0:
            datum=line[2]
            rok=int(datum.split('.')[2])
            vystup_rok_iter=int(datum.split('.')[2])
            print(vystup_rok_iter)
            
        if first_day is None:
            datum=line[2]
            first_day=int(datum.split('.')[0])   
            month=int(datum.split('.')[1])
             
        
        
        # vypočet roku iterarace
        datum=line[2]
        vystup_rok_iter=int(datum.split('.')[2])
        
            
        if vystup_rok_iter != rok:
            rocni_flow=(total/year_counter)
            print(rocni_flow)
            year_counter=0 
            datum=line[2]
            rok=int(datum.split('.')[2])
            print("změna roku iterace") #koment 
            
        # týdení count 
        if counter==7:
            prumer=(total/counter)
            print(prumer)
            counter=0
            print(first_day)
            datum=line[2]
            first_day=int(datum.split('.')[0])   
            month=int(datum.split('.')[1])
            
            
            
        counter+=1
        year_counter+=1
        total+=float(line[3])

        
        
        #prutok=line(float[3])
    #print(total)
    #print(counter)
    #prumer=(total/counter)
    #print(prumer)

    
        
        
    
        
            

        
        





    
