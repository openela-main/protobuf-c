Name:           protobuf-c
Version:        1.3.3
Release:        13%{?dist}
Summary:        C bindings for Google's Protocol Buffers

License:        BSD
URL:            https://github.com/protobuf-c/protobuf-c
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Patch0:         %{url}/commit/ec3d900001a13ccdaa8aef996b34c61159c76217.patch

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(protobuf)

%description
Protocol Buffers are a way of encoding structured data in an efficient yet
extensible format. This package provides a code generator and run-time
libraries to use Protocol Buffers from pure C (not C++).

It uses a modified version of protoc called protoc-c.

%package compiler
Summary:        Protocol Buffers C compiler
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description compiler
This package contains a modified version of the Protocol Buffers
compiler for the C programming language called protoc-c.

%package devel
Summary:        Protocol Buffers C headers and libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-compiler%{?_isa} = %{version}-%{release}

%description devel
This package contains protobuf-c headers and libraries.

%prep
%setup -q
%patch -P 0 -p 1

%build
%configure --disable-static
%make_build

%check
make check

%install
%make_install
rm -vf $RPM_BUILD_ROOT/%{_libdir}/libprotobuf-c.la

%ldconfig_scriptlets

%files
%{_libdir}/libprotobuf-c.so.*
%doc TODO LICENSE ChangeLog

%files compiler
%{_bindir}/protoc-c
%{_bindir}/protoc-gen-c

%files devel
%dir %{_includedir}/google
%{_includedir}/protobuf-c/
%{_includedir}/google/protobuf-c/
%{_libdir}/libprotobuf-c.so
%{_libdir}/pkgconfig/libprotobuf-c.pc

%changelog
* Fri Apr 14 2023 Adrian Reber <areber@redhat.com> - 1.3.3-13
- Applied patch for for CVE-2022-48468 (#2186677)

* Thu Feb 24 2022 Adrian Reber <areber@redhat.com> - 1.3.3-12
- Adapt tests to protobuf-c 1.3.3

* Wed Feb 23 2022 Adrian Reber <areber@redhat.com> - 1.3.3-11
- Added gating tests

* Wed Feb 23 2022 Adrian Reber <areber@redhat.com> - 1.3.3-10
- Rebuilt for errata

* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 1.3.3-9
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 1.3.3-8
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 1.3.3-7
- Rebuilt for removed libstdc++ symbol (#1937698)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 12 14:04:27 CET 2021 Adrian Reber <adrian@lisas.de> - 1.3.3-5
- Rebuilt for protobuf 3.14

* Wed Sep 23 2020 Adrian Reber <adrian@lisas.de> - 1.3.3-4
- Rebuilt for protobuf 3.13

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 14 2020 Adrian Reber <adrian@lisas.de> - 1.3.3-2
- Rebuilt for protobuf 3.12

* Mon Mar 30 2020 Adrian Reber <adrian@lisas.de> - 1.3.3-1
- Update to 1.3.3
- Removed call to autoreconf

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 19 2019 Orion Poplawski <orion@nwra.com> - 1.3.2-1
- Update to 1.3.2

* Thu Dec 19 2019 Orion Poplawski <orion@nwra.com> - 1.3.1-4
- Rebuild for protobuf 3.11

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 22 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.1-1
- Update to 1.3.1

* Wed Nov 21 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.0-6
- Rebuild for protobuf 3.6

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.0-3
- Switch to %%ldconfig_scriptlets

* Wed Nov 29 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.3.0-2
- Rebuild for protobuf 3.5

* Tue Nov 14 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3.0-1
- Update to 1.3.0

* Mon Nov 13 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.1-8
- Rebuild for protobuf 3.4

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 13 2017 Orion Poplawski <orion@cora.nwra.com> - 1.2.1-5
- Rebuild for protobuf 3.3

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Orion Poplawski <orion@cora.nwra.com> - 1.2.1-3
- Rebuild for protobuf 3.2.0

* Sat Nov 19 2016 Orion Poplawski <orion@cora.nwra.com> - 1.2.1-2
- Rebuild for protobuf 3.1.0

* Sun Mar 27 2016 Jan Vcelak <jvcelak@fedoraproject.org> 1.2.1-1
- New upstream release:
  + fix: negative value packing
  + fix: eliminate undefined behavior in zigzag functions
  + fix: generate code that uses universal zero initializer for oneof unions

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 25 2015 Nikos Mavrogiannopoulos <nmav@redhat.com> - 1.1.1-3
- Added protobuf-c-compiler subpackage to reduce runtime

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 23 2015 Nikos Mavrogiannopoulos <nmav@redhat.com> - 1.1.1-1
- new upstream release (#1142988)

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 1.0.1-3
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Aug 06 2014 Nikos Mavrogiannopoulos <nmav@redhat.com> - 1.0.1-1
- new upstream release

* Mon Aug 04 2014 Nikos Mavrogiannopoulos <nmav@redhat.com> - 1.0.0-1
- new upstream release (#1126116)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 11 2013 David Robinson <zxvdr.au@gmail.com> - 0.15-7
- rebuilt for protobuf-2.5.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jun 12 2011 David Robinson <zxvdr.au@gmail.com> - 0.15-3
- rebuilt for protobuf-2.4.1

* Sun Apr 24 2011 David Robinson <zxvdr.au@gmail.com> - 0.15-2
- Spec file cleanup

* Wed Apr 20 2011 David Robinson <zxvdr.au@gmail.com> - 0.15-1
- New upstream release
- Spec file cleanup

* Mon Jan 17 2011 Bobby Powers <bobby@laptop.org> - 0.14-1
- New upstream release
- Removed -devel dependency on protobuf-devel
- Small specfile cleanups

* Wed May 19 2010 David Robinson <zxvdr.au@gmail.com> - 0.13-2
- Spec file cleanup

* Wed May 19 2010 David Robinson <zxvdr.au@gmail.com> - 0.13-1
- Initial packaging
