# E-Commerce Website Version-1
# Introduction
This is a simple E-Commerce Project developed using django framework. This project is integrated with user email authentication and email activation token autentication. Different packages is used while developing this application such as coverage, six, isort, black, stripe, and so on, which are all mentioned in requirements.txt file.  
Stripe payment gateway mechanism is integrated in this application for online transaction between buyers and seller. Stripe webhook is integrated to get real-time data from stripe.  
Testing is done through, unittest and pytest.  

# Tech Stack
  1. [Python 3.9](https://www.python.org/)
  2. [Django 4.0.5](https://www.djangoproject.com/)
  3. [SQLite3](https://www.sqlite.org/index.html)
  4. [jQuery 3.6.0](https://blog.jquery.com/2021/03/02/jquery-3-6-0-released/)
  5. [Bootstrap5](https://getbootstrap.com/)
  6. [Stripe](https://stripe.com/en-de)
  
 # Installation
  **GIT clone from GitHub**
  
  ###### First step is to make a directory.
  ```
  $ mkdir e_commerce
  $ cd e_commerce
  ```
  
  ###### Then clone the [E-commerce App Repo](https://github.com/Shuvam77/ecommerce_v1) from the GitHub.
  ```
  e_commerce $ git clone https://github.com/Shuvam77/ecommerce_v1.git .
  ```
  
  **Python Enviornment**
  ###### Install and activate [Python virtual environments](https://docs.python.org/3/tutorial/venv.html). And activate it.
  ```
  e_commerce $ pipenv shell
  ```
  ###### or
  ```
  e_commerce $ python3 -m venv venv
  e_commerce $ source venv/bin/activate
  ```
  
  ###### Once it has been activated, install requirements.txt.
  ```
  (venv) e_commerce $ pip install -r requirements.txt
  ```
  
  ###### .env file
  ```
  (venv) e_commerce $ touch .env
  ```
  ```
  STRIPE_API_KEY = ENTER_STRIPE_API_KEY
  STRIPE_PUBLISHABLE_KEY = ENTER_STRIPE_PUBLISHABLE_KEY
  ENDPOINT_SECRET = ENTER_STRIPE_WEBHOOK_ENDPOINT_SECRET
  BASKET_SESSION = G6h?r{1b#{ZM6N6_G5)@
  ```
  
  **Start Migration**
  ###### Migration Process
  ```
  (venv) e_commerce $ python manage.py makemigrations
  (venv) e_commerce $ python manage.py showmigrations
  (venv) e_commerce $ python manage.py migrate
  ```
  
  ###### Create SuperUser
  ```
  (venv) e_commerce $ python manage.py createsuperuser
  
  Username: admin
  Email address: admin@email.com
  Password: sudo@123
  ```
  
  ###### Runserver
  ```
  (env) e_commerce $ python manage.py runserver
  ```
  
  **Stripe Webhook Configuration**
  ###### Stripe login in new terminal
  You need to put your credentials to login
  ```
  e_commerce $ ./stripe login
  ```
  
  ###### Activate listen command for webhook
  ```
  e_commerce $ ./stripe listen --forward-to localhost:8000/payment/webhook/
  ```
  
  ###### Logout of stripe webhook
  ```
  e_commerce $ ./stripe logout
  ```
