## Alicia College

This is a website for college student and the lecture.
![alt text](https://github.com/ogunmakindetobi/college/raw/master/src/common/images/page.png "Logo Title Text 1")

* The goal for the user is for educational purpose,which is use by the college lecturers to create new  course for the Semester,this website also allow student to view the course created by the each lecturers for them to have the description about the new course,
mark of the course and the number of the course,this website is useful for the users cause its has good ussfulness for student that are on holidays and lecturer that want to involve student on new course for the new Semester.its also help each college lecturers to register,login and have to create this courses thats student new to focus on.


<ul>
<li>An unregistered user can browse this website to see some pages and read what the website is about on home page and about page.</li>
<li>If they become an user, they will be able to add there course through course page.</li>
<li>Registered users can view the page with the login details. </li>
<li>They can add cafe name(course number), course description, course mark, and course name and its all save driectly on (database).</li>
<li>If they are unable to find the course, they can add a course from "Course  page".</li>
<li>On "Profile page" , there are some course list there listed).
</li>
<li>They can also browse and add/delete  course from "course page","home page".</li>
</ul>


## Deployed page is available here
https://flask-college.herokuapp.com/



## UX

If they havent visted this website before the home page appear first,which shows some wirrting details of the college.

The steps:
 
 # If register:

<ol>
<li>The user can add username and password to register their account</li>
<li>It will navigate the user to " profile" page</li>
</ol>


 # If login:

<ol>
<li>An user can fill in the form to go to "Login"</li>
<li>It will navigate the user to "profile" page</li>
<li>click on course page to create a course for other non Registered users</li>
<li>On the course page , they can add the course  name, description, number and ,mark that each course takes.</li>
<li>When this is create its loops back to home page with message course created sucessfully</li>
<li>The user can see their memory is added on the page</li>
<li>The user can  delete the memory by clicking on the buttons</li>
</ol>

# Course page
* Form to create course.

## Features


### Existing Features

<ul>
<li><b>Feature 1 : Browsing all course created</b> - allows users browsing all the posted course , by visiting home  page</li>
<li><b>Feature 2 : Course information</b> - allows users reading collage and course  information  </li>
<li><b>Feature 3 : Add  memories</b> - allows users adding  their course  memory by filling 'course' form</li>
<li><b>Feature 4 : Contact form</b> - Its allow users to contact collage this is print out on the terminal gitpod and its not pass in database</li>
</ul>


### Features Left to Implement
- I would like to categorise course
- I would like to add more user information and user role.




## Technologies Used


###  Back-end 
<ul>
<li><a href="https://www.python.org/" rel="nofollow">Python</a></li>
<li><a href="https://flask.palletsprojects.com/en/1.1.x/" rel="nofollow">Flask</a> - Python framework For pagination, etc</li>
<li><a href="https://www.dnspython.org/" rel="nofollow">Dnspython</a>-  DNS toolkit for Python</li>
<li><a href="https://www.heroku.com" rel="nofollow">Heroku</a> - Cloud application platform </li>
<li><a href="https://www.mongodb.com/cloud/atlas" rel="nofollow">Mongo DB Atlas</a> - non relational, NO-SQL Database - Cloud based MongoDB server</li>
</ul>


###  Front-end 
<ul>
<li><a href="https://www.javascript.com/" rel="nofollow">Javascript</a> - For auto-complete, navbar, etc</li>
<li><a href="https://jquery.com/" rel="nofollow">Jquery</a> - For auto-complete, navbar, etc</li>
<li><a href="https://getbootstrap.com/">Bootstrap</a>or clean front-end design, and also icons</li>
<li><a href="https://www.w3schools.com/howto/howto_css_modals.asp" rel="nofollow">W3C Modal Box</a> - The project uses W3c's Modal Box to display welcome text.</li>
</ul>

### Image Library

This project is using images from <a href="https://google.com/" rel="nofollow">cloudinary.com</a>, which is used as alternative to image upload facility.

       
## Testing

### PC
I have tested on these browsers:

<ol>
<li>Google Chrome</li>
<li>Firefox</li>
<li>Internet Explorer Edge</li>
</ol>

### Tablet
<ol>
<li>Kindle Fire 8 plus</li>
</ol>

### Mobile 
<ol>
<li>Samsung Galaxy A21s</li>
<li>iPhone 7</li>
<li>HUAWEI Mate 20 lite</li>
</ol>

