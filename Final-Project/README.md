# Noah Dammann Blog

This is my final CS50x project. I created my own blogging website to share my thoughts on fitness. 

## Video Demo:

The video demo is no longer available on YouTube.

## Prerequisites

  - Python 3 - [Download & Install Python](https://www.python.org/downloads/)
  - Django
  ```sh
  pip3 install django
  ```

## Usage 

1. Clone this repo
   ```sh
   git clone https://github.com/noahdammann/CS50 -b CS50x
   ```
2. Move into blog directory
   ```sh
   cd CS50/Final-Project/blog
   ```
3. Start local server
   ```sh
   python manage.py runserver
   ```

## Technical Aspect

I created the site using the django framework on the backend and HTML and CSS on the frontend. There are 6 url paths corresponding to 6 routes defined in views.py. There are 7 different HTML templates and a single static CSS file. There are 2 models, Post and Subscriber which are registered in admin.py. No tests have been written for this application, but it runs perfectly on the django virtual server. The website is mobile responsive. Only the administrator can visit the /new url path and from there, can add a new blog post. The blog features a newsletter which users can sign up for, to then be added to a mailing list which can then be accessed to send all subscibers emails. The blog uses a very simple design which is easy to read so that users have a good experience on the website. The general layout of this blog was inspired by Julian Shapiro's blog and uses a similar theme for headings and text. The home page makes use of the flexbox display to size all of the posts into a container which is then mobile responsive and adjusts according to the users device size. The HTML pages all inherit from a single "layout.html" page in order to minimize repetitive code. Similarly all pages inherit styling from a single "styles.css" page. The backend server seamlessly generates all of the posts that are stored by django, and loads them onto the home page upon rendering. The posts are scaled according to the users device and are centered on the page. The backend also automatically stores all of the email addresses which users sign up with for the newsletter. Each article written can be associated with an image which will the be displayed as its thumbnail on the homepage. 

## Conclusion

Ultimately this project was not about creating a blogging website, instead it was a good opportunity for me to get some practice in creating websites and a useful addition to my portfolio of projects. I've learned more about how to use the django framework and write good code. This blog was created to be the final project for the CS50 computer science course of Harvard University. The course was the very first introduction I had to computer science and programming and looking back at where I came from I've learned so much. I'm grateful to professor Malan and his team for making CS50 happen and making it possible for me to learn how to program for free online. 
