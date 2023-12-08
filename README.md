[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/M_swVJkI)
# Museum-Project
## Group Member Information & Assigned Tasks:
- zachary.lam@ucalgary.ca Zachary Lam (30178786): EERD, database creation, loading inputs via files
- evan.mann@ucalgary.ca Evan Mann (30141069): Relational schema,  data entry interface, SQL roles, menuing system
- trevor.nguyen@ucalgary.ca Trevor Nguyen (30176877): Query code, guest interface
## How to Use & Run the Program:
- Run dataBaseCreation.py
- Run main.py
- Select your user type
- Enter the username and password of the role you wish to use
- If you are a data entry user:
    - Choose the table you would like to modify
    - Choose which modification you would like to make
    - Enter required information as prompted
    - Continue to modify the database by choosing another table or exit
- If you are a guest user:
    - Choose the part of the database that you would like to view: Art pieces, Artists, Exhibitions or Exit Program as desired
    - Follow the prompts and choose the parts of each database you would like to get more information on
    - After the table is shown, you can continue searching or end the code by going up a level and then exiting the program.

## Organization:
- sql scripts folder: contains all sql scripts required (database creation and initialization, sql script with query tasks in the handout, etc...)
- database design folder: EERD and relational schema
- All other python file are functions for the program or the main function
- test.csv is the file that can be used in art object insert when inserting via a file

## Notes
This program is capable of interfacing with the entirety of the data base provided through the data entry user and able to view select parts via the guest user. The guest user is limited to certain areas that we felt were appropriate for that kind of user.