#include <Wire.h>
#include <LiquidCrystal_I2C.h>

const int trainEntrySensor = 2;
const int trainExitSensor = 3;

const int redLED = 5;
const int greenLED = 6;
const int buzzer = 7;

const int servoPin = 9;

LiquidCrystal_I2C lcd(0x27, 16, 2);

bool trainDetected = false;

// ------------------------------------------------
// SEND STATUS TO PYTHON DASHBOARD
// ------------------------------------------------

void sendStatus(
  const char* train,
  const char* gate,
  const char* red,
  const char* green,
  const char* buzzerStatus,
  int countdown
) {

  Serial.print("TRAIN:");
  Serial.print(train);

  Serial.print(",GATE:");
  Serial.print(gate);

  Serial.print(",RED:");
  Serial.print(red);

  Serial.print(",GREEN:");
  Serial.print(green);

  Serial.print(",BUZZER:");
  Serial.print(buzzerStatus);

  Serial.print(",COUNTDOWN:");
  Serial.println(countdown);
}

// ------------------------------------------------
// SETUP
// ------------------------------------------------

void setup() {

  pinMode(trainEntrySensor, INPUT_PULLUP);
  pinMode(trainExitSensor, INPUT_PULLUP);

  pinMode(redLED, OUTPUT);
  pinMode(greenLED, OUTPUT);
  pinMode(buzzer, OUTPUT);
  pinMode(servoPin, OUTPUT);

  Serial.begin(9600);

  lcd.init();
  lcd.backlight();

  // Gate initially OPEN
  setServoAngle(90);

  digitalWrite(greenLED, HIGH);
  digitalWrite(redLED, LOW);
  digitalWrite(buzzer, LOW);

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("NO TRAIN");
  lcd.setCursor(0, 1);
  lcd.print("GATE: OPEN");

  Serial.println("SMART RAILWAY LEVEL CROSSING");
  Serial.println("SYSTEM READY");

  sendStatus(
    "NO",
    "OPEN",
    "OFF",
    "ON",
    "OFF",
    0
  );
}

// ------------------------------------------------
// MAIN LOOP
// ------------------------------------------------

void loop() {

  int entryState = digitalRead(trainEntrySensor);
  int exitState = digitalRead(trainExitSensor);

  // ---------------------------------------------
  // TRAIN DETECTED
  // ---------------------------------------------

  if (entryState == LOW && trainDetected == false) {

    trainDetected = true;

    Serial.println("EVENT:TRAIN_DETECTED");

    digitalWrite(greenLED, LOW);
    digitalWrite(redLED, HIGH);

    // Countdown
    for (int count = 3; count >= 1; count--) {

      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("TRAIN APPROACH");

      lcd.setCursor(0, 1);
      lcd.print("CLOSING IN: ");
      lcd.print(count);

      Serial.print("COUNTDOWN:");
      Serial.println(count);

      sendStatus(
        "YES",
        "CLOSING",
        "ON",
        "OFF",
        "ON",
        count
      );

      digitalWrite(buzzer, HIGH);
      delay(500);

      digitalWrite(buzzer, LOW);
      delay(500);
    }

    // -------------------------------------------
    // CLOSE GATE
    // -------------------------------------------

    setServoAngle(0);

    digitalWrite(buzzer, LOW);

    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("TRAIN PASSING");

    lcd.setCursor(0, 1);
    lcd.print("GATE: CLOSED");

    Serial.println("EVENT:GATE_CLOSED");

    sendStatus(
      "YES",
      "CLOSED",
      "ON",
      "OFF",
      "OFF",
      0
    );

    delay(1000);
  }

  // ---------------------------------------------
  // TRAIN HAS PASSED
  // ---------------------------------------------

  if (exitState == LOW && trainDetected == true) {

    trainDetected = false;

    Serial.println("EVENT:TRAIN_PASSED");

    // Open gate
    setServoAngle(90);

    digitalWrite(redLED, LOW);
    digitalWrite(greenLED, HIGH);
    digitalWrite(buzzer, LOW);

    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("NO TRAIN");

    lcd.setCursor(0, 1);
    lcd.print("GATE: OPEN");

    Serial.println("EVENT:GATE_OPEN");

    sendStatus(
      "NO",
      "OPEN",
      "OFF",
      "ON",
      "OFF",
      0
    );

    delay(1000);
  }
}

// ------------------------------------------------
// MANUAL SERVO CONTROL
// ------------------------------------------------

void setServoAngle(int angle) {

  if (angle == 0) {

    // Move gate from 90° to 0°
    for (int currentAngle = 90;
         currentAngle >= 0;
         currentAngle -= 5) {

      int pulse = map(
        currentAngle,
        0,
        180,
        500,
        2500
      );

      for (int i = 0; i < 2; i++) {

        digitalWrite(servoPin, HIGH);
        delayMicroseconds(pulse);

        digitalWrite(servoPin, LOW);
        delayMicroseconds(20000 - pulse);
      }
    }

  } else {

    // Move gate from 0° to 90°
    for (int currentAngle = 0;
         currentAngle <= 90;
         currentAngle += 5) {

      int pulse = map(
        currentAngle,
        0,
        180,
        500,
        2500
      );

      for (int i = 0; i < 2; i++) {

        digitalWrite(servoPin, HIGH);
        delayMicroseconds(pulse);

        digitalWrite(servoPin, LOW);
        delayMicroseconds(20000 - pulse);
      }
    }
  }
}