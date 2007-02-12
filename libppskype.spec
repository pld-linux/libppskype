Summary:	++Skype library
Summary(pl.UTF-8):	Biblioteka ++Skype
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

%description -l pl.UTF-8
Biblioteka ++Skype to nowy, nowoczesny sposób tworzenia dodatków do
Skype'a niezależnych od platformy.

%package devel
Summary:	Header files for ++Skype library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki ++Skype
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
#Requires:	FILLME (boost,dbus,loki-devel???)

%description devel
Header files for ++Skype library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki ++Skype.

%package static
Summary:	Static ++Skype library
Summary(pl.UTF-8):	Statyczna biblioteka ++Skype
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static ++Skype library.

%description static -l pl.UTF-8
Statyczna biblioteka ++Skype.

%prep
%setup -q -n libskype
%patch0 -p1

%build
%{__make} -f Makefile.unx \
	CCP="%{__cxx}" \
	OPTFLAGS="%{rpmcxxflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -f Makefile.unx install  \
	INSTALL_DIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_includedir}/%{name},%{_libdir}}
mv $RPM_BUILD_ROOT{/h/*,%{_includedir}/%{name}}
mv $RPM_BUILD_ROOT{/lib/*,%{_libdir}}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc TODO
%attr(755,root,root) %{_libdir}/libppskype.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/libppskype

%files static
%defattr(644,root,root,755)
%{_libdir}/libppskype.a
