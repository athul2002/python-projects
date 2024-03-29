from datetime import datetime
start_time = datetime.now()

#Help https://youtu.be/N6PBd4XdnEw
def octant_range_names(mod=5000):
    octant_name_id_mapping = {"1":"Internal outward interaction", "-1":"External outward interaction", "2":"External Ejection", "-2":"Internal Ejection", "3":"External inward interaction", "-3":"Internal inward interaction", "4":"Internal sweep", "-4":"External sweep"}
    df.at[1,'Octant ID']="Mod "+str(mod)
    #initialised a list for getting range values
    range_list=[0]
    #initialised x as variable for getting number of mod ranges
    x=int(len(df)/mod)
    
    #adding range values in the list
    for i in range (x):
        range_list.append(mod*(i+1))
    range_list.append(len(df))
    for i in range(len(range_list)-1):
        for octant in ['1','-1','2','-2','3','-3','4','-4']:
            #counting the counts of octants in the mod ranges
            df.at[2+i,octant]=df['Octant'].iloc[range_list[i]:range_list[i+1]].value_counts()[int(octant)]
        df.at[2+i,'Octant ID']=str(range_list[i])+" - "+ str(range_list[i+1]-1)  
    
    #initialised 2 lists for taking the overall counts of the octant values
    rank_list_overall_1=[]
    rank_list_overall_2=[]    
    #The value of overall octant count is added to both the lists initialised above
    for y in ['1','-1','2','-2','3','-3','4','-4']:
        rank_list_overall_1.append(df[y][0])
        rank_list_overall_2.append(df[y][0])
    #sorting one of the list(rank_list_overall_2) while the other one remains unsorted
    rank_list_overall_2.sort(reverse=True)
    #Initialised a list called final_list_1 for ranking the octants
    final_list_1=[]
    for i in range(0,len(rank_list_overall_2)):
        #rank_list_overall_1 is unsorted list while rank_list_overall_2 is sorted list
        #what the below line do's is: comparing the value is sorted list to that of unsorted list and
        # returns of the index of that value in unsorted array
        #The index is then appended to the final_list_1 list
        final_list_1.append((rank_list_overall_2.index(rank_list_overall_1[i]))+1) 
    for i in range(1,9):
        #adding the rank values in respective columns
        df.at[0,'Rank'+str(i)]=final_list_1[i-1]

        #adding the index of octant having rank 1
        if final_list_1[i-1]==1:
            z=i-1
        for k,x in enumerate([1,-1,2,-2,3,-3,4,-4]):
            try:
                #when the k value becomes equal to that of the z value assigned, octant value corresponding to that is added to variable named value 
                if k==z:
                    value=x
            except:
                continue
    #Adding the rank 1 Octant ID and Octant name
    df.at[0,'Rank1 OctantID']=value
    df.at[0,'Rank1 Octant Name']=octant_name_id_mapping.get(str(value))

    #The above steps for overall octant count is repeated for ranking the octant counts for different mod ranges
    #adding the octant counts in two lists, sorting one list, comparing the values and adding the index values to one list
    #the index values is then printed
    for i in range(len(range_list)-1):
        mod_list_1=[]
        mod_list_2=[]
        for y in ['1','-1','2','-2','3','-3','4','-4']:
            mod_list_1.append(df[y][2+i])
            mod_list_2.append(df[y][2+i])
        mod_list_2.sort(reverse=True)
        final_list_2=[]
        for z in range(0,len(mod_list_2)):
            final_list_2.append((mod_list_2.index(mod_list_1[z]))+1)        
        for z in range(1,9):
            df.at[2+i,'Rank'+str(z)]=final_list_2[z-1]    
            if final_list_2[z-1]==1:
                a=z-1
            for k,x in enumerate([1,-1,2,-2,3,-3,4,-4]):
                try: 
                    if k==a:
                        df.at[2+i,'Rank1 OctantID']=x
                        df.at[2+i,'Rank1 Octant Name']=octant_name_id_mapping.get(str(x))
                except:
                    continue

    df.at[4+len(range_list),'1']='Octant ID'
    df.at[4+len(range_list),'-1']='Octant Name'
    df.at[4+len(range_list),'2']='Count of Rank 1 Mod Values'

    #initialsed a list containing 8 elements with every elements 8
    count_list=[0,0,0,0,0,0,0,0]
    #Traversing Rank1 OctantID column
    #when the value in the columns becomes equal to 1 the first element in list in increased by one
    #when it becomes equal to -1 second elemnt is increased by 1 and respectively for others
    for i in range(2,len(df['Rank1 OctantID'])):
        if df['Rank1 OctantID'][i]==1:
            count_list[0]+=1
        elif df['Rank1 OctantID'][i]==-1:
              count_list[1]+=1  
        elif df['Rank1 OctantID'][i]==2:
              count_list[2]+=1  
        elif df['Rank1 OctantID'][i]==-2:
              count_list[3]+=1      
        elif df['Rank1 OctantID'][i]==3:
              count_list[4]+=1      
        elif df['Rank1 OctantID'][i]==-3:
              count_list[5]+=1  
        elif df['Rank1 OctantID'][i]==4:
              count_list[6]+=1  
        elif df['Rank1 OctantID'][i]==-4:
              count_list[7]+=1  
    #printing the count of rank 1 mod values
    for x,octval in enumerate([1,-1,2,-2,3,-3,4,-4]):
        df.at[5+len(range_list)+x,'1']=octval
        df.at[5+len(range_list)+x,'-1']=octant_name_id_mapping.get(str(octval))
        df.at[5+len(range_list)+x,'2']=count_list[x]


