// Coloque isto junto das variáveis globais, no topo do código
int angX = 90, angY = 90;               // posição atual dos servos
const int CENTRO_X = 522;               // centro do joystick (meio da sua faixa 510-535)
const int CENTRO_Y = 495;               // centro do joystick (meio da sua faixa 490-500)
const int ZONA_MORTA = 20;              // ignora pequenos desvios do centro
const int PASSO_MAX = 3;                // graus por ciclo com o joystick no máximo
unsigned long ultimoDisplay = 0;
int16_t distancia = 0;
float t = 0, h = 0;



/////////////////
while(flag == 1){

  // ---------- JOYSTICK -> SERVO (velocidade proporcional) ----------
  int dx = analogRead(potpinx) - CENTRO_X;
  int dy = analogRead(potpiny) - CENTRO_Y;

  if (abs(dx) > ZONA_MORTA) angX += map(dx, -512, 512, -PASSO_MAX, PASSO_MAX);
  if (abs(dy) > ZONA_MORTA) angY += map(dy, -512, 512, -PASSO_MAX, PASSO_MAX);

  angX = constrain(angX, 0, 180);
  angY = constrain(angY, 0, 180);

  servox.write(angX);
  servoy.write(angY);

  // ---------- SENSORES + OLED (só a cada 500 ms) ----------
  if (millis() - ultimoDisplay >= 500) {
    ultimoDisplay = millis();

    distancia = sensor.readRangeContinuousMillimeters();
    if (sensor.timeoutOccurred()) { Serial.print(" TIMEOUT"); }
    t = dht.readTemperature();
    h = dht.readHumidity();

    display.clear();
    display.setCursor(1,10);
    display.print("Horiz: ");
    display.print(angX);
    display.print("*");
    display.setCursor(1,20);
    display.print("Vert: ");
    display.print(angY);
    display.print("*");
    display.setCursor(1,30);
    display.print("Distancia: ");
    display.print(distancia, 0);
    display.print("mm");
    display.setCursor(1,40);
    display.print("Umidade: ");
    display.print(h, 0);
    display.print("%");
    display.setCursor(1,50);
    display.print("Temperatura: ");
    display.print(t, 1);
    display.print("*C");
    display.display();
  }

  delay(20);   // ciclo rápido = movimento suave
}

/*
O que mudou e por quê:

Movimento suave: antes o loop tinha delay(100) + delay(500), ou seja, 600 ms por ciclo. Agora o servo é atualizado a cada ~20 ms, e o display e os sensores só a cada 500 ms, sem travar o joystick.
Ajuste da velocidade: a velocidade máxima é PASSO_MAX graus a cada 20 ms. Com 3, são cerca de 150°/s. Se ainda estiver rápido, reduza para 2 ou 1. Se ficar lento demais, aumente.
Direção: se o servo girar ao contrário do joystick, troque o sinal: map(dx, -512, 512, PASSO_MAX, -PASSO_MAX).
Zona morta: se o servo derivar sozinho com o joystick solto, aumente ZONA_MORTA. Se os centros não baterem com os do seu joystick, ajuste CENTRO_X e CENTRO_Y com o valor que o analogRead mostra em repouso.
Posição inicial: os servos começam em 90° no primeiro movimento. Se quiser que eles já comecem nessa posição, coloque servox.write(90); servoy.write(90); no setup().

Dois detalhes das linhas do display:

Cada caractere ocupa cerca de 6 px, então “Ângulo Horizontal: 180*” (23 caracteres) passa dos 128 px da tela e quebra para a linha de baixo. Por isso encurtei os textos para “Horiz:” e “Vert:”.
As letras acentuadas como “Â” provavelmente não existem na fonte da biblioteca e aparecem como lixo. Prefira textos sem acento.

Esses dois problemas podem estar ligados ao bug que você vinha tendo na tela, então vale testar se ele ainda aparece com o código novo.
*/