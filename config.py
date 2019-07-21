class Config:
    @staticmethod
    def font_style():
        return 'Helvetica'

    @staticmethod
    def light_text_color():
        # white
        return '#F4FFFD'

    @staticmethod
    def dark_button_bg_color():
        # dark green/black
        return '#000F08'

    @staticmethod
    def light_button_bg_color():
        # lighter green/black
        return '#092327'

    @staticmethod
    def light_button_fg_color():
        # light turquoise
        return '#86E7B8'

    @staticmethod
    def grey_script_title_color():
        # grey
        return '#F0F0F0'

    @staticmethod
    def main_bg_color():
        # grey/blue
        return '#465362'

    @staticmethod
    def nav_bg_color():
        # navy blue
        return '#011936'

    @staticmethod
    def action_bg_color():
        # light navy blue
        return '#0E2B41'

    @staticmethod
    def highlight_grey():
        # dark grey
        return '#404040'

    @staticmethod
    def nav_active_config():
        return {'activebackground': '#ED254E',
                'activeforeground': '#F9DC5C',
                'bg': '#ED254E',
                'fg': '#F9DC5C'
                }

    @staticmethod
    def nav_passive_config():
        return {'bg': Config.nav_bg_color(),
                'fg': Config.light_text_color(),
                'activebackground': Config.nav_bg_color(),
                'activeforeground': Config.light_text_color()
                }

    @staticmethod
    def font_xtra_small():
        return '{}, 7'.format(Config.font_style())

    @staticmethod
    def font_small():
        return '{}, 8'.format(Config.font_style())

    @staticmethod
    def font_medium():
        return '{}, 9'.format(Config.font_style())

    @staticmethod
    def title_font():
        return '{}'.format(Config.font_style()), 11, 'bold'

    @staticmethod
    def entry_font():
        return '{}'.format(Config.font_style()), 9, 'bold'

    @staticmethod
    def entry_config():
        return {'width': 6,
                'font': Config.entry_font(),
                'validate': 'all',
                'justify': 'center',
                }

    @staticmethod
    def xtra_small_button():
        return {'bg': Config.dark_button_bg_color(),
                'fg': Config.light_text_color(),
                'activebackground': Config.light_button_bg_color(),
                'activeforeground': Config.light_button_fg_color(),
                'font': Config.font_xtra_small(),
                'borderwidth': 1,
                'compound': 'center',
                'relief': 'flat',
                'width': 65,
                'height': 13,
                }

    @staticmethod
    def std_button():
        return {'bg': Config.dark_button_bg_color(),
                'fg': Config.light_text_color(),
                'activebackground': Config.light_button_bg_color(),
                'activeforeground': Config.light_button_fg_color(),
                'font': Config.font_medium(),
                'borderwidth': 1,
                'compound': 'center',
                'width': 85,
                }

    @staticmethod
    def spc_button():
        return {'bg': Config.dark_button_bg_color(),
                'fg': Config.light_text_color(),
                'activebackground': Config.light_button_bg_color(),
                'activeforeground': Config.light_button_fg_color(),
                'font': Config.font_medium(),
                'borderwidth': 1,
                'compound': 'center',
                'relief': 'flat',
                }

    @staticmethod
    def std_label():
        return {'bg': Config.action_bg_color(),
                'fg': Config.light_text_color(),
                'font': Config.font_medium()
                }

    @staticmethod
    def title_label():
        return {'bg': Config.action_bg_color(),
                'fg': Config.light_text_color(),
                'font': Config.title_font()
                }

    @staticmethod
    def get_command_list():
        return ['Left Click',
                'Ctrl + Click',
                'Shift + Click',
                'Alt + Click',
                'Ctrl + Alt + Click',
                'Middle Click',
                'Right Click',
                'Ctrl + Right Click',
                'Alt + Right Click',
                'Ctrl + Alt + Right Click',
                'Double Click',
                'Double Right Click',
                'Begin Dragging - Left Click Down',
                'End Dragging - Left Click Up',
                'Move Mouse',
                'Move Mouse By Offset',
                'Press Keyboard Key',
                'Release Keyboard Key',
                'Press Spacebar'
                ]

    @staticmethod
    def get_description_list():
        return ['Press left click at x, y position.',
                'Press Ctrl + Left click at x, y position.',
                'Press Shift + Left Click at x, y position.',
                'Press Alt + Left Click at x, y position.',
                'Press Ctrl + Alt + Left Click at x, y position.',
                'Press Middle Click at x, y position.',
                'Press Right Click at x, y position.',
                'Press Ctrl + Right Click at x, y position.',
                'Press Alt + Right Click at x, y position.',
                'Press Ctrl + Alt + Right Click at x, y position.',
                'Double Left Click at x, y position.',
                'Double Right Click at x, y position.',
                'Press Left Click down at x, y position. Follow this with Move Mouse action to simulate dragging.',
                'Release Left Click down at x, y, position.',
                'Move Mouse to x, y location.',
                'Mose Mouse by x, y relative offset.',
                'Presses keyboard key down.',
                'Releases keyboard key press.',
                'Presses spacebar key.'
                ]
