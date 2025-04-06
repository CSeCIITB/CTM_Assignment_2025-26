# Assembly, but limited memory!


Our dear friend @Owl-A is still at it, wishing to compute Fibonacci numbers in limited memory using Assembly programs. But [Owl-A's script](fib.S) is not working!

Someone informed him that memory was the source of all his troubles but he, being occupied with other things, has now left it to you to figure out how to make things work! He mentioned something of the likes of [Tail Recursion](https://en.wikipedia.org/wiki/Tail_call) before leaving but we are not sure how this would help...

## Instructions

Running `python3 emulator.py` without any arguments ends up reading the `fib.S`; `python3 emulator.py -` reads the assembly from your standard input (NOTE that the assembly input must be followed by `$` on a new line) ; and `python3 emulator.py file.S` reads the assembly from `file.S`. None of the `.py` files or the `template.S` file are required to be read/understood. You only need to understand `fib.S` and reimplement it in such a manner that the memory consumed is now lower!

Setting the [enivornment variable](https://en.wikipedia.org/wiki/Environment_variable) `DEBUG` with the value `"yes"` would allow you to debug your script by providing you additional information.

You needn't try to understand any of the `.py` files or the `template.S` file. Upload your final solution script in [solve.py](solve.py) along with the correct flag.

## Submission

You need to submit the code of fib.S and a detailed writeup for this question, preferably written in Markdown or LaTeX. 

This is quite a difficult challenge similar in difficulty to real CTF challenges. It will test your ability to learn and solve things on the fly.

Even if you are unable to solve it fret not, any progress made will be duly recognised and considered in the grading.
