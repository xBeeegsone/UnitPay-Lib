def result() -> dict:
    return response("result", "Запрос успешно обработан")


def error(err: str) -> dict:
    return response("error", err)


def response(response_type: str, response_description: str) -> dict:
    return {
                response_type: {
                    "message": response_description
                }
            }
