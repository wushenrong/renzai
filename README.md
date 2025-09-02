# RenZai

Basic and generic screens, styles, and transforms for others to make
[Ren'Py](https://www.renpy.org/) feel like Puyo Puyo's Manzai.

This project is not affiliated with SEGA or Ren'Py.

## Rational

Although there are other programs to create Manzai, it is much more practical to
use Ren'Py as it is more intuitive for people to use, has a good animation
system using transforms, and most importantly Ren'Py is a very good dialog
system. So in theory, it should be possible to make Ren'Py feel like Manzai and
this project is the proof. This project does not intend to compete or replace
those programs, they have their own valid purpose of existing and we have our
own. Do not harass others on which project to use and allow people the freedom
to choose, that is the main principle of open source.

If you do use this project and like the work that is being done,
[please contribute to the project](#contributing). This project is not possible
without the help of volunteers, thank you.

## Usage

There are multiple ways to use the screens, styles, and transforms.

It is recommended to copy the scripts as is and have custom styles to inherit
from the existing styles in the scripts. You can copy the individual
configuration variables, screens, styles, and transforms into different parts of
your project. However, this method is less flexible, less maintainable, and
harder to ensure license compliance between external scripts.

Something important to know is that it does not matter how you organize the
scripts as long as you are able to use them, and that you are complying with the
[project's license](#license).

It is also recommended to have Ren'Py run your game's `gui.rpy` and `screen.rpy`
first so all the inherited styles in the script are applied correctly.

Each script have their own comments and usage sections on how to use the
screens, styles, and transforms. You should remove the usage sections for a
smaller distribution bundle.

## Contributing

Have some problems with styles or animations not showing in Ren'Py? Created some
styles, animations or improvements that others can use as a template? Great!
Create an issue at <https://github.com/wushenrong/RenZai/issues>.

Your contribution is greatly appreciated, but first make sure they follow the
guidelines:

- Issues or contribution must be specific to this project.
- Contribution must not contain or reference external content.
- Contribution must have a working example and demonstration.

Failure to follow these guidelines will result in a warning and repeated
offenses will result in a ban from contribution.

## License

RenZai is licensed under the MIT License, the license that is covered by most
parts of Ren'Py. For compliance, follow
[Ren'Py's advice](https://www.renpy.org/doc/html/license.html) of adding a copy
of their license in your game, and adding another reference to this project in
the README, about page, and if applicable App Store description of your project.
