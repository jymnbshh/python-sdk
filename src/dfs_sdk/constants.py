"""
Provides hard-coded values used in this package.  No imports are allowed
since many other modules import this one
"""
__copyright__ = "Copyright 2017, Datera, Inc."

VERSION = "1.2.16"

VERSION_HISTORY = """
Version History:
    1.1.0 -- Initial Version
    1.1.1 -- Metadata Endpoint, Pep8 cleanup, Logging revamp
             Python 3 compatibility, Versioning and Version Headers,
    1.1.2 -- User, Event_system, Internal, Alerts Endpoints/Entities
    1.2.0 -- v2.2 support, API module refactor
    1.2.1 -- Massive rewrite to use /api endpoints instead of manually
             curated list.  Log compression
    1.2.2 -- Change python version check in Connection to be forgivness based
    1.2.4 -- Named object support, hw metics support
    1.2.5 -- v2.2 Paging support
    1.2.6 -- Bugfix for API v2.1 limit parameter
    1.2.7 -- Changed connection to use requests library, added support for
             logs_upload endpoint.  Added 'strict' parameter to constructor
             which allows disabling endpoint validity checks if set to 'False'
    1.2.8 -- Added support for certs, trace_ids and standard logging
    1.2.9 -- Added stream call for use with Metrics style endpoints
    1.2.10 -- Added back create/delete hooks, implemented hook loading and
              a hook inheritance interface.
    1.2.11 -- Increased log rotation size before compression to 50MB
              and decreased number of retained rotations to 5
    1.2.12 -- Added capability of adding custom headers to requests
    1.2.13 -- Added LDAP support to UDC config
    1.2.15 -- Fixed ldap server bug, dropped get_argparser requirement from
              scaffold, changed required requests version because of security
              vulnerability. Updated the readme.
    1.2.16 -- 503 retry support
"""

API_VERSIONS = ("v2", "v2.1", "v2.2")

REST_PORT = 7717
REST_PORT_HTTPS = 7718

DEFAULT_HTTP_TIMEOUT = 300

PYTHON_2_7_0_HEXVERSION = 0x020700f0
PYTHON_2_7_9_HEXVERSION = 0x020709f0
PYTHON_3_0_0_HEXVERSION = 0x030000f0

CACHED_SCHEMA = "/tmp/.cached-schema"

TIMEOUT_503 = 300
