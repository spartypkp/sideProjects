from twilio.rest import Client
import datetime
from datetime import timedelta

account_SID = "ACf3176b8baa00707c6b4acbf7059a77d3"
authentication = "ebef333c44b7ca186f1effc93cc75226"
client = Client(account_SID, authentication)
todays_date = datetime.date.today()

def send_message(message):

    # to the phone number you signed up for Twilio with, or upgrade your
    # account to send SMS to any phone number
    print("Sending message...")

    client.messages.create(to="+16502791844",
                           from_="13309752511",
                           body=message)

def main():


    classes = {}
    CSE331 = [("Project", "Project 3 - Red Black Trees", datetime.date(2020, 10, 22)),
              ("Homework", "Zybooks Acticity 4", datetime.date(2020, 10, 25))]

    MTH314 = [("Pre-Class", "13 - Change Basis Pre-Class-Assignment", datetime.date(2020, 10, 24)),
              ("Pre-Class", "14 - Projections Pre-Class-Assignment", datetime.date(2020, 10, 28))]

    STT180 = [("Homework", "Week 8 3-2-1 Assignment", datetime.date(2020, 10, 24)),
              ("Homework", "Homework 2", datetime.date(2020, 10, 31))]
    classes["CSE331"] = CSE331
    classes["MTH314"] = MTH314
    classes["STT180"] = STT180

    wakeup = "\n\n"
    wakeup += "================\n"
    wakeup += "Good Morning Will!\n"
    now = datetime.datetime.now()
    if now.hour > 12:
        now = "{}:{}PM".format(now.hour-12,now.minute)
    else:
        now = "{}:{}AM".format(now.hour, now.minute)
    wakeup += "It is {} in East Lansing, MI.\n".format(now)
    wakeup += "================\n\n\n"
    result = wakeup
    #print(wakeup)

    for key,val in classes.items():
        msg = "==== {} ====\n".format(key)
        #print("Key:val", key,":",val)
        val.sort()
        assignment = "NA"
        for tup in val:
            if assignment == "NA":
                assignment = tup[0]
                msg += "{} assignments:\n".format(tup[0])
            elif assignment != tup[0]:
                assignment = tup[0]
                msg += "{} assignments:\n".format(tup[0])

            delta_t = tup[2]-todays_date
            msg += "*[{}] is due in [{} days], on [{}].\n".format(tup[1],delta_t.days,tup[2])
        msg += "\n"
        result += msg
    print(result)
    send_message(result)



main()