def result() -> any:
    return response("result", "Запрос успешно обработан")


def error(err) -> any:
    return response("error", err)


def response(response_type, response_description) -> any:
    return {
                response_type: {
                    "message": response_description
                }
            }
