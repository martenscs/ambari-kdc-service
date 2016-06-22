#!/usr/bin/env python
from resource_management.libraries.functions.version import format_hdp_stack_version, compare_versions
from resource_management import *

# server configurations
config = Script.get_config()

kdc_realm = config['configurations']['krb5-config']['kdc.realm']
kdc_domain = config['configurations']['krb5-config']['kdc.domain']
kdc_host = config['configurations']['krb5-config']['kdc.host']
