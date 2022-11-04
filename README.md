<div align="center">


<img width="30%" src="https://user-images.githubusercontent.com/92335127/199920639-43006d67-768c-4451-9bc5-2a775e036a3e.png">

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

> ⚠ Then, go to http://127.0.0.1:8000/inv/inventory/pk

replace pk with any integer number (e.g 1,2,3)

--> for DRF standard interface, we use API endpoint

> ⚠ Then, go to http://127.0.0.1:8000/api/inventory/pk

replace pk with any integer number (e.g 1,2,3)

#

### Filter Inventory

--> To Filter Inventory we use API endpoint :

> ⚠ Then, go to http://127.0.0.1:8000/api/inventory/?name=param1&availability=Param2

replace param1 with any string (e.g 'Antiflu','Aspirin','Paracetamol') and Param2 with True or False

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
<img src="https://user-images.githubusercontent.com/92335127/199919986-fa0a8311-b987-4688-84d0-f30e699b8693.png">
</td> 
<td width="50%">
<br>
<p align="center">
  Inventory Detail
</p>
<img src="https://user-images.githubusercontent.com/92335127/199920081-5fe97b2c-5740-4852-a172-b14ef06f865e.png">  
</td>
</table>

others Images
![image](https://user-images.githubusercontent.com/92335127/199920162-86a82d2b-ebeb-42ae-b868-09f177572852.png)
![image](https://user-images.githubusercontent.com/92335127/199920237-d4dc51da-7292-4997-afc5-9084f354d802.png)
