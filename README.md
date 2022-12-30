
# Wonder Cakes


[View the live project here](https://wondercakes.herokuapp.com/ "Link to deployed site - Wonder Cakes")

## Table of contents

1. [UX](#ux)

    * [Strategy](#strategy)

        * [Project overview](#project-overview)

        * [Project goals](#project-goals)

        * [User stories](#user-stories)

    * [Scope](#scope)

        * [Consistent features implemented](#consistent-features-implemented)

        * [Unique features implemented](#unique-features-implemented)

        * [Features left to implement](#features-left-to-implement)

    * [Structure](#structure)

        * [Database model](#database-model)
        
        * [Applications](#applications)

    * [Skeleton](#skeleton)

        * [Wireframes](#wireframes)

    * [Surface](#surface)

        * [Color scheme](#color-scheme)

        * [Typography](#typography)

        * [Imagery](#imagery)

    * [Web marketing](#web-marketing)

        * [SEO](#seo)

        * [Social media marketing](#social-media-marketing)

        * [Email marketing](#email-marketing)

        * [Privacy policy](#privacy-policy)

* [Testing](#testing)

    * [User story testing](#user-story-testing)

    * [Manual testing](#manual-testing)

    * [Bugs ans issues](#bugs-and-issues)

    * [Validator testing](#validator-testing)

* [Deployment](#deployment)

* [Credits](#credits)

    * [Technologies Used](#technologies-used)

	* [Frameworks, Libraries & Programs Used](#frameworks,-Libraries-&-Programs-Used)

	* [Content](#content)

	* [Media](#media)

* [Acknowledgments](#aknowledgements)


## UX

## 1.  Strategy

### Project overview

### Project goals

### User Stories 

## 2. Scope

### Consistent features implemented

### Unique features implemented

### Future features

## 3. Structure

### Database model

### Applications

## 4. Skeleton

### Wireframes

## 5. Surface

#### Color scheme

### Typography

### Imagery

## 6. Web marketing

### SEO

### Social media marketing

### Email marketing

### Privacy policy

## Testing

## 1. User story testing

## 2. Manual testing

### * Browser Testing

I have tested that this application works using Mackboor Air(Retina, 13-inch, 2020), with macOS Monterey 12.6 installed, using the following browsers.

* Safari Version 16.0 (17614.1.25.9.10, 17614) 
* Google Version 105.0.5195.125 (Official Build) (arm64)

## 3. Bugs and issues

## 4. Validator testing

## Deplpoyment

- This project was developed using a [GitPod](https://gitpod.io/ "Link ot GitPod") workspace. 
- The code was commited to [Git](https://git-scm.com/ "Link to Git").
- The code was pushed to [GitHub](https://github.com/ "Link to GitHub") using the terminal.

The regular process for deployment can be found on the CI Cheat Sheet from the Full Stack Framework.

### Prerequesites

1. Create a repository and workspace

* Create a repository in Github - using the Code Institute [Gitpod Full Template](https://github.com/Code-Institute-Org/gitpod-full-template "Link to gitpod template")

* Click on the green Gitpod button to load the repository workspace in Gitpod.

2. Install Django

* Install Django and Gunicorn ( it will be used to run Django on Heroku) and type the following command in the terminal:

        pip3 install Django=3.2 gunicorn

3. Add python code to .gitgnore file, that are not required in version control

        *.sqlite3
        *.pyc
        __pycache

4. Check that the project's installation is ok by running it on the server, type in the terminal:

        python3 manage.py runserver

    Then open un Port 8000 and the server should say that "The install worked successfully"

5. Run initial migrations with the following code:

        python3 manage.py migrate

6. Create a superuser, type into the terminal:

        python3 managepy createsuperuser

    and add username, email and password

7. Make initial commit to Github by typing the following code:

        git add .
        git commit -m "Initial commit"
        git push

### Deployment

1. Create an external database, using ElephantSQL.

    * Log in to [ElephantSQL.com](!https://www.elephantsql.com/) to access your dashboard.

    * Click the green button 'Create a New Instance'.

    * Set up your plan

        * Give your plan a Name (this is commonly the name of the project)
        * Select the Tiny Turtle (Free) plan
        * You can leave the Tags field blank

    * Select a data center near you.

    * Then click the 'Review' button.

    * Check your details are correct and then click “Create instance” button.

    * Return to the ElephantSQL dashboard and click on the database instance name for this project.

    * In the URL section, clicking the copy icon will copy the database URL to your clipboard.

2. Create a new Heroku app

    * Go to [Heorku Dashbord](https://dashboard.heroku.com/) and click 'New' to create a new app.

    * Give your app a name and select the region closest to you. When you’re done, click Create app to confirm.

    * Open the Settings tab.

    * Add the config var DATABASE_URL, and for the value, copy in your database url from ElephantSQL.

3. In the terminal in Gitpod:
 
    * Install dj_database_url and psycopg2, both of these are needed to connect to your external database.

        pip3 install dj_database_url==0.5.0 psycopg2

    * Update your requirements.txt file with the newly installed packages

        pip freeze > requirements.txt

    * In your settings.py file, import dj_database_url underneath the import for os

        import os
        import dj_database_url

    * Scroll to the DATABASES section and update it to the following code, so that the original connection to sqlite3 is commented out and we connect to the new ElephantSQL database instead. Paste in your ElephantSQL database URL in the position indicated.

    * In the terminal, run the showmigrations command to confirm you are connected to the external database

        python3 manage.py showmigrations

    *  If you are, you should see a list of all migrations, but none of them are checked off

    * Migrate your database models to your new database

        python3 manage.py migrate

    * Load in the fixtures. Please note the order is very important here. We need to load categories first

        python3 manage.py loaddata categories

    * Then products, as the products require a category to be set

        python3 manage.py loaddata products

    * Create a superuser for your new database

        python3 manage.py createsuperuser

4. Confirming your database

    * On the ElephantSQL page for your database, in the left side navigation, select “BROWSER”

    * Click the Table queries button, select auth_user

    * When you click “Execute”, you should see your newly created superuser details displayed. This confirms your tables have been created and you can add data to your database.

5. Set up hosting for the static and media files with AWS (Amazon Web Services).

    * Create user to acces S3 bucket:

        * In AWS account, open IAM service
        * Create a grouo for the user, ideally use a name related with the project
        * Create a policy used to give fulla access to the S3 bucket and attach it to the group
        * Create a user and add them to the group
        * Download the csv file which contains the user access key and the secret key which will be used to authenticate them from Django app.

    * Connect Django to S3 bucket and static files to S3 bucket:

        * In the Gitpod termina, install boto 3 and django-storages
        * Freeze them into requirements.txt file so they get installed on Heroku upon deployment.
        * Add 'storages' to 'installed apps' in settings.py
        * To connect Django to S3: add the below code in settings.py 

        ![connect Django to S3](#)

    * In Heroku app config vars- add the following keys: USE_AWS(value=True), AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY (values from the csv file).

    * Remove 'disable collectstatic' variable: Django will collectstatic files automatically and upload them to S3.

    * In the main project directory in Gitpod, create a file calles 'custom_storages.py' and add the following code to tell Django to use S3 to store static and media files:

        ![S3 store static media files](#)

    * Commit changes to Github.

    * Heroku build log should show all static files were collected successfully.

    * AWS S3 bucket will have a static folder which will contain all the project static files.

6. Add media files to S3 bucket:

    * Open up AWS project bucket.

    * Create a new folder called 'media'.

    * Upload all images used on site and grant public read access.

7. Final steps:

    * Add Stripe keys ( obtained from stripe account > developers > API keys) to Heroku app config vars

    * Create a new webhook endpoint that sends webhooks to the Heroku app rather than to the Gitpod workspace.

    * Add webhook signing secret to Heroku app config vars.


## Credits

* Code Institute Tutor Support: for helping me when I couldn't do it by myself.

* Code Institute: Walkthrough modules in Full Stack Frameworks.

* Code Institute Slack Community: For troubleshooting and FAQ.

* Django documentation: For clarifying all the doubts.

* Stack Overflow: For troubleshooting and FAQ.

* [!Dumpdata command from Django](https://coderwall.com/p/mvsoyg/django-dumpdata-and-loaddata)

* [!How to fix the navbar](https://stackoverflow.com/questions/68381021/how-to-separate-nav-bar-from-the-rest-of-the-page)

* [!How to make footer to stick to the bottom of page](https://dev.to/nehalahmadkhan/how-to-make-footer-stick-to-bottom-of-web-page-3i14#:~:text=To%20do%20this%20just%20remove,make%20content%20align%20to%20center.)

### 1. Technologies Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5 "Link to HTML Wiki")

- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets "Link to CSS Wiki")

- [JavaScript](https://en.wikipedia.org/wiki/JavaScript "Link to JavaScript Wiki")

- [Python](https://en.wikipedia.org/wiki/Python_(programming_language) "Link to Python Wiki")

### 2. Frameworks, Libraries & Programs Used

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

- [Unsplah](www.unsplash.com "Link to the home page"): Used for imagery.

- [Pexels](www.pexels.com "Link to the home page"): Used for imagery.

- [Pixabay](!https://pixabay.com/): Used for imagery.

- [freepik](!https://www.freepik.com/): Used for imagery.

- [Grammarly](!https://www.grammarly.com/ "Link to the home page"): Checked the grammar.

- [Canva](!https://www.canva.com/) : Helped on the making of the logo and the image for the icon.

- [JSON formatter](!https://jsonformatter.org/): Checked and validated the .json files (categories.json and products.json)

- [CSS Formatter](!https://www.cleancss.com/css-beautify/): Beautify the CSS files

- [jQuery CDN](!https://releases.jquery.com/): Used jQuery CDN for the project.

- [Sitemaps](!https://www.xml-sitemaps.com/): Generated the sitemap for my project.

- [MailChimp](!https://www.mailchimp.com/): Used for email-marketing service


### 3. Content

- [The cake shop](!https://the-cakeshop.co.uk/): Inspired and helped to understand how this type of business works.

- [Magnolia baker](!https://www.magnoliabakery.com/): Inspired and helped to understand how this type of business works.

### 4. Media

## Acknowledgments

* My mentor at Code Institute, Brian Macharia, for code review, help and feedback.

<hr>

To create an appeling website with a great UX and UI, the developer make a research throughout the best cooking blogs, with the best and worst features.


#### Strategy
- **Roles**
    - User
    - Admin


The website needs to enable the *user* to:
- search for recipes.
- make comments to a recipe.
- like and unlike recipes.
- upload images from their experiences when adding a recipe.
- register and log in to participate in the blog.
- save recipes to a favorite page.

The website needs to enable the *admin* to:
- Create drafts for finishing later.



