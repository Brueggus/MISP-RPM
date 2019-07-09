%define pymajorver 3
%define pybasever 3.6
%define pylibdir %{python3_sitelib}

Name:		python36-redis
Version:	3.2.1
Release:	1%{?dist}
Summary:	Python client for Redis key-value store

Group:		Development/Languages
License:	MIT License
URL:		https://pypi.org/project/redis/
Source0:	redis-%{version}.tar.gz
Buildarch:  noarch

BuildRequires:  python36, python36-devel, python36-setuptools	
Requires:	    python36

%description
Python client for Redis key-value store

%prep
%setup -q -n redis-%{version}

%build
#intentionally left blank

%install
python3 setup.py install --root=$RPM_BUILD_ROOT

%files
%{pylibdir}/redis
%{pylibdir}/redis-%{version}-py%{pybasever}.egg-info

%changelog
* Tue Jul 09 2019 Alexander Bruegmann <mail@abruegmann.eu> - 2.4.110
- bump to v3.2.1 to meet misp-modules' requirements

* Wed Jul 11 2018 Andreas Muehlemann <andreas.muehlemann@switch.ch> - 2.10.6
- first version for python36
