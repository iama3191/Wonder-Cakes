
# My mommy and me blog


[View the live project here](https://my-mommy-and-me.herokuapp.com/ "Link to deployed link - My mommy and me blog")

## Table of contents

1. [Introduction](#Introduction)

2. [UX](#UX)

	A. [Ideal User Demographic](#Ideal-User-Demographic)

	B. [User Stories](#User-Stories)

	C. [Development Plans](#Development-Plans)

	D. [Design](#Design)

3. [Features](#Features)

	A. [Existing Features](#Existing-Features)

	B. [Features to Implement in the future](#Features-to-Implement-in-the-future)

4. [Issues and Bugs](#Issues-and-bugs)

5. [Technologies Used](#Technologies-used)

	A. [Main Languages Used](#Main-Languages-Used)

	B. [Additional Languages Used](#Additional-Languages-Used)

	C. [Frameworks, Libraries & Programs Used](#Frameworks,-Libraries-&-Programs-Used)

6. [Testing](#Testing)

	A. [Testing.md](TESTING.md)

7. [Deployment](#Deployment)

8. [Credits](#Credits)

	A. [Content](#Content)

	B. [Media](#Media)

	C. [Code](#Code)

9. [Acknowledgments](#Aknowledgements)


## Introduction


## UX

### Ideal User Demographic

The ideal user of this website is:
• Parents
• Cooking Enthusiasts

### User Stories 

#### Users


#### Site Admin
1. As a site admin I can create draft posts so that I can finish writing the content later.

### Development Plans

To create an appeling website with a great UX and UI, the developer make a research throughout the best cooking blogs, with the best and worst features.


#### Strategy
- **Roles**
    - User
    - Admin

- **Demographic**
    - Parents
    - Cooking Enthusiasts

- **Psycographics**
    - Personality & Attitude:
        - Patient
        - Creative
        - Curious
    - Values:
        - Love for quality time in family
    - Lifestyle:
        - Parents
        - Interested in homemade food

The website needs to enable the *user* to:
- search for recipes.
- make comments to a recipe.
- like and unlike recipes.
- upload images from their experiences when adding a recipe.
- register and log in to participate in the blog.
- save recipes to a favorite page.

The website needs to enable the *admin* to:
- Create drafts for finishing later.

#### Scope
the scope was defined to be able to determine the work that needed to be done in terms of the features and of the strategies described.

- *Content Requirements*
The user will be expecting:
    - A comprehensive list of recipes.
    - A detailed list with ingredients and procedure.
    - A list of comments.
    - A page to find the saved recipes.

- *Functionality Requirements*
The user will be able to:
    - Navigate the site easily.
    - Select recipes for trying.
    - Add comments to every recipe.
    - Like or unlike recipes.

### Design

#### Color Scheme

#### Typography

#### Imagery

### Design

#### Data model

The project is hosted on Heroku and the database used is Heroku PostreSQL. Cloudinary is used to store all the images. Two custom models were created for the project: Recipe and Comment. This models were modified from the Walkthrough project from Code Institute 'I Think Therefor I blog'.


## Features

### Existing Features

- **Navigation Bar**

### Features to Implement in the future

- **Favorite Page**
    - Feature: Every user will have on his profile a section with all their favorite recipe (after liking it) for easy access at any time.  
    - Reason for not featuring in this release: The developer run out of enough time for implementation.

- **Third-Party Authentication**
    - Feature: The user will have the ability to register with an existent account on a social media, like Facebook or Google.
    - Reason for not featuring in this release: The developer run out of enough time for implementation.

## Issues and Bugs

**Bug:** 

## Technologies Used

### Main Languages Used
- [HTML5](https://en.wikipedia.org/wiki/HTML5 "Link to HTML Wiki")
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets "Link to CSS Wiki")
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript "Link to JavaScript Wiki")
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language) "Link to Python Wiki")

### Frameworks, Libraries & Programs Used
- [Django](https://www.djangoproject.com/ "Link to Django Project website"): Python Framework used in the development of the project.

- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/index.html "Link to django-allauth documentation"): Used for authentication and account registration.

- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/ "Link to django crispy documentation"): Used to simplify the rendering of Django forms.

- [Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/ "Link to Bootstrap page"): Bootstrap CSS Framework used for styling and to build responsive web pages.

- [Heroku](https://dashboard.heroku.com/ "Link to the Heroku Home Page"): For deployment and hosting of the application.

- [Google Fonts](https://fonts.google.com/ "Link to Google Fonts"): To import the needed fonts for the project: 'Architects Daughter' and 'Open Sans'.

- [Font Awesome](https://fontawesome.com/ "Link to FontAwesome"): Used to add icons and make the blog more interactive.

- [Git](https://git-scm.com/ "Link to Git homepage"): Used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.

- [GitHub](https://github.com/ "Link to GitHub"): Used to store the projects code after being pushed from Git and to create the Kanban board used for this project.

- [Am I Responsive?](http://ami.responsivedesign.is/# "Link to Am I Responsive Homepage"): Checking the responsive.

- [Google Translate](https://translate.google.com/ "Link to Google Translate"): Checking the grammar when needed after translating from Spanish to English.

- [Coolors](https://coolors.co/ "Link to Coolors"): Program used to check compability of color of the blog.

- [Chrome DevTools](https://developer.chrome.com/docs/devtools/ "Link to developer tools page"): Used to test the response on different screen sizes, debugging and to generate a Lighthouse report to analyze page load.

- [HTML Validator](https://validator.w3.org/): Used to check the code for HTML validation.

- [W3 CSS Validator](https://jigsaw.w3.org/css-validator/): Used to check the code for CSS validation.

- [Unsplah](www.unsplash.com "Link to the home page"): Used image for the blog.

- [Pexels](www.pexels.com "Link to the home page"): Used image for the blog.

## Testing

### Browser Testing

I have tested that this application works using Mackboor Air(Retina, 13-inch, 2020), with macOS Monterey 12.6 installed, using the following browsers.

* Safari Version 16.0 (17614.1.25.9.10, 17614) 
* Google Version 105.0.5195.125 (Official Build) (arm64)


### Responsivness


### Validator Testing

#### W3C Markup Validator:


#### W3C CSS Validator:

The W3C CSS Validator Services were used to validate the CSS to ensure there were no errors in there.


### PEP8 Online:


### Lighthouse

The Lighthouse performance tests were mande on an incognito tab for Google's recommnedation.

The tests' criterias were:

* Performance
* Accessibility
* Best Practice
* SEO

* Desktop test 

All criterias were passed with more than 90%.

![Lighthouse performance on desktop view](media/desktop-performance-lighthouse.png)

* Mobile test

I did two tests for this option, the first one had a performance score of 76%, where after reading the message I couldn't find a solution, so I tested on a Samnsung Galaxy A32, and it worked perfectly without any problem, then I repeat the test and all the criterias were passed with more than 90%.

* First Test

![Lighthouse performance on mobile view: 1st attempt](media/1-st-mobile-lighthouse-performance.png)

* Second Test

![Lighthouse performance on mobile view: 2nd attempt](media/2-nd-mobile-lighthouse-performance.png)


Coverage test result: After writing 10 tests, the coverage only got to 70% and didn't keep updating even though, every test is passed.

## Deployment

- This project was developed using a [GitPod](https://gitpod.io/ "Link ot GitPod") workspace. 
- The code was commited to [Git](https://git-scm.com/ "Link to Git").
- The code was pushed to [GitHub](https://github.com/ "Link to GitHub") using the terminal.

The regular process for deployment can be found on the CI Cheat Sheet from the Full Stack Framework.

1. How to clone the repository
2. Create Application and Postgres DB on Heroku
3. Configure Cloudinary to host images used by the application
4. Connect the Heroku app to the GitHub repository
5. Final Deployment steps

### How to clone the repository

When you clone a repository, you copy the repository from GitHub.com to your local machine.

1. Go to the https://github.com/iama3191/PP4-CI repository on GitHUb.

2. Click the 'Code' button to the right-hand side, then click HTTPs and copy the link there.

3. Open a GitBash terminal and navigate to the directory where you want to locate the clone.

4. On the command line, type "git clone" then paste in the copied url and press the Enter key to begin the clone process.

5. To install the packages required by the application use the command : pip install -r requirements.txt.

6. When developing and running the application locally set DEBUG=True in the settings.py file.

7. Changes made to the local clone can be pushed back to the repository using the following commands:

* git add filenames (or "." to add all changed files)
* git commit -m "text message describing changes"
* git push

Any changes pushed to the master branch will take effect on the live project once the application is re-deployed from Heroku.

### Create Application and Postgres DB on Heroku

1. Log in to Heroku at www.heroku.com  (create an account if needed).

2. From the Heroku dashboard, click the Create New App button.

3. On the Create New App page, enter a unique name for the application and select region. Then click Create app.

4. On the Application Configuration page for the new app, click on the Resources tab.

5. In the Add-ons search bar enter "Postgres" and select "Heroku Postgres" from the list (click the "Submit Order Form" button on the pop-up dialog.)

6. Next, click on Settings on the Application Configuration page and click on the "Reveal Config Vars" button - check the DATABASE_URL has been automatically set up.

7. Add a new Config Var called DISABLE_COLLECTSTATIC and assign it a value of 1.

8. Add a new Config Var called SECRET_KEY and assign it a value (any random string of letters, digits and symbols.)

9. The settings.py file should be updated to use the DATABASE_URL and SECRET_KEY environment variable values as follows :

    * DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}

    * SECRET_KEY = os.environ.get('SECRET_KEY')

10. In Gitpod, in the project terminal window, to initialize the data model in the postgres database, run the command : python3 manage.py migrate

11. Make sure the project requirements.txt file is up to date with all necessary supporting files by entering the command : pip3 freeze --local > requirements.txt

12. Commit and push any local changes to GitHub.

In order to be able to run the application on localhost, add SECRECT_KEY and DATABASE_URL and their values to env.py

### Configure AWS


### Connect the Heroku app to the GitHub repository

1. Go to the Application Configuration page for the application on Heroku and click on the Deploy tab.

2. Select GitHub as the Deployment Method and if prompted, confirm that you want to connect to GitHub. Enter the name of the github repository (the one used for this project is (https://github.com/iama3191/PP4-CI) and click on Connect to link up the Heroku app to the GitHub repository code.

3. Scroll down the page and choose to either Automatically Deploy each time changes are pushed to GitHub, or Manually deploy - for this project Manual Deploy was selected.

4. The application can be run from the Application Configuration page by clicking on the Open App button.


The live link for this project is (https://wondercakes.herokuapp.com/)


### Final Deployment steps

Once code changes have been completed and tested on localhost, the application can be prepared for Heroku deployment as follows:

1. Set DEBUG flag to False in settings.py.

2. Ensure this line exists in settings.py to make summernote work on the deployed environment (CORS security feature): X_FRAME_OPTIONS = 'SAMEORIGIN'.

3. Ensure requirements.txt is up to date using the command : pip3 freeze --local > requirements.txt.

4. Push files to GitHub

5. In the Heroku Config Vars for the application delete this environment variable : DISABLE_COLLECTSTATIC.

6. On the Heroku dashboard go to the Deploy tab for the application and click on deploy branch.


## Credits

* Code Institute Tutor Support: for helping me when I couldn't do it by myself.

* Code Institute: Walkthrough modules in Full Stack Frameworks.

* Code Institute Slack Community: For troubleshooting and FAQ.

* Django documentation: For clarifying all the doubts

* Stack Overflow: For troubleshooting and FAQ.

* [!Dumpdata command from Django](https://coderwall.com/p/mvsoyg/django-dumpdata-and-loaddata)


### Code



## Acknowledgements

* My mentor at Code Institute, Brian Macharia, for code review, help and feedback.


