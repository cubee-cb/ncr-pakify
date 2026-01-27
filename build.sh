#!/bin/bash

export OGMO_BUILD_SCRIPT=1

# for linux users; edit these to point to your install's levels folder
GAMEPATH="/mnt/big-chungus/projects/monogame/Ninja_Cat_Remewstered/Ninja Cat Desktop 383"
./pakify.py "$GAMEPATH/Content/levels/" basepak outset sequel finale
./pakify.py "$GAMEPATH/bin/Debug/net8.0/Content/levels/" basepak outset sequel finale testpak
