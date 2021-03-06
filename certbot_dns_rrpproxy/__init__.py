"""
The `~certbot_dns_rrpproxy.dns_rrpproxy` plugin automates the process of
completing a ``dns-01`` challenge (`~acme.challenges.DNS01`) by creating, and
subsequently removing, TXT records using the RRPproxy API.


Named Arguments
---------------

========================================  =====================================
``--dns-rrpproxy-credentials``            RRPproxy account credentials in INI
                                          format. (Required)
``--dns-rrpproxy-propagation-seconds``    The number of seconds to wait for DNS
                                          to propagate before asking the ACME
                                          server to verify the DNS record.
                                          (Default: 120)
``--dns-rrpproxy-staging``                Whether this is a test run (OTE).
========================================  =====================================


Credentials
-----------

Use of this plugin requires a configuration file containing the login
credentials with the required permissions to update DNS zones.

.. code-block:: ini
   :name: credentials.ini
   :caption: Example credentials file:

   certbot_dns_rrpproxy:dns_rrpproxy_s_login = user
   certbot_dns_rrpproxy:dns_rrpproxy_s_pw = password

The path to this file can be provided interactively or using the
``--dns-rrpproxy-credentials`` command-line argument. Certbot records the
path to this file for use during renewal, but does not store the file's contents.

.. caution::
   Users who can read this file can use these credentials to issue arbitrary
   API calls on your behalf. Users who can cause Certbot to run using these
   credentials can complete a ``dns-01`` challenge to acquire new certificates
   or revoke existing certificates for associated domains, even if those
   domains aren't being managed by this server.

Certbot will emit a warning if it detects that the credentials file can be
accessed by other users on your system. The warning reads "Unsafe permissions
on credentials configuration file", followed by the path to the credentials
file. This warning will be emitted each time Certbot uses the credentials file,
including for renewal, and cannot be silenced except by addressing the issue
(e.g., by using a command like ``chmod 600`` to restrict access to the file).

Examples
--------

.. code-block:: bash
   :caption: To acquire a certificate for ``example.com``

   certbot certonly \\
     --authenticator certbot-dns-rrpproxy:dns-rrpproxy \\
     --certbot-dns-rrpproxy:dns-rrpproxy-credentials ~/.secrets/certbot/rrpproxy.ini \\
     -d example.com

.. code-block:: bash
   :caption: To acquire a single certificate for both ``example.com`` and
             ``www.example.com``

   certbot certonly \\
     --authenticator certbot-dns-rrpproxy:dns-rrpproxy \\
     --certbot-dns-rrpproxy:dns-rrpproxy-credentials ~/.secrets/certbot/rrpproxy.ini \\
     -d example.com \\
     -d www.example.com

.. code-block:: bash
   :caption: To acquire a certificate for ``example.com``, waiting 120 seconds
             for DNS propagation

   certbot certonly \\
     --authenticator certbot-dns-rrpproxy:dns-rrpproxy \\
     --certbot-dns-rrpproxy:dns-rrpproxy-credentials ~/.secrets/certbot/rrpproxy.ini \\
     --certbot-dns-rrpproxy:dns-rrpproxy-propagation-seconds 120 \\
     -d example.com

.. code-block:: bash
   :caption: To acquire a certificate for ``*.example.com`` and ``example.com``
             in a staging request

   certbot certonly \\
     --authenticator certbot-dns-rrpproxy:dns-rrpproxy \\
     --certbot-dns-rrpproxy:dns-rrpproxy-credentials ~/.secrets/certbot/rrpproxy.ini \\
     --certbot-dns-rrpproxy:dns-rrpproxy-staging \\
     -d *.example.com \\
     -d example.com

"""
