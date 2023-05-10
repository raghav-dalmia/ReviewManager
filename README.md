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
```
git checkout -b <feature-branch>
# After changes are done
git add .
git commit -m "In past tense"
# Make sure main is up to date when you are ready to commit
git checkout main
git fetch
git pull --no-ff
git rebase main --> Resolve conflicts
git rebase --contiue
git push or even git push --force
# Force won't cause a problem in this case since we have already rebased
```

- Create new branch
- Don't commit any changes related to dependencies, cache and migrations.
  - Commit all your changes (only your change)
  - Then run following commands:
```angular2html
git stash --> Store your changes
git stash pop --> To pop your changes
git stash clear --> Drop your changes (will be deleted, can't get them back)
```
- Raise the PR, get it reviewed and merge it.

### Contributing guidelines
- Don't make any DB calls outside of `dao` class.
- Always create `urls` file for each class and register at main `url` class.
- Always register your app in `settings.py` file.
- We have two setting file
  - `settings.py` - Have settings for dev env
  - `prod_settings.py` - settings for production env. Need to track all the changes done for dev settings and during deployment need to update prod settings.
