# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# IIT Student ID: 20222031
# UOW ID: w1985690
# Date: 20/04/2023

print('Part 1')  #Part 1 
while True:  
 option=input('\nPlease enter number 1 for the student version or number 2 for the staff version: ')
 print()
 if  option=='1':
        print('Student Version')
        while True:
            try:
                valid_credits=(0,20,40,60,80,100,120)
                pass_credits=int(input('Please enter your total pass credits: '))
                if pass_credits not in valid_credits:
                    print('Out of range.')
                    continue
                defer_credits=int(input('Please enter your total defer credits: '))
                if defer_credits not in valid_credits:
                    print('Out of range.')
                    continue
                fail_credits=int(input('Please enter your total fail credits: '))
                if fail_credits not in valid_credits:
                    print(' Out of range.')
                    continue
                if pass_credits + defer_credits + fail_credits!= 120:
                    print('Total incorrect.') 
                    print()
                    continue

                if (pass_credits in valid_credits) and (defer_credits in valid_credits) and (fail_credits in valid_credits):
                    if pass_credits==120:
                        print('Progress')
                        break
                    elif pass_credits==100:
                        print('Progress(module trailer)')
                        break
                    elif (pass_credits==80) or (pass_credits==60) or (pass_credits==40 and defer_credits>0)or (pass_credits<=20 and fail_credits<80):
                        print('Do not progress - module retriever')
                        break
                    else:
                        print('Exclude')
                        break
            except ValueError:
                print('Integer required')
        break
 elif  option=='2':  
        print('Staff version')
        progress_count = trailer_count = retriever_count = excluded_count = 0
        outcome_list=[]    #store outcomes 
        def histogram(progress_count, trailer_count, retriever_count, excluded_count):   #user define function to display the histogram
            print(".................................................................................\n" 
    "Histogram\n"
    "Progress", progress_count, ":", progress_count * "*", "\n"
    "Trailer", trailer_count,  ":", trailer_count * "*", "\n"
    "Retriever", retriever_count, ":", retriever_count * "*", "\n"
    "Excluded", excluded_count, ":", excluded_count * "*", "\n\n" +
    str((progress_count + trailer_count + retriever_count + excluded_count)),"outcomes in total.\n"     #calculate the outcomes and display
    "...................................................................................") 
        while True:
            try:
                valid_credits=(0,20,40,60,80,100,120)
                pass_credits=int(input('Please enter total pass credits: '))
                if pass_credits not in valid_credits:
                    print('Pass credit is in out of range.')
                    continue
                defer_credits=int(input('Please enter total defer credits: '))
                if defer_credits not in valid_credits:
                    print('Defer credit is in out of range.')
                    continue
                fail_credits=int(input('Please enter total fail credits: '))
                if fail_credits not in valid_credits:
                    print('Fail credit is in Out of range.')
                    continue
                if pass_credits + defer_credits + fail_credits!= 120:
                    print('Total incorrect.') 
                    continue
                if (pass_credits in valid_credits) and (defer_credits in valid_credits) and (fail_credits in valid_credits):
                    if (pass_credits==120):
                        outcome='Progress'
                        progress_count+=1
                        outcome_list.append(['Progress-'+str(pass_credits)+','+str(defer_credits)+','+str(fail_credits)])
                        
                    elif (pass_credits==100):
                        outcome='Progress(module trailer)'
                        trailer_count+=1
                        outcome_list.append(['Progress(module trailer)-'+str(pass_credits)+','+str(defer_credits)+','+str(fail_credits)])
                    
                        
                    elif (pass_credits==80) or (pass_credits==60) or (pass_credits==40 and defer_credits>0)or (pass_credits<=20 and fail_credits<80):
                        outcome='Do not progress - module retriever'
                        retriever_count+=1
                        outcome_list.append(['Do not progress-module retriever-'+str(pass_credits)+','+str(defer_credits)+','+str(fail_credits)])
                        
                    else:
                        outcome='Exclude'
                        excluded_count+=1
                        outcome_list.append(['Exclude-'+str(pass_credits)+','+str(defer_credits)+','+str(fail_credits)])
                    print(outcome,'\n')            
            except:
                print('Integer required')
                continue
            print('Would you like to enter another set of data?')
            while True:
                result=str(input("Enter 'y' for yes or 'q' to quit and view results: ")).lower()
                print()
                if result in('y','q'):
                    break
                else:
                    print('Wrong input!')
                    print('You should enter "y" or "q"\n ')
                    continue
            if result=='y':
                continue
            if result=='q':
                    histogram(progress_count, trailer_count, retriever_count, excluded_count)

                    #Part 2
                    print('Part 2')
                    for element in range(len(outcome_list)):   
                            print(*outcome_list[element])   #display all outcomes as a list
                            continue
                    #Part 3
            file = open('Student outcomes.txt', 'w')
            for element in range(len(outcome_list)):
                file.write(*outcome_list[element])   #write all the elemets in a text file
                file.write('\n')
            file.close()
            print("\nPart 3")
            print(open('Student outcomes.txt', 'r').read())
            break
        break
 else: 
    print("please enter either 1 or 2")
    continue
