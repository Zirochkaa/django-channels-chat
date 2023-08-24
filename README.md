# Django channels chat

This repository contains study project - real-time chat using `django`, `channels` and `Tailwind CSS` :)

Based on [SteinOveHelset/djangochat](https://github.com/SteinOveHelset/djangochat/tree/master) course.


## Run project locally

1. Setup and activate your local python environment. [Here](https://www.digitalocean.com/community/tutorial_series/how-to-install-and-set-up-a-local-programming-environment-for-python-3) are few guides on how to do it.
2. Install requirements:
   ```shell 
   pip install requirements.txt
   ```
3. Go to project folder:
   ```shell 
   cd django_channels_chat/
   ```
4. Apply migrations:
   ```shell 
   python manage.py migrate
   ```
5. Create superuser:
   ```shell 
   python manage.py createsuperuser
   ```
6. Run project:
   ```shell 
   python manage.py runserver
   ```
7. Go to [127.0.0.1:8000](http://127.0.0.1:8000/) in your web browser.
