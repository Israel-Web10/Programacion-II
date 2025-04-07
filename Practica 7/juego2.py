import random

class juego2:
    def __init__(self):
        self.numeroDeVidas = 3
        self.record = 0
        self.racha = 0
        self.mejorRacha = 0

    def reiniciaPartida(self):
        self.numeroDeVidas = 3
        print("\nNueva partida iniciada con", self.numeroDeVidas, "vidas.")

    def actualizaRecord(self):
        if self.racha > self.mejorRacha:
            self.mejorRacha = self.racha
            print("🏆 ¡Nuevo récord de racha! Partidas ganadas seguidas:", self.mejorRacha)
        else:
            print("🔁 Racha actual:", self.racha, "| Récord de racha:", self.mejorRacha)

    def quitaVida(self):
        self.numeroDeVidas -= 1
        print("💔 ¡Vida perdida! Vidas restantes:", self.numeroDeVidas)
        return self.numeroDeVidas > 0

class JuegoAdivinaNumero(juego2):
    def __init__(self, vidas):
        super().__init__()
        self.numeroDeVidas = vidas
        self.numeroAAdivinar = 0

    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)

        while True:
            try:
                intento = int(input("🎯 Adivina un número entre 0 y 10: "))
            except ValueError:
                print("⚠️ Por favor, ingresa un número válido.")
                continue

            if intento == self.numeroAAdivinar:
                print("✅ ¡Acertaste!")
                self.racha += 1
                self.actualizaRecord()
                break
            else:
                if self.quitaVida():
                    if intento < self.numeroAAdivinar:
                        print("⬆️ El número es mayor.")
                    else:
                        print("⬇️ El número es menor.")
                else:
                    print("❌ ¡Perdiste! El número era:", self.numeroAAdivinar)
                    self.racha = 0  
                    self.actualizaRecord()
                    break

class JuegoAdivinaPar(juego2):
    def __init__(self, vidas):
        super().__init__()
        self.numeroDeVidas = vidas
        self.numeroAAdivinar = 0

    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.choice([i for i in range(0, 11) if i % 2 == 0])  

        while True:
            try:
                intento = int(input("🎯 Adivina un número *par* entre 0 y 10: "))
            except ValueError:
                print("⚠️ Por favor, ingresa un número válido.")
                continue

            if intento % 2 != 0:  
                print("⚠️ El número debe ser par.")
                continue

            if intento == self.numeroAAdivinar:
                print("✅ ¡Acertaste!")
                self.racha += 1
                self.actualizaRecord()
                break
            else:
                if self.quitaVida():
                    if intento < self.numeroAAdivinar:
                        print("⬆️ El número es mayor.")
                    else:
                        print("⬇️ El número es menor.")
                else:
                    print("❌ ¡Perdiste! El número era:", self.numeroAAdivinar)
                    self.racha = 0  
                    self.actualizaRecord()
                    break

class JuegoAdivinaImpar(juego2):
    def __init__(self, vidas):
        super().__init__()
        self.numeroDeVidas = vidas
        self.numeroAAdivinar = 0

    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.choice([i for i in range(0, 11) if i % 2 == 1])  # solo números impares

        while True:
            try:
                intento = int(input("🎯 Adivina un número *impar* entre 0 y 10: "))
            except ValueError:
                print("⚠️ Por favor, ingresa un número válido.")
                continue

            if intento % 2 == 0:  # Verifica que sea un número impar
                print("⚠️ El número debe ser impar.")
                continue

            if intento == self.numeroAAdivinar:
                print("✅ ¡Acertaste!")
                self.racha += 1
                self.actualizaRecord()
                break
            else:
                if self.quitaVida():
                    if intento < self.numeroAAdivinar:
                        print("⬆️ El número es mayor.")
                    else:
                        print("⬇️ El número es menor.")
                else:
                    print("❌ ¡Perdiste! El número era:", self.numeroAAdivinar)
                    self.racha = 0  
                    self.actualizaRecord()
                    break

class Aplicacion:
    @staticmethod
    def main():
        juego1 = JuegoAdivinaNumero(3)
        juego2 = JuegoAdivinaPar(3)
        juego3 = JuegoAdivinaImpar(3)

        while True:
            print("\n🔢 Juego Adivina Número")
            juego1.juega()

            print("\n➗ Juego Adivina Número Par")
            juego2.juega()

            print("\n➕ Juego Adivina Número Impar")
            juego3.juega()

            continuar = input("\n¿Quieres jugar otra vez? (s/n): ").lower()
            if continuar != "s":
                print("👋 Gracias por jugar. Tu mejor racha fue:")
                print("🏆 Adivina Número: ", juego1.mejorRacha)
                print("🏆 Adivina Número Par: ", juego2.mejorRacha)
                print("🏆 Adivina Número Impar: ", juego3.mejorRacha)
                break

if __name__ == "__main__":
    Aplicacion.main()