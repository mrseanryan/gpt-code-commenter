from . import config

class bcolors:
    HEADER = '\033[95m'
    DARK_BLUE = '\033[34m'
    DARK_MAGENTA = '\033[35m'
    DARK_CYAN = '\033[36m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def colorize(text, color):
    start_color = color if config.IS_COLOR_ENABLED else ""
    end_color = bcolors.ENDC if config.IS_COLOR_ENABLED else ""
    colorized = f"{start_color}{text}{end_color}"
    return colorized

# Theming
CONFIG_COLOR = bcolors.DARK_MAGENTA
IMPORTANT = bcolors.WARNING
QUESTION_COLOR = bcolors.DARK_CYAN
RESULT_COLOR = bcolors.OKGREEN + bcolors.BOLD
SECTION_COLOR = bcolors.OKBLUE + bcolors.BOLD
TEST_SECTION_COLOR = bcolors.WARNING + bcolors.BOLD
ERROR_COLOR = bcolors.FAIL + bcolors.BOLD
WARNING_COLOR = bcolors.WARNING + bcolors.BOLD
END_COLORS = bcolors.ENDC
