# Book Den - Data Centric Milestone Project

Book Den is a website which alows users to search and access books' description, name of author, and image. To this, there will be 
an additional link added to allow the user to read snippets/excerpt of the book from google http://books.google.co.uk/ / http://books.google.com/.

The site will also allow registered users to review any books they've read, which other (both registered and non-registered) users will have access
to, giving them an insight into what others have thought of the same books / books they may not have yet read / books they were considering purchasing. 

Each review added by registered accounts will include the features of updating, editing, and deleting their inital entry.



## UX

- As a user, I want a place where I can search for new books. 
- As a user, I want to leave reviews to help others make their decision on what books to read, and access reviews others have left to make an informed decisions 
on books I've not yet read, or books I would have otherwise not considered reading.
- As a user, I want to be able to update my review at any point after posting.
- As a user, I want to be able to delete my review at any point after posting.


## Wireframes



# Features

## Existing features
### Logging in / registering an account
- New users have the option to sign up and register an account, with a 'Sign up' button always visible on the navigation bar (with the exception of when a user has already
logged into their existing account).
- 'Log in' option visible on the navigation bar to allow existing users to log into their account, and have access to the feature of submitting a review.
- 'Sign up' link available within the 'Log in' page, and 'Log in' link available within the 'Sign up page' to allow any registered users to go from the sign up page, to the
correct page should they have somehow ended up in the wrong place, and vice versa for any new users to easily go from the 'Log in' page, to the 'Sign up' page. 
- All usersnames are required to be a minimum of 4 characters long, and a maximum of 15.
- All passwords are required to be a minimum of 5 characters long, and a maximum of 15.
- Both usernames and passwords required to follow pattern attribute added to input tags, as basic data validation, to only allow strings (both lower case and uppercase) 
from A-Z, and numbers from 0-9 


### User session
- Session cookies used to display registered users username on their profile, upon logging in.
- Session cookies also used in index.html to present the username of the person who has submitted a review.
<!--- **NOTE TO SELF: have also implemented feature to delete cookies upon logging out - test before writing about this --->


### About website
- About section of the website to be visible within index.html - this will be side by side with the reviews submitted by registered users.

## Features to implement

- Requirement for email address to be used as part of the sign up page (input form to require: Username / Email address / Password) - this would then allow some form of 
email recovery system if any users have forgotten their password. 
- A password check which ensures the user has entered the correct password during the Sign up page, to avoid users not being able to log back into their account
should they have made a typo/some form of error during the initial sign up stage


