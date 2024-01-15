<h1 align="center">●Employee onboarding and adaptation service </h1>

The program is designed to organize and effectively carry out onboarding processes and adaptation of new employees in the organization.
<p align='center'>
<a href ='readme.md' style='border:solid; padding:3px; border-color:white; border-radius:5px'>Change language to RU</a>
</p>

### Prerequisites:
Install the following programs:
 - [Python: 3.6-3.12 (For launch by the company)](https://www.python.org/downloads/release/python-3120/)
 - [MySQL Workbench 8.0 CE(For launch by the company)](https://downloads.mysql.com/archives/workbench/)
 - [VS code 1.7-1.85 (For launch by the company)](https://code.visualstudio.com/download)
 - [PyCharm 2022.2.2-2023.3.2 (For launch by the company)](https://pycharm-community-edition.en.softonic.com)

### Launching the program from the employee's side.
To run the program itself, you need to run the file with the .exe extension, “EOAS.exe”.

### Launch of the program by the company.
**1)** To launch the program on the company's part, the first thing you will need to do is create a database in MySQL Workbench 8.0 CE. To do this, enter the following SQL query.


```sql
CREATE DATABASE IF NOT EXISTS onboarding_db;
USE onboarding_db;
CREATE TABLE IF NOT EXISTS feedback (
  id int AUTO_INCREMENT PRIMARY KEY,
  name varchar(255) NOT NULL,
  position varchar(255) NOT NULL,
  phone varchar(20) NOT NULL,
  feedback text NOT NULL,
  satisfaction_level varchar(10) NOT NULL
);
```

**2)** After this, you need to launch a cross-platform development environment (VS code, PyCharm and others) (the requirements for development environments are specified in the prerequisites) and paste your data in the following code

```python
self.db_connection = mysql.connector.connect(
    host='Your host'',
    port = Port,
    user='Username'',
    password='Database password'',
    database='Database name'
)
```
**3)**  Next, you need to enter the following commands in the Windows Terminal to install the necessary libraries:
#### PyQt6:
```shell
pip install PyQt6
```
#### MySQL Connector:
```shell
pip install mysql-connector-python
```
Now you can run the .py file, “EOAS,py”.

## Change of filled materials.
If you want to change the information in the materials you fill out, you need to:

**1)** Run the program using cross-platform development environments (VS code, PyCharm and others) (requirements for development environments are specified in the prerequisites).

**2.1.** To change the information of the training materials, you need to find line 198 in the code, select the remaining information and change it at your discretion.
(for navigation - this is located immediately below the lines:
```python
def create_training_materials_widget(self):
    self.training_materials_widget = QWidget()
    layout = QVBoxLayout()
    text_materials = QTextEdit()
    text_materials.setPlainText(
)
```

**2.2.** To change information about the company, you need to find line 325 in the code, select the remaining information and change it at your discretion.

(for navigation - this is located immediately below the lines:
   ```python
def create_company_info_widget(self):
    self.company_info_widget = QWidget()
    layout = QVBoxLayout()
    text_company_info = QTextEdit()
    text_company_info.setPlainText(
)
```

**2.3.** To change the information in manuals and instructions, you need to find line 375 in the code, highlight the remaining information and change it at your discretion.
(for navigation - this is located immediately below the lines:
```python
def create_guides_widget(self):
    self.guides_widget = QWidget()
    layout = QVBoxLayout()
    text_guides = QTextEdit()
    text_guides.setPlainText(
)
```


## Video
If you need to visually see how to run the program correctly, we made a video of the original version upon release [link](https://www.youtube.com/watch?v=-q8mcdRpf_M); some things may differ due to different operating systems and versions, but the concept is common to all.

## Changing the connection from LocalHost to IP address.

If you want all IP addresses connected to the same local network with you to have access to your MySQL database, you can create a user with the hostname pattern %, which means "any host".
In order to change the connection type from LocalHost to IP address, you must first enter the following SQL queries in MySQL Workbench:

```sql
CREATE USER 'username'@'%' IDENTIFIED BY 'yourpassword';
GRANT ALL PRIVILEGES ON *.* TO 'username'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;
```
Next, you need to run the file with the .py extension, “EOAS,py”, using one of the development environments. Next, we find lines 12-18 of the file:
```python
self.db_connection = mysql.connector.connect(
    host='Your host'',
    port = Port,
    user='Username'',
    password='Database password'',
    database='Database name'
)
```
Сhange them. Instead of “localhost” - indicate the IP address of the current host. Specify the port. In “user” we indicate the user who was added to MySQL, we also change “password”. In “database” we indicate the name of your database. Now anyone who is connected to the same local network with you will be able to enter information into the database using the program.

## Changing the database connection from Local Network to Global.
To do this, you will need to enter your data in the following part of the code:
```python
self.db_connection = mysql.connector.connect(
    host='Your host'',
    port = Port,
    user='Username'',
    password='Database password'',
    database='Database name'
)
```


## Developers
The developers of the program are:
**Shatilo Mikhail Sergeevich**
•	Student
•	Group 231-323
•	Moscow Polytechnic University
•	107023, Moscow, st. B. Semenovskaya, 38
•	mihailshattt@gmail.com

**Belonogov Artem Igorevich**
•	Student
•	Group 231-323
•	Moscow Polytechnic University
•	107023, Moscow, st. B. Semenovskaya, 38
•	belonogovartem110805@gmail.com

## Feedback
For feedback, call/text **+7(952)672-98-10**