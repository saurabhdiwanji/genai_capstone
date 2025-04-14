from dotenv import load_dotenv

def init():
    # Initialize the environment for the project
    print("Initializing project environment...")
    
    # Load configuration settings
    load_dotenv()
    
    # Display initialization message
    print('Project environment initialized successfully.');
