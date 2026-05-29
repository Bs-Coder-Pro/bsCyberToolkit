import os
import sys

from rich.console import Console
from rich.panel import Panel
from rich.align import Align

# =========================================================
# IMPORT MODULE
# =========================================================
try:
    from bannerGenerator import banner_generator_with_progressBar as bgp

except ImportError as error:

    print(f"\n[ IMPORT ERROR ] {error}")
    print("\nMake sure:")
    print("- bannerGenerator folder exists")
    print("- __init__.py exists inside folder")
    print("- banner_generator_with_progressBar.py exists")

    sys.exit(1)


# rich console
console = Console()

# version of [ banner generator & progressbar ]
VERSION = "v0.0.1"


# clear screen of the terminal
def clear_screen():

    os.system("cls" if os.name == "nt" else "clear")


# title of the bs [ banner generator & progressbar ]
def show_title():

    title_panel = Panel(
        Align.center(
            "[bold green]" "BS BANNER GENERATOR WITH PROGRESSBAR" "[/bold green]"
        ),
        border_style="cyan",
        padding=(1, 4),
        expand=False,
    )

    console.print()
    console.print(Align.center(title_panel))
    console.print()


# text menu
def show_menu():

    options = (
        f"[bold cyan]VERSION : {VERSION}[/bold cyan]\n\n"
        f"[bold green][* / 1 / s / S ][/bold green] "
        f"START\n\n"
        f"[bold yellow][ENTER][/bold yellow] "
        f"CONTINUE APPLICATION\n\n"
        f"[bold red][2 / Q / q / 0][/bold red] "
        f"EXIT PROGRAM"
    )

    menu_panel = Panel(
        Align.center(options),
        title="[bold green]MAIN MENU[/bold green]",
        subtitle="[bold green]BS CLI TOOL[/bold green]",
        border_style="bright_yellow",
        padding=(1, 5),
        width=70,
    )

    show_title()

    console.print(Align.center(menu_panel))


# application run function
def run_application():

    try:

        app = bgp.TerminalTools()

        app.menu()

    except AttributeError:

        console.print(
            "\n[bold red]"
            "[ ERROR ]: TerminalTools class "
            "or menu() method not found."
            "[/bold red]"
        )

    except Exception as error:

        console.print(f"\n[bold red]" f"[ ERROR ]: {error}" f"[/bold red]")


# panel termination function
def termination_panel():

    console.print()

    console.print(
        Align.center(
            Panel(
                "[bold red]" "[ BANNER GENERATOR PROGRAM TERMINATED ]" "[/bold red]",
                border_style="red",
                width=60,
            )
        )
    )


# error function for user
def invalid_choice_panel():

    console.print()

    console.print(
        Align.center(
            Panel(
                "[bold red]" "[!] Invalid Choice!" "[/bold red]",
                border_style="red",
                width=50,
            )
        )
    )


# main run function
def main():

    while True:

        clear_screen()

        show_menu()

        try:

            # terminal input style
            choice = console.input(
                "\n[bold cyan]┌──([/bold cyan]"
                "[bold green]bs-terminal[/bold green]"
                "[bold cyan])[/bold cyan]\n"
                "[bold cyan]└─$ [/bold cyan]"
            ).strip()

            #  program terminating conditions
            if choice.lower() in ("2", "q", "0", "quit", "exit"):

                termination_panel()

                sys.exit(0)

            # start the program
            elif choice.lower() in ["1", "s", "S"]:

                console.print(
                    "\n[bold green]" "[+] Starting Application..." "[/bold green]\n"
                )

                run_application()

            elif choice == "":

                console.print(
                    "\n[bold yellow]" "[+] Continuing Application..." "[/bold yellow]\n"
                )

                run_application()

            # error handling with condition
            else:

                invalid_choice_panel()

                input("\nPress ENTER To Continue...")

        # error handling: [ ctrl + c ]
        except KeyboardInterrupt:

            console.print(
                "\n\n[bold red]" "[!] Program Interrupted By User." "[/bold red]"
            )

            sys.exit(0)

        except Exception as error:

            console.print(
                f"\n[bold red]" f"[ UNEXPECTED ERROR ] {error}" f"[/bold red]"
            )

            input("\nPress ENTER To Continue...")


# main program runner
if __name__ == "__main__":
    main()
