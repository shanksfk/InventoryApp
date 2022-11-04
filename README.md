<div align="center">
<img width="30%" src="https://user-images.githubusercontent.com/72341453/134747028-7e2d90cc-a92f-4f66-815e-54a0d50cca54.PNG">

# InventoryApp

</div>

### Cloning the repository

--> Clone the repository using the command below :

```bash
git clone https://github.com/shanksfk/InventoryApp

```

--> Move into the directory where we have the project files :

```bash
cd InventoryApp

```

--> Create a virtual environment :

```bash
# Let's install virtualenv first
pip install virtualenv

# Then we create our virtual environment
virtualenv envname

```

--> Activate the virtual environment :

```bash
envname\scripts\activate

```

--> Install the requirements :

```bash
pip install -r requirements.txt

```

#

### Running the App

--> To run the App, we use :

```bash
python manage.py runserver

```

> ⚠ Then, the development server will be started at http://127.0.0.1:8000/

#

### View List Inventories

--> To View List Inventories we use API endpoint :

> ⚠ Then, go to http://127.0.0.1:8000/inv/inventories

--> for DRF standard interface, we use API endpoint

> ⚠ Then, go to http://127.0.0.1:8000/api/inventory

#

### View Detail Inventory

--> To View Detail Inventory we use API endpoint :

> ⚠ Then, go to http://127.0.0.1:8000/inv/inventory/<pk>

replace <pk> with any integer number (e.g 1,2,3)

--> for DRF standard interface, we use API endpoint

> ⚠ Then, go to http://127.0.0.1:8000/api/inventory/<pk>

replace <pk> with any integer number (e.g 1,2,3)

#

### Filter Inventory

--> To Filter Inventory we use API endpoint :

> ⚠ Then, go to http://127.0.0.1:8000/api/inventory/?name=<param>

replace <param> with any string (e.g 'Antiflu','Aspirin','Paracetamol')

#

### Manage Inventory Using Admin Panel

--> To Manage Inventory Using Admin Panel we use API endpoint :

> ⚠ Then, go to http://127.0.0.1:8000/admin

use login detail as follow:
username: user
password: 123456

to create superuser

```bash
python manage.py createsuperuser

```

#

### App Preview :

<table width="100%"> 
<tr>
<td width="50%">      
&nbsp; 
<br>
<p align="center">
 Inventory List
</p>
<img src="https://user-images.githubusercontent.com/72341453/134747262-0a92233d-8010-40f8-84c5-8d94895aac44.PNG">
</td> 
<td width="50%">
<br>
<p align="center">
  Inventory Detail
</p>
<img src="https://user-images.githubusercontent.com/72341453/134747155-3ca5b55f-b064-4741-aeae-abe90bddf41e.PNG">  
</td>
</table>
