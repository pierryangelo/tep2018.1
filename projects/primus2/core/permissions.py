from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user


# A view UsuarioList só pode ser acessada por o super usuário.
# Usuários regulares poderão visualizar outros perfis, porém só podem modificar
# ou deletar o seu próprio perfil.
class IsAdminOrNothing(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False

        return request.user.is_superuser

# Somente usuários podem acessar outros perfis, porém só podem realizar alterações
# em seu perfil.
class IsProfileOwnerOrIsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False

        return request.user.is_superuser or request.user.is_professor

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj == request.user


# Na view PlanoDeEstudoList, todos os professores ou administradores podem visualizar todos
# os planos, porém somente o professor dono de cada plano pode alterar/remover.
class IsProfessorAndPlanOwnerOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False

        return request.user.is_professor or request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        return obj.professor == request.user or request.user.is_superuser


# Somente professores podem cadastrar atividades






# Estudantes só podem ver suas próprias atividades
class IsDonoAtividade(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Professores têm acesso às atividades cadastradas por ele
        if hasattr(request.user, 'is_professor'):
            return obj.estudante.is_professor and obj.plano.professor == request.user

        # Estudantes têm acesso somentes às suas atividades
        if hasattr(request.user, 'is_aluno'):
            return obj.estudante.is_aluno and obj.estudante == request.user

