How to start hacking:

cd into either of flask or django, then..
cd into the directory named after the storage provider, then..
source .setup

if you're creating a new project/storage provider, then do the following within that directory:

echo "source ../../global-app-setup" > .setup

---
This is an idea I have for project management, somewhat based on concepts from Kanban.

The name kitchen refers to the use of different commercial kitchen metaphors being used within the application:

Order
* A task/project request
* An Order contains limited information
    * What needs to be done
    * When it needs to be done by
    * Priority

Customer
* Customers are the business owner of an Order

Expo (Expediter)
* An Expo facilitates a project, similar to a project manager
* The Expo determines whether or not an Order is active or inactive

Reservation
* The committed deadline for an Order
* The Expo sets the reservation for an Order

Station
* An order can be in one of the following Stations
    * Cooking: Currently being worked on (Active Tasks)
    * Thawed: Can be worked on but not currently (Inactive Tasks)
    * Frozen: A Thawed Order that will not be worked on due to lack of priority
    * Burnt: An Order that is past its Reservation

Priority
* Within each Station, there are 3 priorities, with specific constraints
    * Cooking
        * High Priority: There can only ever be 1 High Priority Order in this Station
        * Medium Priority: There can only ever be 2 Medium Priority Orders in this Station
        * Low Priority: There can only ever be 3 Low Priority Orders in this Station
    * Thawed
        * High Priority: There can only ever be 5 High Priority Orders in this Station
        * Medium Priority: There can only ever be 10 Medium Priority Orders in this Station
        * Low Priority: There can only ever be 15 Low Priority Orders in this Station
    * Frozen
        * Orders in this Station are not prioritized and there are no limits to how many can exist
    * Burnt
        * The constraints around this Station are still being fleshed out

Line
* The Line is the list of people available for any given Order

Party
* The Party is the list of stakeholders for any given Order

Ingredients
* Ingredients are effectively a list of previous Orders that can be used to estimate Reservations

Prep
* The Expo receives the initial Order, consults Ingredients, selects people from Line, sets Reservation
* The Expo sets an Order as Cooking or Thawed. Default Station is Thawed.

Order Up/Table Order/Send Back
* When a member of the Party completes an Order, they will click Order Up
* The Expo will review the Order by consulting a checklist
* A positive review will Table the Order (the Customer will be notified that the Order is complete)
* A negative review will Send the Order back to the member of the Party

Walk In
* A Walk In is an adhoc Order that is immediately promoted to High Priority in the Cooking Station
* Customers will be allowed a certain number of Walk Ins
* A Walk In will cause further limiting around Priority/Station rules, still being fleshed out

Now that the definitions are out of the way, it is important to note that priority management is 100% automatic. Promoting an Order to High Priority in the Cooking Station means that whatever was in that Station previously is demoted to Medium Priority. The Order with the later Reservation will then be demoted to Low Priority. The Order with the latest Reservation in Low Priority will be demoted to the Thawed Station. The same shuffling occurs until the Order with the latest Reservation in Low Priority in the Thawed Station drops off to the Frozen Station. What this allows for is flexible re-prioritization of tasks with a high level of visibility into tradeoffs.

As this is something I sketched out after dinner, it may never see the light of day. :)
