from hoymilesapi import Hoymiles 
from dotenv import load_dotenv
import os
from datetime import datetime
import json
load_dotenv()


g_envios = {
    "last_time": datetime.today().strftime("%Y-%m-%d %H:%M:%S"),
    "load_cnt": 0,
    "load_time": datetime.today().strftime("%Y-%m-%d %H:%M:%S"),
}
config ={
    "HOYMILES_USER": os.getenv("HOYMILES_USER"),
    "HOYMILES_PASSWORD": os.getenv("HOYMILES_PASSWORD"),
}

hoymiles = Hoymiles(os.getenv("PLANT_ID"), config, g_envios, meter=True)

hoymiles.get_plant_hw()
hoymiles.update_devices_status()
data = hoymiles.get_solar_data()
hoymiles.get_alarms()

print(json.dumps(hoymiles.solar_data, indent=4))
