Building a website so I can easily automate the musician booking process.

Backend: Python Django

.gitignore setup to leave out files with possbile privacy issues i.e. sqlite DB and settings.py.

Users:
- Admin

- Contractors (musicians)
--> Require their own signup form. This form automatically generates a contractor profile for them.

- Clients (view the event they have booked)
--> Do not require their own signup form as this would be provided to them.

To Do:
- Client Model
- If client tries to login to contractor portal redirect them somewhere.

