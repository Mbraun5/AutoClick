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
    def main_bg_color():
        # grey/blue
        return '#465362'

    @staticmethod
    def nav_bg_color():
        # navy blue
        return '#011936'

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
    def font_small():
        return '{}, 8'.format(Config.font_style())
