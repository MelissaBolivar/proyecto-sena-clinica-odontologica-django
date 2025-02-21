from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")  # Usa .get() para evitar errores
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print(f"Usuario autenticado: {user.username}, Rol: {getattr(user, 'role', 'No definido')}")  # Debug seguro

            # Redirigir según el rol
            role = getattr(user, "role", None)  # Evita errores si el atributo no existe
            if role == "admin":
                return redirect("admin_dashboard")
            elif role == "auxiliar":
                return redirect("auxiliar_dashboard")
            elif role == "dentista":
                return redirect("dentista_dashboard")
            elif role == "paciente":
                return redirect("paciente_dashboard")
            else:
                print("No tiene rol asignado, volviendo al home")
                return redirect("home")

        else:
            print("Credenciales incorrectas")
            return redirect("login")

    # Si es GET, renderizar la plantilla del login
    return render(request, "login.html")  # Asegúrate de que el template exista


"""
def redirect_to_dashboard(user):
    if user.role == "admin":
        return redirect('admin_dashboard')
    elif user.role == "auxiliar":
        return redirect('auxiliar_dashboard')
    elif user.role == "dentista":
        return redirect('dentista_dashboard')
    elif user.role == "paciente":
        return redirect('paciente_dashboard')
    return redirect('login')
"""
@login_required
def admin_dashboard(request):
    return render(request, 'login/admin_dashboard.html')

@login_required
def auxiliar_dashboard(request):
    return render(request, 'login/auxiliar_dashboard.html')

@login_required
def dentista_dashboard(request):
    return render(request, 'login/dentista_dashboard.html')

@login_required
def paciente_dashboard(request):
    return render(request, 'login/paciente_dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')