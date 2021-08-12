![](static/images/logo.png)

# Hoffi Coffi
---

## Introduction

Welcome to Hoffi Coffi, thats '**Love Coffee**' in the **Welsh language**. The app is designed to bring coffee drinkers like myself, together to choose their favourite coffees from a list of products. It will also allow people who have not tried certain coffees to see possible coffee's to try next. 

## UX
---

### User Stories 

*Generic User*

* As a user, I want to be able to **learn** about a variety of coffees. 

* As a user, I want to be able to **keep up to date** about my favourite coffees from the list of products. 

* As a user, I want to be able to **request** my favourite coffees be added to the site. 

*Developers Goals* 

* As a developer, I want to be able to create a usable app. 

* As a developer, I want to be able to increase the passion for coffee. 


### Design 

1. **Logo** 
The logo was created using [Free Logo Maker](https://logomakr.com). It was designed to to show the love for coffee that can be shared by two people. The coffee beans are used in place of a heart and colored red to symbolise this. This logo can be seen at the top of this page. 

2. **Colour Scheme**

The colours for the website were chosen using [Coolors](https://coolors.co/). They were chosen with the aim to represent coffee and the love that goes into it. The chosen colours are:

![](wireframes/hoffi-coffi-coolors.png)

3. **Fonts**

The website has the main font of Roboto Slab, which was chosen due to it **readability to all users**. Furthermore, it modern which will fit with the aim of the website. It was chosen using [Google Fonts](https://fonts.googleapis.com/css2?family=Roboto+Slab&display=swap) and has the default of Sans Serif. 

4. **Wireframes**

The wireframes for this website where created using [Balsamiq](https://balsamiq.com/wireframes/?gclid=CjwKCAjwltH3BRB6EiwAhj0IUBrAHe-2BiRjQmQGSO-FZIjoEjkckL_kVyJXd5ShGVwKqDaDMqKjvBoCQksQAvD_BwE)

![](wireframes/desktop.png)
![](wireframes/tablet.png)
![](wireframes/phone.png)

### Database Structure

Key      | Value
---------|-----------
_id      | ObjectId
username | String
password | String

Key           | Value
--------------|-----------
_id           | ObjectId
product_name  | String
origin        | String
price         | String
image_url     | String
taste         | String

## Features
---

### Existing Features

The features that were added to the project were designed to have a high level of usability.

* The **logo** will be wrapped in anchor tags which will allow the user to click on it to return to the home page. 
* The **Navbar** will have links to home, admin and sign in which will allow the user to easily navigate around the page. It will also be a sticky navbar to help users navigate when they are scrolling through the page.
* The **hamburger menu** will be used on mobile phone to allow the user to navigate their way around the website easily without overcrowding the screen. 
* The **home page** will incorporate all coffee cards with each having their own image of coffee. There will also be a welcome message to the website.  
* The **contact form** allows the user to get in contact with any questions that they may have. 
* The **admin panel** will allow admin users to sign in and **Create, Update, Edit and Delete** coffee.
* The **footer** will allow the user to naviagte to other pages with a menu and will show the hoffi coffi logo. 

### Features Left to Implement

* The option for users to **buy the coffee** that they like through the website.
* For users to be able to add thier **own choices** on the website. 
* For users to be able to **create a profile** and **favourite** certain coffees.

## Technologies Used
---

### **Languages:**

* HTML
* CSS
* JavaScript
* JSON
* Python 

## **Frameworks and Libraries**

* [Bootstrap](https://getbootstrap.com/)
* [Font Awesome](https://fontawesome.com/)
* [Google Fonts](https://fonts.google.com/specimen/Lato?sidebar.open&selection.family=Lato)
* Flask

### **Tools Used**

* [Coolors](https://coolors.co/3c1642-086375-1dd3b0-fffdfd-ffffff) 
* [Balsamiq](https://balsamiq.com/wireframes/?gclid=CjwKCAjwltH3BRB6EiwAhj0IUBrAHe-2BiRjQmQGSO-FZIjoEjkckL_kVyJXd5ShGVwKqDaDMqKjvBoCQksQAvD_BwE)
* [Free Logo Maker](https://logomakr.com)
* [Gitpod Online IDE](https://www.gitpod.io/)
* [Github](https://github.com/)
* [Favicon Creator](https://www.favicon.cc/?action=import_request)

## Testing
---

### All Sections

**Plan** – I want the app to allow the users to be able find the most update information on the top coffees from around the world.

**Implementation** – Ensuring that users were able to access the information about the top coffees from around the world. The information is clear and concise as not to confuse the user.

**Test** –  This was tested by asking friends and family to use the app and to see if they were able to find the information that the were looking for to educate themselves on coffee. 

**Result** – The coffee information was presented to the user clear and readable to the users. 

**Verdict** – This test passed based on the notes in the criteria above. 



## Deployment 
---

The information below explains how to create a clone of the Hoffi Coffi repository in Github, how to work with a local copy and how to deploy to Heroku

In order to clone the repository you will need the following:

* Python - version 3.0
* A Heroku account
* A Github acoount
* MonogoDB account

### Cloning the repository

To create a local respository, follow the steps below:

1. Navigate to Ted-Williams/hoffi-coffi
2. Below the menu click Code.
3. Copy the URl using the clipboard to the righthand side.
4. Open you preferred IDE for example Gitpod.
5. Type git clone into the terminal and paste the respository URl.
6. Click enter and the clone will be created.

### Working with a local copy

You will need to follow the steps below in order to work with a local copy.

1. Install the correct requirements
    * Go to you workspace that holds the local copy 
    * Type **pip3 install -r requirements.txt** into the terminal

2. Creating a database in MongoDB
    * Create a MongoDB account at [MongoDB](https://account.mongodb.com/)
    * Sign in
    * Create a cluster
    * Create a database
    * Create two collections, **Users** and **Coffee**
    * Use the database structure above

3. Setting up the Environment Variables
    * Inside your IDE create a file called .gitignore
    * Add the following text in the gitignore file - evn.py
    * Create a personal secret key and password. Add the text below to your env.py file. 

    import os
    
    os.environ.setdefault("IP", "0.0.0.0")

    os.environ.setdefault("PORT", "5000")

    os.environ.setdefault("DEBUG", "1")

    os.environ.setdefault("SECRET_KEY", "YOURSECRETKEY")

    os.environ.setdefault("MONGO_URI", "mongodb+srv://YOURPASSWORD@YOURCLUSTERNAME.obvuh.mongodb.net/YOURDATABASENAME?retryWrites=true&w=majority")

    os.environ.setdefault("MONGO_DBNAME", "YOURDATABASENAME")

4. Run the App
    * In the terminal type python3 app.py

### Deploy to Heroku

To host this project on Heroku, follow the steps below

1. Creating a Heroku account 
    * Sign up to Heroku
    * Create a new app and select the nearest region to you

2. Workspace preparation
    * Type pip3 freeze --local > requirements.txt into the terminal to create a requirements.txt file.
    * Type python app.py > Procfile in the terminal to create a Procfile. 

3. Deployment section 
    * In the deployment section of Heroku, choose the GitHun for automatic deployment
    * Enter the name for your repo. Click "search". When it finds the repo, click the "connect" button.
    * Click "settings". Scroll down and click "Reveal config vars". Set up the same variables as in your env.py (IP, PORT, SECRET_KEY, MONGO_URI and MONGODB_NAME): You shouldn't set the DEBUG variable in under config vars, only in your env.py to prevent DEBUG being active on live website.
    * Click "Deploy" and click "Enable automatic deployment".
    * Once the app is built - Click view app. 
    * Use git push to push to Heroku.

## Credits
---

* I would like to thank [Simen Dehlin](https://github.com/Eventyret) for his continued support, help and words of encouragement throughout this project. 


***This project is fictitous and was created for educational purposes as part of the Code Institute Milestone Project 3***

