# Plan for Travel Site
## Databases Needed
1. users (one-to-many)
2. trips (many-to-many)

    - Fk (Foreign Key) --> 1:x
        - Creator
    - x:x -->
        - Attendees

## Templates Needed
1. Login/registration forms
2. Show all trips
    - Trips involving user
    - Trips not involving user
3. Show one trip's details
4. Add new trip

## Routes/Views Needed
### Login & Registration App
- "/" & "/main"
    - Log/reg page
- "/login"
    - Login
- "/logout"
    - Logout
### Travels App
- "/destinations/travel/{id}"
    - Show one page
- "/travels/add"
    - New trip page
- "travels"
    - Dashboard shows all trips

## Queries Needed
- Trips involving user
    - User.objects.filter(traveled_by=id)
- Trips not involving user
    - User.objects.exclude(traveled_by=id)
- Trip info
    - Trip.objects.get(id=id)

## Tests Needed


### References Used
1. Django User Auth - <https://docs.djangoproject.com/en/1.11/topics/auth/customizing/>
2. Selenium WebDriver - <http://www.seleniumhq.org/docs/03_webdriver.jsp/>