import json
import Settings



settings = Settings.Settings.fromFile("./mod-settings.dat")

with open("mod-settings.json","w") as f:
    f.write(json.dumps(settings.getSettingsJson(),indent=4))
    

settings.toBinaryFile("./mod-settings-copy.dat")