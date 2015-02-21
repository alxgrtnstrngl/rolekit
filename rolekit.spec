Summary: A server daemon with D-Bus interface providing a server roles
Name: rolekit
Version: 0.2.0
Release: 1%{?dist}
URL: http://fedorahosted.org/rolekit
License: GPLv2+
Source0: https://fedorahosted.org/released/rolekit/%{name}-%{version}.tar.bz2
BuildArch: noarch
BuildRequires: gettext
BuildRequires: intltool
# glib2-devel is needed for gsettings.m4
BuildRequires: glib2, glib2-devel, dbus-devel
BuildRequires: systemd-units
BuildRequires: docbook-style-xsl
Requires: dbus-python
Requires: python-futures
Requires: python-slip-dbus
Requires: python-decorator
Requires: python-IPy
Requires: pygobject3-base
Requires: firewalld
Requires: systemd
Requires: NetworkManager
Requires: yum
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
rolekit is a server daemon that provides a D-Bus interface and server roles.


%prep
%setup -q

%build
%configure

%install
%{__mkdir_p} $RPM_BUILD_ROOT/%{_datadir}/bash-completion/completions
make install DESTDIR=%{buildroot}

# Move the testrole into documentation instead of the live system
%{__mkdir_p} $RPM_BUILD_ROOT/%{_docdir}/examples/
%{__mv} $RPM_BUILD_ROOT/%{_prefix}/lib/rolekit/roles/testrole \
        $RPM_BUILD_ROOT/%{_docdir}/examples/


#%find_lang %{name} --all-name

%post
%systemd_post rolekit.service

%preun
%systemd_preun rolekit.service

%postun
%systemd_postun_with_restart rolekit.service


#%files -f %{name}.lang
%files
%doc COPYING README
%{_sbindir}/roled
%{_bindir}/rolectl
%defattr(-,root,root)
%dir %{_sysconfdir}/rolekit
%dir %{_sysconfdir}/rolekit/roles
%dir %{_prefix}/lib/rolekit
%dir %{_prefix}/lib/rolekit/roles
%{_prefix}/lib/rolekit/roles/domaincontroller/*.py*

%{_prefix}/lib/rolekit/roles/databaseserver/*.py*
%{_prefix}/lib/rolekit/roles/databaseserver/tools/rk_db_setpwd.py*

%config(noreplace) %{_sysconfdir}/sysconfig/rolekit
%{_unitdir}/rolekit.service
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/rolekit1.conf
%{_datadir}/polkit-1/actions/org.fedoraproject.rolekit1.policy
%{_datadir}/dbus-1/system-services/org.fedoraproject.rolekit1.service
%attr(0755,root,root) %dir %{python_sitelib}/rolekit
%attr(0755,root,root) %dir %{python_sitelib}/rolekit/config
%attr(0755,root,root) %dir %{python_sitelib}/rolekit/server
%attr(0755,root,root) %dir %{python_sitelib}/rolekit/server/io
%{python_sitelib}/rolekit/*.py*
%{python_sitelib}/rolekit/config/*.py*
%{python_sitelib}/rolekit/server/*.py*
%{python_sitelib}/rolekit/server/io/*.py*
%{_mandir}/man1/role*.1*
%{_mandir}/man5/role*.5*
%{_docdir}/examples/

%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/rolectl


%changelog
* Thu Jan 22 2015 Stephen Gallagher <sgallagh@redhat.com> 0.2.0-1
- New Database Server Role
- Enhancements to async.py for impersonation and passing stdin

* Mon Nov 17 2014 Stephen Gallagher <sgallagh@redhat.com> 0.1.2-1
- More documentation updates
- Allow roles to override MAX_INSTANCES
- Remove the instance if settings-verification fails

* Mon Nov 17 2014 Stephen Gallagher <sgallagh@redhat.com> 0.1.1-1
- Improve documentation
- Remove incomplete database server role
- Add bash-completion file
- Bug-fixes

* Mon Oct 13 2014 Thomas Woerner <twoerner@redhat.com> 0.1.0-1
- Update role instance state on roled wakup.
- New package and group installation during role deployment
- RoleBase: Use systemd targets for start() and stop()
- New support for systemd targets
- RoleBase: Handle NULL types
- Domain Controller: Export properties
- Added missing requires for firewalld, systemd, NetworkManager and yum
- New --settings-file option for rolectl, replaces --set option
- New firewall handling
- Property fixes, new property checks
- Bug fixes

* Fri Aug 22 2014 Thomas Woerner <twoerner@redhat.com> 0.0.3-1
- Domain Controller: Add decommission routine
- Better trapping of non-ASCII output on subprocess
- Domain Controller deployment
- Make decommission asynchronous
- Improve exception logging
- DBusRole: New method get_name, using in RoleD.getNamedRole
- Enable logging of subprocess output
- Implement starting and stopping services, and use it in databaseserver
- New async.async_subprocess_future helper
- Changed async naming conventions
- Convert exceptions in D-Bus methods in async methods
- Added missing resetError message
- Several fixes and cleanups

* Mon Aug 11 2014 Thomas Woerner <twoerner@redhat.com> 0.0.2-1
- new instance support
- new rolectl command line tool
- new redeploy feature for instances
- new async support for deploy, start and stop D-Bus methods
- finalized states
- adapted D-Bus interface for instances
- dbus activation and auto-termination after some inactivity time
- dbus exception handling fixes
- build fixes and cleanups (distcheck, po/Makefile.in.in, ..)
- several fixes and cleanups

* Fri May 23 2014 Thomas Woerner <twoerner@redhat.com> 0.0.1-1
- initial package (proof of concept implementation)
