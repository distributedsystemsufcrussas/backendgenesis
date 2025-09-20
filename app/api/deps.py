
async def get_current_active_user(user: User = Body(...)) -> User:
    # Esta é uma função de simulação.
    # Em um app real, você decodificaria um token JWT para obter o usuário.
    return user