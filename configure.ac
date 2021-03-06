# Process this file with autoconf to produce a configure script.

AC_PREREQ([2.69])

m4_define([PKG_NAME], rolekit)
m4_define([PKG_VERSION], m4_bpatsubst(m4_esyscmd([grep "Version:" rolekit.spec]), [Version:\W\([0-9.]*\)\W], [\1]))
m4_define([PKG_RELEASE], m4_bpatsubst(m4_esyscmd([grep "Release:" rolekit.spec]), [Release:\W\([0-9.]*\).*\W], [\1]))
m4_define([PKG_TAG], m4_bpatsubst(m4_format(r%s-%s, PKG_VERSION, PKG_RELEASE), [\.], [_]))

AC_INIT(PKG_NAME,PKG_VERSION)
AC_CONFIG_SRCDIR([src/rolekit])
AC_PREFIX_DEFAULT([/usr])

AM_INIT_AUTOMAKE([1.11 tar-ustar no-define foreign dist-bzip2 no-dist-gzip])

AC_SUBST([PACKAGE_RELEASE], '[PKG_RELEASE]')
AC_DEFINE_UNQUOTED([PACKAGE_RELEASE], ["$PACKAGE_RELEASE"])
AC_SUBST([PACKAGE_TAG], '[PKG_TAG]')
AC_DEFINE_UNQUOTED([PACKAGE_TAG], ["$PACKAGE_TAG"])

AC_PROG_INSTALL
AC_PROG_LN_S
AC_PROG_MKDIR_P
AC_PROG_SED
AC_PROG_GREP
AC_PROG_AWK
AC_PROG_MAKE_SET
AM_PATH_PYTHON([3.4])

AC_PATH_PROG([XSLTPROC], [xsltproc])
AC_PATH_PROG([KILL], [kill], [/usr/bin/kill])

#############################################################

AC_ARG_ENABLE([systemd],
       AS_HELP_STRING([--disable-systemd], [Disable systemd support]),
       [use_systemd=$enableval], [use_systemd=yes])
AM_CONDITIONAL(USE_SYSTEMD, test x$use_systemd = xyes)
AC_SUBST(USE_SYSTEMD)

AC_ARG_ENABLE([sysconfig],
    [AS_HELP_STRING([--enable-sysconfig], [Install sysconfig file])],
    [INSTALL_SYSCONFIG="${enableval}"], [INSTALL_SYSCONFIG='no'])
AM_CONDITIONAL(INSTALL_SYSCONFIG, [test x$INSTALL_SYSCONFIG = xyes])
AC_SUBST(INSTALL_SYSCONFIG)

AC_ARG_WITH([systemd-unitdir],
       AS_HELP_STRING([--with-systemd-unitdir], [Directory for systemd service files]),
       [SYSTEMD_UNITDIR=$withval], [SYSTEMD_UNITDIR="$(pkg-config systemd --variable=systemdsystemunitdir)"])
AC_SUBST(SYSTEMD_UNITDIR)

AC_ARG_WITH([systemd-confunitdir],
       AS_HELP_STRING([--with-systemd-confunitdir], [Directory for local edits to systemd service files]),
       [SYSTEMD_CONFUNITDIR=$withval], [SYSTEMD_CONFUNITDIR="$(pkg-config systemd --variable=systemdsystemconfdir)"])
AC_SUBST(SYSTEMD_CONFUNITDIR)


AC_ARG_WITH([system-bus-services-dir],
       AS_HELP_STRING([--with-system-bus-services-dir], [Directory for system services files]),
       [SYSTEM_BUS_SERVICES_DIR=$withval], [SYSTEM_BUS_SERVICES_DIR="$(pkg-config dbus-1 --variable=system_bus_services_dir)"])
AC_SUBST(SYSTEM_BUS_SERVICES_DIR)

AC_ARG_WITH([bashcompletiondir],
       AS_HELP_STRING([--with-bashcompletiondir=DIR], [Bash completions director
y]),
       [BASHCOMPLETIONDIR=$withval], [BASHCOMPLETIONDIR="${datadir}/bash-completion/completions"])
AC_SUBST(BASHCOMPLETIONDIR)

#############################################################

AC_SUBST([GETTEXT_PACKAGE], '[PKG_NAME]')
AC_DEFINE_UNQUOTED([GETTEXT_PACKAGE], ["$GETTEXT_PACKAGE"],)

IT_PROG_INTLTOOL([0.35.0], [no-xml])
AM_PO_SUBDIRS

AC_CONFIG_COMMANDS([xsl-cleanup],,[rm -f doc/xml/transform-*.xsl])

AC_CONFIG_FILES([Makefile
		 config/Makefile
		 doc/Makefile
		 doc/man/Makefile
		 doc/man/man1/Makefile
		 doc/man/man5/Makefile
		 doc/xml/Makefile
		 doc/graphics/Makefile
		 po/Makefile.in
		 shell-completion/Makefile
		 src/rolekit/config/__init__.py
		 src/Makefile])
AC_OUTPUT
