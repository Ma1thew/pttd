Name:           pttd
Version:        0
Release:        1%{?dist}
Summary:        A global push-to-talk daemon for Wayland

License:        WTFPL
URL:            https://github.com/Ma1thew/pttd
Source0:        pttd.tar.gz

Requires:       python3
Requires:       python3-gobject
Requires:       python3-dbus
Requires:       python3-pulsectl

BuildArch:      noarch

%description
A global push-to-talk daemon for Wayland

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p  %{buildroot}

cp -a * %{buildroot}

%files
%defattr(-,root,root,-)
%license LICENSE
/usr/bin/pttd
/usr/bin/ptt-client
/usr/share/dbus-1/system.d/com.github.ma1thew.pttd.conf
/usr/lib/systemd/system/pttd.service
/usr/lib/systemd/user/ptt-client.service
/usr/share/pttd/keyboard/LICENSE
/usr/share/pttd/keyboard/__init__.py
/usr/share/pttd/keyboard/__main__.py
/usr/share/pttd/keyboard/_canonical_names.py
/usr/share/pttd/keyboard/_generic.py
/usr/share/pttd/keyboard/_keyboard_event.py
/usr/share/pttd/keyboard/_keyboard_tests.py
/usr/share/pttd/keyboard/_nixcommon.py
/usr/share/pttd/keyboard/_nixkeyboard.py
