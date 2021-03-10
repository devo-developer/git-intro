# USING CLASS
item_no = 0
student = {}


class studentDetails:

    def switch(self):
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
        menu = input("Enter Menu Item: ")
        default = "Incorrect month"
        return getattr(self, 'menu_' + str(menu), lambda: default)()

    def menu_1(self):
        print("\n")
        print("========================")
        print("Enter Details of Student")
        print("========================")
        Roll = input("Enter the Roll No (enter 'q' to quit) : ")
        if Roll == "q":
            self.switch()
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
            self.menu_1()

    def view(self):
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

    def menu_2(self):
        self.view()
        self.switch()

    def menu_3(self):
        self.view()
        print("\n")
        u_roll = input("Enter the Roll No to Update (enter 'q' to quit) : ")
        if u_roll == 'q':
            self.switch()
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
            self.view()
            self.switch()

    def menu_4(self):
        print("\n")
        d_roll = input("Enter Roll Number to delete (enter 'q' to quit) : ")

        if d_roll in (student["roll"] for student in student.values()):

            menu_5_roll = input("Are you sure you want to delete?[y/n] : ")
            if menu_5_roll == "y":
                del student[int(d_roll)]
                print("Student has been deleted")
                self.view()
                self.menu_4()

            elif menu_5_roll == "n":
                print("Delete has been cancelled")
                self.view()
                self.menu_4()

            elif menu_5_roll == "q":
                self.view()
                self.switch()

        elif d_roll == "q":
            self.view()
            self.switch()

        else:
            print("The roll number not exist.")
            self.view()
            self.menu_5()

    def menu_5(self):
        print("Exiting...")


s = studentDetails()
s.switch()
