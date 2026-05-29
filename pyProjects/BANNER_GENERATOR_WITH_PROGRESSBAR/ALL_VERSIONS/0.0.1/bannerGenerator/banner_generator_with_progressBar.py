import os
import sys
import time
import random

# REQUIRED MODULES
try:
    import pyfiglet
    from tqdm import tqdm

    from rich.console import Console
    from rich.panel import Panel
    from rich.align import Align
    from rich.progress import (
        Progress,
        SpinnerColumn,
        BarColumn,
        TextColumn,
        TimeRemainingColumn,
    )

except ImportError as error:

    print(f"[ERROR] Missing Module: {error}")
    print("Install Required Modules:")
    print("pip install rich pyfiglet tqdm")

    sys.exit(1)


# TERMINAL TOOLS CLASS
class TerminalTools:

    def __init__(self):

        self.console = Console()

        # COLORS
        self.RED = "\033[91m"
        self.GREEN = "\033[92m"
        self.YELLOW = "\033[93m"
        self.BLUE = "\033[94m"
        self.MAGENTA = "\033[95m"
        self.CYAN = "\033[96m"
        self.WHITE = "\033[97m"

        # STYLES
        self.BOLD = "\033[1m"
        self.ITALIC = "\033[3m"
        self.UNDERLINE = "\033[4m"

        # RESET
        self.RESET = "\033[0m"

        # RANDOM COLORS
        self.COLORS = [
            self.RED,
            self.GREEN,
            self.YELLOW,
            self.BLUE,
            self.MAGENTA,
            self.CYAN,
        ]

    # CLEAR TERMINAL
    @staticmethod
    def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")

    # MAIN BANNER
    def main_banner(self):

        banner = pyfiglet.figlet_format("BS TERMINAL", font="slant")

        self.console.print(Align.center(f"[bold cyan]{banner}[/bold cyan]"))

    # CREATE CUSTOM BANNER
    def create_banner(self):

        self.clear_screen()

        panel = Panel(
            "[bold green]BANNER GENERATOR[/bold green]", border_style="green", width=60
        )

        self.console.print(Align.center(panel))

        banner_text = input("\nENTER BANNER TEXT: ").strip()

        if not banner_text:
            banner_text = "BS"

        print("""
[1] Simple Banner
[2] Bold Banner
[3] Italic Banner
[4] Underline Banner
[5] Colourful Banner
[6] Random Colour Banner
""")

        choose = input("Choose Banner Style: ").strip()

        try:

            font = "standard"

            if choose == "2":
                font = "big"

            elif choose == "3":
                font = "slant"

            elif choose == "5":
                font = "doom"

            banner = pyfiglet.figlet_format(banner_text, font=font)

            # RANDOM COLOR
            color = self.WHITE

            if choose == "2":
                color = self.GREEN

            elif choose == "3":
                color = self.YELLOW

            elif choose == "4":
                color = self.BLUE

            elif choose == "5":
                color = self.CYAN

            elif choose == "6":
                color = random.choice(self.COLORS)

            print(f"{color}{banner}{self.RESET}")

        except Exception as error:

            print(f"\n{self.RED}" f"[ERROR] {error}" f"{self.RESET}")

    # OLD PROGRESS BAR
    def old_progressbar(self):

        self.clear_screen()

        self.console.print(
            Align.center(
                Panel(
                    "[bold green]OLD PROGRESS BAR[/bold green]",
                    border_style="green",
                    width=60,
                )
            )
        )

        for _ in tqdm(range(100), desc="Loading", ncols=80, colour="green"):

            time.sleep(0.02)

        print(f"\n{self.GREEN}" f"[SUCCESS] Completed!" f"{self.RESET}")

    # FUTURISTIC PROGRESS BAR
    def futuristic_progressbar(self):

        self.clear_screen()

        self.console.print(
            Align.center(
                Panel(
                    "[bold cyan]" "FUTURISTIC PROGRESS BAR" "[/bold cyan]",
                    border_style="cyan",
                    width=60,
                )
            )
        )

        progress = Progress(
            SpinnerColumn(),
            TextColumn("[bold cyan]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]" "{task.percentage:>3.0f}%"),
            TimeRemainingColumn(),
        )

        with progress:

            task = progress.add_task("[green]Initializing System...", total=100)

            for _ in range(100):

                time.sleep(0.03)

                progress.update(task, advance=1)

        self.console.print("\n[bold green]" "[SUCCESS] System Loaded!" "[/bold green]")

    # MAIN MENU
    def menu(self):

        while True:

            self.clear_screen()

            self.main_banner()

            menu_text = """
[bold cyan][1][/bold cyan] Banner Generator

[bold cyan][2][/bold cyan] Old ProgressBar

[bold cyan][3][/bold cyan] Futuristic ProgressBar


[bold red][0][/bold red] Exit
"""

            panel = Panel(
                Align.center(menu_text),
                title="[bold green]MAIN MENU[/bold green]",
                subtitle="[bold green]BS TERMINAL TOOL[/bold green]",
                border_style="bright_blue",
                padding=(1, 5),
                width=80,
            )

            self.console.print(Align.center(panel))

            choose = (
                self.console.input(
                    "\n[bold yellow]" "[ Choose Option ] ~> " "[/bold yellow]"
                )
                .strip()
                .lower()
            )

            # OPTIONS
            if choose == "1":

                self.create_banner()

            elif choose == "2":

                self.old_progressbar()

            elif choose == "3":

                self.futuristic_progressbar()

            # EXIT
            elif choose in ["0", "q", "quit", "exit"]:

                self.console.print(
                    Align.center(
                        Panel(
                            "[bold red]" "[ Closing BS TERMINAL ]..." "[/bold red]",
                            border_style="red",
                            width=50,
                        )
                    )
                )

                time.sleep(1)

                sys.exit(0)

            # INVALID
            else:

                self.console.print(
                    Align.center(
                        Panel(
                            "[bold red]" "[ERROR] Invalid Choice!" "[/bold red]",
                            border_style="red",
                            width=50,
                        )
                    )
                )

            input(
                f"\n{self.GREEN}" f' [ Press "ENTER" To Continue ]...' f"{self.RESET}"
            )
