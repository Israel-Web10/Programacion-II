import random
class Juego:
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

class JuegoAdivinaNumero(Juego):
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

class Aplicacion:
    @staticmethod
    def main():
        juego = JuegoAdivinaNumero(3)
        while True:
            juego.juega()
            continuar = input("\n¿Quieres jugar otra vez? (s/n): ").lower()
            if continuar != "s":
                print("👋 Gracias por jugar. Tu mejor racha fue:", juego.mejorRacha)
                break

if __name__ == "__main__":
    Aplicacion.main()