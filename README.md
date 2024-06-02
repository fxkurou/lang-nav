# Simple Navbar

This is a little Django project that contain a website header and nav bar that can be used as a template for any website. It also contains a simple language switcher that can be used to translate the website into different languages.

## Features

This project implements a website header that contains a navigation and a language switcher. The navigation itself contains working links. Articles are selected from the database (translation too).

![image](https://github.com/fxkurou/lang-nav/assets/118657685/0553d793-ecff-45e2-acef-a509defe76ac)

Project also translated into 3 languages:
  * English
  * Spanish
  * Franch

# Usage

1. First clone the repository from Github:
```bash
  $ git clone https://github.com/fxkurou/lang-nav.git
```
2. Navigate to project directory:
 
```bash
   cd path/to/project
```
3. Set up vurtual environment (optional)
```bash
   python -m venv venv
```
4. Install the required Python packages:
```bash
  pip install -r requirements.txt
```
5. Migrate the database:

```bash
  #Make migrations
  python manage.py makemigrations

  # Run the migrations
  python manage.py migrate
```
6. Run the server:
```bash
   # Run the server
  python manage.py runserver
```
