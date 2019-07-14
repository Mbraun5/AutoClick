class Config:
    # Bg color for root frame
    def __init__(self):
        self.main_bg_color = '#465362'

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
        return {'bg': '#011936',
                'fg': '#F4FFFD',
                'activebackground': '#011936',
                'activeforeground': '#F4FFFD'
                }

