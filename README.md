
# BOCHE Restaurant

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
        <td>Authentication</td>
        <td>
            <p>As a site user I can create an account so that I make, see, update and cancel my reservations.</p>
            <p>As a site user I can login to my account using username and password so that I check, cancel, or make a reservation.</p>
            <p>As a site user I can logout from my account so that my information is safe and reservations are saved.</p>
            <p>As a site admin I can login to the admin page so that I manage reservations made by site users.</p>
            <p>As a site admin I want users to receive notifications when they login or logout so that their user experience is better.</p>
        </td>
    </tr>

</table>