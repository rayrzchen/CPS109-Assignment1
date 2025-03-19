'''For my CPS109 assignment, I wish to make a program which analyze user’s 
input to help him solve a choice problem between 4 types of reinforcement 
in psychology, which I learned that in PSY107 this semester. 
After identified the reinforcement type he needs, 
my program will provide an example 
and generate a txt output if user wants it.'''

lst_r = ['pr', 'nr', 'pp', 'np'] # Lists of 4 reinforcement types

#Determine the right type of reinforcement type based on user's input
def r_chk(a, b):
    if a == 'i' and b == 'i':
        return 'pr'
    if a == 'i' and b == 'd':
        return 'nr'
    if a == 'r' and b == 'i':
        return 'pp'
    if a == 'r' and b == 'd':
        return 'np'
    return 'invalid'

# Write examples into a dictionary for further use
def ex_w(file):
    dic_ex = {}
    i = 0 #count number i
    for line in file:
        dic_ex[lst_r[i]] = line
        i += 1
    return dic_ex

# file that contains details of each reinforcements type
file = open("reinforcements.txt") 
dic_r = {} # Dictionary of details of each reinforcments type
c1 = 0 # count number c1
# Write details of reinforcements into the dictionary
for line in file:
    dic_r[lst_r[c1]] = line
    c1 += 1
file.close()

# Print the program introduction
file = open('opening.txt')
for line in file:
    print(line,end = '')
file.close()

# Get user's input, repeat if invalid
type_r = 'invalid' # Type of reinforcement
while type_r == 'invalid':
    chk_a = input('\n\nDo you wish to improve or remove your current habit?(i or r): ')
    chk_b = input('\nDo you wish to increase stimuli or decrease?(i or d): ')
    type_r = r_chk(chk_a, chk_b)
    
    # remind user that the input is invalid
    if type_r == 'invalid':
        print("You entered invalid response. Please re-enter\n")

# display the reinforcement type user needs
print('\nWhat you need is:')
print(dic_r[type_r])

# check if user needs to display an example, repeat if input invalid
chk_ex = ''
while chk_ex != 'y' and chk_ex != 'n':
    chk_ex = input("\nDo you want me to display an example for this reinforcement?(Y/N): ").lower()
    if chk_ex != 'y' and chk_ex != 'n':
        print("invalid input, please try again")
        
# display the example if user wants it
if chk_ex == 'y':
    file = open('samples.txt')
    dic_ex = ex_w(file) # only use this method when user needs an example
    file.close()
    print(dic_ex[type_r])

# check if user needs a file output. repeat if input invalid
chk_op = ''
while chk_op != 'y' and chk_op != 'n':
    chk_op = input('\nDo you want a file output for the type and the example?(Y/N): ').lower()
    if chk_op != 'y' and chk_op != 'n':
        print("invalid input, please try again")

# create the file if users needs it
if chk_op == 'y':
    file = open("cps109_a1_output.txt", 'w')
    file_ex = open('samples.txt')
    dic_ex = ex_w(file_ex) # write the dictionary of examples
    file_ex.close()
    
    # write the file output.txt
    file.write(dic_r[type_r])
    file.write("\nExample:\n")
    file.write(dic_ex[type_r])
    file.close()
    print("file created, name: cps109_a1_output.txt")

print("Thank you for using this program!")

    








