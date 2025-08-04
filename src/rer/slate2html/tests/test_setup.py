# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from rer.slate2html.testing import RER_SLATE2HTML_INTEGRATION_TESTING  # noqa: E501

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that rer.slate2html is properly installed."""

    layer = RER_SLATE2HTML_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")

    def test_product_installed(self):
        """Test if rer.slate2html is installed."""
        self.assertTrue(self.installer.is_product_installed("rer.slate2html"))

    def test_browserlayer(self):
        """Test that IRerSlate2HtmlLayer is registered."""
        from plone.browserlayer import utils
        from rer.slate2html.interfaces import IRerSlate2HtmlLayer

        self.assertIn(IRerSlate2HtmlLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = RER_SLATE2HTML_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer.uninstall_product("rer.slate2html")
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if rer.slate2html is cleanly uninstalled."""
        self.assertFalse(self.installer.is_product_installed("rer.slate2html"))

    def test_browserlayer_removed(self):
        """Test that IRerSlate2HtmlLayer is removed."""
        from plone.browserlayer import utils
        from rer.slate2html.interfaces import IRerSlate2HtmlLayer

        self.assertNotIn(IRerSlate2HtmlLayer, utils.registered_layers())
