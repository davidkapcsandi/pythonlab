#open a new text file called teams.txt, and add the names of 5 sports teams.
#read and display the names of the 1st, 4th teams in the files.
#edit the the teams,txt file so that the top line is replaces with "new line"
#print out the edited file line by line
file = open("teams.txt", "w")
sports_teams = ["Sport1", "sport2" , "sport3", "Sport4", "sport5"]
for i in sports_teams:
    newline = i + "\n"
    file.write(newline)
file.close()

file = open("teams.txt", "r")

lines = file.readlines()

file.close()

print(lines[0].strip())
print(lines[3].strip())

file = open ("teams.txt", "r")
lines = file.readlines()
file.close
lines[0] = "New line"

file = open("teams.txt", "w")
for i in range(len(lines)):
    if i == len(lines):
        file.write(lines[i])
    else:
        file.write(lines[i].strip()+ "\n")
file.close()

file = open("teams.txt" , "r")
for line in file:
    print(line.strip())
file.close()