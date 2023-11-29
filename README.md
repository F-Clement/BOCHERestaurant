![Display](/static/reservation/images/responsive.png)

Live URL:[BOCHE Restaurant](https://bocherestaurant-7ba3daeb5c57.herokuapp.com/)

BOCHE Restaurant is a reservation application designed to help users make
reservations before going to the Restaurant. Users will be able to create an
account, then login before being granted access to making a reservation. A user
can create, view, update and cancel reservations. However for security purposes,
a user can only see his or her own reservation, while the admin(in this case the
the Restaurant management) can manage all user reservation. A particular number
of Tables are created with given capacity and then the tables are assigned to
users based on the number of people they input on their reservation. A maximum
number of five people is is allowed and in case a user tries to make reserve
a pariticular date and time where 5 other reservations have been made then he or
she will get a message notifying them there is not available tabe at that time.

## Project Goals

### User Goals

- The user wants to be able to make reservations so that they are sure about
  having a table when they go to eat.
  - The user also wants to be able to manage his reservations so that he can make
  changes or cancel before time when it is not possible.
  
### Site Owner Goals

- The site owner wants to be able to receive reservations from customers before
  they visit the Restaurant so as to keep an orderly environment.
  - The site owner also wants to present a menu to users so they can make up their
  minds even before stepping into the restaurant.
  
## Existing Features

- Navigation Menu
  There is a navigation menu at the top to help users navigate the pages of the
    website easily. To the left is the name of the website acting as a logo.
    ![Navigation Menu](/static/reservation/images/menu.png)
  
- Footer
  There is a footer to the bottom of every page. Useful information such as open
    hours, address and contact details can be seen in the footer.
    ![Footer](/static/reservation/images/footer.png)
  
- Restaurant Menu
  There is a Menu page showing the different meals and drinks users can consume at
    BOCHE Restaurant. This helps users to prepare their minds before coming to eat.
    ![Restaurant Menu](/static/reservation/images/resmenu.png)
  
- Add Reservations
  There is an add reservation page, where the users fills in his information for
    his reservation, selects date and time then submits. He is notified with if this
    reservation is a success or not with a message.
    ![Add Reservation](/static/reservation/images/addreserv.png)
  
- View Reservations
  A user can only view his own reservations. While the admin can manage all the
    reservations in the database.
    ![View Reservations](/static/reservation/images/reservations.png)
  
## User Stories

<table>
    <tr>
        <th>Milestones</th>
        <th>User Story</th>
    </tr>
    <tr>
        <td>Basic Functionality</td>
        <td>
            <p>As a developer I can set up a Django project so that code for the intended application can be written.</p>
            <p>As a developer I can create a base.html template so that it extends to other templates and we avoid repetition and remain consistent.</p>
            <p>As a developer I can create a navigation menu so that users can easily navigate through the application.</p>
            <p>As a developer I can create a website footer in the base template so that it extends to other templates and we display some useful information there.</p>
            <p>As a developer I can deploy my empty project so that I confirm everything as far as deployment is concern works well to avoid last minute surprises.</p>
        </td>
    </tr>
    <tr>
        <td>
            Authentication
        </td>
        <td>
            <p>As a site user I can create an account so that I make, see, update and cancel my reservations.</p>
            <p>As a site user I can login to my account using username and password so that I check, cancel, or make a reservation.</p>
            <p>As a site user I can logout from my account so that my information is safe and reservations are saved.</p>
            <p>As a site admin I can login to the admin page so that I manage reservations made by site users.</p>
            <p>As a site admin I want users to receive notifications when they login or logout so that their user experience is better.</p>
        </td>
    </tr>
    <tr>
        <td>
            Reservation
        </td>
        <td>
            <p>As a site user I can make a reservation so that I am sure to get a table and food in the restaurant on the date and time of my reservation.</p>
            <p>As a site user I can see my reservation so that incase I forget the details I can login and to check.</p>
            <p>As a site user I can change my reservation so that incase of any emergency or changes in my schedule I still get a chance.</p>
            <p>As a site user I can cancel my reservation so that in the case where I can not be there on the reserved date I can notify the managers by just canceling the reservation.</p>
        </td>
    </tr>
    <tr>
        <td>
            Authorisation
        </td>
        <td>
            <p>As a site user I can only make a reservation if I am logged inn so that reservations I create are associated only to me.</p>
            <p>As a site user I can only view my reservations if I am logged inn so that others cannot see my reservations.</p>
            <p>As a site user I can only edit my reservation if I am logged in so that others cannot edit my reservations.</p>
            <p>As a site user I can only cancel my reservation if I am logged in so that other users cannot cancel my reservations.</p>
        </td>
    </tr>
    <tr>
        <td>
            Prevent Double Booking
        </td>
        <td>
            <p>As a site user I can only make a reservation if there is an available table so that the tables are not double booked.</p>
            <p>As a site user I can be notified about the status of my reservation so that I know if the reservation was successful if not why.</p>
        </td>
    </tr>
    <tr>
        <td>
            Add CSS Styling
        </td>
        <td>
            <p>As a restaurant owner I would like my login page responsive so as to improve user experience while login in.</p>
            <p>As a restaurant owner I would like my signup page to be responsive so as to improve user experience when they signup.</p>
            <p>As a restaurant owner I would like my add_reservation page to be responsive so as to improve user experience when they make a reservation.</p>
            <p>As a restaurant owner I would like my homepage to be responsive so as to improve user experience when the visit the restaurant website.</p>
            <p>As a restaurant owner I would like my logout page to be responsive so as to improve user experience when they logout.</p>
            <p>As a restaurant owner I would like my Menu page to display the restaurant menuso that customers can have an idea of what to eat before coming on the day of their reservation.</p>
        </td>
    </tr>
    <tr>
        <td>
            Testing and Documenting
        </td>
        <td>
            <p>As a site developer I can write tests for my application so that In the process I confirm it works like I want it to.</p>
            <p>As a site developer I can write a readme file for my application so that other developers can read it to better understand my code.</p>
        </td>
    </tr>
    



</table>