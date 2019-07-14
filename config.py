class Config:
    @staticmethod
    def font_style():
        return 'Helvetica'

    @staticmethod
    def light_text_color():
        return '#F4FFFD'

    @staticmethod
    def main_bg_color():
        return '#465362'

    @staticmethod
    def nav_bg_color():
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
