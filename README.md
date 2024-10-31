# Tennis Exercise

Tennis is a sport with a quirky scoring system.
Quoting [Wikipedia](https://en.wikipedia.org/wiki/Tennis#Scoring):

> A game consists of a sequence of points played with the same player serving. A game is won by the first player to have won at least four points in total and at least two points more than the opponent. The running score of each game is described in a manner peculiar to tennis: scores from zero to three points are described as "love", "15", "30", and "40", respectively. If at least three points have been scored by each player, making the player's scores equal at 40 apiece, the score is not called out as "40–40", but rather as "deuce". If at least three points have been scored by each side and a player has one more point than his opponent, the score of the game is "advantage" for the player in the lead. During informal games, advantage can also be called "ad in" or "van in" when the serving player is ahead, and "ad out" or "van out" when the receiving player is ahead; alternatively, either player may simply call out "my ad" or "your ad".
>
> The score of a tennis game during play is always read with the serving player's score first. In tournament play, the chair umpire calls the point count (e.g., "15–love") after each point. At the end of a game, the chair umpire also announces the winner of the game and the overall score.

And a game is just a small part of a match.


## Goal

Write an interactive program to help the chair umpire tracking a single game of a tennis match.
At each interaction with the user, the program must report the running score and ask for the player who scored the next point.
The program terminates at the end of the game, announcing the winner of the game and the overall score.

_This is a multi-stage exercise._
Your first solution is constrained to be basic, and you will have to revise later according to some specific directives. 
**Objects and classes are out of the scope of this exercise, so do not use them.**

## Example usage

Here is an example of what the program is expected to read from and write to the terminal.
```
****************************
* TENNIS GAME TRACKER - v1 *
****************************

Running score: love-all

Next point (S for serving player; R for receiving player): a
Wrong value ignored!

Running score: love-all

Next point (S for serving player; R for receiving player): s

Running score: 15-love

Next point (S for serving player; R for receiving player): r

Running score: 15-all

Next point (S for serving player; R for receiving player): r

Running score: 15-30

Next point (S for serving player; R for receiving player): s

Running score: 30-all

Next point (S for serving player; R for receiving player): s

Running score: 40-30

Next point (S for serving player; R for receiving player): r

Running score: deuce

Next point (S for serving player; R for receiving player): s

Running score: ad-in

Next point (S for serving player; R for receiving player): r

Running score: deuce

Next point (S for serving player; R for receiving player): r

Running score: ad-out

Next point (S for serving player; R for receiving player): s

Running score: deuce

Next point (S for serving player; R for receiving player): s

Running score: ad-in

Next point (S for serving player; R for receiving player): s

End of the game: Serving player win
```


## Version 1

Implement the specification quickly, as a script manipulating the following dictionary:
```python
points = {
    'R': 0,
    'S': 0,
}
```
**Do not define any supporting function or auxiliary variables.**

Use the built-in functions `input()` and `print()` for I/O operations.
Let the user type `S` (or `s`) when a point is scored by the serving player, and `T` (or `t`) when a point is scored by the receiving player.
Ask again if a wrong value is given by the user.

_Do not overdo. Around 50-100 lines of code should suffice._

### Example solution

```python
print("""
****************************
* TENNIS GAME TRACKER - v1 *
****************************
""".strip())

points = {
    'R': 0,
    'S': 0,
}

while True:
    print("\nRunning score: ", end="")
    if points['R'] >= 3 and points['S'] >= 3:
        if points['R'] == points['S']:
            print("deuce", end="")
        elif points['R'] > points['S']:
            print("ad-out", end="")
        else:
            print("ad-in", end="")
    else:
        if points['S'] == 0:
            print("love", end="")
        elif points['S'] == 1:
            print(15, end="")
        elif points['S'] == 2:
            print(30, end="")
        elif points['S'] == 3:
            print(40, end="")
        print("-", end="")
        if points['R'] == points['S']:
            print("all", end="")
        elif points['R'] == 0:
            print("love", end="")
        elif points['R'] == 1:
            print(15, end="")
        elif points['R'] == 2:
            print(30, end="")
        elif points['R'] == 3:
            print(40, end="")

    next_point = input("\n\nNext point (S for serving player; R for receiving player): ").upper()
    if next_point in points:
        points[next_point] += 1
    else:
        print("Wrong value ignored!")
        continue

    if points['R'] >= 4 or points['S'] >= 4:
        if points['R'] > points['S'] + 1:
            print("\nEnd of the game: Receiver player win", end="")
            break
        if points['S'] > points['R'] + 1:
            print("\nEnd of the game: Serving player win", end="")
            break
```


## Version 2

Revise your code according to the following directives:
- Define appropriate functions to improve your code.
  - Call previously defined functions only. Do not call functions defined later in the code.
  - **Add auxiliary variables** if it makes sense.
  - **Do not use type hints.**
- Have a `main()` function and _avoid global variables_.
- Have all I/O operations in the `main()` function.
- Reduce the size of the `main()` function as much as possible, and try to follow the _Five Lines of Code_ principles for all other functions.

_Around 50-100 lines of code should suffice._



### Example solution

```python
def banner():
    return """
****************************
* TENNIS GAME TRACKER - v2 *
****************************
    """.strip()


def advantage_scoring(serving_points, receiver_points):
    if serving_points == receiver_points:
        return "deuce"
    if receiver_points > serving_points:
        return "ad-out"
    return "ad-in"


def score(points):
    scores = ["love", "15", "30", "40"]
    return scores[points]


def running_score(serving_points, receiver_points):
    if serving_points >= 3 and receiver_points >= 3:
        return advantage_scoring(serving_points, receiver_points)
    else:
        return f"{score(serving_points)}-{'all' if serving_points == receiver_points else score(receiver_points)}"


def check_winner(serving_points, receiver_points):
    if serving_points >= 4 or receiver_points >= 4:
        if receiver_points > serving_points + 1:
            return "Receiver player"
        if serving_points > receiver_points + 1:
            return "Serving player"


def main():
    print(banner())

    points = {
        'R': 0,
        'S': 0,
    }

    while True:
        print("\nRunning score:", running_score(points['S'], points['R']), '\n')
        next_point = input("Next point (S for serving player; R for receiving player): ").upper()
        if next_point in points:
            points[next_point] += 1
        else:
            print("Wrong value ignored!")
            continue

        winner = check_winner(points['S'], points['R'])
        if winner:
            print(f"\nEnd of the game: {winner} win")
            break


if __name__ == "__main__":
    main()
```


## Version 3

Revise your code according to the following directives:
- Follow the _Five Lines of Code_ principles also for the `main()` function.
- **Add type hints** to all functions.
- Identify (with comments) each function calling (directly or indirectly) the `input()` function.
- Identify (with comments) each function calling (directly or indirectly) the `print()` function.
- Identify (with comments) each function changing (directly or indirectly) the state of the program.
- Expand the comments from the previous points with all paths leading to the event of interest.
  For example, if `main()` calls `foo()`, which increment `points['S']`, and calls `bar()`, which call `print()`, you can opt for
```python
# output:
#   bar > print
# state:
#   foo > increment
def main() -> None:
    ...
```

_Around 100-200 lines of code should suffice._


### Example solution

```python
def banner() -> str:
    return """
****************************
* TENNIS GAME TRACKER - v3 *
****************************
    """.strip()


def advantage_scoring(serving_points: int, receiver_points: int) -> str:
    if serving_points == receiver_points:
        return "deuce"
    if receiver_points > serving_points:
        return "ad-out"
    return "ad-in"


def score(points: int) -> str:
    scores = ["love", "15", "30", "40"]
    return scores[points]


def running_score(serving_points: int, receiver_points: int) -> str:
    if serving_points >= 3 and receiver_points >= 3:
        return advantage_scoring(serving_points, receiver_points)
    else:
        return f"{score(serving_points)}-{'all' if serving_points == receiver_points else score(receiver_points)}"


def check_winner(serving_points: int, receiver_points: int) -> str:
    if serving_points >= 4 or receiver_points >= 4:
        if receiver_points > serving_points + 1:
            return "Receiver player"
        if serving_points > receiver_points + 1:
            return "Serving player"


# input:
#   input
# state:
#   increment
def read_next_point(points: dict[str, int]) -> bool:
    next_point = input("Next point (S for serving player; R for receiving player): ").upper()
    if next_point in points:
        points[next_point] += 1
        return True
    return False


# input:
#   read_next_point > input
# output:
#   print
#   print
# state:
#   read_next_point > increment
def print_running_score_and_read_next_point(points: dict[str, int]) -> bool:
    print("\nRunning score:", running_score(points['S'], points['R']), '\n')
    if not read_next_point(points):
        print("Wrong value ignored!")
        return False
    return True


# output:
#   print
def print_end_of_the_game(serving_points: int, receiver_points: int) -> bool:
    winner = check_winner(serving_points, receiver_points)
    if winner:
        print(f"\nEnd of the game: {winner} win")
        return True
    return False


# input:
#   print_running_score_and_read_next_point > read_next_point > input
# output:
#   print_running_score_and_read_next_point > print
#   print_running_score_and_read_next_point > print
#   print_end_of_the_game > print
# state:
#   print_running_score_and_read_next_point > read_next_point > increment
def main_loop(points: dict[str, int]) -> None:
    while True:
        if not print_running_score_and_read_next_point(points):
            continue
        if print_end_of_the_game(points['S'], points['R']):
            break


# input:
#   main_loop > print_running_score_and_read_next_point > read_next_point > input
# output:
#   print
#   main_loop > print_running_score_and_read_next_point > print
#   main_loop > print_running_score_and_read_next_point > print
#   main_loop > print_end_of_the_game > print
# state:
#   initialization
#   main_loop > print_running_score_and_read_next_point > read_next_point
def main() -> None:
    print(banner())

    points = {
        'R': 0,
        'S': 0,
    }

    main_loop(points)


if __name__ == "__main__":
    main()
```