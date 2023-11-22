#include <Adafruit_ADS1X15.h>
#include <ArduinoJson.h>

  StaticJsonDocument<200> doc;
  StaticJsonDocument<200> doc_send;
  char out[100];

  Adafruit_ADS1115 ads;     
  
  int operacao = 0;
  int intensidade = 1;
  float leituraOD = 0.0, leituraOE = 0.0, leituraT = 0.0;
  
  float leituraODescuro = 0.0, leituraOEescuro = 0.0, leituraTescuro = 0.0;
  float leituraODcorrigida = 0.0, leituraOEcorrigida = 0.0, leituraTcorrigida = 0.0;
  float razaoCalibracaoODT = 0.0, razaoCalibracaoOET = 0.0;
  float leituraODcorrigidaCalibrada = 0.0, leituraOEcorrigidaCalibrada = 0.0;
  float protecaoOD = 0.0, protecaoOE = 0.0;

void setup() {
  Serial.begin(9600);
  while (!Serial) continue; // Comando trava o código caso a porta serial esteja intativa
  
  if (!ads.begin()) {
   // while (1);
  }
  analogWrite(3,0);
  
}

void loop() {

  intensidade = readjson("var1");
  operacao = readjson("Operacao");
  
  switch(operacao){
    case 0:

    leituraODescuro = 0.0;
    leituraOEescuro = 0.0;
    leituraTescuro = 0.0;
    leituraODcorrigida = 0.0;
    leituraOEcorrigida = 0.0;
    leituraTcorrigida = 0.0;
    razaoCalibracaoODT = 0.0;
    razaoCalibracaoOET = 0.0;
    leituraODcorrigidaCalibrada = 0.0;
    leituraOEcorrigidaCalibrada = 0.0;
    protecaoOD = 0.0; 
    protecaoOE = 0.0;
    
    enviardados();
    
    //operacao = 10;
      
    break;

    case 1:

    analogWrite(3,0);
    delay(10000);
    for(int i = 0; i < 500; i++){
      leituraOD = leituraOD + ads.readADC_SingleEnded(0);
      leituraOE = leituraOE + ads.readADC_SingleEnded(2);
      leituraT = leituraT + ads.readADC_SingleEnded(1);
      delay(10);
    }
    leituraODescuro = leituraOD/500;
    leituraOEescuro = leituraOE/500;
    leituraTescuro = leituraT/500;
    leituraOD = 0;
    leituraOE = 0;
    leituraT = 0;

    enviardados();
    
    //operacao = 10;
      
    break;

    case 2:

    analogWrite(3,intensidade);
    delay(10000);
    for(int i = 0; i < 500; i++){
      leituraOD = leituraOD + (ads.readADC_SingleEnded(0) - leituraODescuro);
      leituraOE = leituraOE + (ads.readADC_SingleEnded(2) - leituraOEescuro);
      leituraT = leituraT + (ads.readADC_SingleEnded(1) - leituraTescuro);
      delay(10);
    }
    leituraOD = leituraOD/500;
    leituraOE = leituraOE/500;
    leituraT = leituraT/500;
    razaoCalibracaoODT = (leituraOD/leituraT);
    razaoCalibracaoOET = (leituraOE/leituraT);
    leituraOD = 0;
    leituraOE = 0;
    leituraT = 0;
    analogWrite(3,0);

    enviardados();
    
    //operacao = 10;
      
    break;

    case 3:

    analogWrite(3,intensidade);
    delay(10000);
    for(int i = 0; i < 500; i++){
      leituraOD = leituraOD + ((ads.readADC_SingleEnded(0) - leituraODescuro)/razaoCalibracaoODT);
      leituraOE = leituraOE + ((ads.readADC_SingleEnded(2) - leituraOEescuro)/razaoCalibracaoOET);
      leituraT = leituraT + (ads.readADC_SingleEnded(1) - leituraTescuro);
      delay(10);
    }
    leituraOD = leituraOD/500;
    leituraOE = leituraOE/500;
    leituraT = leituraT/500;
    protecaoOD = 100*(1-(leituraOD/leituraT));
    protecaoOE = 100*(1-(leituraOE/leituraT));

    analogWrite(3,0);

    enviardados();
    
    //operacao = 10;
      
    break;

    default:
    
    break;

    
    
  }

}

int readjson(String var_json){
  String teststr;

    if (Serial.available() > 0){
      Serial.setTimeout(10); //sets the maximum milliseconds to wait for serial data.
      
      String teststr = Serial.readStringUntil('\n'); //read until timeout
      teststr.trim();                       // remove any \r \n whitespace at the end of the String
  
      int str_len = teststr.length() + 1;   // Length (with one extra character for the null terminator)
      char teste[str_len];                  // Prepare the character array (the buffer) 
      teststr.toCharArray(teste, str_len);  // Copy it over 
      

  
      // Deserialize the JSON document
      DeserializationError error = deserializeJson(doc, teste);
  
      
      // Test if parsing succeeds.
      if (error) {
      }else{
        return doc[var_json];
      }
    }
}

void enviardados(){

  Serial.print("x");
  print_number(leituraODescuro);
  Serial.print("x");
  
  Serial.print("x");
  print_number(leituraOEescuro);
  Serial.print("x");
  
  Serial.print("x");
  print_number(leituraTescuro);
  Serial.print("x");
  
  Serial.print("x");
  print_number(leituraODcorrigida);
  Serial.print("x");
  
  Serial.print("x");
  print_number(leituraOEcorrigida);
  Serial.print("x");
  
  Serial.print("x");
  print_number(leituraTcorrigida);
  Serial.print("x");
  
  Serial.print("x");
  print_number(10000*razaoCalibracaoODT);
  Serial.print("x");
  
  Serial.print("x");
  print_number(10000*razaoCalibracaoOET);
  Serial.print("x");
  
  Serial.print("x");
  print_number(leituraODcorrigidaCalibrada);
  Serial.print("x");
  
  Serial.print("x");
  print_number(leituraOEcorrigidaCalibrada);
  Serial.print("x");
  
  Serial.print("x");
  print_number(10000*protecaoOD);
  Serial.print("x");
  
  Serial.print("x");
  print_number(10000*protecaoOE);
  Serial.println("x");
  
}


void print_number(int number){

// Código retorna cada algarismo de um número do início pro fim
   
    float aux2 = 0;
    float aux3 = 0;
   
    int digitos = 5;
    int numero = abs(number);
   
    for(int i = 1;i<=digitos;i++){
        aux2 = numero/float(pow(10,digitos));
        aux3 = floor( aux2*pow(10,i) ) - 10*floor( aux2*pow(10,i-1) );
        Serial.print(aux3);
        
    }

}
