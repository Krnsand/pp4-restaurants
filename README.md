
## Portfolio Project 4: Full Stack Toolkit

![Multi screen mockup](static/images/multi-device-mockup.png)

This project is built as part of the Code Institute Full Stack Software Development course. For this course, Dirk Ornee had to built a fourth Portfolio Project. Since his cousin just started a nail salon and was in dire need of a website with booking capabilities, what better way to build a fourth Portfolio Project and help somebody at the same time! Important note: this is not the actual live version that is used by the nail salon, this version is used purely as a project for Code Institute and users can book appointments freely (you won't suddenly be expected to show up at a nail salon).

## Live Site

[Vivid Fusion](https://restaurant-concept.herokuapp.com/)

## Github Repository

[PortfolioProjectFour](https://github.com/DOdrums/PortfolioProjectFour)


<!-- TOC -->

- [Smart House Inventory](#smart-house-inventory)
    - [Portfolio Project 4: Full Stack Toolkit](#portfolio-project-4-full-stack-toolkit)
    - [Live Site](#live-site)
    - [Github Repository](#github-repository)
    - [UX](#ux)
        - [Business Goals](#business-goals)
        - [Target Audience](#target-audience)
        - [User Stories](#user-stories)
        - [Structure of the app](#structure-of-the-app)
        - [Logic/Database Diagram](#logicdatabase-diagram)
        - [Color Scheme](#color-scheme)
        - [Features](#features)
            - [Book page](#book-page)
            - [User dashboard](#user-dashboard)
            - [Home](#home)
            - [Nav bar](#nav-bar)
            - [Hero Image](#hero-image)
            - [Treatments](#treatments)
            - [About](#about)
            - [Footer](#footer)
            - [About](#about)
            - [Treatments](#treatments)
            - [Gallery](#gallery)
            - [Contact](#contact)
            - [Login/Logout](#loginlogout)
            - [Admin](#admin)
        - [Future Features](#future-features)
            - [Notifications](#notifications)
    - [Credits](#credits)
        - [Code](#code)
        - [Images](#images)
        - [Technologies used](#technologies-used)
    - [Testing](#testing)
    - [Security Features and Defensive Design](#security-features-and-defensive-design)
        - [User authentication](#user-authentication)
        - [Form Validation](#form-validation)
        - [Database Security](#database-security)
    - [Deployment](#deployment)
        - [Local Deployment](#local-deployment)
        - [Production Deployment Initial](#production-deployment-initial)
            - [Create Heroku app:](#create-heroku-app)
            - [Connect Postgres Database:](#connect-postgres-database)
            - [Deploy App on Heroku:](#deploy-app-on-heroku)
        - [Production Deployment Update](#production-deployment-update)
            - [PostgreSQL database:](#postgresql-database)
    - [Acknowledgements](#acknowledgements)

<!-- /TOC -->


## UX

### Business Goals

The main goal of this project is to give a user the ability to book appointments at the Vivid Fusion Restaurant Group. User should also get a good sense of the different restaurants the are included in this special group concept and know what to expect from each individual restaurant. When the user has made a reservation at one of the restaurants, they should be able to edit and delete said reservation on an account page.

### Target Audience

The target audience is anyone who likes food and would enjoy a concept like this, where they have all the information they might need in one place as well as a broad variety of food to try.

### User Stories

User stories were written with frequent restuarant goers in mind, as well as people how might not go out too often. They were all written to fit within the agile methodology and they have the following criteria:

* title
* clear description
* acceptance criteria
* tasks, when acceptance criteria alone weren't clear enough
* epic
* priority (must have, should have, could have)

In the picture below you can see an example of the user stories before work on the project was started:

![user stories board](static/images/user-stories-1.png)

And the user stories board after finishing the project:

![user stories board updated](static/images/user-stories-2.png)

As you can see there are three stories left, none of them were Must-Haves however so I felt ok with leaving them behing. To view all the user stories in detail, visit the project page: [user stories board](https://github.com/users/DOdrums/projects/3/views/1)


### Structure of the app

The app is designed to have be easily navigated, highly accessable from every page, as well as with a strong focus on the booking functionality. All pages include the booking button when the user is logged in. The home page specifically features a booking button right on top, as well as one right in the middle of the welcome image so it is easy to book whener the user feels inclined.

### Logic/Database Diagram

The logic of the app was thought out by making a database diagram, to visualize which objects will need to be created for this app to be functional and how they will be connected to each other. Notably, the initial database diagram was incomplete, which was discovered during production of the app. See the images below:

Initial database diagram:

![database diagram](static/images/database-diagram.png)

Updated database diagram:

![database diagram](static/images/database-diagram-updated.png)

Django's Class-Based Generic Views were used, to build the models in an Object Oriented way. For the User model specifically, the Django package 'AllAuth' was used. This does a lot of the work for you, like creating unstyled login, sign-up and forgot password pages and functionality and creating the User model and User Manager model. For the purposes of this project, I decided that the 'AllAUth' packaged templates were just fine, I would however in the fututre like to override them and make something on my own. 

My models are as followed:

The Restaurant model:

* used to create restaurants in the admin panel to be viewed on the live site and bookable
* displays the name of the restaurant, an adress as well as opening/closing times and if it is open on mondays and tuesdays or not

The Booking model:

* used to create bookings in the admin panel as well as to be used in a booking form on the live site
* as the fields for restaurant, user, name, email, date, time, number of guests and for a comment if the user has any allergies or dietary restrictions the restaurant might need to know
* was used to develop the reservations form on the site

The User model:

* built with Django AllAuth.


### Color Scheme

The color scheme of the site was inspired by the hero image that I really liked, see the image below. I feel it creates a coherent theme accross the site without being too repetitive. The forms are styled to collaborate with the navbar, darker and sleek. While the cards are meant to be more light and matched with the image with a more rounded feel to them.

![color scheme](static/images/color-scheme.png)

### Features

The app's biggest feature is the home page. Read more about it in its section. Then we have the "Book a table" page where the user can make areservation, and the bookings page where the user can view, edit and delete their resevations. The navbar is featured on all pages and from there the user can go to the booking page to make a reservation, their individual booking page where their reservations are listed, as well as log in or out.

#### Home page

The home page has an about section, a gallery of images "from the restaurants", as well as a section where the user can click on each restaurant to go to their individual page if they want to know more about them before making a reservatoin. These pages are mostly just to give a brief introduction to the restaurants and give the user a feel for their atmosphere, not to be a complete restaurant website in itself.

![home page](static/images/book.png)

The about page is meant to introduce the user to the restaurant concept as well as give a very brief explanation of what to be expected from the different restaurants

![about page](static/images/book-selected-treatment.png)

The restaurant boxes are links to the different restaurants where the user is introduced a little bit more to the individual restaurants as well as they allow the users to get a feel for the place, if it will be a place where they will find joy or not.

![restaurants boxes](static/images/book-confirmation.png)

The gallery shows some pictures "from the restaurants" (these aren't real restaurants if that was wasn't clear) to give the users a welcoming feel and tickle their intrerest into making a reservation

![gallery](static/images/book-confirmation.png)


#### Make a Reservation

This page is just a reservations form. Here the user can choose which restaurant they want to make a reservation at, how many their party will consist of, at what date and time, as well as leave a comment if there is any addintional information the restaurant might need. 

![reservations form](static/images/dashboard.png)

This page is only reachable once logged in as you need an account to make a reservation.

![error message reservation](static/images/dashboard.png)

Once a reservation has been made, the user gets a message to confirm the reservation.

![reservations confirmed](static/images/dashboard.png)


#### Bookings page

Here the user is greeted with a page with all their bookings (if they have any yet) as neat little cards that they can click on to get the details about individual bookings. These reservation cards are listed in the order of the nearest date, so that the user  will know which of their many many lovely dinner reservations is next in line at all times.

![bookings page](static/images/dashboard.png)

This page is only reachable once logged in as it contains sensitive information. If someone were to try to access it without being logged in, they will be directed to the signup page.


#### Details page 

The details page shows the user the details of ther reservations. The restaurant, the date and time, number of guests, as well as their comment if they decided to leave one. Here the user can also choose to edit or delete their reservations. There are buttons that will tak ethem to the next page, or back to their bookings page if they rather want that.

![details page](static/images/nav-home.png)

This page is also only reachable once logged in as it contains sensitive information and no one but the user should be able to access the bookings. If someone were to try to access it without being logged in, they will get an error message.

![details error message](static/images/dashboard.png)

#### Edit page

On this page the user can edit their reservations. The fields that can be edited are, time, date, number of guests and the comment. If the user wants to change the restaurant they will have to delete the reservation make a new one instead.

![edit page](static/images/nav-other.png)

This page is also only reachable once logged in as it contains sensitive information and no one but the user should be able to access the bookings. If someone were to try to access it without being logged in, they will get an error message.

![edit error message](static/images/dashboard.png)

#### Delete page

On this page the user can delete their reservation.

![delete page](static/images/home-hero-image.png)

This page is also only reachable once logged in as it contains sensitive information and no one but the user should be able to access the bookings. If someone were to try to access it without being logged in, they will get an error message.

![delete error message](static/images/dashboard.png)

#### Signup page

The signup page is what it sounds like, the page where a potential user can sign up for an account!

![signup page](static/images/home-treatments.png)

#### About

Below the treatments, user will find a little text about the salon, with a photo.

![home-about](static/images/home-about.png)

#### Footer

At the bottom of the page, there is a footer. The footer houses a map with the location of NailsbyFaar, some contact info and the social links.

![home-footer](static/images/home-footer.png)

#### About

The next page is the about page. This is simply an extension of the about section on the home page and features an image and some text about the owner of the salon.

![about](static/images/about.png)

#### Treatments

The treatments page features the main treatments with explanations of what they are. There is also a book button for the user to immediately book an appointment.

![treatments](static/images/treatments.png)

#### Gallery 

The gallery page displays a little gallery with some images of recent work done by Nailsbyfaar. On the bottom of the page, the user is encouraged to visit her instagram.

![gallery](static/images/gallery.png)

![gallery-insta](static/images/gallery-insta.png)

#### Contact

The contact page displays a simple form for the user to fill out in order to send a message to the owner.

![contact](static/images/contact.png)

#### Login/Logout

If a user doesn't have an account yet, they can sign up, by filling in the form.

![signup](static/images/sign-up.png)

Once a user has an account, they can login.

![login](static/images/login.png)

If the user wants to logout via the navbar, they'll have to confirm this decision.

![logout](static/images/logout.png)


#### Admin

Site owner has a lot of control over the website and database entries via the admin panel. If they login as a superuser, they can edit/delete/add a whole range of objects:

![admin](static/images/admin.png)

The user can look at registered email-adresses, appointments, gallery images, planning, treatments and users. The social accounts are not in use and groups can be used if wanted. Let's have a look at some of them.

The first thing you would probably add is a planning, so users know which times they can book. This is what the planning object looks like:

![admin-planning](static/images/admin-planning.png)

After adding a planning, some treatments should be added, so a user can actually book a treatment. The treatments can be displayed in the booking module, on the home page and treatment page, both or neither. This is what the overview of different treatments will look like:

![admin-treatments](static/images/admin-treatments.png)

A treatment object looks as follows:

![admin-change-treatment](static/images/admin-change-treatment.png)

After adding these object, a user should now be able to see a fully functional book page and be able to book an appointment. After some appointments are booked, you'll see a list of appointments in the admin panel:

![admin-appointments](static/images/admin-appointments.png)

Which when opened, look as follows:

![admin-change-appointment](static/images/admin-change-appointment.png)

The final thing that can be added is some images for the gallery page.

![admin-gallery](static/images/admin-gallery.png)

### Future Features

An important feature for the admin, is a link to a google agenda that displays all appointments in a calender. This way, there is a clear and easy oversight in the planning. This was also the only remaining user story.

#### Notifications

Users can already receive notifications via email, but it would be great to have the option of enabling sms notifications, since these tend to reach the user better (no danger of ending up in the spam folder).


## Credits

### Code

* [Stackoverflow(answer from 'Aaron')](https://stackoverflow.com/a/61139427/16545052) - for the regex validation on the 'allowed_times' model.
* [Stackoverflow(answer from 'xyres')](https://stackoverflow.com/a/43305140/16545052) - for using Django context variables in Javascript.
* [Reddit(answer from OP himself)](https://www.reddit.com/r/django/comments/ma35nu/django_allauth_custom_signup_form_doesnt_save_all/) - to allow allauth adapter to be overriden, for saving of phone numbers in database.
* [Medium article](https://gavinwiener.medium.com/modifying-django-allauth-forms-6eb19e77ef56) - for adding extra fields to allauth.
* [Medium article](https://medium.com/@ksarthak4ever/django-custom-user-model-allauth-for-oauth-20c84888c318) - for making a custom user model connected to allauth.
* [Stackoverflow(answer from 'Stilian')](https://stackoverflow.com/a/67664840/16545052) - for the clean method in the booking form
* [Stackeroverflow(answer from 'Colin')](https://stackoverflow.com/a/36925822/16545052) - for making a workaround for the disabled field in the booking form
* [Stackeroverflow(answer from 'Devang Padhiyar')](https://stackoverflow.com/a/55561290/16545052) - to add two querysets together in Dashboard view
* [Stackeroverflow(answer from 'fceruti')](https://stackoverflow.com/a/9957402/16545052) - to update a user instances information in the POST method of the Dashboard view.
* [Stackeroverflow(answer from 'Alex Fuentes')](https://stackoverflow.com/a/25319333/16545052) - to make the alert message that appears when editing user data slide up after 4 seconds. 
* [Codepen](https://codepen.io/dotproto/pen/mdOXve) - for the css code of a divider used on homepage.
* [Stackeroverflow(answer from 'Griffosx')](https://stackoverflow.com/a/13624393/16545052) - to check if loop index is even or uneven in treatments page. 
* [Stackoverflow(answer from 'vee')](https://stackoverflow.com/a/70415401/16545052) - to listen to the mobile navbar events.
* [Github(responsive-html-email-template)](https://github.com/leemunroe/responsive-html-email-template) - for a basic html template for emailing.


### Images

All images used in the readme are screenshots of the project and a multi device mock up generated with [mockup generator](https://techsini.com/multi-mockup/index.php)
Images inside the app are either royalty free stock imagery, or courtesy of NailsbyFaar.

### Technologies used

[HTML](https://html.spec.whatwg.org/) - for the structure of the website and mocking of the terminal (written by Code Institute)

[HTMLemail/inline](https://htmlemail.io/inline/) - for making the email html template into inline html.

[CSS](https://www.w3.org/Style/CSS/Overview.en.html) - to provide styling to the page.

[JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) - for the structure of the website and mocking of the terminal (written by Code Institute)

[Python](https://www.python.org/) - to write all the logic of the app

[Django](https://www.djangoproject.com/) - used as main framework for the app, which both all backend and most frontend elements are built on. The following notable libraries/packages were added to django:

* django-ses: for handling emails with Amazon's SES.
* django-allauth: for handing all user models and login functionality.
* cloudinary: for saving images in cloudinary and serving them to the client.
* django-crispy-forms: for making the django forms look better.

[ElephantSQL](https://www.elephantsql.com/) - used to manage a PostgreSQL database.

[Bootstrap 5.2](https://getbootstrap.com/) - used to style the grunt of the project.

[Jquery](https://jquery.com/) - to make DOM manipulation a bit less painful.

[Lucidchart](https://www.lucidchart.com/pages/) used to make a database diagram.

[Gitpod](https://www.gitpod.io/) - used to connect a browser based VScode to github.

[Github](https://github.com/) - used for version control and deployment of the website.

[Heroku](https://dashboard.heroku.com/) - to deploy the app.

[JShint](https://jshint.com/) - used to validate javascript.

[NuHtmlChecker](https://validator.w3.org/nu/) - used to validate HTML.

[Multi Device Website Mockup Generator](https://techsini.com/multi-mockup/index.php) - to create an image of the website shown on different devices.

## Testing

Extensive testing was done to make sure all the features work as expected. To read all about this, please go to the separate [testing document](TESTING.md).

## Security Features and Defensive Design

### User authentication

* Django's all auth was used for login and sign up functionality.
* Django's superuser is used to limit access to admin panel.

### Form Validation

Extensive form validation is used on front end as well as backend.

### Database Security

All secret keys connecting the database are stored in a env.py file that is never pushed to github. Furthermore, Cross-Site Request Forgery (CSFR) tokens were used on all forms throughout the project.

## Deployment

### Local Deployment

To test the app locally, the terminal within VScode was used. The steps to run this:

* In your project workspace folder, open a terminal
* Run the command: ```python3 manage.py runserver```
* Hit the 'open browser' button or visit ```http://localhost:8000/``` in the browser.
* Use the website as usual.

A local database was used for most of the local deployment usage, since it was necessary for the automated tests to run. However, the switch to using the production database could be easily made, in case migrations needed to be performed or otherwise. Furthermore, in the development version, DEBUG was set to False, so error messages would show follow.

### Production Deployment Initial

Before starting work, the project was deployed to Heroku. This was done early in the process, to prevent having to deal with difficulties of deployment close to the project deadline. The following steps needed to be performed:

#### Create Heroku app:

* Login in to Heroku
* Create a new app.
* Select "New" and "Create new app".
* Give the new app a name and click "Create new app".
* Select a region (Europe for this app).

#### Connect Postgres Database:

* Open your app on the main dashboard of Heroku.
* Open the Resources tab and scroll to the add-ons section.
* Type 'Postgres' and select the Heroku Postgres option.
* Copy the DATABASE_URL in the Config Vars section of the Settings tab.
* To use the Postgres database in your development environment, copy the DATABASE_URL in your env.py file.

#### Deploy App on Heroku:

* Click "Settings".
* Navigate to the "Config Vars" section and click "Reveal Config Vars"
* Add SECRET_KEY variable
* Add CLOUDINARY_URL variable
* Add AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY variables.
* Under "Deployment Method" click on "GitHub" to get access to your repository.
* Enable Automatic Deploys" or click "Deploy Branch" to deploy your app.

### Production Deployment Update

Since Heroku stopped offering free tiers on the 28th of november 2022, it was necessary to make a few adjustments to the whole production deployment of the app. 

#### PostgreSQL database:

The Postgres database add-on that was previously used within Heroku was now no longer free and thus a different service had to be used. The choice went to [ElephantSQL](https://www.elephantsql.com/), since they offer a free tier. A [script](https://github.com/Code-Institute-Org/postgres-migration-tool) written by Code Institutes team was used to copy the original database to the new database. The steps are described in the [github readme](https://github.com/Code-Institute-Org/postgres-migration-tool) of that script.

After that, the steps were as follows:

* remove database add on from Heroku.
* remove old DATABASE_URL config var from settings and post new url from ElephantSQL database in its place.
* transform app from free tier to an eco dyno.

## Acknowledgements

This website was built as part of the Full Stack Software Development course from Code Institute. I would like to thank my mentor Adeye Adegbenga, for his excellent feedback and guidance throughout the development of the project. I would also like to thank friends and family, who all took a look at the finished project to make sure it worked well and checked if I could improve things.