from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user


# Planos de Estudo só podem ser visualizados por Usuários que têm o atributo professor
# e este atributo deve estar definido como True
class IsProfessorOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if hasattr(request.user, 'is_professor') and request.user.is_professor == True:
            return True

        return False