from cli import CommandLineGameView

view = CommandLineGameView()

view.run(
    [
        "start 20 20",
        "place house 5 5",
        "place well 5 8",
        "place house 5 5",
        "show"
    ]
)