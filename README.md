# IMPORTANT: Don't run this script using your main account, use a different account
> I do not gurantee that your account won't be blocked

## The script is for sending tweets from your account automatically every 60 seconds

Every 60 seconds because twitter has a cap of 2400 tweets every 24 hours.
I wouldn't recommend anything less than 37 seconds or your account might get blocked by Twitter.

### PREREQUISITES
* [Developer account](https://developer.twitter.com/apps) You need to have a developer account for this and then you need to create an app. Make sure to set the app permissions to 'read and write' and then generate the 'access_token' and 
'access_token_secret' keys. 
Make sure to save the api_key, api_secret_key, access_token and access_token_secret key to your notepad before proceeding and then put them in your script.py
https://developer.twitter.com/apps

* [Git](https://git-scm.com/downloads)

* [Heroku Account](https://www.heroku.com/) (Only if you are planning to run the script on a server)

* [Python](https://www.python.org/downloads/)


Additional info: Each tweet send from a single twitter account has to be unique hence the time stamp in line(21) in script.py which makes every tweet unique


# Running the script
## I would recommend running the script locally on your machine
   ```If you do plan to run the script on a server then
   increase the time from 60 seconds to 180 seconds
   ```

1. If you want to run the script locally on your machine just run the ```script.py``` file.
   NOTE-If you are using Windows you need to install python https://www.python.org/downloads/
   Open terminal or command-prompt in the folder where your script.py is saved and enter the following commands:
   ```bash
   $ pip install tweepy
   ```
   ```bash
   $ python script.py
   ```

2. If you want to run the script on Heroku server upload all the files to Heroku server
   Follow these steps:
   1. Create heroku account https://www.heroku.com/
      Create an app
      Install heroku cli https://devcenter.heroku.com/articles/heroku-cli

   2. ```git clone``` this repository. 
      If you are using Windows you need to install git https://git-scm.com/downloads
      Open your terminal or command-prompt and enter this command:
      ```bash
      $ git clone https://github.com/anx12/tweetBot
      ```
   
   3. Move into the cloned folder
      ```bash
      $ cd tweetBot
      ```
      
   4. Open script.py in your editor and place your api_key, api_secret_key, 
      access_token and access_token_secret keys in script.py
   
   5. Then commit the changes 
      ```bash
      $ git add .
      ```
      ```bash
      $ git commit -m "change keys"
      ```
      
   6. Upload files to Heroku
      ```bash
      $ heroku login
      ```
      ```bash
      $ heroku git:clone -a your_Heroku_app_name
      ```
      ```bash
      $ git push heroku master
      ```
      
   7. To run your application
      ```bash
      $ heroku ps:scale worker=1
      ```
      
   8. From now on you can use usual git commands (push, add, commit, etc.) to update your app. 
      Every time you push heroku master your app gets redeployed with updated source code
      
   9. To see your logs
      ```bash
      $ heroku logs --tail
      ```
      
   10. To stop your application
       ```bash
       $ heroku ps:scale worker=0
       ```
     
      
   

