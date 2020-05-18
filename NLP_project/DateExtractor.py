import re
import string

numbers = "(^a(?=\s)|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand)"
day = "(monday|tuesday|wednesday|thursday|friday|saturday|sunday)"
week_day = "(monday|tuesday|wednesday|thursday|friday|saturday|sunday)"
month = "(january|february|march|april|may|june|july|august|september|october|november|december)"
dmy = "(year|day|week|month)"
rel_day = "(today|yesterday|tomorrow|tonight|tonite)"
expression1 = "(before|after|earlier|later|ago)"
expression2 = "(this|next|last)"
iso = "\d+[/-]\d+[/-]\d+ \d+:\d+:\d+\.\d+"
year = "((?<=\s)\d{4}|^\d{4})"
regularxp1 = "((\d+|(" + numbers + "[-\s]?)+) " + dmy + "s? " + expression1 + ")"
regularxp2 = "(" + expression2 + " (" + dmy + "|" + week_day + "|" + month + "))"

date = "([012]?[0-9]|3[01])"
regularxp3 = "(" + date + " " + month + " " + year + ")"
regularxp4 = "(" + month + " " + date + "[th|st|rd]?[,]? " + year + ")"

re1 = re.compile(regularxp1, re.IGNORECASE)
re2 = re.compile(regularxp2, re.IGNORECASE)
re3 = re.compile(rel_day, re.IGNORECASE)
re4 = re.compile(iso)
re5 = re.compile(year)
re6 = re.compile(regularxp3, re.IGNORECASE)
re7 = re.compile(regularxp4, re.IGNORECASE)

def extractDate(text):

    date_found = []

    found = re1.findall(text)
    found = [a[0] for a in found if len(a) > 1]
    for date in found:
        date_found.append(date)

    found = re2.findall(text)
    found = [a[0] for a in found if len(a) > 1]
    for date in found:
        date_found.append(date)

    found = re3.findall(text)
    for date in found:
        date_found.append(date)

    found = re4.findall(text)
    for date in found:
        date_found.append(date)

    found = re6.findall(text)
    found = [a[0] for a in found if len(a) > 1]
    for date in found:
        date_found.append(date)

    found = re7.findall(text)
    found = [a[0] for a in found if len(a) > 1]
    for date in found:
        date_found.append(date)

    found = re5.findall(text)
    for date in found:
        date_found.append(date)


    return date_found
