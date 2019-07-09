%define pymajorver 3
%define pybasever 3.6
%define pylibdir %{python3_sitelib}

Name:		python36-stix2_patterns
Version:	1.1.0
Release:	1%{?dist}
Summary:	Validate STIX 2 Patterns

Group:		Development/Languages
License:	BSD License
URL:		https://pypi.org/project/stix2_patterns/
Source0:	fake-tgz.tgz
Source1:    stix2_patterns-%{version}-py2.py3-none-any.whl
Buildarch:  noarch

BuildRequires:  python36, python36-devel, python36-setuptools	
Requires:	    python36

%description
Validate STIX 2 Patterns

%prep
%setup -q -n fake-tgz

%build
#intentionally left blank

%install
unzip %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT/%{pylibdir}
mv stix2patterns $RPM_BUILD_ROOT/%{pylibdir}
mv stix2_patterns-%{version}.dist-info $RPM_BUILD_ROOT/%{pylibdir}
ln -s /%{pylibdir}/stix2patterns $RPM_BUILD_ROOT/%{pylibdir}/stix2_patterns

%files
%{pylibdir}/stix2patterns
%{pylibdir}/stix2_patterns
%{pylibdir}/stix2_patterns-%{version}.dist-info

%changelog
* Tue Jul 09 2019 Alexander Bruegmann <mail@abruegmann.eu> - 1.1.0-1
- update to 1.1.0 to fix dependency issues

* Wed Jul 18 2018 Andreas Muehlemann <andreas.muehlemann@switch.ch> - 0.6.0
- first version for python36
