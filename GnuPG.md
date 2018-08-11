This fork and subsequent branches mark a deliberate fork in existing Limnoria in order to get rid of some known to be insecure software.  The problem software is the old python-gnupg package, along with all other wrappers utilising modules like `subprocess` or `sh`.

The replacement is the official Python bindings for GPGME and thus requires that software to be installed as a dependency.  This will also increase the restrictions on Python versions.  As such it is unlikely to be merged with Limnoria until after Python 2.7 is fully EOL (in less than a year and a half).

-- Ben McGinnes <ben@gnupg.org>, signed by [0x321E4E2373590E5D](GnuPG.md.asc)
