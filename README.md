
# Wonder Cakes


[View the live project here](https://my-mommy-and-me.herokuapp.com/ "Link to deployed site - Wonder Cakes")

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

<hr>
Need to check this 

1. How to clone the repository
2. Create Application and Postgres DB on Heroku
3. Configure Cloudinary to host images used by the application
4. Connect the Heroku app to the GitHub repository
5. Final Deployment steps

<hr>

### How to clone the repository

When you clone a repository, you copy the repository from GitHub.com to your local machine.

1. Go to the https://github.com/iama3191/PP5-CI repository on GitHUb.

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

* [!How to fix the navbar](https://stackoverflow.com/questions/68381021/how-to-separate-nav-bar-from-the-rest-of-the-page)

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



