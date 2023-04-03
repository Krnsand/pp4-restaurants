
## Portfolio Project 4: Full Stack Toolkit

![Multi screen mockup](static/images/multi-device-mockup.png)

This project is built as part of the Code Institute Full Stack Software Development course. I decided to make an app that would make dining and choosing restaurants a littl bit easier for some people. Important note: this is not an actual live site that exists out in the world, it is used purely as a project for Code Institute and users can make reservations freely (you won't be expected to show up at any restaurants).

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
            - [Home Page](#home-page)
            - [Make a Reservation](#make-reservation)
            - [Bookings](#bookings)
            - [Details](#details)
            - [Edit](#edit)
            - [Delete](#delete)
            - [Signup](#signup)
            - [Login](#login)
            - [Logout](#logout)
            - [Navbar](#navbar)
            - [Footer](#footer)
            - [Violet](#violet)
            - [Green](#green)
            - [Orange](#orange)
            - [Admin](#admin)
        - [Future Features](#future-features)
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
            - [Connect ElephantSQL Database:](#connect-postgres-database)
            - [Deploy App on Heroku:](#deploy-app-on-heroku)
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


#### Make Reservation

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

On this page the user can delete their reservation. It is shown with a message asking if the user is sure they want to delete. There is a back button as well in case the user does not want to delete the booking.

![delete page](static/images/home-hero-image.png)

This page is also only reachable once logged in as it contains sensitive information and no one but the user should be able to access the bookings. If someone were to try to access it without being logged in, they will get an error message.

![delete error message](static/images/dashboard.png)

#### Signup

The signup page is what it sounds like, the page where a potential user can sign up for an account! If the user is a recurring user, there is a link to the login page here as well.

![signup page](static/images/home-treatments.png)

The form shows error messages in case the form is not filled out correctly.

![signup errors](static/images/home-treatments.png)

#### Login

This page is where an already user can log into their account! If they for some reason don't already have an account, there is a link to the signup page here as well.

![login](static/images/home-about.png)

The form shows error messages in case the username and password do not match.

![login errors](static/images/home-treatments.png)

#### Logout

This is the logout page, the user is asked if they really want to log out.

![logout](static/images/home-footer.png)

#### Navbar

The navbar is visable on all pages for easy navigation. When logged in there is a "book a table" button in the navbar

![navbar in](static/images/about.png)

But when the user is not logged in, it is not possible to book a table

![navbar out](static/images/about.png)

#### Footer

The footer holds the contact information to the restaurant group Vivid Fusion. For now they handle all reservations and question, until the restaurants themselves are more self sufficient on that front.

![footer](static/images/treatments.png)

#### Violet Fusion 

This is the "Home Page" of Violet Fusion, the first restaurant in this group. Here the user can read a little bit about it before choosing to make a reservation.

![violet](static/images/gallery.png)

![violet-about](static/images/gallery-insta.png)

#### Green Dining

This is the "Home Page" of Green Dining, the second restaurant in this group. Here the user can read a little bit about it before choosing to make a reservation.

![green](static/images/gallery.png)

![green-about](static/images/gallery-insta.png)

#### Orange Cushion

This is the "Home Page" of Orange Cushion, the third and last (so far) restaurant in this group. Here the user can read a little bit about it before choosing to make a reservation.

![orange](static/images/gallery.png)

![orange-about](static/images/gallery-insta.png)


#### Error 404

This is an error page where the user has clicked on a page that is currently unavailable.

![error](static/images/logout.png)


#### Admin

Site owner has a lot of control over the website and database entries via the admin panel. If they login as a superuser, they can edit/delete/add a whole range of objects:

![admin](static/images/admin.png)

### Future Features

A future feature I would like to implement is the ability to check availability for tables at the different restaurants and in that way avoid double bookings.


## Credits

### Code

* [Codemy.com on Youtube](https://www.youtube.com/@Codemycom) - for the styling of forms as well as linking bookings to specific users.
* [AOS](https://michalsnik.github.io/aos/) - for making the dispay-delay easy 
* [Restaurantly](https://themewagon.com/themes/free-bootstrap-5-html-5-restaurant-website-template-restaurantly/) - a bootstrap template whos layout I liked but could not use straight up as it did not work well with django. I ended up copying sections of code to use in my project, see comments in code.

### Images

All images used in the readme are screenshots of the project and a multi device mock up generated with [mockup generator](https://techsini.com/multi-mockup/index.php)
All images inside the app are royalty free stock imagery.

### Technologies used

[HTML](https://html.spec.whatwg.org/) - for the structure of the website and mocking of the terminal (written by Code Institute)

[CSS](https://www.w3.org/Style/CSS/Overview.en.html) - to provide styling to the page.

[JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) - for the structure and animation of the website.

[Python](https://www.python.org/) - to write all the logic of the app

[Django](https://www.djangoproject.com/) - used as main framework for the app, which both all backend and most frontend elements are built on. The following notable libraries/packages were added to django:

* django-allauth: for handing all user models and login functionality.
* cloudinary: for saving images in cloudinary and serving them to the client.
* django-crispy-forms: for making the django forms look better.
* django-bootstrap-datepicker-plus - for the datepicker in the bookings form.

[ElephantSQL](https://www.elephantsql.com/) - used to manage a PostgreSQL database.

[Bootstrap 4](https://getbootstrap.com/) - used to style most of the project.

[Lucidchart](https://www.lucidchart.com/pages/) used to make a database diagram.

[Gitpod](https://www.gitpod.io/) - used to connect a browser based VScode to github.

[Github](https://github.com/) - used for version control and deployment of the website.

[Heroku](https://dashboard.heroku.com/) - to deploy the app.

[NuHtmlChecker](https://validator.w3.org/) - used to validate HTML.

[JigsawW3](https://jigsaw.w3.org/css-validator/validator.html.en) - used to validate css.

[JShint](https://jshint.com/) - used to validate javascript.

[PEP8 and black](https://pypi.org/project/black/) - used to format python.

[Multi Device Website Mockup Generator](https://techsini.com/multi-mockup/index.php) - to create an image of the website shown on different devices.

## Testing

Testing was done through out the project to make sure all the features work as expected. To read all about this, please go to the separate [testing document](TESTING.md).

## Security Features and Defensive Design

### User authentication

* Django's all auth was used for login and sign up functionality.
* Django's superuser is used to limit access to admin panel.

### Form Validation

Form validation is used on front end as well as backend.

### Database Security

All secret keys connecting the database are stored in a env.py file that is never pushed to github. Furthermore, Cross-Site Request Forgery (CSFR) tokens were used on all forms throughout the project.

## Deployment

### Local Deployment

To test the app locally, the terminal within VScode was used. The steps to run this:

* In your project workspace folder, open a terminal
* Run the command: ```python3 manage.py runserver```
* Hit the 'open browser' button or visit ```http://localhost:8000/``` in the browser.
* Use the website as usual.

The local database db_sqlite3 was used for most of the local deployment process, since it was easier to reset migrations in case of misatakes or a change of mind during the development process. However, in the development version, DEBUG was set to True, so that error messages would show.

### Production Deployment Initial

Before starting work, the project was deployed to Heroku. This was done early in the process, to prevent having to deal with difficulties of deployment close to the project deadline. I did however run into difficulties anyways with my static files and cloudinary, but the tutors of Code Institute helped me fix these issues. The following steps were performed for deployment:

#### Create Heroku app:

* Login in to Heroku
* Create a new app.
* Select "New" and "Create new app".
* Give the new app a name and click "Create new app".
* Select a region (Europe for this app).

#### Connect ElephantSQL Database:

* Log in to ElephantSQL.com to access your dashboard
* Click “Create New Instance”
* Set up your plan: Project name, Select the Tiny Turtle (Free) plan
* Select “Select Region” (EU-North-1 (Stockholm)) for this app
* Then click “Review”
* Click “Create instance”
* Return to the ElephantSQL dashboard and click on the database instance name for this project
* In the URL section, click the copy icon to copy the database URL
* Set up an os.environ["DATABASE_URL"]="<copiedURL>" in the env.py file

#### Deploy App on Heroku:

* Click "Settings".
* Navigate to the "Config Vars" section and click "Reveal Config Vars"
* Add SECRET_KEY variable
* Add CLOUDINARY_URL variable
* Add DATABASE_URL variables
* Add PORT 8000 variable
* Add DISABLE_COLLECTSTATIC : 1 (until final deployment, then delete that config var)
* Under "Deployment Method" click on "GitHub" to get access to your repository.
* Enable Automatic Deploys" or click "Deploy Branch" to deploy your app.


## Acknowledgements

This website was built as part of the Full Stack Software Development course from Code Institute. I would like to thank my mentor Andre Aquilina, for his excellent feedback, guidance, patience and ability to explain things in ways I understand throughout the development of the project. I would also like to thank friends and family, who all took a look at the finished project to make sure it worked well and checked if I could improve things.