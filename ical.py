#! /usr/bin/env python
import cgitb
#cgitb.enable()
cgitb.enable(display=0, logdir="/var/log/apache2")
import cgi

from icalendar import Calendar, Event
import requests


print ("Content-type: text/calendar; charset=utf-8\n")

#print ("Content-type: text/html\n\n")  # text/calendar; charset=utf-8
#print ("<pre>")
#print ("-----------------------")

# ---------------------------
# Decode incoming URL params
# ---------------------------
# ToDo:  cart=, url=
form = cgi.FieldStorage()
cart = form["cart"].value

# --------------------------
# Get ical data from server
# --------------------------
response = requests.get('https://recollect.a.ssl.fastly.net/api/places/1398809C-D914-11E8-9F8E-74314CD49AF7/services/298/events.en.ics?client_id=6E9C39E8-4398-11EB-9A55-553BAE06D4E6')

# --------------------------
# Filter requested events
# --------------------------
inCal = Calendar.from_ical(response.text)

outCal = Calendar()

outCal.add('VERSION', inCal['VERSION'])
outCal.add('PRODID', inCal['PRODID'])
outCal.add('METHOD', inCal['METHOD'])
outCal.add('X-PUBLISHED-TTL', inCal['X-PUBLISHED-TTL'])
outCal.add('X-WR-CALDESC', inCal['X-WR-CALDESC'])
outCal.add('X-WR-CALNAME', inCal['X-WR-CALNAME'])
outCal.add('X-WR-TIMEZONE', inCal['X-WR-TIMEZONE'])

for event in inCal.walk('vevent'):
    summary = event['SUMMARY']
    if cart in summary:
        event['SUMMARY'] = summary[summary.find(cart):]
        outCal.add_component(event)
        
#    print(event['SUMMARY'])


# --------------------------
# Ouput filtered calendar:
# --------------------------

#print (response.headers)
#print ("-----------------------")
#print (response.text)
print (outCal.to_ical().decode().replace("\r\n","\n"))
#print (outCal.to_ical().decode())
#print ("</pre>")
