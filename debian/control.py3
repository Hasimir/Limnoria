Source: limnoria-gnupg
Section: net
Priority: optional
Maintainer: Valentin Lorentz <progval@progval.net>
Build-Depends: debhelper (>=3.9.2), dh-python, cdbs (>= 0.4.90~), python3 (>=3.4), python3-setuptools
XS-Python-Version: >=3.4
Standards-Version: 3.9.2

Package: limnoria-gnupg
Architecture: all
Depends: python3 (>=3.4), dh-python, ${misc:Depends}
Recommends: python3-simplejson, python3-feedparser, python3-sqlite3
Suggests: python3-twisted-core, python3-twisted-names, python3-dictclient, python3-dateutil, python3-sqlalchemy, libgpgme, libgpgme-dev
Conflicts: supybot, limnoria
Provides: supybot, limnoria
Replaces: supybot, limnoria
Section: net
Priority: optional
Homepage: https://github.com/ProgVal/Limnoria
Description: Fork of the robust and user-friendly Python IRC bot Supybot.
 It provides several enhancements, such as internationalization and
 embedded HTTP server available to plugins. All plugins written for
 Supybot are still compatible with Limnoria.

