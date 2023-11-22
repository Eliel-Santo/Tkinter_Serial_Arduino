#include <ArduinoJson.h>

  StaticJsonDocument<200> doc;
  StaticJsonDocument<200> doc_send;
  char out[100];

  const int led1_pin = LED_BUILTIN;
  
    long long tempo_antigo = millis();
    
void setup() {
  // Initialize serial port
  Serial.begin(9600);
  while (!Serial) continue; // Comando trava o código caso a porta serial esteja intativa

  pinMode(LED_BUILTIN, OUTPUT);

}

void loop() {
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
      if (!error) {

        // Fetch values.
        //
        // Most of the time, you can rely on the implicit casts.
        // In other case, you can do doc["time"].as<long>();
        short var1 = doc["var1"];
        short var2 = doc["var2"];
        short var3 = doc["var3"];
        short var4 = doc["var4"];
        short var5 = doc["var5"];
        short operacao = doc["Operacao"];

        int output[12] = {0};
      
//      
//        if(var1 == 1){
//          digitalWrite(led1_pin, HIGH);   // turn the LED on (HIGH is the voltage level)
//        }else if (var1 == 0){
//          digitalWrite(led1_pin, LOW);    // turn the LED off by making the voltage LOW
//        }
//      
//        if(var2 == 1){
//          digitalWrite(led1_pin, HIGH);   // turn the LED on (HIGH is the voltage level)
//        }else if (var2 == 0){
//          digitalWrite(led1_pin, LOW);    // turn the LED off by making the voltage LOW
//        }
//              
//        if(var3 == 1){
//          digitalWrite(led1_pin, HIGH);   // turn the LED on (HIGH is the voltage level)
//        }else if (var3 == 0){
//          digitalWrite(led1_pin, LOW);    // turn the LED off by making the voltage LOW
//        }
//              
//        if(var4 == 1){
//          digitalWrite(led1_pin, HIGH);   // turn the LED on (HIGH is the voltage level)
//        }else if (var4 == 0){
//          digitalWrite(led1_pin, LOW);    // turn the LED off by making the voltage LOW
//        }
//
//        if(var5 == 1){
//          digitalWrite(led1_pin, HIGH);   // turn the LED on (HIGH is the voltage level)
//        }else if (var5 == 0){
//          digitalWrite(led1_pin, LOW);    // turn the LED off by making the voltage LOW
//        }
      
        if(operacao == 3){
          digitalWrite(led1_pin, HIGH);   // turn the LED on (HIGH is the voltage level)
//          Envio_Dados();
        }else if (operacao == 2){
          digitalWrite(led1_pin, LOW);    // turn the LED off by making the voltage LOW
        }



        
        
      }
      
    }
    
    // LEMBRAR DE DEFINIR QUE SÓ DEVE ENVIAR CASO ALGUM DADO SEJA ALTERADO - Checar se essa lógica funciona ou se só enviaria um JSON VAZIO

    if (millis() - tempo_antigo >= 5000){
      Envio_Dados();
      tempo_antigo = millis();
    }
   
  delay(10);
}

void Envio_Dados(){

  Serial.println("x11111xx22222xx33333xx44444xx55555xx66666xx77777xx88888xx99999xx00000xx12345xx54321xx11111xx22222xx33333xx44444xx55555xx66666xx77777xx88888xx99999xx00000xx12345xx54321xx11111xx22222xx33333xx44444xx55555xx66666xx77777xx88888xx99999xx00000xx12345xx54321x");
  Serial.flush(); // Waits for the transmission of outgoing serial data to complete.
}
