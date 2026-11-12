import random

class Tragamonedas:
    """Clase base que modela el comportamiento general de una máquina tragamonedas."""

    def __init__(self, nombre, creditos):
        self.nombre = nombre
        self._creditos = creditos          # Encapsulación: saldo protegido
        self._total_jugado = 0             # Total acumulado de apuestas
        self._total_ganado = 0             # Total acumulado de premios ganados

    def mostrar(self):
        """Muestra el estado actual del saldo de la máquina."""
        estado = f"S/ {self._creditos}" if self._creditos > 0 else "💀 SIN CRÉDITOS"
        print(f"🎰 {self.nombre} — {estado}")

    def girar(self):
        """Genera 3 símbolos aleatorios y los muestra en pantalla."""
        simbolos = ["🍒", "🔔", "💎", "🍀", "⭐", "7️⃣"]
        resultado = []
        for _ in range(3):
            indice = random.randint(0, len(simbolos) - 1)
            resultado.append(simbolos[indice])
        print(f"[ {resultado[0]}  {resultado[1]}  {resultado[2]} ]")
        return resultado

    def jugar(self, apuesta):
        """Gestiona la lógica de la apuesta, giro y premios estándar."""
        if self._creditos == 0:
            print("💀 Esta máquina no tiene créditos.")
            return False

        if apuesta > self._creditos:
            print(f"❌ No tienes suficiente saldo. Créditos disponibles: S/ {self._creditos}")
            return False

        self._creditos -= apuesta
        self._total_jugado += apuesta
        resultado = self.girar()

        # Condición 1: Tres símbolos iguales (Jackpot x10)
        if resultado[0] == resultado[1] == resultado[2]:
            premio = apuesta * 10
            print(f"🎉 ¡JACKPOT! Ganaste S/ {premio}")
            self._creditos += premio
            self._total_ganado += premio
        # Condición 2: Dos símbolos iguales (Premio x2)
        elif resultado[0] == resultado[1] or resultado[1] == resultado[2] or resultado[0] == resultado[2]:
            premio = apuesta * 2
            print(f"✨ ¡Dos iguales! Ganaste S/ {premio}")
            self._creditos += premio
            self._total_ganado += premio
        # Condición 3: Ninguna coincidencia
        else:
            print(f"😢 Perdiste S/ {apuesta}")

        return True

    def mostrar_estadisticas(self):
        """Muestra el balance financiero histórico de la máquina."""
        print(f"   🎰 {self.nombre}")
        print(f"   Apostado: S/ {self._total_jugado} | Ganado: S/ {self._total_ganado}")
        balance = self._total_ganado - self._total_jugado
        signo = "+" if balance >= 0 else ""
        print(f"   Balance: S/ {signo}{balance} | Créditos actuales: S/ {self._creditos}\n")


class TragamonedasFrutas(Tragamonedas):
    """Máquina temática de frutas con su propio conjunto de símbolos."""

    def __init__(self, nombre, creditos):
        super().__init__(nombre, creditos)

    def girar(self):
        simbolos = ["🍒", "🍋", "🍊", "🍇", "🍉", "🍓"]
        resultado = []
        for _ in range(3):
            indice = random.randint(0, len(simbolos) - 1)
            resultado.append(simbolos[indice])
        print(f"[ {resultado[0]}  {resultado[1]}  {resultado[2]} ]")
        return resultado


class TragamonedasClasico(Tragamonedas):
    """Máquina clásica de casino con campanas, diamantes y sietes."""

    def __init__(self, nombre, creditos):
        super().__init__(nombre, creditos)

    def girar(self):
        simbolos = ["7️⃣", "💎", "🔔", "⭐", "💲", "🎰"]
        resultado = []
        for _ in range(3):
            indice = random.randint(0, len(simbolos) - 1)
            resultado.append(simbolos[indice])
        print(f"[ {resultado[0]}  {resultado[1]}  {resultado[2]} ]")
        return resultado


