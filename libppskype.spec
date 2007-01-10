Summary:	++Skype library
Name:		libppskype
Version:	0
Release:	0.1
License:	LGPL v2.1
Group:		Libraries
Source0:	http://www.icebrains-soft.com/files/distribs/libppskype/%{name}.tar.bz2
# Source0-md5:	84cf9b1b32f3369435642a17a0e3c445
URL:		http://www.icebrains-soft.com/skype_library_0
BuildRequires:	boost-date_time-devel
BuildRequires:	dbus-devel
BuildRequires:	loki-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
++Skype library is a new, modern way to develop platform independent
Skype add-on software.

%prep
%setup -q -n libskype

%build
%{__make} -f Makefile.unx

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO
