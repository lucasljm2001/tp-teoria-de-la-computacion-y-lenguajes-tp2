def controlar_residuos(nivel_peligrosidad, cantidad, destino):
    if cantidad > 450:
        print(f"El residuo ha sido rechazado porque pesa mas de lo permitido (450kg).")
        return "Rechazado"
    else:
        print(f"El residuo con peligrosidad {nivel_peligrosidad} de {cantidad}kg y destino {destino} ha sido procesado.")
        return "Procesado"