class TragamonedasMundial(Tragamonedas):
    """Máquina temática con banderas y reglas especiales de bonificación."""

    def __init__(self, nombre, creditos):
        super().__init__(nombre, creditos)

    def girar(self):
        simbolos = ["🇵🇪", "🇦🇷", "🇫🇷", "🇧🇷", "🇪🇸", "🏴󠁧󠁢󠁥󠁮󠁧󠁿"]
        resultado = []
        for _ in range(3):
            indice = random.randint(0, len(simbolos) - 1)
            resultado.append(simbolos[indice])
        print(f"[ {resultado[0]}  {resultado[1]}  {resultado[2]} ]")
        return resultado

    def jugar(self, apuesta):
        """Reglas especiales: Triplete x15 y bono de recuperación con la bandera de Perú."""
        if self._creditos == 0:
            print("💀 Esta máquina no tiene créditos.")
            return False

        if apuesta > self._creditos:
            print(f"❌ No tienes suficiente saldo. Créditos disponibles: S/ {self._creditos}")
            return False

        self._creditos -= apuesta
        self._total_jugado += apuesta
        resultado = self.girar()
        tiene_peru = "🇵🇪" in resultado

        if resultado[0] == resultado[1] == resultado[2]:
            premio = apuesta * 15
            print(f"🏆 ¡TRIPLETE MUNDIALISTA! Ganaste S/ {premio}")
            self._creditos += premio
            self._total_ganado += premio
        elif resultado[0] == resultado[1] or resultado[1] == resultado[2] or resultado[0] == resultado[2]:
            premio = apuesta * 2
            print(f"⚽ ¡Dos iguales! Ganaste S/ {premio}")
            self._creditos += premio
            self._total_ganado += premio
        elif tiene_peru:
            print("🇵🇪 ¡Apareció la blanquirroja! Recuperas tu apuesta.")
            self._creditos += apuesta
            self._total_ganado += apuesta
        else:
            print(f"😢 Perdiste S/ {apuesta}")

        return True


def jugar_en_maquina(maquina):
    """Controla el bucle de apuestas en la máquina seleccionada."""
    while maquina._creditos > 0:
        maquina.mostrar()
        try:
            apuesta = int(input("¿Cuánto apuestas? (0 para volver al menú): "))
        except ValueError:
            print("⚠️ Ingresa un número entero válido.")
            continue

        if apuesta == 0:
            print("🔙 Volviendo al menú principal...\n")
            break

        if apuesta < 0:
            print("⚠️ La apuesta no puede ser negativa.")
            continue

        maquina.jugar(apuesta)
        print()

    if maquina._creditos == 0:
        print(f"💸 Te quedaste sin créditos en {maquina.nombre}.\n")


def iniciar_casino():
    """Menú principal interactivo de Casino Royale."""
    maquinas = [
        TragamonedasFrutas("La Frutal", 200),
        TragamonedasClasico("La Clásica", 300),
        TragamonedasMundial("Mundial 2026", 150),
    ]

    while True:
        print("=" * 38)
        print("        🎰 CASINO ROYALE 🎰")
        print("=" * 38)

        for i, m in enumerate(maquinas, 1):
            estado = f"S/ {m._creditos}" if m._creditos > 0 else "💀 SIN CRÉDITOS"
            print(f"  {i}. {m.nombre} ({estado})")

        print(f"  {len(maquinas) + 1}. Mostrar estadísticas de todas las máquinas")
        print(f"  {len(maquinas) + 2}. Salir del casino")

        try:
            opcion = int(input("\nElige una opción: "))
        except ValueError:
            print("⚠️ Opción inválida. Intenta nuevamente.\n")
            continue

        if 1 <= opcion <= len(maquinas):
            maquina_elegida = maquinas[opcion - 1]
            if maquina_elegida._creditos == 0:
                print("💀 Esta máquina está sin créditos. Por favor elige otra.\n")
            else:
                print(f"\n--- Entrando a {maquina_elegida.nombre} ---")
                jugar_en_maquina(maquina_elegida)

        elif opcion == len(maquinas) + 1:
            print("\n📊 ESTADÍSTICAS GENERALES DEL CASINO")
            print("-" * 38)
            for m in maquinas:
                m.mostrar_estadisticas()

        elif opcion == len(maquinas) + 2:
            print("\n💰 ¡Gracias por visitar el Casino Royale! Vuelve pronto.")
            break
        else:
            print("⚠️ Opción fuera de rango.\n")


if __name__ == "__main__":
    iniciar_casino()

