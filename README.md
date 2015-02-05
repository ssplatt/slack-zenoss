# Slack - Zenoss Integration WebHook Script
A Slack incoming webhook to show events from Zenoss.

To use:
* In Slack, create a new Incoming WebHook
* set the channel to post to, i.e. #alerts
* set the name of the bot, i.e. Zenoss-bot
* set a custom icon, i.e. search for one you like and upload it.
* copy the WebHook URL
* save slack_zenoss.py to /usr/local/bin on your Zenoss server
* ```chmod 755 /usr/local/bin/slack_zenoss.py```
* Use your favorite editor to paste your WebHook URL in the hookurl="" variable in slack_zenoss.py
* back in Zenoss, click Events then Triggers
* create a new trigger by clicking the +, give it a name like "PushToSlack", make sure the Enabled box is checked
* click Notifications, make a new notification by pressing the +, name it something like "PushToSlack", select "Command" as the action, make sure the Enabled box is checked
* on the Content tab, set the commands:

```
command: /usr/local/bin/slack_zenoss.py --message=${evt/message} --summary=${evt/summary} --device='${evt/device}' --component='${evt/component}' --severity='${evt/severity}' --detail_url='${urls/eventUrl}' --ack_url='${urls/ackUrl}' --close_url='${urls/closeUrl}' --dev_events_url='${urls/eventsUrl}'

clear command: /usr/local/bin/slack_zenoss.py --message=${evt/message} --summary=${evt/summary} --device='${evt/device}' --component='${evt/component}' --severity='${evt/severity}' --detail_url='${urls/eventUrl}' --cleared_by='${evt/clearid}' --dev_events_url='${urls/eventsUrl}' --reopen_url='${urls/reopenUrl}'
```

* click Submit to save

only some of the Event Expressions are used in this script at the moment. For a full list of expressions, see http://community.zenoss.org/docs/DOC-12029
