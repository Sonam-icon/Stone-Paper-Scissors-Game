import random


class StonePaperScissors:
    """Simple command-line Stone Paper Scissors game."""

    CHOICES = ["stone", "paper", "scissors"]

    def __init__(self):
        self.user_score = 0
        self.computer_score = 0

    def get_computer_choice(self):
        return random.choice(self.CHOICES)

    def get_result(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "draw"

        if (
            (user_choice == "stone" and computer_choice == "scissors")
            or (user_choice == "paper" and computer_choice == "stone")
            or (user_choice == "scissors" and computer_choice == "paper")
        ):
            return "user"

        return "computer"

    def play_round(self):
        user_choice = input(
            "Choose stone, paper, or scissors (or type 'quit' to exit): "
        ).strip().lower()

        if user_choice == "quit":
            return False

        if user_choice not in self.CHOICES:
            print("Invalid choice. Please try again.\n")
            return True

        computer_choice = self.get_computer_choice()

        print(f"Computer chose: {computer_choice}")

        result = self.get_result(user_choice, computer_choice)

        if result == "user":
            self.user_score += 1
            print("You win!")
        elif result == "computer":
            self.computer_score += 1
            print("Computer wins!")
        else:
            print("It's a draw!")

        print(
            f"Score → You: {self.user_score} | "
            f"Computer: {self.computer_score}\n"
        )

        return True

    def play(self):
        print("=== Stone Paper Scissors ===")

        while self.play_round():
            pass

        print("\nFinal Score")
        print(f"You: {self.user_score}")
        print(f"Computer: {self.computer_score}")
        print("Thanks for playing!")


if __name__ == "__main__":
    game = StonePaperScissors()
    game.play()
