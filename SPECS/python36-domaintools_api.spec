%define pymajorver 3
%define pybasever 3.6
%define pylibdir %{python3_sitelib}

Name:		python36-domaintools_api
Version:	0.3.3
Release:	1%{?dist}
Summary:	DomainTools' Official Python API

Group:		Development/Languages
License:	MIT License
URL:		https://pypi.org/project/domaintools_api/
Source0:	domaintools_api-%{version}.tar.gz
Buildarch:  noarch

BuildRequires:  python36, python36-devel, python36-setuptools	
Requires:	    python36

%description
DomainTools' Official Python API

%prep
%setup -q -n domaintools_api-%{version}

%build
#intentionally left blank

%install
python3 setup.py install --root=$RPM_BUILD_ROOT

%files
%{_bindir}/domaintools
%{pylibdir}/domaintools
%{pylibdir}/domaintools_api-%{version}-py%{pybasever}.egg-info
%{pylibdir}/domaintools_async/*

%changelog
* Tue Jul 09 2019 Alexander Bruegmann <mail@abruegmann.eu> - 0.3.3-1
- update to 0.3.3 to fix dependency issues

* Wed Jul 11 2018 Andreas Muehlemann <andreas.muehlemann@switch.ch> - 0.2.2
- first version for python36
