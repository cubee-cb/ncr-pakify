#!/bin/bash

# for linux users; if your save is in another location, please edit this
CUSTOMPATH="$HOME/.config/cubee/ninjacat/customPacks/vanillaDevel/"

export OGMO_BUILD_SCRIPT=1
./pakify.py "$CUSTOMPATH" basepak outset sequel finale bouldo testpak
