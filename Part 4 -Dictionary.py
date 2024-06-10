user_input='y'
outcome_dictionary = {'Progress': ([]), 'Progress (module trailer)': [], 'Module retriever': [], 'Exclude': []}
student_id_list = []
outcome_data_tuple=()

while user_input=='y': #First while loop
    student_id = input('Please enter student ID: ').lower()
    
    if student_id not in student_id_list:
        student_id_list.append(student_id)
    else:
        print('Student ID already exists.\n')
        continue
    while user_input=='y': #why? second while loop
        try:
            valid_credits = (0, 20, 40, 60, 80, 100, 120)
            pass_credits = int(input('Please enter your total pass credits: '))
            if pass_credits not in valid_credits:
                print('Out of range.')
                continue
            defer_credits = int(input('Please enter your total defer credits: '))
            if defer_credits not in valid_credits:
                print('Out of range.')
                continue
            fail_credits = int(input('Please enter your total fail credits: '))
            if fail_credits not in valid_credits:
                print(' Out of range.')
                continue
            if pass_credits + defer_credits + fail_credits != 120:
                print('Total incorrect.')
                print()
                continue

        except ValueError:
            print('Integer required')
            continue

        outcome_data_tuple = (student_id, pass_credits, defer_credits, fail_credits)
        if (pass_credits in valid_credits) and (defer_credits in valid_credits) and (fail_credits in valid_credits):
            if pass_credits == 120:
                outcome = "Progress"
                outcome_dictionary["Progress"].append(outcome_data_tuple)
            elif pass_credits == 100:
                outcome = "Progress (module trailer)"
                outcome_dictionary["Progress (module trailer)"].append(outcome_data_tuple)
            elif (pass_credits==80) or (pass_credits==60) or (pass_credits==40 and defer_credits>0)or (pass_credits<=20 and fail_credits<80):
                outcome = "Module retriever"
                outcome_dictionary["Module retriever"].append(outcome_data_tuple)
            else:
                outcome = "Exclude"
                outcome_dictionary["Exclude"].append(outcome_data_tuple)

        print(outcome, "\n")
        break

    user_input = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ").lower()
    print()
    if user_input == "q":
        print("Part 4:")
        for (key, value) in outcome_dictionary.items():
            for i in value:
                print(i[0] + " : " + key + " - " + str(i[1]) + ", " + str(i[2]) + ", " + str(i[3]))
        break 
    else:
        continue  # returns to the very beginning after variable declaration


        