I also used Google Chrome's device emulator to test on all types of devices.


I have asked on Code Institute's peer review community to test this website and received feedbacks:


Also, this was run through these validators.

<ul>
<li><a href="https://jigsaw.w3.org/css-validator/" target="_blank">CSS Validation Service</a></li>
<li><a href="https://validator.w3.org/" target="_blank">Markup Validation Service</a></li>
<li><a href="https://jshint.com/" target="_blank">JS Hint</a></li>
</ul>


### Test Results

<ol>
<li>Mobile view on home page is wild and its was fix </li>
<li>The course list was close to the home page wirttings its was fixed by adding p tag </li>
<li>The database doesnt received form list before its was fix by chnaging from create_course to courses - fixed</li>
<li>The 'Delete' button was too big counldnt  - fixed</li>
<li>Course form was not listed on mobile view and i add the list tag and  - fixed</li>
</ol>




<h3>How to test this project</h3>

<ol>
<li>On the home page you have the details news about the college which the course that are created</li>
<li>Fill in the form with a username and password, press 'Register' button</li>
<li>It will redirect to "Your Profile Information" page</li>
<li>Click on  and fill in form to  'Add Your course' page </li>
<li>Fill in the form - add 2 or more characters on 'cafe' field to see auto-complete is working</li>
<li>create course  form to go to 'home page ' page</li>
<li> Its will create course and redirect you back to home page</li>
<li>fill in contact forms its print out on terminal</li>
<li>Login form is working perfectly and you cant login without register </li>
<li>register page is working by using new username and password to register</li>
<li> Add course in course page its appear on home page through database</li>
<li>Choose one of the course , click on 'Delete' button to delete cafe</li>
<li>Click on 'Logout' button to logout</li>
</ol>


## Deployment

This project was developed on Github, using Gitpod as IDE. It has only master branch.
This is pushed and deployed on to heroku.

Deployed project is found here:

https://flask-college.herokuapp.com/


This project utilises Mongo DB to use NO-SQL (non-relational) database.
Before cloning the project:

<ol>
<li>Add a database collection 'brightonCafes' on <a href="https://www.mongodb.com/cloud/atlas" target="_blank">MongoDB Atlas</a></li>
<li>Create a database and these tables: 
   <ul>
   <li>college</li>
   <li>courses</li>
   <li>users</li>
   </ul>
</li>
</ol>

## To run this project on your local repository
This project will be deployed following these steps:
<ol>
<li>Add your own repository on your Github account</li>
<li>Click the green 'Gitpod' button on top-right corner of this repo(If you can't find the button, install 'Gitpod' extension on your Chrome browser</li>
<li>Gitpod launches</li>
<li>Run the following command (Replace the 'USERNAME' and 'REPO' to your username and repo name):</li>
 
```

git remote set-url origin https://github.com/USERNAME/REPO.git

```


<li>Add env.py file on your root folder, add these lines:
 
```
import os

os.environ['SECRET_KEY'] = '- YOUR SECRET KEY - '
os.environ['MONGO_URI'] = '- YOUR MONGO URI -' 

```
</li>
<li>Run this command below to install all the modules on requirements.txt file:

```

pip3 install -r requirements.txt

```
</li>
<li>Run the code by running this code below:
 
```

python3 app.py

```

</li>
</ol>


## Remote Deployment (Run the project on Heroku.com)
If you want to add it to your Heroku account, follow the instructions below:

<ol>
<li>Add an app for this project</li>
<li>Add environment variables 'SECRET_KEY' and 'MONGO_URI' on your app</li> 
<li>Add PORT on your app</li> 
<li>On your Gitpod workspace, login to heroku by running this code below:
 
 
```

heroku login -i

```

</li> 
<li>Select your app by running this code below (Replace '- YOUR APP NAME -' with your own app name):
 
```

git init

heroku git:remote -a  - YOUR APP NAME -

```

</li>
<li>Run this code below to push the code to your Heroku app:

```

git push heroku master

```

</li>
<li>When the app is deployed, click on 'Open App' button to run your app </li>
</ol>

## Credits

### Content

<ul>
<li>This project is using icons from Materialize.</li>
</ul>

### Media

<ul>
<li>- The photos and texts used in this website are taken from:
<ul>
<li>https://www.google.com</li>

</ul>
</li>



</ul>


### Acknowledgements

- I received inspiration for this project from a resume project provided by Code Institute.
- My new mentor brain
