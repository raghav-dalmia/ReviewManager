# ReviewManager

### Clear all migrations
Reference: https://www.linkedin.com/pulse/how-do-i-reset-django-migration-nitin-raturi?trk=pulse-article_more-articles_related-content-card
```angular2html
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete
rm -rf db.sqlite3
pip uninstall django
pip install django
python manage.py makemigrations 
python manage.py migrate
python manage.py createsuperuser
```
### Things to keep in mind before making any change
- Take fresh pull of main branch
- Create new branch
- Don't commit any changes related to dependencies, cache and migrations.
  - Commit all your changes (only your change)
  - Then run following commands:
```angular2html
git stash
git stash drop
git stash clear
```
- Raise the PR, get it reviewed and merge it.
- Never force push to main branch.

### Contributing guidelines
- Don't make any DB calls outside of `dao` class.
- Always create `urls` file for each class and register at main `url` class.
- Always register your app in `settings.py` file.
- We have two setting file
  - `settings.py` - Have settings for dev env
  - `prod_settings.py` - settings for production env. Need to track all the changes done for dev settings and during deployment need to update prod settings.
