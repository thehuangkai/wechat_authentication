WeChat official account authentication using flask

This are the files for authenticating a wechat official account bot. main.py authenticates the bot by handling a GET request sent by the
wechat platform. You can read more about it on the official wechat documentations. custom_keyboard.py adds a custom wechat keyboard by sending
a post request with the keyboard as body data. 

Getting Started

My simple app is created with flask and hosted on an apache server. Mod_wsgi is needed to be configured for using the app. Make sure these 2 are 
installed.

Special notes:
High recommend to understand the wechat documentations first and receive your own bot tokens before working on it. Request data are in XML format
instead of JSON, except for the custom keyboard which needs to be in JSON format.
