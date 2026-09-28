import os

class Settings:
    PROJECT_NAME: str = "Smart Traffic & Emergency Routing API"
  # Replace YOUR_ACTUAL_PASSWORD with the password you created during PostgreSQL installation
    DATABASE_URL: str = "postgresql://postgres:ram050406@localhost:5432/traffic_db"
    MQTT_BROKER: str = os.getenv("MQTT_BROKER", "localhost")
    MQTT_PORT: int = 1883
    MQTT_TOPIC: str = "traffic/intersection_1"

settings = Settings()