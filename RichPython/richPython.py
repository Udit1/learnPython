from rich import inspect, console, print
from rich.color import Color
color = Color.parse("red")
inspect(color, methods=True)
console.print([1, 2, 3])
console.print("[blue underline]Looks like a link")
console.print(locals())
console.print("FOO", style="white on blue")
