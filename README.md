# Turbo RMF
This web application gives cyber security professionals the opportunity to automake most of the assesment phase of RMF. You can now implement vulnerability fixes & verify configuration at the click of a button. Your system modifications are then saved to a database. This makes system engineering easy.
- Load Checklist 127.0.0.1:8000/upload/
- Select Checklist 127.0.0.1:8000/checklists/
- Modify Checklist 127.0.0.1:8000/vuln/

![turbo-rmf_snippet](https://user-images.githubusercontent.com/15160643/35486600-249460ba-0425-11e8-80b5-5b204e88f7d3.PNG)


## Requirements
- Python 3.6
- Django Python 2.0.1
- Pywinrm 3.0
- Django Rest Framework v3

## Install Resources and Run
- pip install Django==2.0.1
- pip install djangorestframework
- pip install pywinrm
- cd ${PROJECT ROOT}
- python manage.py runserver

## Browse to site
127.0.0.1:8000/vuln/
