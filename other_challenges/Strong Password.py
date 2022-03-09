def minimumNumber(n, password):
    required = 0
    if not (any(ch.isupper() for ch in password)):
        required += 1
    if not (any(ch.islower() for ch in password)):
        required += 1
    if not (any( not ch.isalnum() for ch in password)):
        required += 1
    if not (any( ch.isdigit() for ch in password)):
        required += 1
    total_length = n + required
    required += 6 - total_length if total_length < 6 else 0
    return required
minimumNumber(5,"2bb#A")
