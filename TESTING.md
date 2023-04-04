<!-- TOC -->

- [Validator Testing](#validator-testing)
    - [HTML](#html)
        - [Unclosed div](#unclosed-div)
    - [CSS](#css)
    - [Javascript](#javascript)
    - [Python](#python)
    - [Lighthouse](#lighthouse)
- [Browser Testing](#browser-testing)
- [Device Testing](#device-testing)
- [Manual Testing](#manual-testing)
- [Bugs](#bugs)

<!-- /TOC -->

## Validator Testing

### HTML

All HTML pages were run though the [nu-html-checker](https://validator.w3.org/). Most pages displayed zero errors, but some did, namely:

#### Open divs

After closing a couple open divs there were no errors in my HTML

![open div](static/assets/img/README-img/html.png)


### CSS

The only error I got was a missing s on a display-delay class, after fixing that there were no errors

![css-validator](static/assets/img/README-img/css.png)

### Javascript

I did not write the js myself, this I copied from the before mentioned template. With this said, there were no errors, just warnings. All missing semicolons were added but the warnings I left be

![js-validator](static/assets/img/README-img/javascript.png)

### Python

Editor suggestions for python formatting were used, using Black. A PEP8 max line-length of 79 characters was used throughout all Python files. All lasting errors are lines too long that I didn't manage to section off without breaking the code.

### Lighthouse

Lighthouse was used on all pages. Almost all pages returned around 90 scores on all categories, however, there were a few mentions in the console about error messages being shown in the console. WIll look into this till next project.:

![lighthouse](static/assets/img/README-img/lighthouse.png)

## Browser Testing

The project was tested extensively on Google Chrome and Safari browsers, where no browser compatibility issues came up.

## Device Testing

The project was tested on a multitude of devices: several iPhones, android phones, linux laptops and Macbook Pro. The website was properly responsive on all devices.

## Manual Testing

I have tested every button manually to make sure they all work as intended. I have tested to redirect my browser to different view paths from when being logged off to see if I can access those pages without being logged in, without success. 

## Bugs

* When trying to add ```first_name``` and ```last_name``` variables to the database, it would not save anything. The code in form.py was copied from a [medium post](https://gavinwiener.medium.com/modifying-django-allauth-forms-6eb19e77ef56), so it was time to inspect this code closer and see if anything was wrong with it. When playing around with the line ```self.cleaned_data.pop("last_name")``` the error ```'dict' does not have attribute 'pop'``` popped up. This meant it was not an array, but a dictionary. So the line had to be changed to ```self.cleaned_data["last_name"]``` and upon doing this, the first and last name did get saved to the database!
* The accordion element in the user dashboard would not get rounded borders even when ```border-radius: 2%;``` was set. This was due to the overflow not being hidden. After setting ```overflow: hidden;``` on the same element, the issue was fixed and the border-radius was now displaying properly.
* The POST method of the Dashboard view was not able to save data on existing users. The ```is_valid()``` validation would complain saying ```email already exists.``` The problem is that the method tried to create a new instance, when email (which is used as Username on the User model) should be unique, so no two users with the same email address can exist. The method however was not supposed to create a new user, but update the existing one. It took a while to find the issue, but the solution was actually quite simple: adding ```instance=request.user``` to the EditUserForm() form made the save method work on the specific user.