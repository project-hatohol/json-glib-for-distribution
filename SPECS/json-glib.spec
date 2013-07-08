Name: json-glib
Version: 0.12.6
# PH means Project Hatohol's build
Release: 1PH
License: LGPLv2
Group: Development/Libraries
Summary: JSON-GLib is a library providing serialization and deserialization support for the JavaScript Object Notation (JSON).
URL: http://wiki.gnome.org/JsonGlib/
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Source0: %{name}-%{version}.tar.bz2

BuildRequires: glib2-devel >= 2.16

%description
JSON-GLib is a C library based on GLib and released under the terms of
the GNU Lesser General Public License version 2.1. It provides a parser
and a generator GObject classes and various wrappers for the complex data
types employed by JSON, such as arrays and objects.

JSON-GLib uses GLib native data types and the generic value container GValue
for ease of development. It also provides integration with the GObject classes
for direct serialization into, and deserialization from, JSON data streams.

%package devel
Summary: Header files for the json-glib library
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: glib2-devel >= 2.16

%description devel
Header files for the json-glib library.

%prep
%setup -q

%build
%configure

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.a

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README COPYING NEWS AUTHORS
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gtk-doc/*

%changelog
* Mon Jul 08 2013 Kazuhiro Yamato <kazuhiro.yamato@miraclelinux.com>
- Inital RPM spec. file by Project Hatohol.
