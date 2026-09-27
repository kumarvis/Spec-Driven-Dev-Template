"""Entry point for the calculator desktop application."""

from calculator.ui import CalculatorWindow


def main() -> None:
    app = CalculatorWindow()
    app.mainloop()


if __name__ == "__main__":
    main()
