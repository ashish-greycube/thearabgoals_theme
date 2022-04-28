# -*- coding: utf-8 -*-
# Copyright (c) 2020, GreyCube Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.installer import update_site_config


def after_install():
    website_context = {
        "splash_image": "/assets/thearabgoals_theme/images/arab_goals.png"}
    update_site_config("website_context", website_context)
