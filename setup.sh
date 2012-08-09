#!/bin/bash

sudo apt-get -y install python-setuptools
sudo apt-get -y install python-pygame
easy_install PyYaml

tmp=/tmp/path.tmp
dest=./src/sprites/playerUp.txt
touch $tmp
for path in `find . -type f | sed "s#^.#$(pwd)#" | grep back* | grep -v .png`; do
	echo $path >> $tmp
done
mv $tmp $dest


tmp=/tmp/path.tmp
dest=./src/sprites/playerDown.txt
touch $tmp
for path in `find . -type f | sed "s#^.#$(pwd)#" | grep front*`; do
	echo $path >> $tmp
done
mv $tmp $dest

tmp=/tmp/path.tmp
dest=./src/sprites/playerLeft.txt
touch $tmp
for path in `find . -type f | sed "s#^.#$(pwd)#" | grep front*`; do
	echo $path >> $tmp
done
mv $tmp $dest

tmp=/tmp/path.tmp
dest=./src/sprites/playerRight.txt
touch $tmp
for path in `find . -type f | sed "s#^.#$(pwd)#" | grep front*`; do
	echo $path >> $tmp
done
mv $tmp $dest
