# SPDX-FileCopyrightText: 2025 Samuel Wu
#
# SPDX-License-Identifier: MIT-0

## Nameplate Configuration Variables ###########################################
##
## These variables control the look, size, how nameplates are displayed.

## The width, height, and borders of the nameplate containing the character's
## name, or None to automatically size it.
define gui.nameplate_width = None
define gui.nameplate_height = None

## The borders of the nameplate containing the character's name, in left, top,
## right, bottom order.
define gui.nameplate_borders = Borders(5, 5, 5, 5)

## If True, the background of the nameplate will be tiled, if False, the
## background of the nameplate will be scaled.
define gui.nameplate_tile = False

## The horizontal alignment of the character's name. This can be 0.0 for left-
## aligned, 0.5 for centered, and 1.0 for right-aligned.
define gui.nameplate_text_xalign = 0.0

## The size of the text used by the nameplate.
define gui.nameplate_text_size = 24

## The boldness of the text used by the nameplate.
define gui.nameplate_text_bold = True


## Nameplate screen ############################################################


screen nameplate(who, transition=None, plate_style="nameplate", name_style="nameplate_who"):

    frame:
        style plate_style
        at transition
        text who style name_style

style nameplate is frame
style nameplate_who is default

style nameplate:
    xsize gui.nameplate_width
    ysize gui.nameplate_height

style nameplate_who:
    properties gui.text_properties("nameplate")

    yalign 0.5
    outlines [ (4, "#000000", 0, 0) ]


## Transformations #############################################################

## You should have a yalign that is between 0.0 for the top of the screen and
## 1.0 for the bottom of the screen.
transform slide_in_left:
    yalign 0.85

    # Ran when using the `show screen` statement
    on show:
        xpos -1.0
        linear 0.5 xalign 0.1

    # Ran when using the `hide screen` statement
    on hide:
        linear 0.5 xpos -1.0

transform slide_in_right:
    yalign 0.85

    on show:
        xpos 2.0
        linear 0.5 xalign 0.9

    on hide:
        linear 0.5 xpos 2.0


## Usage #######################################################################


... # Define your characters.


label start:
    # To show a nameplate, use the `show screen` statement and provide a name
    # to the nameplate to show. It is important to include the `as` clause to
    # hide the nameplate and to show additional nameplates.
    #
    # You should pass an transformation to properly animate and align the
    # nameplates. Additional style names can be passed in to change the style of
    # the nameplate and the style of the name's text.
    show screen nameplate("Eileen", slide_in_left) as e_np
    show screen nameplate("Lucy", slide_in_right) as l_np

    ... # Some dialog later.

    # Hide the nameplates.
    hide screen e_np
    hide screen l_np

    return
