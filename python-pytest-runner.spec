%global modulename pytest-runner
%global _modulename pytest_runner

Name: python-%{modulename}
Version: 2.9
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

%package -n python3-%{modulename}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modulename}}
Requires:       python3-pytest
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-pytest

%description -n python3-%{modulename} %{_description}

Python 3 version.

%prep
%autosetup -n %{modulename}-%{version}

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
%{__python2} setup.py test
%{__python3} setup.py test

%files -n python2-%{modulename}
%doc README.rst
%license LICENSE
%{python2_sitelib}/ptr.py*
%{python2_sitelib}/%{_modulename}-%{version}-py%{python2_version}.egg-info/

%files -n python3-%{modulename}
%doc README.rst
%license LICENSE
%{python3_sitelib}/ptr.py
%{python3_sitelib}/%{_modulename}-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/__pycache__/ptr.*

%changelog
* Sat Aug 06 2016 Vadim Rutkovsky <vrutkovs@redhat.com> - 2.9-1
- Initial package
