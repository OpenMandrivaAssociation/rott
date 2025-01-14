%define Werror_cflags	%nil

Name:			rott
Version:		1.1.2
Release:		2
Summary:		Rise of the Triad
Group:			Games/Arcade
License:		GPL
URL:			https://icculus.org/rott/
Source0:		http://icculus.org/rott/releases/%{name}-%{version}.tar.gz
Source1:		%{name}-shareware.sh
Source2:		%{name}-registered.sh
Source3:		%{name}.autodlrc
Source4:		%{name}-shareware.desktop
Source5:		%{name}-registered.desktop
Source6:		%{name}.png
# Note: this gets applied during build, not during prep!
Source7:		%{name}-1.0-registered.patch
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:  pkgconfig(sdl)
BuildRequires:  SDL_mixer-devel

%description
This is the icculus.org Linux port of Apogee's classic 3d shooter
Rise of the Triad, which has been released under the GPL by Apogee.
This version is enhanced with the 'high' resolution rendering from
the winrott port.


%package shareware
Summary:	Rise of the Triad shareware version
Group:		Games/Arcade

%description shareware
This is the icculus.org Linux port of Apogee's classic 3d shooter
Rise of the Triad (RotT), which has been released under the GPL by
Apogee. This version is enhanced with the 'high' resolution
rendering from the winrott port.

This package contains the engine for the shareware version of RotT.
In order to play the shareware version, you will need the shareware
datafiles. Which can be freely downloaded from Apogee/3DRealms, but
cannot be distributed as a package. When you start RotT for the
first time it will offer to download the datafiles for you.

%package registered
Summary:	Rise of the Triad registered version
Group:		Games/Arcade
Requires:	zenity

%description registered
This is the icculus.org Linux port of Apogee's classic 3d shooter
Rise of the Triad (RotT), which has been released under the GPL by
Apogee. This version is enhanced with the 'high' resolution
rendering from the winrott port.

This package contains the engine for the registered version of RotT.
If you own the registered version, this allows you to play the
registered version under Linux. Place the registered RotT datafiles
in a dir and start rott-registered from this dir.

%prep
%setup -q %{name}-%{version}

%build
pushd rott
	%__make %{?jobs:-j%{jobs}} \
		EXTRACFLAGS="$RPM_OPT_FLAGS -Wno-unused -Wno-pointer-sign -fno-strict-aliasing"
	%__mv %{name} \
		%{name}-shareware.bin

	
	%__make clean
	%__make SHAREWARE=0 \
		EXTRACFLAGS="$RPM_OPT_FLAGS -Wno-unused -Wno-pointer-sign -fno-strict-aliasing"
	%__mv %{name} \
		%{name}-registered.bin
popd

%install
# no make install target, DIY
%__install -dm 755 %{buildroot}%{_gamesbindir}
%__install -m 755 %{name}/%{name}-* \
	%{buildroot}%{_gamesbindir}
%__install -m 755 %{SOURCE1} \
	%{buildroot}%{_gamesbindir}/%{name}-shareware
%__install -m 755 %{SOURCE2} \
	%{buildroot}%{_gamesbindir}/%{name}-registered

# the autodownloader-stuff
%__install -dm 755 %{buildroot}%{_gamesdatadir}/%{name}
%__install -m 644 %{SOURCE3} \
	%{buildroot}%{_gamesdatadir}/%{name}

# desktop file and icon stuff
%__install -dm 755 %{buildroot}%{_datadir}/pixmaps
%__install -m 644 %{SOURCE6} \
	%{buildroot}%{_datadir}/pixmaps

%__install -dm 755 %{buildroot}%{_datadir}/applications
%__install -m 644 %{SOURCE4} \
	%{buildroot}%{_datadir}/applications


%__install -m 644 %{SOURCE5} \
	%{buildroot}%{_datadir}/applications

# man-page
%__install -dm 755 %{buildroot}%{_mandir}/man6
%__install -m 644 doc/%{name}.6 \
	%{buildroot}%{_mandir}/man6/%{name}-shareware.6
%__install -m 644 doc/%{name}.6 \
	%{buildroot}%{_mandir}/man6/%{name}-registered.6

%clean
[ -d "%{buildroot}" -a "%{buildroot}" != "" ] && %__rm -rf "%{buildroot}"

%files shareware
%defattr(-,root,root,-)
%doc README doc/*.txt
%{_gamesbindir}/%{name}-shareware*
%dir %{_gamesdatadir}/%{name}
%{_gamesdatadir}/%{name}/*
%{_mandir}/man6/%{name}-shareware.6*
%{_datadir}/applications/%{name}-shareware.desktop


%files registered
%defattr(-,root,root,-)
%doc README doc/*.txt
%{_gamesbindir}/%{name}-registered*
%dir %{_gamesdatadir}/%{name}

%{_mandir}/man6/%{name}-registered.6*
%{_datadir}/applications/%{name}-registered.desktop
%{_datadir}/pixmaps/%{name}.png


%changelog
* Wed Oct 24 2012 Zombie Ryushu <ryushu@mandriva.org> 1.1.2-1mdv2012.0
+ Revision: 819674
- remove dated patch
- remove dated patch
- Upgrade to 1.1.2

* Wed Mar 31 2010 Zombie Ryushu <ryushu@mandriva.org> 1.1.1-1mdv2010.1
+ Revision: 530170
- Fix up SPEC file
- Fix Desktop Shortcuts
- import rott


* Wed Nov 11 2009 Toni Graffy <toni@links2linux.de> - 1.1.1-0.pm.1
- update to 1.1.1
* Thu Sep 04 2008 Toni Graffy <toni@links2linux.de> - 1.1-0.pm.1
- update to 1.1
* Sun Jun 22 2008 Toni Graffy <toni@links2linux.de> - 1.0-0.pm.2
- corrected Group
* Fri Nov 23 2007 Toni Graffy <toni@links2linux.de> - 1.0-0.pm.1
- initial build for packman 1.0
- spec file, patches, scipts  adapted from fedora package
  from Hans de Goede <j.w.r.degoede@hhs.nl>
