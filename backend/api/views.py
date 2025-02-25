from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Game


# user request new game this is the very first stage of the game object.
# after creating the new game object initial values will save to the db
@api_view(["POST"])
def new_game(request):

    try:
        new_game_obj = Game()
        new_game_obj.initialize_new_game()
        new_game_obj.save()
        # return Response(
        #     {"id": new_game_obj.id, "word": new_game_obj.hidden_word},
        #     status=status.HTTP_201_CREATED,
        # )
        return Response(
            {"id": new_game_obj.id},
            status=status.HTTP_201_CREATED,
        )

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# game/<int:id>
# to this action it will retrive request with integer value (id)
# it will search the game object with id inside the db and return
@api_view(["GET"])
def get_state(request, id):
    try:
        exsisting_game = Game.objects.get(id=id)

        return Response(
            {
                # "word": exsisting_game.hidden_word,
                "game_status": exsisting_game.game_status,
                "identified_word": exsisting_game.identified_word,
                "wrong_guesses": exsisting_game.wrong_guesses,
                "remaining_attempts": exsisting_game.remaining_attempts,
            }
        )

    except Game.DoesNotExist:
        return Response({"error": "Game not found"}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# to this action it will retrive request with integer value (id) and in the payload it will retrieve JSON object
# with received_char property.
@api_view(["POST"])
def guess_char(request, id):
    try:
        try:
            exsisting_game = Game.objects.get(id=id)
        except Game.DoesNotExist:
            return Response(
                {"error": "Game not found"}, status=status.HTTP_404_NOT_FOUND
            )

        # get the received_char value from the payload
        received_char = str(request.data.get("received_char")).lower()

        # check and validate the received_char
        if (
            len(received_char) != 1
            or not isinstance(received_char, str)
            or not received_char
            or not received_char.isalpha()
        ):
            return Response(
                {"error": "Invalid input"}, status=status.HTTP_400_BAD_REQUEST
            )
        else:

            # send to process the the received value in to the process function that from the exsisting game object
            result = exsisting_game.process_guess(received_char)

            # return the response
            return Response(
                {
                    "message": result,
                    "game_status": exsisting_game.game_status,
                    "identified_word": exsisting_game.identified_word,
                    "remaining_attempts": exsisting_game.remaining_attempts,
                }
            )

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
