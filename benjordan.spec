Summary:	Ben Jordan Case 1: In Search of the Skunk-Ape - an adventure game
Name:		benjordan
Version:	1.0.0
Release:	1
Source0:	http://www.grundislavgames.com/games/bj1deluxe.zip
License:	distributable
Group:		Games/Adventure
Url:		https://www.grundislavgames.com/benjordan/case1.php
BuildArch:	noarch
Requires:	ags
BuildRequires:	icoutils

%description
Ben's first case finds him in the Florida Everglades looking for something
known as "The Skunk-Ape" which is said to be a local variation on Bigfoot.

Several park rangers have been murdered, and so Ben is called in to
investigate the possibility that the Skunk-Ape is involved.

%prep
%setup -qcn %{name}

%build
wrestool -x --all BJ1Deluxe.exe >%{name}.ico
icotool -x %{name}.ico

%install
mkdir -p %{buildroot}%{_prefix}/games/%{name} \
	%{buildroot}%{_bindir} \
	%{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/icons/hicolor/48x48/apps
cp -a acsetup.cfg BJ1Deluxe.exe *.vox %{buildroot}%{_prefix}/games/%{name}
cp -a %{name}*.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
cat >%{buildroot}%{_bindir}/%{name} <<'EOF'
#!/bin/sh
cd %{_prefix}/games/%{name}
exec %{_bindir}/ags BJ1Deluxe.exe
EOF
cat >%{buildroot}%{_datadir}/applications/%{name}.desktop <<'EOF'
[Desktop Entry]
Type=Application
Name=Ben Jordan Case 1: In Search of the Skunk-Ape
GenericName=Adventure Game
Exec=%{name}
Icon=%{name}
Categories=Game;AdventureGame;
EOF
chmod +x %{buildroot}%{_bindir}/%{name} %{buildroot}%{_datadir}/applications/*.desktop

%files
%doc Handbook
%{_bindir}/%{name}
%{_prefix}/games/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/applications/%{name}.desktop
