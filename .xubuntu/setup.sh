#!/usr/bin/env bash

sudo groupadd -r autologin
sudo gpasswd -a $USER autologin

# To launch MPF after starting the X Server
mkdir -p $HOME/.config/autostart
ln -s $HOME/futurama/.xubuntu/mpf.desktop \
  $HOME/.config/autostart/mpf.desktop

# Prevents a serial error with some hardware
sudo usermod -a -G dialout $USER
# Probably prevents full minute delay when not
# connected to the internet (unconfirmed)
sudo sed -i -e 's/NM_ONLINE_TIMEOUT=60/NM_ONLINE_TIMEOUT=5/g' \
  /etc/systemd/system/network-online.target.wants/NetworkManager-wait-online.service
