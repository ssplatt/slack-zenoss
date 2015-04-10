from zope.interface import implements

try:
    from Products.Zuul.infos.actions import ActionContentInfo
except ImportError:
    from Products.Zuul.infos import InfoBase as ActionContentInfo

from Products.Zuul.infos.actions import ActionFieldProperty

from ZenPacks.community.Slack.interfaces import ISlackActionContentInfo


class SlackActionContentInfo(ActionContentInfo):
    implements(ISlackActionContentInfo)

    slackUrl = ActionFieldProperty(ISlackActionContentInfo, 'slackUrl')
    proxyUrl = ActionFieldProperty(ISlackActionContentInfo, 'proxyUrl')
    proxyUsername = ActionFieldProperty(ISlackActionContentInfo, 'proxyUsername')
    proxyPassword = ActionFieldProperty(ISlackActionContentInfo, 'proxyPassword')

