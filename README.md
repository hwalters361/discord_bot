# discord_bot
A simple script and tutorial on how to use the discord API to create a bot that sends private messages.

***

To write a script that sends private messages to Discord users, you can use the `discord.py` library in Python. To work with the Python library and the Discord API, you must first create a bot and copy its token from the Discord application.

This can be done by following these steps :

1.  Check that you’re logged on to the Discord app.
2.  Navigate to the application page.
3.  Click on the “New Application” button.
4.  Give the application a name and click “Create”.
5.  Go to the “Bot” tab and then click “Add Bot”. You will have to confirm by clicking "Yes, do it!".

Now your bot has been created, the next step is to copy the token. Note that this token is your bot's password so don't share it with anybody. It could allow someone to log in to your bot and do all sorts of bad things. You can regenerate the token if it accidentally gets shared.

After successfully obtaining the bot token, invite the bot to the server where you want it to perform actions and ensure that the bot has the necessary permissions within the server to send messages and read user IDs. 

Now you're ready to start using the discord API. Before you start, check that you have Python installed, and install the `discord.py` library by running :

```python
pip install discord.py
```

Use the simple script `simple_bot.py` in this repository as an example that you can adapt to your needs.

The provided script works by setting up the bot by creating a bot instance and defining an event that prints a message when the bot is successfully logged in, it then defines a command called `send_message` and sends a private message to a specified user. 

To execute the command, open a direct message with the bot by clicking on its name in the server member list and selecting "Message". In the DM chat with the bot, type the `!send_message` followed by the user's mention or their ID and the message you want to send. Here's an example:
```
!send_message @username Hello! This is a private message.
```
Once the command is executed, the bot should send a confirmation message.

Don't forget to replace `YOUR_BOT_TOKEN` with the actual token when running the script.
