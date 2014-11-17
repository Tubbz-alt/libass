Name:           libass
Version:        0.12.0
Release:        1
Summary:        Portable library for SSA/ASS subtitles rendering

Group:          System Environment/Libraries
License:        ISC
URL:            https://github.com/libass
Source0:        %{name}-%{version}.tar.xz

BuildRequires:  fontconfig-devel
BuildRequires:  fribidi-devel
BuildRequires:  libpng-devel

%description
Libass is a portable library for SSA/ASS subtitles rendering.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%check
make check


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc Changelog COPYING
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libass.pc
