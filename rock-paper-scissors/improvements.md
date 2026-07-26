# Rock Paper Scissors

### Feature 1: Show both choices

Store both the player and computer choices as variables and output them before showing the result.

> [!NOTE]
> **Skills**
> Variables 
> F-strings

<details>
<summary>See example implementation</summary>

```python
def main() -> None:
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()

    print(f'You chose: {player_choice}')
    print(f'The computer chose: {computer_choice}')
    print(determine_winner(player_choice, computer_choice))
```
</details>

<details>
<summary>Expected result</summary>

```console
You chose: rock 
The computer chose: rock
Try again! Draw.
```
</details>

## Feature 2: Allow repeated rounds

Wrap the game in a while loop to allow users to continue playing until a keyword is provided

> [!NOTE]
> **Skills**
> While loops (Break, and Continue)
> Boolean Conditions
> Reusing functions
> Reusing variables

The game should continue to run until the player enters `quit` opposed to one of the game options. 

<details>
<summary>See example implementation</summary>

```python
def main() -> None:
    ...
```
</details>

<details>
<summary>Expected result</summary>

```console
...
```
</details>