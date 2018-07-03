def is_dono_plano(user, atividade):
    if hasattr(user, 'is_professor') and user.is_professor == True:
        return atividade.plano.professor == user
    return False