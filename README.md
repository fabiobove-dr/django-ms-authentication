# django-ms-authentication
A sample user authentication using Microsoft Graph APIs


# How does it work
This is an example of integration between MS Graph APIs and Django.<br>
We use MS suite to enable users to authenticate on our application, and use services that otherwhise wouldn't be available.<br>
For demonstration purpose we have two hidden sections that only authenticated users can reach:
 - Hidden Page
 - Another Hidden Page

# Authentication  
The "/ms_authentication" folder contains the django application which manages the user authentication<br>
The "/django_ms_authentication" folder instead is the directory of the whole project<br>

For the authentication we need to register the application on Azure, and then create a "oauth_settings.yml" file
that needs to be stored in the main project folder ("/django_ms_authentication")<br>
<br>
app_id: "2" <br>
app_secret: "" <br>
redirect: "http://localhost:8000/callback" <br>
scopes: ""<br>
authority: "https://login.microsoftonline.com/common"<br>
authorize_endpoint: "/oauth2/v2.0/authorize"<br>
token_endpoint: "/oauth2/v2.0/token"<br>
<br>
The application needs to be configured as multitenant on the Azure panel.
<br>
# Lyouts and templates
The lyouts of the pages can be modified and is stored in the templates and static directories.<br>
