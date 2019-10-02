#!/usr/bin/env python
import csv,string


filepath = "/Users/kritikaversha/Desktop/CDO_Uncleaned_Modified.csv"
fileout = "/Users/kritikaversha/Desktop/CleanedCDO.csv"
state_list=('AL','MO','AK','MT','AZ','NE','AR','NV','CA','NH','CO','NJ','CT','NM','DE','NY','DC','NC','FL','ND','GA','OH','HI','OK','ID','OR','IL','PA','IN','RI','IA','SC','KS','SD','KY','TN','LA','TX','ME','UT','MD','VT','MA','VA','MI','WA','MN','WV','MS','WI','WY')
NE_England=['CT', 'ME', 'MA', 'NH', 'RI','VT']
Mid_Atlantic=['NJ', 'NY', 'PA']
East_NC=['IL', 'IN', 'MI', 'OH', 'WI']
West_NC=['IA', 'KS', 'MN', 'MO', 'NE', 'ND', 'SD']
South_Atlantic=['DE', 'FL', 'GA', 'MD', 'NC', 'SC', 'VA', 'D.C.','W.V']
East_SC=['AL', 'KY', 'MS', 'TN']
West_SC=['AR', 'LA', 'OK','TX']
Mountain=['AZ', 'CO', 'ID', 'MT', 'NV', 'NM', 'UT','WY']
Pacific=['AK', 'CA', 'HI', 'OR', 'WA']

with open(filepath,'rb') as csvfile, open(fileout,'wb') as opfile:
    writer = csv.writer(opfile)
    writer.writerow(["Year","Salary(Dollars)","Industry","State","Region"])
    reader = csv.reader(csvfile)
    count=0
    next(reader, None)
    for rows in reader:
        count=count+1
        print count,rows
        all=string.maketrans('','')
        nodigs=all.translate(all, string.digits)
        salpart1 = ((rows[2]).split('-'))[0]
        salary = (((salpart1).split('.'))[0]).translate(all, nodigs)
        year = ((rows[1]).strip()).replace(',','')
        industry = ((((rows[3]).split("/"))[0]).split(","))[0]
        state = list(set((rows[4]).split(', ')).intersection(state_list))
        
        if "Michigan" in rows[4] or "Ann Arbor" in rows[4] :
            state = ['MI']

        if "Ohio" in rows[4]:
            state = ['OH']

        if "New York" in rows[4]:
            state = ['NY']

        if "Pennsylvania" in rows[4]:
            state = ['PA']

        if "Texas" in rows[4]:
            state = ['TX']

        if "San Francisco" in rows[4]:
            state = ['CA']
        
        if state == []:
            print state,rows[4],"No Match"
           
        if len(state)==0:
            region = "None"
        if len(state)!=0:
            if state[0] in NE_England:
                region = "North East(England)"
            if state[0] in Mid_Atlantic:
                region = "North East(Mid Atlantic)"
            if state[0] in East_NC:
                region = "Mid-West(East North Central)"
            if state[0] in West_NC:
                region = "Mid-West(West North Central)"
            if state[0] in South_Atlantic:
                region = "South(South Atlantic)"
            if state[0] in East_SC:
                region = "South(East South Central)"
            if state[0] in West_SC:
                region = "South(West South Central)"
            if state[0] in Mountain:
                region = "West(Mountain)"
            if state[0] in Pacific:
                region = "West(Pacific)"

        if salary and year and industry and len(state)!=0  :
            print rows
            writer.writerow([year,salary,industry,state[0],region])
        elif year and industry and len(state)==0 :
            print rows
            writer.writerow([year,salary,industry,rows[4],region])
