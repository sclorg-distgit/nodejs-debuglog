%{?scl:%scl_package nodejs-debuglog}
%{!?scl:%global pkg_name %{name}}

# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}



%global barename debuglog

Name:               %{?scl_prefix}nodejs-debuglog
Version:            1.0.1
Release:            5%{?dist}
Summary:            Backport of util.debuglog from node v0.11

Group:              Development/Libraries
License:            MIT
URL:                https://www.npmjs.org/package/debuglog
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz
BuildArch:          noarch
%if 0%{?fedora} >= 19
ExclusiveArch:      %{nodejs_arches} noarch
%else
ExclusiveArch:      %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:      nodejs010-runtime
%description
To facilitate using the `util.debuglog()` function that will be available
when node v0.12 is released now, this is a copy extracted from the source.

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/debuglog
cp -pr package.json debuglog.js \
    %{buildroot}%{nodejs_sitelib}/debuglog

%nodejs_symlink_deps

%files
%doc LICENSE README.md
%{nodejs_sitelib}/debuglog/

%changelog
* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.1-5
- rebuilt

* Tue Dec 01 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.1-4
- Enable scl macros

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jul 22 2014 Ralph Bean <rbean@redhat.com> - 1.0.1-1
- Initial packaging for Fedora.
