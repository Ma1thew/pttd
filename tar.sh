#!/bin/sh

NAME=pttd
VERSION=0

if [ ! -d .git ]; then
    echo "This dosen't look like a git repository; are you sure you're in the right place?"
fi

if [ -d "$NAME-$VERSION" ]; then
    rm -rf "$NAME-$VERSION"
fi

if [ -f pttd.tar.gz ]; then
    rm pttd.tar.gz
fi

if [ -d 'usr/share/pttd/keyboard/__pycache__' ]; then
    rm -rf 'usr/share/pttd/keyboard/__pycache__'
fi

mkdir "$NAME-$VERSION"

cp -r 'usr' "$NAME-$VERSION/usr"
mkdir "$NAME-$VERSION/usr/bin"
mkdir -p "$NAME-$VERSION/usr/share/licenses/pttd/"
cp 'LICENSE' "$NAME-$VERSION/usr/share/licenses/pttd/LICENSE"
cp 'pttd' 'ptt-client' "$NAME-$VERSION/usr/bin"
find "$NAME-$VERSION" -type f -exec chmod 644 {}
chmod 755 "$NAME-$VERSION/usr/bin/pttd"
chmod 755 "$NAME-$VERSION/usr/bin/ptt-client"
tar -zcvf pttd.tar.gz "$NAME-$VERSION"

rm -rf "$NAME-$VERSION"
