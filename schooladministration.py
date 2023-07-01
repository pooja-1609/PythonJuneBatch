import csv
def write_into_csv(info_list):
    with open('student_info.csv' , 'a' , newline = '') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(["Name" , "Age" , "Contact_Number" , "E-mail ID"])
    
        writer.writerow(info_list)
condition = True
student_num = 1

while(condition):
    student_info = input("enter student information for student #{} in the following sequence (name age contact_number e-mail ID)".format(student_num))
    student_info_list = student_info.split(' ')
    print(f"\nThe entered information is such as - \nName: {student_info_list[0] }\nAge: {student_info_list[1]}\nContact_number: {student_info_list[2]}\nE-mail ID:{student_info_list[3]}")

    choice_check = input("Is the entered information correct? (yes/no):")

    if choice_check == "yes":
        write_into_csv(student_info_list)

        condition_check = input("Enter (yes/no) if you want to enter info for another student:")
        if condition_check == "yes":
            condition = True
            student_num = student_num + 1

        elif condition_check == "no":
            condition = False
    
    elif choice_check == "no":
        print("\nPlease re-enter the information!!!")
    

