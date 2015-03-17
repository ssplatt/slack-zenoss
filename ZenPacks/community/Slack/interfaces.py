######################################################################
#
# Copyright 2012 Zenoss, Inc.  All Rights Reserved.
#
######################################################################

from zope.interface import Interface
try:
    from Products.Zuul.interfaces.actions import IActionContentInfo
except ImportError:
    from Products.Zuul import IInfo as IActionContentInfo
from Products.Zuul.interfaces import IFacade
from Products.Zuul.form import schema
from Products.Zuul.utils import ZuulMessageFactory as _t


class ISlackActionContentInfo(IActionContentInfo):

    slackUrl = schema.TextLine(
        title=_t(u'Slack URL'),
        order=90,
    )

    proxyUrl = schema.TextLine(
        title=_t(u'Proxy URL'),
        order=100,
    )

    proxyUsername = schema.TextLine(
        title=_t(u'Proxy username'),
        order=110,
    )

    proxyPassword = schema.Password(
        title=_t(u'Proxy password'),
        order=120,
    )

