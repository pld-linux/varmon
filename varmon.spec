Summary:	RAID management tool for Mylex DAC960/DAC1164 controllers
Summary(pl.UTF-8):   Narzędzie do zarządzania macierzami RAID na kontrolerach Mylex DAC960/DAC1164
Name:		varmon
Version:	1.2.0
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/varmon/%{name}-%{version}.tar.gz
# Source0-md5:	fd251b64ad4976ef8573f0d2a20a02f9
URL:		http://varmon.sourceforge.net/
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
VARMon is a GNU licensed RAID manipulation / management tool for Mylex
DAC960/DAC1164 controller family.

%description -l pl.UTF-8
VARMon to narzędzie do zarządzania i manipulacji macierzami RAID na
kontrolerach Mylex z rodziny DAC960/DAC1164.

%prep
%setup -q

%build
%{__cc} %{rpmcflags} %{rpmldflags} -o varmon varmon.c -Wall -lncurses -I/usr/include/ncurses

%install
rm -rf $RPM_BUILD_ROOT
install -D varmon $RPM_BUILD_ROOT%{_sbindir}/varmon

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README *.pdf
%attr(755,root,root) %{_sbindir}/varmon
