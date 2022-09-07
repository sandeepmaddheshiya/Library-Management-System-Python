import time



class library():
    shell=["Python","C & C++","Web Development","Java"]
    record={}



student=library()
good_guy=library()
librarian=library()

while(True):
    print("------------------------------------------------")
    print("|                  WELCOME!                    |")
    print("|NOTHING IS PLEASANTER THAN EXPLORING A LIBRARY|")
    print("|                                              |")
    print("------------------------------------------------")
    print("LOADING...")
    time.sleep(2)

    l=int(input("SELECT: \n"
          "1: LIBRARIAN \n"
          "2: STUDENT \n"
          "3: EXIT \n"))

    if l==1:
        while(True):
            l1 = int(input("WHAT DO YOU WANT TO DO? \n"
                           "1: CHECK RECORDS \n"
                           "2: VIEW AVAILABLE BOOKS \n"
                           "3: GO BACK \n"))
            if l1==1:
                print(librarian.record)
            elif l1==2:
                print(librarian.shell)
            elif l1==3:
                break
            else:
                print("PLEASE ENTER A VALID INPUT")
                continue


    elif l==2:
        n=int(input("SELECT WHAT YOU WANT TO DO \n"
                    "1: TO LEND A BOOK \n"
                    "2: TO REUTRN A BOOK \n"
                    "3: TO DONATE A BOOK \n"
                    "4: TO EXIT \n"))

        name = input("ENTER YOUR NAME")

        if n==1:
            while(True):


                print("BOOKS AVAILABLE")
                print(library.shell)
                s1=input("ENTER THE NAME OF THE BOOK YOU WANT TO LEND")
                student.shell.remove(s1)
                student.record[f"{s1}"]=[f"{name}"]
                #Later will have to maintain the record in text file

                a1=int(input("DO YOU WANT TO LEND MORE?"
                             "1: YES"
                             "2: NO"))
                if a1==1:
                    continue
                elif a1==2:
                    break
                else:
                    print("PLEASE ENTER A VALID INPUT")


        elif n==2:
            try:
                while(True):
                    s2 = input("ENTER THE NAME OF THE BOOK YOU WANT TO RETURN")
                    student.shell.append(s2)
                    student.record.pop(s2)
                    # Later will have to maintain the record in text file

                    a2 = int(input("DO YOU WANT TO RETURN MORE?"
                                   "1: YES"
                                   "2: NO"))
                    if a2 == 1:
                        continue
                    elif a2 == 2:
                        break
                    else:
                        print("PLEASE ENTER A VALID INPUT")
            except:
                print("PLEASE LEND A BOOK FIRST")


        elif n==3:
            while (True):
                s3 = input("ENTER THE NAME OF THE BOOK YOU WANT TO DONATE")
                # Later will have to maintain the record in text file

                good_guy.shell.append(s3)
                a3 = int(input("DO YOU WANT TO DONATE MORE?"
                               "1: YES"
                               "2: NO"))
                if a3 == 1:
                    continue
                elif a3 == 2:
                    break
                else:
                    print("PLEASE ENTER A VALID INPUT")

        elif n==4:
            break

        else:
            print("PLEASE ENTER A VALID INPUT")
    elif l==3:
        break

    else:
        print("PLEASE ENTER A VALID INPUT")
        continue






