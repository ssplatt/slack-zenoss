# Updated from https://github.com/ssplatt/slack-zenoss
# adds arguments for event context and URL.
#
#!/usr/bin/env python
import json
import httplib2

from urlparse import urlparse

def sendSlack(slackUrl='http://www.slack.com',proxyUrl=None,proxyUsername=None,proxyPassword=None,**data):
    evt=data['evt']
    device=evt.device
    component=evt.component
    severity=evt.severity
    message=evt.message
    summary=evt.summary
    cleared_by=evt.clearid

    detail_url = data['urls']['eventUrl']
    ack_url = data['urls']['ackUrl']
    close_url = data['urls']['closeUrl']
    dev_events_url = data['urls']['eventsUrl']
    reopen_url = data['urls']['reopenUrl']
    devUrl=data['urls']['deviceUrl'] 

    # setup the output
    # set the color based on severity
    if severity == 5:
        color = "danger" #red
    elif severity == 4:
        color = "#FF9B01" #orange
    elif severity == 3:
        color = "FFEA00" #yellow
    elif severity == 2:
        color = "#0372B8" #blue
    elif severity == 1:
        color = "#757575" #gray
    elif severity == 0:
        color = "good" #green
    else:
        color = ""
    
    if cleared_by is None:
        fields = [{
            "title": "Actions",
            "value": "<"+detail_url+"|Event Details>\n<" + ack_url + "|Acknowledge>\n<" + close_url + "|Close>\n<" + dev_events_url + "|View Device Events>",
            "short": False
        }]
    else:
        # clear event triggered
        color = "good" #green
        message = "CLEAR: " + message
        summary = "CLEAR: " + summary
        fields = [{
            "title": "Actions",
            "value": "Cleared by: " + cleared_by + "\n<" + reopen_url + "|Reopen>",
            "short": False
        }]
        
    attachment = [{
        "fallback": summary,
        "text": summary,
        "title": "<"+devUrl+"|"+device+">",
        "title_link": detail_url,
        "color": color,
        "fields": fields
    }]

    # post to slack
    payload = json.dumps({
	"icon_url":"http://www.zenoss.com/sites/default/files/favicon_0.png",
	"username":"zenossbot",
        "attachments": attachment
    })
   
    if proxyUrl:
	parsedUrl=urlparse(proxyUrl)
	proxyHost=parsedUrl.hostname
	proxyPort=parsedUrl.port
	h = httplib2.Http(disable_ssl_certificate_validation=True,proxy_info = httplib2.ProxyInfo(httplib2.socks.PROXY_TYPE_HTTP, proxyHost, proxyPort)) 
    else:
    	h = httplib2.Http(disable_ssl_certificate_validation=True)
    (resp, content) = h.request(slackUrl, "POST", body=payload, headers={'content-type':'application/json'} )
    
