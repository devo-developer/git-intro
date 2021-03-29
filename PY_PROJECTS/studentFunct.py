# USING FUNCTION - CURD APP Student Details
item_no = 0
student = {}


def menu():
    global item_no
    print("\n")
    print("=========================")
    print("Choose a menu item {1..5}")
    print("=========================")
    print("1.Add Details")
    print("2.Print student Details")
    print("3.Edit student Details")
    print("4.Detele Student Detail")
    print("5.Exit")
    print("==========================")
    item_no = input("Enter Menu Item: ")
    indirect(int(item_no))


def add():
    print("\n")
    print("========================")
    print("Enter Details of Student")
    print("========================")
    Roll = input("Enter the Roll No (enter 'q' to quit) : ")
    if Roll == "q":
        indirect(0)
    else:
        Name = input("Enter the Name: ")
        Gender = input("Enter the Gender: ")
        Total = input("Enter the Total Marks: ")

        student[int(Roll)] = {
            "roll": Roll,
            "name": Name,
            "gender": Gender,
            "total": Total
        }
        print("\n")
        print("Successfully Added the details:")
        add()


def view():
    print("\n")
    print("=====================================================")
    print("Roll no\t\tName\t\tGender\t\tTotal")
    print("=====================================================")
    for p_id, p_info in student.items():
        info_dictionary = p_info

        values = info_dictionary.values()
        values_list = list(values)
        print(values_list[0]+'\t\t'+values_list[1]+'\t\t' +
              values_list[2]+'\t\t'+values_list[3]+'\t\t')
    print("=====================================================")


def display():
    view()
    indirect(0)


def edit():
    view()
    print("\n")
    u_roll = input("Enter the Roll No to Update (enter 'q' to quit) : ")
    if u_roll == 'q':
        indirect(0)
    else:
        print("If you do not want to update a property enter nothing")
        for p_id, p_info in student.items():
            roll_no = p_info["roll"]
            if roll_no == u_roll:

                u_name = input("Enter the Name: [" + p_info["name"] + "] ")
                if u_name == "":
                    p_info.update({"name": p_info["name"]})
                else:
                    p_info.update({"name": u_name})
                u_gender = input(
                    "Enter the Gender: [" + p_info["gender"] + "] ")
                if u_gender == "":
                    p_info.update({"gender": p_info["gender"]})
                else:
                    p_info.update({"gender": u_gender})
                u_total = input(
                    "Enter the Total Mark: [" + p_info["total"] + "] ")
                if u_total == "":
                    p_info.update({"total": p_info["total"]})
                else:
                    p_info.update({"total": u_total})
        print("Updation Successful...")
        view()
        indirect(0)


def delete():
    print("\n")
    d_roll = input("Enter Roll Number to delete (enter 'q' to quit) : ")

    if d_roll in (student["roll"] for student in student.values()):

        delete_roll = input("Are you sure you want to delete?[y/n] : ")
        if delete_roll == "y":
            del student[int(d_roll)]
            print("Student has been deleted")
            view()
            delete()

        elif delete_roll == "n":
            print("Delete has been cancelled")
            view()
            delete()

        elif delete_roll == "q":
            view()
            indirect(0)

    elif d_roll == "q":
        view()
        indirect(0)

    else:
        print("The roll number not exist.")
        view()
        delete()


def ext():
    print("Exiting...")


def indirect(i):
    switcher = {
        0: menu,
        1: add,
        2: display,
        3: edit,
        4: delete,
        5: ext
    }
    func = switcher.get(i, lambda: print('Invalid'))
    return func()


indirect(item_no)
