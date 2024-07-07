import io
import json
import os



class Settings:
    
    def __init__(self):
        self.version = [0,0,0,0]
        self.settings = {"version": [0,0,0,0]}
        
    @staticmethod
    def fromData(bytes):
        """
        Creates a Settings object from binary data

        Args:
            bytes (bytes): The bytes containing the mod settings

        Returns:
            Settings: A Settings object with the settings from the bytes.
        """
        import Reader
        # Create a Settings object
        settings = Settings()
        data = io.BytesIO(bytes)
        settings.settings = Reader.readSettings(data)
        settings.version = settings.settings["version"]
        
        
        return settings


    @staticmethod
    def fromFile(file):
        """
        Creates a Settings object from a file.

        Args:
            file (str): The path to the file.

        Returns:
            Settings: A Settings object with the settings from the file.
        """
        file = os.path.expandvars(file)
        if not os.path.exists(file):
            raise FileNotFoundError(f"File not found: {file}")
        
        # Create a Settings objec
        settings = None
        
        # Read the file
        with open(file, 'rb') as f:
            settings = Settings.fromData(f.read())
        return settings
    
    
    
    def getSettingsJson(self):
        return self.settings
    
    def toBinaryData(self):
        import Writer
        return Writer.encodeSettings(self)
    
    def toBinaryFile(self, file):
        with open(file, 'wb') as f:
            f.write(self.toBinaryData())