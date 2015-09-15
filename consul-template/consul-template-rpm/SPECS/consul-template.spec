Name:           consul-template
Version:        0.10.0
Release:        1%{?dist}
Summary:        Generic template rendering and notifications with Consul

Group:          System Environment/Daemons
License:        MPLv2.0
URL:            https://github.com/hashicorp/consul-template
Source0:        https://github.com/hashicorp/consul-template/releases/download/v%{version}/%{name}_%{version}_linux_amd64.tar.gz
Source1:        %{name}.service
Source2:        %{name}.hcl
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%if 0%{?fedora} >= 14 || 0%{?rhel} >= 7
BuildRequires:  systemd-units
Requires:       systemd
%endif
Requires:       consul
Requires(pre): shadow-utils

%description
Generic template rendering and notifications with Consul.

This project provides a convenient way to populate values from Consul into the filesystem using the consul-template daemon.

The daemon consul-template queries a Consul instance and updates any number of specified templates on the filesystem. As an added bonus, consul-template can optionally run arbitrary commands when the update process completes. See the Examples section for some scenarios where this functionality might prove useful.

%prep
%setup -q -c

%install
mkdir -p %{buildroot}/%{_bindir}
cp %{name}_%{version}_linux_amd64/consul-template %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_sysconfdir}/%{name}
cp %{SOURCE2} %{buildroot}/%{_sysconfdir}/%{name}/

%if 0%{?fedora} >= 14 || 0%{?rhel} >= 7
mkdir -p %{buildroot}/%{_unitdir}
cp %{SOURCE1} %{buildroot}/%{_unitdir}/

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%clean
rm -rf %{buildroot}
%endif

%files
%defattr(-,root,root,-)
%dir %attr(750, root, root) %{_sysconfdir}/%{name}
%attr(640, root, root) %{_sysconfdir}/%{name}/%{name}.hcl
%if 0%{?fedora} >= 14 || 0%{?rhel} >= 7
%{_unitdir}/%{name}.service
%endif
%attr(755, root, root) %{_bindir}/consul-template



%doc


%changelog
* Tue Sep 15 2015 Uchio Kondo <udzura@udzura.jp>
- Initial
