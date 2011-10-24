Summary:	Fixed-point AAC decoder library
Summary(pl.UTF-8):	Biblioteka stałoprzecinkowego dekodera AAC
Name:		opencore-aacdec
Version:	1.0.0
%define	subver	svn14
Release:	0.%{subver}.1
License:	Apache v2.0
Group:		Libraries
# svn checkout http://opencore-aacdec.googlecode.com/svn/trunk/ opencore-aacdec
Source0:	%{name}-%{subver}.tar.xz
# Source0-md5:	5993bcd98f7dfd13fa0422a7a7432425
Patch0:		%{name}-fix.patch
URL:		http://code.google.com/p/opencore-aacdec/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.7
BuildRequires:	curl-devel >= 7.16
BuildRequires:	libtool
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
opencore-aacdec is a library, that implements fixed-point AAC decoder,
optimized for ARM processors. This library is based on PacketVideo
implementation. opencore-aacdec can decode: AAC, AAC+SBR and
AAC+SBR+PS. It's able to decode ADTS (and maybe ADIF) streams.

%description -l pl.UTF-8
opencore-aacdec to biblioteka implementująca stałoprzecinkowy dekoder
AAC, zoptymalizowany dla procesorów ARM. Jest oparta na implementacji
PacketVideo. Dekoduje AAC, AAC+SBR i AAC+SBR+PS; potrafi zdekodować
strumienie ADTS i być może ADIF.

%package devel
Summary:	Header files for opencore-aacdec library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki opencore-aacdec
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for opencore-aacdec library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki opencore-aacdec.

%package static
Summary:	Static opencore-aacdec library
Summary(pl.UTF-8):	Statyczna biblioteka opencore-aacdec
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static opencore-aacdec library.

%description static -l pl.UTF-8
Statyczna biblioteka opencore-aacdec.

%package netplayer
Summary:	Network-enabled AAC player using opencore-aacdec library
Summary(pl.UTF-8):	Sieciowy odtwarzacz AAC wykorzystujący bibliotekę opencore-aacdec
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Requires:	curl-libs >= 7.16

%description netplayer
Network-enabled AAC player using opencore-aacdec library.

%description netplayer -l pl.UTF-8
Sieciowy odtwarzacz AAC wykorzystujący bibliotekę opencore-aacdec.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/opencore-aacdec
%attr(755,root,root) %{_libdir}/libaacdec.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libaacdec.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaacdec.so
%{_libdir}/libaacdec.la
%{_includedir}/aacdec

%files static
%defattr(644,root,root,755)
%{_libdir}/libaacdec.a

%files netplayer
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/aacNetPlayer
