import os


class Settings:
    
    def __init__(self):
        self.version = [0,0,0,0]
        self.settings = {"version": [0,0,0,0]}
        

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
        
        # Create a Settings object
        settings = Settings()
        
        # Read the file
        with open(file, 'r') as f:
            # Read the version
            version = int(f.readline())
            settings.version = version

            # Read the settings
            for line in f:
                key_value = line.split(':')
                settings.settings[key_value[0].strip()] = key_value[1].strip()

        return settings
