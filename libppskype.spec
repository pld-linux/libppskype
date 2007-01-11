# TODO
# - devel, shared library and -static
Summary:	++Skype library
Name:		libppskype
Version:	0
Release:	0.1
License:	LGPL v2.1
Group:		Libraries
Source0:	http://www.icebrains-soft.com/files/distribs/libppskype/%{name}.tar.bz2
# Source0-md5:	84cf9b1b32f3369435642a17a0e3c445
Patch0:		%{name}-optflags.patch
URL:		http://www.icebrains-soft.com/skype_library_0
BuildRequires:	boost-date_time-devel >= 1.33.1
BuildRequires:	boost-regex-devel >= 1.33.1
BuildRequires:	boost-test-devel >= 1.33.1
BuildRequires:	dbus-devel
BuildRequires:	loki-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
++Skype library is a new, modern way to develop platform independent
Skype add-on software.

%prep
%setup -q -n libskype
%patch0 -p1

%build
%{__make} -f Makefile.unx \
	CCP="%{__cxx}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -f Makefile.unx install  \
	INSTALL_DIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_includedir}/%{name},%{_libdir}}
mv $RPM_BUILD_ROOT{/h/*,%{_includedir}/%{name}}
mv $RPM_BUILD_ROOT{/lib/*,%{_libdir}}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO
%{_includedir}/libppskype
%{_libdir}/libppskype.a
%attr(755,root,root) %{_libdir}/libppskype.so
