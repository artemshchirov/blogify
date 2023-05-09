# Blogify

It's a publishing platform, a blog with elements of a social network.

## Description

- Social network with the ability to publish personal diaries.
- Create your own page on the website.
- View all posts of an author when visiting their page.
- Users can access other users' pages, subscribe to them, and comment on their posts.
- Authors can choose a name and a unique address for their page.
- Posts can be submitted to groups and viewed alongside posts from different authors.

## Tech

- Python
- Django
- DRF
- DRF-Simple
- JWT
- Django CORS
- Pillow
- sorl-thumbnail
- Bootstrap

## Running the Project in Dev Mode

### Clone the repository and navigate to it in the command line

```bash
git clone https://github.com/artemshchirov/blogify.git
cd blogify
```

### Install and activate the virtual environment

```bash
# Windows
python -m venv venv
source venv/Scripts/activate
python -m pip install --upgrade pip
```

```bash
# Linux / macOS
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
```

### Install the dependencies from the `requirements.txt` file

```bash
pip install -r requirements.txt
```

## Navigate to the directory with the manage.py file and execute the following commands

### Run migrations

```bash
python manage.py migrate
```

### Create a superuser

```bash
python manage.py createsuperuser
```

### Collect static files

```bash
python manage.py collectstatic
```

### Run the project

```bash
python manage.py runserver
```
