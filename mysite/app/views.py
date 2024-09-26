#primero hay que hacer los viwer el metodo uado en 
# render para renderizar las pantillas
from django.shortcuts import render, redirect
from django.views.generic import View 

from django.contrib.auth import login, authenticate, logout

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# guardamos los datos o caturamos los datos que  se colocan en el formulario 
class Vregistro(View):   
    def get(self, request):
       form=UserCreationForm()      
       return render(request, "inicio/registro.html",{"form":form})
       
   # al darle click en registrar no redireccionara a la pagina de login 
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            # si el usuario existe nos redireccionara a la pagina de login 
            return redirect("logis")
        else:
            print(form.errors)
        # Asegúrate de devolver algo incluso si el formulario no es válido ,
        #me regresa el formulario si es vacio para que el lo llene .
        return render(request, "inicio/registro.html", {"form": form})
          
 

def loginn(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")
            usuario = authenticate(username=nombre_usuario, password=contraseña)
            if usuario is not None:
                login(request, usuario)
                return render(request, "inicio/menu_principal.html")  # Corregido aquí
            else:
                messages.error(request,"usuario no valido")
        else:
            messages.error(request,"imformacion incorrecta ")
    else:
        form = AuthenticationForm()
    return render(request, "inicio/login.html", {"form": form})

# funcion de menu principal 
def menu_principal(request):
    return render (request, 'inicio/menu_principal.html' )  


   # funcion de cerrar sesion       
def cerrar_sesion(request):
# con logout se usa para cerrar la cesito de un usuario logeado
    logout(request)
    return redirect("logis")



