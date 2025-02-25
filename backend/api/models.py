import random
from django.conf import settings
from django.db import models


# model for Game and bind with python ORM
class Game(models.Model):

    # class properties and methods
    hidden_word = models.CharField(max_length=10, null=False, blank=False)
    identified_word = models.CharField(max_length=10)
    wrong_guesses = models.IntegerField(default=0)
    max_attempts = models.IntegerField()
    remaining_attempts = models.IntegerField()
    game_status = models.CharField(max_length=10, default="InProgress")

    # when user request new game, this method triggers and initiate basic values for the game object
    def initialize_new_game(self):
        self.hidden_word = str(random.choice(settings.STATIC_WORDS)).lower()
        self.identified_word = self.make_placeholder_for_word(self.hidden_word)
        self.max_attempts = self.count_attempts(self.hidden_word)
        self.remaining_attempts = self.calculate_guesses_count(
            self.max_attempts, self.wrong_guesses
        )

    # generate a placeholder string for the selected hidden word
    def make_placeholder_for_word(self, word):
        placeholder_string = "_" * len(word)
        return placeholder_string

    # count how many guesses user have with lenght of hidden word devided by 2 (and round it to nearest number)
    def count_attempts(self, word):
        return round(len(word) / 2)

    # count how many attemts user still got
    def calculate_guesses_count(self, max_attempts: int, wrong_guesses: int):
        return max_attempts - wrong_guesses

    # this will accept 2 params (exsisting, new) values, then merge them together
    def merge_blank(self, word1, word2):
        merged_word = list(word1)

        for i in range(len(word1)):
            if word1[i] == "_":
                merged_word[i] = word2[i]

        return_string = "".join(merged_word)
        return return_string

    # this is where the user guess finds, it's correct or not
    def process_guess(self, char: str):

        # check the game status before begin the process
        if self.game_status == "InProgress":

            # check if user input alredy found or not
            if char in self.identified_word:
                return "Already guessed this character"

            # check user input containing in the hidden word in anywhere
            # if not it is wrong guess. need to increment the wrong_guesses
            if char not in self.hidden_word:
                self.wrong_guesses += 1
                self.remaining_attempts = self.calculate_guesses_count(
                    self.max_attempts, self.wrong_guesses
                )

                # check the wrong_guesses count and max_attempts count and decide the status as Lost and save it inside db
                if self.wrong_guesses >= self.max_attempts:
                    self.game_status = "Lost"
                    self.save()
                    return "Char is not in the hidden word"

                # game is still playing and showing how many attempts left. and saving current state in db
                self.save()
                return f"Char is not in the hidden word. {self.remaining_attempts} attempts remaining"

            # create temparary list from identified_word
            # find the input inside the hidden word and it's places (indexes) in the word.
            # multiple occurences can be there
            placeholder = list(self.identified_word)
            for i, c in enumerate(self.hidden_word):
                if c == char:
                    placeholder[i] = char

            # asign the placeholder list (after joining as string) to the identified_word
            # this is like how many chars found so far
            self.identified_word = "".join(placeholder)

            # compare the equality of the guess so far word and original hidden word
            # decide the game_status and store it in db
            if self.identified_word == self.hidden_word:
                self.game_status = "Won"
                self.save()
                return "You won the game"

            # user input char is correct guess and user still have same attempts
            self.save()
            return f"Correct guess. {self.remaining_attempts} attempts remaining"

        # if user requst fame with other game_status than InProgress (Won or Lost)
        else:
            return "Game is already over"
