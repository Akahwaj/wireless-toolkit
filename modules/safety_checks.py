def authorized_use_check() -> bool:
    response = input(
        "Do you confirm you are using this toolkit only in an authorized environment? (yes/no): "
    ).strip().lower()

    return response in {"y", "yes"}
