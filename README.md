# This project is not supported anymore. If you want to make changes, please fork and maintain your own fork.

# Slack - Zenoss Integration WebHook Script
A Slack notification using an incoming webhook to show events from Zenoss.

To use:
* Install the ZenPack using  zenpack--install=PATH_TO_EGG
* In Slack, create a new Incoming WebHook
* Set the channel to post to, i.e. #alerts
* Set the name of the bot, i.e. Zenoss-bot
* Set a custom icon, i.e. search for one you like and upload it.
* Copy the WebHook URL
* In Zenoss, click Events then Triggers, and then Notifications
* Create a new Notification by clicking the +, give it a name like "PushToSlack" and choose "Slack" from the Action pulldown
* click Submit to save
* Open the new notification and click content.
* Paste the webhook Url in to the slackUrl field
* click Submit to save

![alt tag](https://raw.githubusercontent.com/jregovic/slack-zenoss/master/ZenossSlack.png)
