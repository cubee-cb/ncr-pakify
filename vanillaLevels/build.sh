#!/bin/bash

# for linux users; if your save is in another location, please edit this
CUSTOMPATH="$HOME/.config/cubee/ninjacat/customPacks"

export OGMO_BUILD_SCRIPT=1
./pakify.py "$CUSTOMPATH/vanillaDevel/" basepak outset sequel
./pakify.py "$CUSTOMPATH/vanillaFuture/" finale bouldo testpak
