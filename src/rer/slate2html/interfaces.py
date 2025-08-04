# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IRerSlate2HtmlLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""
