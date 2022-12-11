import csv
import datetime 
try:
    with open('data_test3.csv','r' ) as csv_file, open("vystup_test.csv", "w", encoding="utf-8", newline="") as csv_test_1, open("vystup_test_year.csv", "w", encoding="utf-8", newline="") as csv_test_year:
        csv_reader=csv.reader(csv_file)  

        writer_week = csv.writer(csv_test_1)
        writer_year = csv.writer(csv_test_year)
        
        prefix=None #data ve všech řádcích stejná 
        first_day_week=None #první den týdne
        first_day_year=None #první den roku 
        counter_week= 0 #počítá dny v týdnu 
        counter_year=0 #počíta dny v roce 
        sum_week=0 #týdení kumuluční průtok 
        sum_year=0 #roční kumulační průtok 
        year_base=0 # slouží k identifikaci změny roku v datech 
        month_year=None #měsíc vypsaný pro roční prutok 
        chyby_v_prutoku=[]
        chybejici_data=[]
        max_prutok=None 
        min_prutok=None
        expected_date=None #očekávané následující datum 
        
        for line in csv_reader:
            
            datum=line[2]
            
            formatted_date=datetime.datetime.strptime(datum, '%d.%m.%Y')

            if not expected_date: 
                expected_date = formatted_date + datetime.timedelta(days=1)
            else: #je aktuální datum stejné, jako datum očekávané ?
                if formatted_date!=expected_date:
                    days_missing=(formatted_date-expected_date).days #Počet dní mezi očekávaným a načteným datem
                    for i in range (0, days_missing):
                        chybejici_data.append(datetime.datetime.strftime(expected_date + datetime.timedelta(days=i), '%d-%m-%Y'))
                    expected_date=formatted_date+datetime.timedelta(days=1)
                else:
                    expected_date += datetime.timedelta(days=1)
                    
            year=[int(datum.split('.')[2])]
            
            # Výpočet maximálních a minimálních průtoků 
            if max_prutok is None or float(line[3]) > max_prutok:
                max_prutok=float(line[3])
                max_date=[int(datum.split('.')[0]),int(datum.split('.')[1]),int(datum.split('.')[2])] 
                
            if min_prutok is None or float(line[3]) < min_prutok: 
                min_prutok=float(line[3])
                min_date=[int(datum.split('.')[0]),int(datum.split('.')[1]),int(datum.split('.')[2])]
                
            if prefix is None: 
                prefix=line[0:2]
                print(prefix)
            
            if first_day_week is None: #datum prvního počítaného dne 7deního prutoku 
                first_day_week=[int(datum.split('.')[0])]   
                month=[int(datum.split('.')[1])]
                
            if counter_week==1: # zaznamená datum pro zápis 7denních prutoků 
                day_write=[int(datum.split('.')[0])]
                month_write=[int(datum.split('.')[1])]
                year_write=[int(datum.split('.')[2])]
                
            
            if first_day_year is None: #zaznam dne pro zapis do prumerného ročního průtoku 
                first_day_year=[int(datum.split('.')[0])] 
                
            if year_base==0:
                year_base= [int(datum.split('.')[2])]
            
            if month_year is None:
                month_year=[int(datum.split('.')[1])]
                
            # nekorektní vstupy poze záporné průtoky 
            if float(line[3]) <= 0:
                chyba_den=[int(datum.split('.')[0])] 
                chyba_month=[int(datum.split('.')[1])]
                chyba_year=[int(datum.split('.')[2])]
                
                chyby_v_prutoku.append(chyba_den+chyba_month+chyba_year)
            
            # Zapíše roční průměrný průtok s datem 1.dne a  měsíce 
            if year_base!=year: # očekávaný rok není stejný jako iterovaný --> zápis ročního prutoku 
                writer_year.writerow(prefix + first_day_year+ month_year + year_base+ [round(sum_year/counter_year, 4)])
                counter_year=0 # vynuluje roční počítadlo 
                sum_year=0
                
                month_year=[int(datum.split('.')[1])]
                year_base= [int(datum.split('.')[2])] # nastavý nový očekávaný rok pro další iteraci
            
            # zapíše průměrný průtok za týden, zapíše datum 1. dne týdnu 
            if counter_week==7:
                writer_week.writerow(prefix + day_write + month_write+year_write+ [round(sum_week/counter_week, 4)])
                counter_week=0
                sum_week=0
                # Nové datum 
                first_day_week=[int(datum.split('.')[0])]   
                month=[int(datum.split('.')[1])]
                year= [int(datum.split('.')[2])]
                
            # Přičíta 1 k počítadlu dnu v roce a v 7 dennim období 
            counter_week+=1
            sum_week+=float(line[3]) #příčítá 1 ke kumulačnímu průtoku 7mi dní 
            counter_year+=1
            sum_year+=float(line[3]) # kumulační průtok roční 
            
            #cyklus skončí před dokončením roku, nebo týdne - vypíší se průtsoky za zbilé dny do konce dat 
        writer_year.writerow(prefix + first_day_year+ month_year + year_base+ [round(sum_year/counter_year, 4)])
        writer_week.writerow(prefix + first_day_week+ month+year+ [round(sum_week/counter_week, 4)])
        
        print(f"maximální prutok: {max_prutok,max_date}")
        print(f"minimální průtok: {min_prutok,min_date}")
        
        if len(chyby_v_prutoku)!=0:
            print(f"chybné průtoky ve dnech {chyby_v_prutoku}.")
            
        if len(chybejici_data)>0:
            print(f"chybějící dny {chybejici_data}.")
    
except FileNotFoundError:
    print("Soubor nenalezen, ujistěte se že soubor bude nalezený")
except IndexError:
    print ("Chyba vstupních dat")
except ValueError:
    print ("Hodnota ze souboru je v nesprávném formátu, zkontrolujte data v souboru")