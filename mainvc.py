
import os
import csv

print ("Election Results")
print("------------------------------------------")

csvpath = os.path.join("election_data.csv")

candidate = []
khan_c = 0
correy_c = 0
li_c = 0
otooley_c = 0
votes = 0
tvotes = 0

with open(csvpath) as csvfile:
    reader = csv.reader(csvfile, delimiter = ",")
    header = next(reader)
    votes += 1
         
    for row in reader:
        tvotes = tvotes +1 

        if row[2] not in candidate:
            candidate.append(row[2])

        if row[2] == "Khan":
            khan_c = khan_c +1
        
        if row[2] == "Correy":
            correy_c = correy_c +1
        
        if row[2] == "Li":
            li_c = li_c +1
        
        if row[2] == "O'Tooley":
            otooley_c = otooley_c +1

percent_Khan = round(khan_c / tvotes *100,2)
percent_correy = round(correy_c  / tvotes *100,2)
percent_li = round(li_c  / tvotes *100,2)
percent_otooley = round(otooley_c  / tvotes *100,2)

list = [percent_otooley, percent_correy, percent_Khan,percent_li]

#Print of votes
print(f'{str("Total Votes:")} {tvotes}')
#Print division
print("-----------------------------------------")

print(f'{"Khan:"} {float(percent_Khan)}{"%"} {"("}{khan_c}{")"}')
print(f'{"Correy:"} {percent_correy}{"%"} {"("}{correy_c}{")"}')
print(f'{"Li:"} {percent_li}{"%"} {"("}{li_c}{")"}')
print(f'{"OTooley:"} {percent_otooley}{"%"} {"("}{otooley_c}{")"}')

print("-----------------------------------------")    

maxl = max(list)

if maxl == percent_Khan:
    print("Winner:" + "Khan")
if maxl == percent_correy:
    print("Winner:" + "Correy")
if maxl == percent_li:
    print("Winner:" + "Li")
if maxl == percent_otooley:
    print("Winner:" + "O'Tooley")

output_file = os.path.join("py_poll.txt")
with open(output_file,"w") as text_file:
    text_file.write("Election Results")
    text_file.write("\n")
    text_file.write("------------------------")
    text_file.write("\n")
    text_file.write("Total Votes: "+ str(tvotes))
    text_file.write("\n")
    text_file.write("------------------------")
    text_file.write("\n")
    text_file.write("Khan:"+ str(percent_Khan)+"%" + "(" + str(khan_c) +")")
    text_file.write("\n")
    text_file.write("Correy:" + str(percent_correy)+"%" + "(" + str(correy_c) + ")")
    text_file.write("\n")
    text_file.write("Li:" + str(percent_li)+"%" + "("+str(li_c)+")")
    text_file.write("\n")
    text_file.write("OTooley:" + str(percent_otooley)+"%" + "("+str(otooley_c)+")")
    text_file.write("\n")
    text_file.write("------------------------")
    text_file.write("\n")
    text_file.write("Winner: " + "Khan")
    text_file.write("\n")
    text_file.write("------------------------")