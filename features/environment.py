import subprocess
import time
import sys
import os
from behave import fixture
from selenium import webdriver
from selenium.webdriver.common.by import By

flask_process = None

def before_all(context):
    """Start Flask server before running tests"""
    global flask_process
    
    flask_path = os.path.join(os.path.dirname(__file__), '..', 'app.py')
    python_exe = sys.executable
    
    try:
        flask_process = subprocess.Popen(
            [python_exe, flask_path],
            cwd=os.path.dirname(__file__) + '/..',
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        
        # Wait for Flask to start
        time.sleep(3)
        print(f"Flask server started with PID: {flask_process.pid}")
    except Exception as e:
        print(f"Failed to start Flask: {e}")
        raise

def before_scenario(context, scenario):
    """Initialize driver before each scenario"""
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    
    try:
        options = webdriver.ChromeOptions()
        context.driver = webdriver.Chrome(options=options)
        context.driver.set_page_load_timeout(10)
        context.driver.implicitly_wait(5)
    except Exception as e:
        print(f"Failed to initialize webdriver: {e}")
        raise

def after_scenario(context, scenario):
    """Clean up driver after each scenario"""
    if hasattr(context, 'driver') and context.driver:
        try:
            context.driver.quit()
        except:
            pass

def after_all(context):
    """Stop Flask server after tests"""
    global flask_process
    if flask_process:
        try:
            flask_process.terminate()
            flask_process.wait(timeout=5)
            print("Flask server stopped")
        except Exception as e:
            print(f"Error stopping Flask: {e}")


