# pttd

## Overview

A basic daemon/client pair I hacked together to allow global push-to-talk under Wayland. The daemon runs as root and reports the state of a single button; the client communicates with the daemon over DBus and mutes/unmutes the default microphone via PulseAudio. Hopefully this can eventually be superseded by a proper, permission-managed system in Wayland or org.freedesktop.Portal.

This is my first time interacting with GLib, DBus, and PulseAudio, so improvements are welcome.


## Installation

For Fedora, there is a provided spec file for building an RPM. To build it, first run `rpmdev-setuptree` from the `rpmdevtools` package. Then run the provided `tar.sh` script to generate a source tar. Copy this to `~/rpmbuild/SOURCES/pttd.tar.gz`, and copy `pttd.spec` to `~/rpmbuild/SPECS/pttd.spec`. Finally, change directory to `~/rpmbuild` and run `rpmbuild -ba SPECS/pttd.spec` from the `rpm-build` package. The output RPM is in `~/rpmbuild/RPMS/noarch`.

## Setup

Just start and enable `pttd.service` system-wide and start and enable `ptt-client.service` in `--user` mode. Configure your voice chat software to always listen to the microphone (or, in the case of Discord, choose a very low voice activation threshold).

## Missing Functionality

At present, pttd is uses a fixed key (alt) and fixed list of known voice-chat software (Discord) for which sounds are played, and there is no support for external configuration. There is also no way to temporarily disable PTT outside of stopping `ptt-client`. To change the key, edit `pttd`.

## License

Code in `usr/share/pttd/keyboard` is under the MIT License, originally from https://github.com/boppreh/keyboard, and is provided here for easy packaging. `usr/share/pttd/{,de}activate.wav` are from `https://www.reddit.com/r/discordapp/comments/4ytdf0/where_are_sound_files_stored/`. All other content is under the WTFPL (see `LICENSE`).
