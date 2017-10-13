%global modulename pytest-runner
%global _modulename pytest_runner

Name: python-%{modulename}
Version: 2.12.1
Release: 1%{?dist}
Summary: Invoke py.test as distutils command with dependency resolution

License: MIT
URL: https://pypi.python.org/pypi/%{modulename}
# setuptools-scm requires a pypi tarball and doesn't like github tarball
Source0: https://files.pythonhosted.org/packages/source/p/%{modulename}/%{modulename}-%{version}.tar.gz

BuildArch: noarch

%global _description \
Setup scripts can use pytest-runner to add setup.py test support for pytest runner.

%description %{_description}

# Python 2 pytest is too old on EL7
%if 0%{?fedora} || 0%{?rhel} > 7
%package -n python2-%{modulename}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modulename}}
Requires:       python2-pytest
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-setuptools_scm
BuildRequires:  python2-pytest

%description -n python2-%{modulename} %{_description}

Python 2 version.
%endif

%package -n python%{python3_pkgversion}-%{modulename}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{modulename}}
Requires:       python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-setuptools_scm
BuildRequires:  python%{python3_pkgversion}-pytest

%description -n python%{python3_pkgversion}-%{modulename} %{_description}

Python %{python3_version} version.

%prep
%autosetup -n %{modulename}-%{version}

%build
# Python 2 pytest is too old on EL7
%if 0%{?fedora} || 0%{?rhel} > 7
%py2_build
%endif
%py3_build

%install
%if 0%{?fedora} || 0%{?rhel} > 7
%py2_install
%endif
%py3_install

%check
%if 0%{?fedora} || 0%{?rhel} > 7
%{__python2} setup.py test
%endif
%{__python3} setup.py test

%if 0%{?fedora} || 0%{?rhel} > 7
%files -n python2-%{modulename}
%doc README.rst
%license LICENSE
%{python2_sitelib}/ptr.py*
%{python2_sitelib}/%{_modulename}-%{version}-py%{python2_version}.egg-info/
%endif

%files -n python%{python3_pkgversion}-%{modulename}
%doc README.rst
%license LICENSE
%{python3_sitelib}/ptr.py
%{python3_sitelib}/%{_modulename}-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/__pycache__/ptr.*

%changelog
* Fri Oct 13 2017 Vadim Rutkovsky <vrutkovs@redhat.com> - 2.12.1-1
-  Update to 2.12.1 (#1487972)

* Fri Sep 29 2017 Troy Dawson <tdawson@redhat.com> - 2.9-6
- Cleanup spec file conditionals

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 9 2017 Orion Poplawski <orion@cora.nwra.com> - 2.9-4
- Build python 3 version for EPEL

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 13 2016 Stratakis Charalampos <cstratak@redhat.com> - 2.9-2
- Rebuild for Python 3.6

* Sat Aug 06 2016 Vadim Rutkovsky <vrutkovs@redhat.com> - 2.9-1
- Initial package
