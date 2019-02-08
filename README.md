# Commission (used car dealer's)

- The application implements the used car dealer's support.
- Project is written in Django using the django REST framework.
- A logged-in user can add new cars, edit and delete own cars, and view a list of all available cars.
- The administrator additionally has the ability to edit and delete any car.
- The project is configured to work with the PostreSQL database.
- Car data is stored in the database in the jsonb field (corresponding to JSONField in Car model).
- An additional model was prepared along with migration defining the required car data structure 
in order to generate the appropriate form by the front-end.
- In addition, a page with a list of users is available.