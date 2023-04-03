<!-- TOC -->

- [Validator Testing](#validator-testing)
    - [HTML](#html)
        - [Trailing slash](#trailing-slash)
        - [Unclosed div](#unclosed-div)
        - [Bootstrap class outside of class tag](#bootstrap-class-outside-of-class-tag)
    - [CSS](#css)
    - [Javascript](#javascript)
    - [Python](#python)
    - [Lighthouse](#lighthouse)
- [Browser Testing](#browser-testing)
- [Device Testing](#device-testing)
- [Manual Testing](#manual-testing)
    - [Site Navigation](#site-navigation)
    - [Home Page](#home-page)
    - [About Page](#about-page)
    - [Treatments Page](#treatments-page)
    - [Gallery Page](#gallery-page)
    - [Book page](#book-page)
    - [Contact page](#contact-page)
    - [User Dashboard](#user-dashboard)
- [Automated testing](#automated-testing)
    - [Running the test suite](#running-the-test-suite)
- [Bugs](#bugs)

<!-- /TOC -->

## Validator Testing

### HTML

All HTML pages were run though the [nu-html-checker](https://validator.w3.org/nu/). Most pages displayed zero errors, but some did, namely:

#### Trailing slash

One of the link elements for a css file, was closed, when link element are self closing. This means the closing slash is not necessary. Though this doesn't throw any errors, it's better to remove the slash.

![trailing-slash](static/images/html-trailing-slash.png)

#### Unclosed div

On the user dashboard page, one of the div's was not closed. This is definitely something that should be fixed, since it can cause unwanted behavior. The unclosed div caused three errors. These errors were resolved after closing the div.

![html-unclosed-div](static/images/html-unclosed-div.png)

#### Bootstrap class outside of class tag

On an h1 element, a mb-5 bootstrap class was used outside of a ```class=""``` tag. This caused the mb-5 class to have not effect. This was fixed by putting the mb-5 class inside of a class tag.

![html-bootstrap-class-without-tag](static/images/html-bootstrap-without-class.png)

### CSS

The CSS file validator had very little errors, but did show one suggestion. One of the copy-pasted classes for the hr element used on multiple pages used a ```left``` argument, when the validator would've used a ```to left``` argument. Though this didn't change any of the behavior, the argument was fixed, to be sure. After this, the CSS validator threw no further errors or warnings.

![css-validator](static/images/css-for-left.png)

### Javascript

The Javascript validator did throw a few important errors that were promptly fixed. In all JS files there were missing semi-colons, to no surprise. These were added, which resulted most JS files to come up clean. The one file that did throw some meaningful errors, was the datepicker.js file. A few of the variables in the for loops, were not declared with ```var``` or ```let```, which did not cause any functional errors, but can easily cause issues in the future. This was fixed after which no meaningful errors besides misinterpreted Django Templating warnings and JQuery warnings.

![js-validator](static/images/js-global-var-for-loop.png)

### Python

Editor suggestions for python formatting were used, using Black. A PEP8 max line-length of 99 characters was used throughout all Python files. Most errors had to do with accidental CamelCases, whitespace, missing docstrings and missing newlines.

### Lighthouse

Lighthouse was used on all pages. Almost all pages returned 90+ scores on all categories:

![lighthouse-green](static/images/lighthouse-green.png)

The Gallery page had a performance score that could be improved by lazy loading the gallery images. This can be added in a future update:

![lighthouse-orange](static/images/lighthouse-orange.png)

## Browser Testing

The project was tested extensively on Google Chrome and Safari browsers, where no browser compatibility issues came up.

## Device Testing

The project was tested on a multitude of devices: several iPhones, android phones, linux laptops and Macbook Pro. The website was properly responsive on all devices.

## Manual Testing

### Site Navigation
| Element               | Action     | Expected Result                                                    | Pass/Fail |
|-----------------------|------------|--------------------------------------------------------------------|-----------|
| NavBar                |            |                                                                    |           |
| Site Brand (logo)     | Click      | Redirect to home                                                   | Pass      |
| Home Link             | Click      | Redirect to home                                                   | Pass      |
| About Link            | Click      | Open About page                                                    | Pass      |
| Treatments link       | Click      | Open Treatments page                                               | Pass      |
| Gallery link          | Click      | Open Gallery page                                                  | Pass      |
| Book link             | Click      | Open Book page                                                     | Pass      |
| Contact link          | Click      | Open Contact page                                                  | Pass      |
| Account Dropdown      | Click      | Open My Account dropdown                                           | Pass      |
| My Account Dropdown   | Display    | 'Dashboard' and 'Logout' become visible                            | Pass      |
| Dashboard link        | Click      | Open dashboard page                                                | Pass      |
| Dashboard link        | Display    | Only visible if user is logged in                                  | Pass      |
| Logout Link           | Click      | Open logout confirm page                                           | Pass      |
| Logout Link           | Display    | Only visible if user is logged in                                  | Pass      |
| Log In Link           | Click      | Open Login page                                                    | Pass      |
| Log In Link           | Display    | Not visible if user logged in                                      | Pass      |
| Sign Up Link          | Click      | Open Sign up page                                                  | Pass      |
| All Nav Links         | Hover      | lighten text                                                       | Pass      |
| Mobile View           |            |                                                                    |           |
| Hamburger Menu        | Responsive | Display when screen size reduces to medium size                    | Pass      |
| Hamburger Menu        | Click      | Opens up hamburger menu                                            | Pass      |
| Site Brand (logo)     | Click      | Redirect to home                                                   | Pass      |
| Home Link             | Click      | Redirect to home                                                   | Pass      |
| About Link            | Click      | Open About page                                                    | Pass      |
| Treatments link       | Click      | Open Treatments page                                               | Pass      |
| Gallery link          | Click      | Open Gallery page                                                  | Pass      |
| Book link             | Click      | Open Book page                                                     | Pass      |
| Contact link          | Click      | Open Contact page                                                  | Pass      |
| Account Dropdown      | Click      | Open My Account dropdown                                           | Pass      |
| My Account Dropdown   | Display    | 'Dashboard' and 'Logout' become visible                            | Pass      |
| Dashboard link        | Click      | Open dashboard page                                                | Pass      |
| Dashboard link        | Display    | Only visible if user is logged in                                  | Pass      |
| Logout Link           | Click      | Open logout confirm page                                           | Pass      |
| Logout Link           | Display    | Only visible if user is logged in                                  | Pass      |
| Log In Link           | Click      | Open Login page                                                    | Pass      |
| Log In Link           | Display    | Not visible if user logged in                                      | Pass      |
| Sign Up Link          | Click      | Open Sign up page                                                  | Pass      |
|                       |            |                                                                    |           |
| Footer                |            |                                                                    |           |
| All links             | Click      | Open in new tab and to correct location                            | Pass      |

### Home Page
| Element               | Action  | Expected Result                 | Pass/Fail |
|-----------------------|---------|---------------------------------|-----------|
| Book Now! Button      | Click   | Open Book page                  | Pass      |
| Treatment cards       | Click   | Click on body opens treatments  | Pass      |
| Treatment cards       | Click   | Click on book opens book page   | Pass      |
| About section links   | Click   | Opens all related link          | Pass      |

### About Page
| Element               | Action  | Expected Result                 | Pass/Fail |
|-----------------------|---------|---------------------------------|-----------|
| Entire page           | Display | Responsive and readable         | Pass      |

### Treatments Page
| Element               | Action  | Expected Result                     | Pass/Fail |
|-----------------------|---------|-------------------------------------|-----------|
| Whole page            | Display | Correct treatments are displayed    | Pass      |
| Book button           | Click   | Open book page                      | Pass      |

### Gallery Page
| Element               | Action  | Expected Result                     | Pass/Fail |
|-----------------------|---------|-------------------------------------|-----------|
| Whole page            | Display | Images are displayed in carousel    | Pass      |
| Carousel              | Display | Carousel display amount of picture  | Pass      |
| Carousel              | Display | Carousel displays pictures titles   | Pass      |
| Carousel              | Click   | Carousel displays next picture      | Pass      |
| Carousel              | Click   | Carousel displays previous picture  | Pass      |
| Instagram link        | Click   | Open instagram in new tab           | Pass      |

### Book page
| Element                    | Action                                    | Expected Result                            | Pass/Fail |
|----------------------------|-------------------------------------------|--------------------------------------------|-----------|
| Open page user logged      | Display                                   | Personal info auto-filled                  | Pass      |
| Open page user not logged  | Display                                   | Personal info not auto-filled              | Pass      |
| Treatment field            | Click                                     | Available treatments dropdown              | Pass      |
| Treatment field            | Leave empty                               | On submit: form won't submit               | Pass      |
| Treatment field            | Leave empty                               | Error message displays                     | Pass      |
| Email field                | Insert incorrect format                   | On submit: form won't submit               | Pass      |
| Email field                | Insert incorrect format                   | Error message displays                     | Pass      |
| Email field                | Insert correct format                     | On submit: form submit                     | Pass      |
| Email field                | Leave empty                               | On submit: form won't submit               | Pass      |
| First name field           | Insert incorrect format                   | On submit: form won't submit               | Pass      |
| First name field           | Insert incorrect format                   | Error message displays                     | Pass      |
| First name field           | Insert correct format                     | On submit: form submit                     | Pass      |
| First name field           | Leave empty                               | On submit: form won't submit               | Pass      |
| Last name field            | Insert incorrect format                   | On submit: form won't submit               | Pass      |
| Last name field            | Insert incorrect format                   | Error message displays                     | Pass      |
| Last name field            | Insert correct format                     | On submit: form submit                     | Pass      |
| Last name field            | Leave empty                               | On submit: form won't submit               | Pass      |
| Datepicker                 | Select date                               | Date becomes blue                          | Pass      |
| Datepicker                 | Select time                               | Time becomes blue and filled in Date field | Pass      |
| Book button                | Click                                     | Appointment gets booked, user redirected   | Pass      |

### Contact page
| Element                    | Action                                    | Expected Result                            | Pass/Fail |
|----------------------------|-------------------------------------------|--------------------------------------------|-----------|
| Open page user logged      | Display                                   | Personal info auto-filled                  | Pass      |
| Open page user not logged  | Display                                   | Personal info not auto-filled              | Pass      |
| Email field                | Insert incorrect format                   | On submit: form won't submit               | Pass      |
| Email field                | Insert incorrect format                   | Error message displays                     | Pass      |
| Email field                | Insert correct format                     | On submit: form submit                     | Pass      |
| Email field                | Leave empty                               | On submit: form won't submit               | Pass      |
| First name field           | Insert incorrect format                   | On submit: form won't submit               | Pass      |
| First name field           | Insert incorrect format                   | Error message displays                     | Pass      |
| First name field           | Insert correct format                     | On submit: form submit                     | Pass      |
| First name field           | Leave empty                               | On submit: form won't submit               | Pass      |
| Last name field            | Insert incorrect format                   | On submit: form won't submit               | Pass      |
| Last name field            | Insert incorrect format                   | Error message displays                     | Pass      |
| Last name field            | Insert correct format                     | On submit: form submit                     | Pass      |
| Last name field            | Leave empty                               | On submit: form won't submit               | Pass      |
| Subject field              | Leave empty                               | On submit: form won't submit               | Pass      |
| Message field              | Leave empty                               | On submit: form won't submit               | Pass      |

### User Dashboard
| Element                    | Action                                    | Expected Result                            | Pass/Fail |
|----------------------------|-------------------------------------------|--------------------------------------------|-----------|
| Open page user logged      | Display                                   | Dashboard page is displayed                | Pass      |
| Open page user not logged  | Display                                   | User gets redirected to login page         | Pass      |
| Edit button                | Fields of personal info pop open          | On submit: form won't submit               | Pass      |
| First name field           | Insert incorrect format                   | On submit: form won't submit               | Pass      |
| First name field           | Insert incorrect format                   | Error message displays                     | Pass      |
| First name field           | Insert correct format                     | On submit: form submit                     | Pass      |
| First name field           | Leave empty                               | On submit: form won't submit               | Pass      |
| Last name field            | Insert incorrect format                   | On submit: form won't submit               | Pass      |
| Last name field            | Insert incorrect format                   | Error message displays                     | Pass      |
| Last name field            | Insert correct format                     | On submit: form submit                     | Pass      |
| Last name field            | Leave empty                               | On submit: form won't submit               | Pass      |
| Save button                | Click                                     | Form submits, alert displays               | Pass      |
| Appointment accordion      | Click                                     | Accordion opens, displays info             | Pass      |
| Appointment accordion      | Display                                   | Grey buttons if appt less than 48 hrs ahead| Pass      |
| Cancel                     | Click                                     | Modal pops up asking for confirmation      | Pass      |
| Cancel modal               | Click Cancel                              | Appointment gets canceled                  | Pass      |
| Change date                | Click                                     | Redirect to change date page               | Pass      |
| Change date page           | Display                                   | All info auto filled, only date editable   | Pass      |
| Change date page           | Change date                               | Date field is filled                       | Pass      |
| Change date button         | Click                                     | Form submits                               | Pass      |

## Automated testing

Some automated tests were written for testing views and models of both the User and Salon app. This is handy in case packages need upgrading, or major changes to the app are made. In this case, automated tests can be run first, to find obvious errors caused by the changes. After that, manual testing should still be performed.

### Running the test suite

The tests are run by entering ```python3 manage.py test``` in the terminal window (inside the project folder). This will automatically run all test. If running tests in quick succession, it's recommended to add ```--keepdb``` at the end, so the database doesn't have to be rebuild for every test cycle. The test in the suite for this project all pass, but if one would fail, it would be displayed with a clear error message, so errors can be solved.

![testing](static/images/testing.png)

## Bugs

* When trying to add ```first_name``` and ```last_name``` variables to the database, it would not save anything. The code in form.py was copied from a [medium post](https://gavinwiener.medium.com/modifying-django-allauth-forms-6eb19e77ef56), so it was time to inspect this code closer and see if anything was wrong with it. When playing around with the line ```self.cleaned_data.pop("last_name")``` the error ```'dict' does not have attribute 'pop'``` popped up. This meant it was not an array, but a dictionary. So the line had to be changed to ```self.cleaned_data["last_name"]``` and upon doing this, the first and last name did get saved to the database!
* The accordion element in the user dashboard would not get rounded borders even when ```border-radius: 2%;``` was set. This was due to the overflow not being hidden. After setting ```overflow: hidden;``` on the same element, the issue was fixed and the border-radius was now displaying properly.
* The POST method of the Dashboard view was not able to save data on existing users. The ```is_valid()``` validation would complain saying ```email already exists.``` The problem is that the method tried to create a new instance, when email (which is used as Username on the User model) should be unique, so no two users with the same email address can exist. The method however was not supposed to create a new user, but update the existing one. It took a while to find the issue, but the solution was actually quite simple: adding ```instance=request.user``` to the EditUserForm() form made the save method work on the specific user.