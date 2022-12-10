import csv

with open('data.csv','r' ) as csv_file, open("vystup_test.csv", "w", encoding="utf-8", newline="") as csv_test_1, open("vystup_test_year.csv", "w", encoding="utf-8", newline="") as csv_test_year:
    csv_reader=csv.reader(csv_file) # takhle to vytiskne jako list, ve kterim mužeš makat jako frajer 

    writer_week = csv.writer(csv_test_1)
    writer_year = csv.writer(csv_test_year)
    
    prefix=None #data ve všech řádcích stejná 
    first_day=None #první den týdne
    first_day_year=None #první den roku 
    counter_week= 0 #počítá dny v týdnu 
    counter_year=0 #počíta dny v roce 
    sum_week=0 
    sum_year=0
    year_base=0
    month_year=None
    chyby_v_prutoku=[]
    
    for line in csv_reader:
        
        datum=line[2]
        year=[int(datum.split('.')[2])]
        
        if prefix is None: 
            prefix=line[0:2]
            print(prefix)
        
        if first_day is None:
            datum=line[2]
            first_day=[int(datum.split('.')[0])]   
            month=[int(datum.split('.')[1])]
            
        
        if first_day_year is None:
            datum=line[2]
            first_day_year=[int(datum.split('.')[0])] 
            
        if year_base==0:
            datum=line[2]
            year_base= [int(datum.split('.')[2])]
        
        if month_year is None:
            datum=line[2]
            month_year=[int(datum.split('.')[1])]
            
        #nekorektní vstupy 
        if float(line[3]) <= 0:
            chyba_den=[int(datum.split('.')[0])] 
            chyba_month=[int(datum.split('.')[1])]
            chyba_year=[int(datum.split('.')[2])]
            
            chyby_v_prutoku.append(chyba_den+chyba_month+chyba_year)
        
        
        if year_base!=year:
            writer_year.writerow(prefix + first_day_year+ month_year + year_base+ [round(sum_year/counter_year, 4)])
            counter_year=0
            sum_year=0
            #datum=line[2]
            month_year=[int(datum.split('.')[1])]
            year_base= [int(datum.split('.')[2])]
        
        
        if counter_week==7:
            writer_week.writerow(prefix + first_day+ month+year+ [round(sum_week/counter_week, 4)])
            counter_week=0
            sum_week=0
            # Nové datum 
            datum=line[2]
            first_day=[int(datum.split('.')[0])]   
            month=[int(datum.split('.')[1])]
            year= [int(datum.split('.')[2])]
            
    
        counter_week+=1
        sum_week+=float(line[3])
        counter_year+=1
        sum_year+=float(line[3]) 
        
        #cyklus skončí před dokončením roku, nebo týdne 
    writer_year.writerow(prefix + first_day_year+ month_year + year_base+ [round(sum_year/counter_year, 4)])
    writer_week.writerow(prefix + first_day+ month+year+ [round(sum_week/counter_week, 4)])