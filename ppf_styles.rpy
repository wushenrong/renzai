# SPDX-FileCopyrightText: 2025 Samuel Wu
#
# SPDX-License-Identifier: MIT-0

## GUI Configuration Variables #################################################
##
## These variables control the look, size, how namebox are displayed.

## The placement of the speaking character's name, relative to the textbox.
## These can be a whole number of pixels from the left or top, or 0.5 to center.
## This corresponds to the gui.name_xpos variable.
define gui.ppf_name_xpos = 400

## The color of the dialogue text in nvl mode, use what_color to override this
## variable.
define gui.ppf_nvl_text_color = "#ffa"

## The horizontal alignment of the dialogue text in nvl mode. This can be 0.0
## for left-aligned, 0.5 for centered, and 1.0 for right-aligned.
## This corresponds to the gui.nvl_text_xalign variable.
define gui.ppf_nvl_text_xalign = 0.5


## Styles ######################################################################


style ppf_window is window
style ppf_namebox is namebox

# TODO: Figure out a way to replace the background of the nvl window
style ppf_nvl_dialogue is nvl_dialogue

style ppf_window:
    # TODO: Figure out how to have a smooth transition of the textbox with a solid background
    background Solid("#000")

style ppf_namebox:
    xpos gui.ppf_name_xpos

    background Frame("gui/frame.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)

style ppf_nvl_dialogue:
    color gui.ppf_nvl_text_color
    xalign gui.ppf_nvl_text_xalign
    textalign gui.ppf_nvl_text_xalign
    layout ("subtitle" if gui.ppf_nvl_text_xalign else "tex")

    outlines [ (4, "#000", 0, 0) ]


## Usage #######################################################################


# Define your characters and apply styles to the characters as you would
define e = Character("Eileen", window_style="ppf_window", namebox_style="ppf_namebox")
define e_nvl = Character(None, kind=nvl, what_style="ppf_nvl_dialogue")

# Use the styles as normal
label start:

    ... # Dialog in nvl and adv mode

    return
