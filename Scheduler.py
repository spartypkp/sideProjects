from twilio.rest import Client
import datetime
from datetime import timedelta

account_SID = "CHANGED FOR PRIVACY REASON"
authentication = "CHANGED FOR PRIVACY REASON"
client = Client(account_SID, authentication)
todays_date = datetime.date.today()


types_str = ["Homework", "Project", "Quiz", "Exam"]
courses_str = ["CMSE381", "CSE404", "CSE440", "CEM142", "MMG141"]

def add_assignment():
    print("==== Assignment Input ====")
    course = 0
    correct_courses = [1, 2, 3, 4, 5]
    # Get course number
    while course not in correct_courses:
        try:
            course = int(input("For which class? CMSE381 (1), CSE404 (2), CSE440 (3), CEM142 (4), MMG141 (5)"))

        except TypeError:
            print("Error. Please only input a value in [1,2,3,4,5].")
            continue
        if course in correct_courses:
            break
        print("Error. Please only input a value in [1,2,3,4,5].")

    course = courses_str[course-1]

    name = input("What is the assignment name?")


    correct_types = [1, 2, 3, 4]
    ass_type = 0
    while ass_type not in correct_types:
        try:
            ass_type = int(input("What is the assignment type? {Homework (1), Project(2), Quiz(3), Exam(4)}"))
        except TypeError:
            print("Error. Please only input a value in [1,2,3,4].")
            continue
        if ass_type in correct_types:
            break
        print("Error. Please only input a value in [1,2,3,4].")

    due_date = ""
    #00/00/00
    while(True):
        due_date = input("What is the due date? {mm/dd/yy}.")
        if len(due_date) != 8:
            print("Error. Invalid date format.")
        try:
            month = int(due_date[0:2])
            day = int(due_date[3:5])
            year = int(due_date[6:8])
            if month > 12 or month <= 0:
                print("Error. Invalid date format.")
                continue
            if day > 31 or day <= 0:
                print("Error. Invalid date format.")
                continue
            if year != 21:
                print("Error. Invalid date format.")
                continue
            break
        except:
            print("Error. Invalid date format.")

    due_date = datetime.date(2021, month, day)
    ass_str = types_str[ass_type-1]
    tup = due_date, name, ass_str, course
    with open("Data.txt", mode="a") as file:
        date_str = due_date.isoformat()
        print(date_str)
        print(type(date_str))
        line = date_str + "*" + tup[1] + "*" + tup[2] + "*" + tup[3]
        file.write(line)
        file.close()


def due_in_some_days(day_delta):
    ALL = get_ALL()
    message = "=" * 24 + "\n"
    message += "======= DUE SOON =======\n"
    delta = timedelta(days=day_delta)
    for assignment in ALL:
        date = assignment[0]
        name = assignment[1]
        ass_type = assignment[2]
        course = assignment[3]
        due_delta = date - todays_date
        if due_delta <= delta:
            message += "{}: {} [{}] is due on {} in {} days.\n".format(course, name, ass_type, date, due_delta.days)
        else:
            break
    message += "="*24 + "\n"
    return message

def due_today():
    ALL = get_ALL()
    delta = timedelta(days=1)
    message = "="*24 + "\n"
    message += "======= DUE TODAY ======\n"
    for assignment in ALL:
        date = assignment[0]
        name = assignment[1]
        ass_type = assignment[2]
        course = assignment[3]
        due_delta = date - todays_date
        if due_delta <= delta:
            message += "{}: {} [{}] is due.\n".format(course, name, ass_type)
    message += "="*24 + "\n"
    return message

def send_message(message):

    # to the phone number you signed up for Twilio with, or upgrade your
    # account to send SMS to any phone number
    print("Sending message...")

    client.messages.create(to="MY PHONE NUMBER",
                           from_="SPOLFED TWILIO NUMBER",
                           body=message)

def get_ALL():
    copy = []
    with open("Data.txt",mode="r") as file:
        for line in file:
            current = line[:-1]
            split = current.split("*")
            tup = datetime.date.fromisoformat(split[0]), split[1], split[2], split[3]
            copy.append(tup)
    copy.sort()
    return copy


def main():
    global ALL
    ALL = get_ALL()

    '''
    today_message = due_today()
    soon_message = due_in_some_days(2)
    print(today_message)
    print(soon_message)
    '''
    while(True):
        add_assignment()


if __name__ == "__main__":
    main()
