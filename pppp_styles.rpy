style pppp_namebox is bubble_namebox
style pppp_who is bubble_who
style pppp_what is bubble_what

style pppp_namebox:
    xalign 0.0
    xanchor 0.5
    yalign 0.5

style pppp_who:
    color "#fff"
    xalign 0.5
    textalign 0.5

style pppp_what:
    xalign 0.3

define e = Character("Eileen", kind=bubble, namebox_style="pppp_namebox")
define e_and_l = Character("Eileen & Lucy", kind=bubble, namebox_style="pppp_namebox", what_style="pppp_what")
