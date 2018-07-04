from rest_framework import permissions

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


# Professor só pode apagar as disciplinas dos planos que é autor.
class IsProfessorOwnerOfSubjectOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False

        return request.user.is_professor or request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        return obj.plano.professor == request.user or request.user.is_superuser


# Professor só pode apagar as assuntos das disciplinas de que é autor.
class IsProfessorOwnerOfSubjectOfDisciplineOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False

        return request.user.is_professor or request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        return obj.disciplina.plano.professor == request.user or request.user.is_superuser


class IsProfessorOrAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False

        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_professor or request.user.is_superuser


# Permite estudantes marcarem as atividades como concluídas,
# estudantes não podem deletar atividades (somente marcá-las como realizadas)
class StudentsCanDeleteTheirActivities(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False

        return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if request.user.is_professor:
            return obj.assunto.disciplina.plano.professor == request.user

        if request.user.is_aluno and request.method in permissions.SAFE_METHODS:
            return True

        if request.method == 'PATCH':
            if request.user == obj.estudante:
                return True

        return False