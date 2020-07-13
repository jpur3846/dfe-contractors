Building a website so I can easily automate the musician booking process.

Backend: Python Django

Users:
- Admin

- Contractors (musicians)
--> Require their own signup form. This form automatically generates a contractor profile for them.

- Clients (view the event they have booked)
--> Do not require their own signup form as this would be provided to them.

To Do:
- Client Model
- If client tries to login to contractor portal redirect them somewhere.
- User forgotten password
- Make invoice and other aspects have all details.
- Pretty up views.
- Feedback form.
- Gig history
- Comment on events
- Complete event details -> calculate GST etc.
- Con-client app for their special view
- User updates need to propagate through the system.
- Standardise profile picture size
- Singer songlist
- Create a blacklist option.

NB/Other Issues to fix:
- Block get requests to worksheets (i.e. events/1) or wrong number/404.
- .gitignore setup to leave out files with possbile privacy issues i.e. sqlite DB and secret key.

Dependencies:
- Django
- Python 3
- Pillow
- Report lab (python3 -m pip install reportlab) for PDFs
- pip install --pre xhtml2pdf 
- Email Debugging python -m smtpd -n -c DebuggingServer localhost:1025