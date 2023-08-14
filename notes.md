- pillow -- is used for image fields in the application

- we can create application using
  -- python3 manage.py startapp name

       (each app is like a model in nodejs)

- matplotlib and seaborn to generate charts

- pip freeze -- to get all the installed packages and their versions

---

- first we need to create the model in the app ( customers, products, etc..) in the models.py file

- then we need to register the model in admin.py (admin.site.register(className))

- if we nade any changes to the models we need to run
  --- python3 manage.py makemigrations

- and to generate the migrations we need to run
  --- pytohn3 manage.py migrate
