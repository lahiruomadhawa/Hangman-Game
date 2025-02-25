<template>
  <div>
    <h2>Hangman Game</h2>
    <div>
      <button @click="startNewGame">Start new game</button>
      <br />
      <div v-if="newGameId">
        <h3>
          Hangman started. The game ID is <b>{{ newGameId }}</b>
        </h3>
      </div>
    </div>
    <div>
      <h3>Enter game ID below to start exsisting game.</h3>
    </div>
    <div>
      <input
        type="text"
        v-model="existingGameId"
        placeholder="Enter exisitng game id"
        @keyup="startExsistingGame"
      />
      <br />
      <!-- <button @click="startExsistingGame">Start Existing Game</button> -->
      <br />
    </div>

    <div v-if="gameState">
      <h4>
        Game Status : <b>{{ gameState.game_status }}</b>
      </h4>
      <h4>
        Identified Word: <b>{{ gameState.identified_word }}</b>
      </h4>
      <h4>
        Wrong Guesses: <b>{{ gameState.wrong_guesses }}</b>
      </h4>
      <h4>
        Remaining Attempts: <b>{{ gameState.remaining_attempts }}</b>
      </h4>
    </div>

    <div v-if="errorMsgs">
      <h3>
        Error when starting game : <b>{{ errorMsgs }}</b>
      </h3>
    </div>
    <div>
      <div v-if="(newGameId || existingGameId) && !errorMsgs">
        <div>
          <h3>Input letter for a guess here</h3>
        </div>
        <input
          type="text"
          maxlength="1"
          v-model="charGuessed"
          placeholder="Enter a letter for guess"
        />
        <br />
        <button @click="submitUserGuess">Submit Guess</button>
      </div>
      <div>
        <h3 v-if="guessedCharMsgs">{{ guessedCharMsgs }}</h3>
        <br />
        <h3 v-if="guessedCharError">Error : {{ guessedCharError }}</h3>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { ref } from "vue";

export default {
  name: "GameComponent",
  setup() {
    //initiated ref constants for two-way communication
    const newGameId = ref(null);
    const gameState = ref(null);
    const errorMsgs = ref(null);
    const existingGameId = ref("");

    const charGuessed = ref("");
    const guessedCharError = ref(null);
    const guessedCharMsgs = ref(null);

    //start the game and retrieve the game id
    function startNewGame() {
      try {
        axios
          .post("http://127.0.0.1:8000/api/game/new/")
          .then((response) => {
            newGameId.value = response.data.id;
          })
          .catch((error) => {
            errorMsgs.value = error.response?.data?.error;
          });
      } catch (error) {
        errorMsgs.value = error;
      }
    }

    // get the already started game status
    function startExsistingGame() {
      try {
        if (!existingGameId.value) {
          errorMsgs.value = "Please enter game id.";
          return;
        } else {
          errorMsgs.value = null;
          axios
            .get("http://127.0.0.1:8000/api/game/" + existingGameId.value + "/")
            .then((response) => {
              gameState.value = response.data;
            })
            .catch((error) => {
              errorMsgs.value = error.response?.data?.error;
            });
        }
      } catch (error) {
        errorMsgs.value = error;
      }
    }

    // submit the user guessed char to process
    async function submitUserGuess() {
      try {
        if (!existingGameId.value) {
          guessedCharError.value = "Start a new or existing game first.";
          return;
        }

        if (!charGuessed.value || charGuessed.value.length !== 1) {
          guessedCharError.value = "Please enter a single valid letter.";
          return;
        }

        guessedCharError.value = null;

        const serverResponse = await axios.post(
          "http://127.0.0.1:8000/api/game/" + existingGameId.value + "/guess/",
          {
            received_char: charGuessed.value,
          }
        );
        guessedCharMsgs.value = serverResponse.data.message;
        startExsistingGame();
      } catch (error) {
        guessedCharError.value = error;
      }
    }
    return {
      startNewGame,
      startExsistingGame,
      submitUserGuess,
      newGameId,
      errorMsgs,
      existingGameId,
      gameState,
      charGuessed,
      guessedCharError,
      guessedCharMsgs,
    };
  },
};
</script>

<style scoped>
button {
  background-color: #42b983;
  color: white;
  border: none;
  padding: 10px 15px;
  font-size: 16px;
  cursor: pointer;
  border-radius: 5px;
}
input {
  padding: 10px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-right: 5px;
}
</style>