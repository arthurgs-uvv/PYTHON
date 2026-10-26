#include "Keypad.h"     //TECLADO
#include "SimpleOLED.h" //OLED
#include <Servo.h>      //SERVO
#include <Wire.h>       //SENSOR DISTANCIA
#include "VL53L0X.h"    //SENSOR DISTANCIA
#include "DHT.h"        //SENSOR TEMPERATURA E UMIDADE

#define DHTPIN 4        //SENSOR TEMPERATURA E UMIDADE
#define DHTTYPE DHT11   //SENSOR TEMPERATURA E UMIDADE

//SENSOR DE DISTANCIA
VL53L0X sensor;

//SENSOR TEMPERATURA E UMIDADE
DHT dht(DHTPIN, DHTTYPE);

//adição do servo
Servo servox;  // create servo object to control a servo
Servo servoy;

char texto[5]; // Suporta 4 caracteres + o '\0' terminador
int indice = 0; // Controla em qual posição do vetor vamos salvar a tecla
int flag = 0; //flag de acesso ao programa

int potpiny = A0;  // analog pin used to connect the potentiometer
int potpinx = A1;
int valy, valx;    // variable to read the value from the analog pin


//OLED
SimpleOLED display(0x3C, 128, 64);
// setcursor(x, y) -> y [10 / 60]


//TECLADO
const byte LINHAS = 4;
const byte COLUNAS = 4;

char mapaTeclas[LINHAS][COLUNAS] = {
  {'1','2','3','A'},
  {'4','5','6','B'},
  {'7','8','9','C'},
  {'*','0','#','D'}
};

byte pinosLinhas[LINHAS] = {8, 7, 6, 5}; 
byte pinosColunas[COLUNAS] = {12, 11, 10, 9}; 

Keypad teclado = Keypad(makeKeymap(mapaTeclas), pinosLinhas, pinosColunas, LINHAS, COLUNAS);

void setup() {
  //inicialização do servo
  servox.attach(2);  // attaches the servo on pin 9 to the servo object
  servoy.attach(3);

  display.begin();
  delay(1000);

  Serial.begin(9600);

  // SENSOR MOVIMENTO
  Wire.begin();
  sensor.setTimeout(500);
  if (!sensor.init())
  {
    Serial.println("Failed to detect and initialize sensor!");
    while (1) {}
  }
  sensor.startContinuous();

  // SENSOR TEMP E UMIDADE
  pinMode(DHTPIN, INPUT_PULLUP);
  Serial.println("DHTxx test!");
  delay( 200 );
  dht.begin();
  
  // OLED
  Serial.println("Teclado Inicializado...");
  
  display.clear();
  display.setCursor(1,10);  
  display.println("Digite 4 letras:");
  display.display();
}

void loop() {
  // Lê o teclado constantemente
  char teclaPressionada = teclado.getKey();
  
  // SE uma tecla real foi pressionada
  if (teclaPressionada) {
    
    // Salva a tecla na posição atual e avança o índice
    texto[indice] = teclaPressionada;
    indice++;
    
    // Mostra no monitor serial para testes
    Serial.print("Digitado: ");
    Serial.println(teclaPressionada);

    // Atualiza o display mostrando o que já foi digitado até agora
    display.clear();
    display.setCursor(10,10);
    display.print("Digitando: ");
    
    // Finaliza temporariamente a string para o display conseguir exibir
    texto[indice] = '\0'; 
    display.print(texto);
    display.display();

    // SE completou os 4 caracteres
    if (indice >= 4) {
      texto[4] = '\0'; // Finaliza a string de forma segura na última posição
      char senha[5]={'1','2','3','4','\0'};
      
      display.clear();
      display.setCursor(10,10);
      display.print("Texto Final: ");
      display.print(texto);
      display.display();
      display.clear();

      if(strcmp(senha, texto)==0){
        display.setCursor(10,10);
        display.print("Acesso Liberado");
        display.display();
        flag = 1;    
        
      }
      else{
        display.setCursor(10,10);
        display.print("Acesso Negado");
        display.display();
        flag = 0;
      }
    }

    while(flag == 1){
      display.clear();
      
      // MEDIDOR DE DISTANCIA
      int16_t distancia = sensor.readRangeContinuousMillimeters(); //Variavel
      if (sensor.timeoutOccurred()) { Serial.print(" TIMEOUT"); }  //Teste de funcionalidade
      //display.println("\t");
      // Verifica se alguma leitura falhou

      // MEDIDOR DE TEMPERATURA
      // Lê a temperatura em Celsius (the default)
      float t = dht.readTemperature();
      // Lê a Umiddade
      float h = dht.readHumidity();
   
      // SERVO
      valx = analogRead(potpinx);
      valy = analogRead(potpiny);
      delay(100);
      if((valx > 535 || valx < 510) || (valy > 500 || valy < 490)){
        //valx = analogRead(potpinx);            // reads the value of the potentiometer (value between 0 and 1023)
         valx = map(valx, 0, 1023, 0, 180);     // scale it for use with the servo (value between 0 and 180)
         servox.write(valx); 
        // valy = analogRead(potpiny);
         valy = map(valy, 0, 1023, 0, 180); 
         servoy.write(valy);            // sets the servo position according to the scaled value                          // waits for the servo to get there
      }
      
      //PRINTS NO OLED
      display.setCursor(1,10);
      display.print("Angulo Horizontal: ");
      display.print(valx);
      display.print("*");
      display.setCursor(1,20);
      display.print("Angulo Vertical: ");
      display.print(valy);
      display.print("*");
      display.setCursor(1,30);
      display.print("Distancia: ");
      display.print(distancia,2);
      display.print("mm");
      display.setCursor(1,40);
      display.print("Umidade: ");
      display.print(h);
      display.print("%");
      display.setCursor(1,50);
      display.print("Temperatura: ");
      display.print(t);
      display.print("*C");
      display.display();

      delay(500);
    }
  }
}
