Summary:	RAID management tool for Mylex DAC960/DAC1164 controllers
Summary(pl):	Narzêdzie do zarz±dzania macierzami RAID na kontrolerach Mylex DAC960/DAC1164
Name:		varmon
Version:	1.0.2
Release:	2
License:	GPL
Group:		Applications/System
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/varmon/%{name}-%{version}.tar.gz
URL:		http://varmon.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
VARMon is a GNU licensed RAID manipulation / management tool for Mylex
DAC960/DAC1164 controller family.

%description -l pl
VARMon to narzêdzie do zarz±dzania macierzami RAID na kontrolerach
Mylex z rodziny DAC960/DAC1164.

%prep
%setup -q

%build
%{__cc} %{rpmcflags} %{rpmldflags} -o varmon varmon.c -Wall -lncurses

%install
rm -rf $RPM_BUILD_ROOT
install -D varmon $RPM_BUILD_ROOT%{_sbindir}/varmon

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/varmon
