Summary:	photo uploader
Name:		photo-uploader
Version:	0.9
Release:	2
License:	GPL v2+
Group:		Applications
Source0:	http://dl.cihar.com/photo-uploader/latest/%{name}-%{version}.tar.bz2
# Source0-md5:	f62d904f6b81ecd3a30dbc7e8465743a
Patch0:		%{name}-ext.patch
URL:		http://cihar.com/software/photo-uploader/
BuildRequires:	rpm-pythonprov
Requires:	python-modules
Requires:	python-pycurl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple Python script to upload photos to minilab and other services.

%prep
%setup -q
%patch0 -p1

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
		--root=$RPM_BUILD_ROOT \
		--optimize=2

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/photo-upload
%dir %{py_sitescriptdir}/phoupl
%{py_sitescriptdir}/phoupl/*.py[co]
%dir %{py_sitescriptdir}/phoupl/services
%{py_sitescriptdir}/phoupl/services/*.py[co]
%{py_sitescriptdir}/photo_uploader-*.egg-info
%{_mandir}/man1/photo-upload.1*
