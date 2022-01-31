# MIT License
# 
# Copyright (c) 2021 Xinas
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

import datetime

mod = "mod4"
terminal = "alacritty"

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),


    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    
    Key([mod], "r", lazy.spawn("rofi -show drun -icon-theme 'Papirus' -show-icons -theme android_notification"),
        desc="Spawn rofi"
    ),
    Key([mod], "c", lazy.spawn("rofi -show calc -modi calc -no-show-match -no-sort -theme android_notification"), desc="Spawn rofi calculation"),
    Key([mod], "p", lazy.spawn("rofi -show p -modi p:\"rofi-power-menu --no-symbols\" -theme android_notification"), desc="Spawn rofi power menu"),

    # Sound
    Key([mod, "control"], "m", lazy.spawn("pamixer --toggle-mute"))
]

groups = [Group(i, label='○') for i in "123456789"]

for i in groups:
    keys.extend([
        # mod + number of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod + shift + number of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
    ])

layouts = [
    layout.Tile(
        border_focus='#5e81ac',
        border_normal='#2e3440',
        margin=8,
        ratio=0.5
    )
]

widget_defaults = dict(
    font='Hurmit Nerd Font',
    fontsize=12
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        wallpaper="~/.config/qtile/wallpaper/ponyo.png",
        wallpaper_mode="fill",
        top=bar.Bar(
            [
                # Left side
                widget.Image(
                    filename="~/.config/qtile/archnordic.png",
                    margin = 3
                ),
                widget.GroupBox(
                    active='eceff4',
                    this_current_screen_border='5e81ac',
                    inactive='4c566a',
                    fontsize=20,
                    highlight_method = 'text',
                    margin_x = 0,
                    margin_y = 3
                ),
                widget.Spacer(),

                # Center
                widget.TaskList(),
                widget.Spacer(),

                # Right side
                widget.CheckUpdates(
                    distro = "Arch_checkupdates",
                    display_format = "&#x1F4E6; {updates} Updates",
                    no_update_string = "&#x1F4E6; Up to date",
                    update_interval = 43200
                ),
                widget.TextBox(
                    text = "|"
                ),
                widget.PulseVolume(
                    fmt="&#x1F509; {}",
                    update_interval=0.001
                ),
                widget.TextBox(
                    text = "|"
                ),
                widget.Systray(),
                widget.Clock(
                    format="&#x1F4C5; %a %d, %b %H:%M"
                ),
                widget.TextBox(
                    text = " "
                ), 
            ],
            24,
            background='#3b4252'
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []
main = None
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