from platform import python_version
ver = python_version()
try:
    import pandas as pd
    try:
        #Reaading the input excel file
        df = pd.read_excel("octant_input.xlsx")
        
        #computing the average values of U,V and W and adding them to column
        U_Avg  = df['U'].mean()
        df.at[0,'U Avg']=U_Avg
        V_Avg  = df['V'].mean()
        df.at[0,'V Avg']=V_Avg
        W_Avg  = df['W'].mean()
        df.at[0,'W Avg']=W_Avg
        
        #computing U',V' and W'
        df["U'=U - U avg"]=df['U']-df['U Avg'][0]
        df["V'=V - V avg"]=df['V']-df['V Avg'][0]
        df["W'=W - W avg"]=df['W']-df['W Avg'][0]
        #Finding the Octant and adding those in Octant column
        for i in range(len(df)):
            if df["U'=U - U avg"][i]>0 and df["V'=V - V avg"][i]>0 and df["W'=W - W avg"][i]>0:
                df.at[i,"Octant"]=1
            elif df["U'=U - U avg"][i]>0 and df["V'=V - V avg"][i]>0 and df["W'=W - W avg"][i]<0:
                df.at[i,"Octant"]=-1
            elif df["U'=U - U avg"][i]<0 and df["V'=V - V avg"][i]>0 and df["W'=W - W avg"][i]>0:
                df.at[i,"Octant"]=2
            elif df["U'=U - U avg"][i]<0 and df["V'=V - V avg"][i]>0 and df["W'=W - W avg"][i]<0:
                df.at[i,"Octant"]=-2
            elif df["U'=U - U avg"][i]<0 and df["V'=V - V avg"][i]<0 and df["W'=W - W avg"][i]>0:
                df.at[i,"Octant"]=3
            elif df["U'=U - U avg"][i]<0 and df["V'=V - V avg"][i]<0 and df["W'=W - W avg"][i]<0:
                df.at[i,"Octant"]=-3
            elif df["U'=U - U avg"][i]>0 and df["V'=V - V avg"][i]<0 and df["W'=W - W avg"][i]>0:
                df.at[i,"Octant"]=4
            elif df["U'=U - U avg"][i]>0 and df["V'=V - V avg"][i]<0 and df["W'=W - W avg"][i]<0:
                df.at[i,"Octant"]=-4
        
        df['']=''
        df.at[0,'Octant ID']="Overall Count"
        df.reset_index(drop=True) 
        count1,counti,count2,countii,count3,countiii,count4,countiv=0,0,0,0,0,0,0,0

        #Calculating the count of octants (Overall count)
        #Variable count1 takes count of octant 1, Counti takes count of octant -1 and similarly for others.
        # Traversing through the column octant and add one to the respective count variable 
        for i in range(len(df)):
            if df.at[i,'Octant'] == 1:
                count1+=1
            elif df.at[i,'Octant']==-1:
                counti+=1
            elif df.at[i,'Octant']==2:
                count2+=1
            elif df.at[i,'Octant']==-2:
                countii+=1
            elif df.at[i,'Octant']==3:
                count3+=1
            elif df.at[i,'Octant']==-3:
                countiii+=1
            elif df.at[i,'Octant']==4:
                count4+=1
            elif df.at[i,'Octant']==-4:
                countiv+=1

        #Printing the overal counts
        df.at[0,'1']=count1
        df.at[0,'-1']=counti
        df.at[0,'2']=count2
        df.at[0,'-2']=countii
        df.at[0,'3']=count3
        df.at[0,'-3']=countiii
        df.at[0,'4']=count4
        df.at[0,'-4']=countiv
        df.at[1,'']="User Input"

        mod=5000
        try:
            #Function call
            octant_range_names(mod)
        except:
            print("Function not found")
        df.to_excel('octant_output_ranking_excel.xlsx', index=False)  
    except FileNotFoundError:
        print("Unable to open the file! Please check again")

except ImportError:
    print("Module Pandas not Found!")

if ver == "3.8.10":
    print("Correct Version Installed")
else:
    print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")

#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))